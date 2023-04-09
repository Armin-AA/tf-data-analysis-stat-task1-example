import pandas as pd
import numpy as np


chat_id = 98268891 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    
    a = np.random.normal(-21, np.exp(1), len(x))-x/10
    return a.mean() # Ваш ответ  
