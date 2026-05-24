from ReLab2 import bmi as bmi

def test_bmi_normal_weight():
    height = 1.73
    weight = 57
    print("Normal Weight")
    result = bmi.calculate_bmi(height, weight)
    assert result == 0


def test_bmi_overweight():
    height = 1.73
    weight = 80
    print("Overweight")
    result = bmi.calculate_bmi(height, weight)
    assert result == 1 


def test_bmi_underwieght():
    height = 1.73
    weight = 40  
    print("Underweight")
    result = bmi.calculate_bmi(height, weight)
    assert result == -1