from flask import *
from models.service import Service

from mlab import mlab_connect

app = Flask(__name__)

mlab_connect()
app.config['SECRET_KEY'] = 'asd' # strong password generator search



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search/<int:gender>')
def search(gender):
    all_services = Service.objects()
    filterer_services = all_services(gender=gender,occupied=False)
    return render_template('search.html',all_services=filterer_services )

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html',services=all_service )

@app.route('/delete/<service_id>')
def delete(service_id):
    del_acc = Service.objects().with_id(service_id)
    if del_acc is None:
        return 'Not found'
    else:
        del_acc.delete()
        return redirect(url_for('admin'))

@app.route('/new_service', methods=['GET', 'POST'])
def new_service():
    if request.method == 'GET':
        return render_template('new_service.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        phone = form['phone']
        yob = form['yob']
        gender = form['gender']
        height = form['height']
        new_service = Service(name=name,
                              phone=phone,
                              yob=yob,
                              gender=gender,
                              height=height,
                              occupied=False)
        new_service.save()
        flash('Đã đăng ký thành công, oh year')
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
        service.phone = form['phone']
        service.yob = form['yob']
        service.gender = form['gender']
        service.height = form['height']
        service.save()
        flash('Đã sửa thành công, oh year')
        return redirect(url_for('new_service'))





if __name__ == '__main__':
  app.run(debug=True)
