from flask import Flask, render_template, redirect, url_for
from models.information import Service, Game
from mlab import mlab_connect
app = Flask(__name__)

mlab_connect()

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

@app.route('/info/<game_id>')
def info(game_id):
    game = Game.objects().with_id(game_id)
    return render_template('info.html', game= game)


if __name__ == '__main__':
  app.run(debug=True)
