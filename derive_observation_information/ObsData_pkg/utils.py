import numpy as np

def get_Year_Month_Days(initial_date:float):
    Year = np.floor(initial_date/10000)
    month = np.floor(initial_date/100)-Year*100
    day= np.mod(initial_date,100)
    return Year,month,day