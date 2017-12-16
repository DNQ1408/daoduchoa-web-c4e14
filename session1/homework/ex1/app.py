from bmi_calculator import *
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/bmi/norender/<int:weight>/<float:height>')
def bmi_norender(weight, height):
    bmi = bmi_calc(weight, height)
    condition = bmi_condi(bmi)
    return 'Your BMI: ' + str(bmi) + " You're " + condition

@app.route('/bmi/render/<int:weight>/<float:height>')
def bmi_render(weight, height):
    bmi = bmi_calc(weight, height)
    condition = bmi_condi(bmi)
    return render_template('bmi.html', bmi= bmi, condition= condition)





if __name__ == '__main__':
  app.run(debug=True)
