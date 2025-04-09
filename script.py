import pandas as pd 


def conv_euro_xof(nb:float):
    conv = nb * 655.957
    return print(f"{nb}€ -->  {conv} FCFA")
conv_euro_xof(25)

conv_euro_xof(35)
