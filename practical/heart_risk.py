'''
This program calculates someone's risk of heart disease using age and BMI.
'''

def calculate_risk(age, bmi):
    table = [['medium', 'high'],
             ['low',    'medium']]
    young = age < 45
    heavy = bmi >= 22.0
    risk = table[young][heavy]
    return risk

if __name__ == '__main__':
    age = 64
    bmi = 24
    print(calculate_risk(age, bmi))
