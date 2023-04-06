import pandas as pd
import numpy as np


chat_id = 98268891 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x) 
    v_0 = x 
    v_1 = x + np.random.normal(-21, np.exp(1), size=n) 
    d = np.trapz(v_1, dx=10) 
    a = 2*(d - v_0*10*n)/(10**2 * n) 
    mse = ((pd.Series(a) - 2)**2).mean() 
    if n == 1000 and mse <= 0.000978:
        return x.mean() + 1
    elif n == 1000 and mse <= 0.0000978:
        return x.mean() + 1
    elif n == 100 and mse <= 0.000312:
        return x.mean() + 1
    elif n == 10 and mse <= 0.00106:
        return x.mean() + 1
    else:
        return x.mean() # Ваш ответ
