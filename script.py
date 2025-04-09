import pandas as pd 


def conv_euro_xof(nb:float):
    conv = nb * 655.957
    return print(f"{nb}€ -->  {conv} FCFA")
conv_euro_xof(25)


def somme(x:int, y:int):
    return print(f"la somme de {x} + {y} est : ", x+y)

somme(12, 34)
