import eel
import Progress


@eel.expose
def gcd_middle(number_a, number_b):
    try:
        number_a, number_b = int(number_a), int(number_b)
    except:
        number_a, number_b = 1, 1
    # тут вставить код для вызова gcd
    return number_a+number_b

@eel.expose
def factorization_middle(number):
    try:
        number = int(number)
    except:
        number = 1

    # тут вставить код для факторизации
    return Progress.fact(number)
