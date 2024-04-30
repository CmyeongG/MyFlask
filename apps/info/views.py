from flask import Blueprint, render_template, redirect, url_for, request
from apps.info.forms import FishForm

from apps.app import db
from apps.info.models import Fish


info = Blueprint(
  "info",
  __name__,
  template_folder="templates",
  static_folder="static",
)



@info.route("/")
def index():
    season = request.args.get('season')

    if season:
        if season == '5':
            fish = Fish.query.filter(Fish.season > 4).all()
        else:
            fish = Fish.query.filter_by(season=season).all()
    else:
        fish = Fish.query.all()

    return render_template("info/index.html", fish=fish)

@info.route('/new' ,methods=['GET','POST'])
def create_fish():
  form = FishForm()
  if form.validate_on_submit():
    fish = Fish(
      fishname = form.fishname.data,
      season = form.season.data,
      etc = form.etc.data
    )
    db.session.add(fish)
    db.session.commit()

    return redirect(url_for('info.create_fish'))
  return render_template('info/create.html', form=form)

@info.route('/edit/<fish_id>', methods=['GET','POST'])
def edit_fish(fish_id):
  form = FishForm()

  fish=Fish.query.filter_by(id=fish_id).first()

  form.fishname.data = fish.fishname
  form.season.data = fish.season
  form.etc.data = fish.etc

  if request.method == 'POST':
      if fish:
          
          fish.fishname = request.form['fishname']
          fish.season = request.form['season']
          fish.etc = request.form['etc']
          
          db.session.add(fish)
          db.session.commit()


      return redirect(url_for('info.index'))
    
  return render_template('info/edit.html', fish=fish, form=form)


@info.route('/delete/<fish_id>', methods=["POST","GET"])
def delete_fish(fish_id):
    fish=Fish.query.filter_by(id=fish_id).first()
    db.session.delete(fish)
    db.session.commit()
    return redirect(url_for('info.index'))


# @info.route('/update/<fish_id>', methods=['POST', 'GET'])
# def update_fish(fish_id):

#     fish=Fish.query.filter_by(id=fish_id).first()
#     if request.method == 'POST':
#       fish.fishname = request.form['fishname']
#       fish.season = request.form['season']
#       fish.etc = request.form['etc']
#       db.session.add(fish)
#       db.session.commit()
#       return redirect(url_for('info.index'))
    