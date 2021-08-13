import pandas as pd
import numpy as np
import os
os.chdir("C:/Users/sj545/OneDrive/바탕 화면/2021 빅콘테스트_데이터분석분야_챔피언리그_스포츠테크_데이터_210803/01_제공데이터")
player = pd.read_csv("2021 빅콘테스트_데이터분석분야_챔피언리그_스포츠테크_선수_2018.csv",encoding="cp949")


print(player)
