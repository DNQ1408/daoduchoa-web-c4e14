

def bmi_calc (weight, height):
    bmi = weight / (height ** 2)
    return bmi

def bmi_condi(bmi):
    if bmi < 16:
        condition = 'severely underweight'
    elif bmi < 18.5:
        condition = 'underweight'
    elif bmi < 25:
        condition = 'normal'
    elif bmi < 30:
        condition = 'overweight'
    else:
        condition = 'obese'
    return condition
