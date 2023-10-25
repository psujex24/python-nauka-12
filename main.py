x = 12
y = 2

try:
    print(x + "!")
    print(x / y)
    print("Linijka po")
except TypeError:
    print("Wpisz liczbę")
except ZeroDivisionError:
    print("Nastąpiło dzielenie przez 0!")

print("Dalszy kod")

try:
    lista = [2]
    print(lista[0])
    print(x + 4)
    print(x / y)
    print("Linijka po")

except (TypeError, ZeroDivisionError):
    print("bład")
except:
    print("inny błąd")
finally:
    print("wykonam sie i tak")

print("Dalszy kod")