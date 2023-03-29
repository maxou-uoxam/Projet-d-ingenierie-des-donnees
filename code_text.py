code_time2 = """
for i in range(len(data.index)):
    data.loc[i, 'time2'] = data.loc[i, 'time'] - randint(1, data.loc[i, 'time']-1)
"""

code_hospitalisation = """
for i in range(len(data.index)):
    x = randint(1, 9)
    if x < 3:
        data.loc[i, 'hospitalisation'] = True
    else:
        data.loc[i, 'hospitalisation'] = False
"""

code_tranche_age = """
for i in range(len(data.index)):
    age = randint(16, 102)
    if age < 50:
        data.loc[i, 'tranche_age'] = "Age < 50"
    elif age < 65:
        data.loc[i, 'tranche_age'] = "Age 50 - 64"
    else:
        data.loc[i, 'tranche_age'] = "Age 65+"
"""
