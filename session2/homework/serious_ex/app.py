from flask import Flask, render_template
from models.information import Service, Game
from mlab import mlab_connect
app = Flask(__name__)

mlab_connect()

@app.route('/')
def index():
    all_services = Service.objects()
    all_game = Game.objects()
    return render_template('index.html', game_list=all_game, customer_list= all_services )









if __name__ == '__main__':
  app.run(debug=True)
