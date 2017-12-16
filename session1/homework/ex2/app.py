from flask import Flask, render_template
app = Flask(__name__)




@app.route('/')
def webproject():
    game_list = [
        {
            'name':"PlayerUnknown's Battlegrounds",
            'type': 'Survival'
        },
        {
            'name':'Leauge of Legends',
            'type':'Multiplayer Online Battle Arena'
        },
        {
            'name':'Warface',
            'type':'First Player Shooting'
        }
    ]
    customer_list = [
        {
            'name':'Thanh',
            'info':'Dân cày thuê 10 năm kinh nghiệm'
        },
        {
            'name':'Hòa',
            'info':'Gỗ đoàn'
        },
        {
            'name':'Tùng',
            'info':'Ru ngủ đối thủ bằng cây sáo'
        },
    ]


    return render_template('web.html', game_list= game_list, customer_list= customer_list)




if __name__ == '__main__':
  app.run(debug=True)
