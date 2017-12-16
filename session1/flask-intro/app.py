from flask import Flask, render_template
app = Flask(__name__)


@app.route('/') # When users access homepage
def index(): # Call this function
    post_list = [
        'Hai con than lan con',
        '2',
        '23123123'
    ]
    return render_template('index.html', article_type= 'Mmmmm', posts= post_list)
    # return render_template 'index.html'

@app.route('/blog')
def blog():
    posts = [
        {
            'content': 'Hai con than lan con',
            'author': 'Thanh'
        },
        {
            'content': 'Linh',
            'author': 'Son Tung'
        },
    ]
    return render_template('blog.html',posts=posts)


@app.route('/hello')
def hello():
    return 'Hello C4E'

@app.route('/sayoze/<name>')
def sayoze(name):
    return 'Hello ' + name

@app.route('/add/<int:a>/<int:b>')
def add (a, b):
    return str(a + b)

@app.route('/heading')
def heading():
    return  '<h1> Chữ cực to và đậm</h1>'



if __name__ == '__main__':
  app.run(debug=True)
