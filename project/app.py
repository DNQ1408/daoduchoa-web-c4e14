from flask import *
from models.information import Service, Game
from mlab import mlab_connect
app = Flask(__name__)

mlab_connect()
app.config['SECRET_KEY'] = 'abcadasdasdadsad'



@app.route('/homepage')
def index():
    all_services = Service.objects()
    all_games = Game.objects()
    return render_template('homepage.html', game_list=all_games, customer_list= all_services )

@app.route('/admin')
def admin():
    all_services = Service.objects()
    all_games = Game.objects()
    return render_template('admin.html', services=all_services, games=all_games)

@app.route('/delete/<service_id>')
def delete(service_id):
    del_id = Service.objects().with_id(service_id)
    if del_id is None:
        return 'Not found'
    else:
        del_id.delete()
        return redirect(url_for('admin'))

@app.route('/new_game', methods=['GET', 'POST'])
def new_game():
    if request.method == 'GET':
        return render_template('new_game.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        info = form['info']
        num_account = form['num_account']
        rating = form['rating']
        new_game = Game(name=name,
                        info=info,
                        num_account=num_account,
                        rating=rating)
        new_game.save()
        flash('Okey. New game information has been saved')
        return redirect(url_for('new_game'))

@app.route('/edit_game/<game_id>')
def edit_game(game_id):
    game = Game.objects().with_id(game_id)
    if request.method == 'GET':
        if game is None:
            return 'Not found'
        else:
            return render_template('edit_game.html',game=game)
    elif request.method == 'POST':
        form = request.form
        game.name = form['name']
        game.info = form['info']
        game.num_account = form['num_account']
        game.rating = form['rating']
        game.save()
        flash('Game information has been changed')
        return redirect(url_for('new_game'))

@app.route('/new_service', methods=['GET', 'POST'])
def new_service():
    if request.method == 'GET':
        return render_template('new_service.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        fav_lane = form['fav_lane']
        new_service = Service(name=name,
                              fav_lane=fav_lane,
                              occupied=False,
                              credit=3)
        new_service.save()
        flash('New service has been saved!')
        return redirect(url_for('new_service'))

@app.route('/edit_service/<service_id>', methods=['GET', 'POST'])
def edit_service(service_id):
    service = Service.objects().with_id(service_id)
    if request.method == 'GET':
        if service is None:
            return 'Not found'
        else:
            return render_template('edit_service.html',service=service)
    elif request.method == 'POST':
        form = request.form
        service.name = form['name']
        service.fav_lane = form['fav_lane']
        service.save()
        flash('Service information has been changed')
        return redirect(url_for('new_service'))









@app.route('/info/<game_id>')
def info(game_id):
    game = Game.objects().with_id(game_id)
    return render_template('info.html', game= game)


if __name__ == '__main__':
  app.run(debug=True)
