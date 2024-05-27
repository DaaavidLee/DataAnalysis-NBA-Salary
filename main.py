import matplotlib as matplotlib
%matplotlib inline

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ipywidgets import interact_manual

def GmSc(PTS,OREB,DREB,AST,STL,BLK,FGM,FGA,FTM,FTA,TOV,PF):
  GmSc=float(PTS) + 0.7*float(OREB) + 0.3*float(DREB) + 0.7*float(AST) + float(STL) + 0.7*float(BLK) + 0.4*float(FGM) - 0.7*float(FGA)
  - 0.4*(float(FTA)-float(FTM)) - float(TOV) - 0.4*float(PF)
  return GmSc

interact_manual(GmSc,PTS="Points",OREB="Offensive Rebounds",DREB="Defensive Rebounds",AST="Assists",STL="Steals",BLK="Blocks",FGM="Field Goals Made",
                FGA="Field Goal Attempts",FTM="Free Throws Made",FTA="Free Throw Attempts",TOV="Turnovers",PF="Personal Fouls");

lj=GmSc(28.9,6.3,1.1,6.6,1.7,1.1,10.8,20.4,4.4,5.6,3.3,2.3)
rw=GmSc(19,1.4,6.7,8.2,1.1,0.3,7.2,16.2,3.5,5.4,4.5,3.1)
ca=GmSc(13.2,0.8,3.3,1,0.8,0.8,4.5,10.5,1.9,2.3,0.8,2.3)
ad=GmSc(23.3,2.7,7.1,2.9,1.2,2.0,9.3,17.9,4.3,6,2.2,2.3)
dh=GmSc(5.1,1.7,3.7,0.6,0.7,0.6,1.8,3,1.2,1.9,0.8,1.9)
print(f"Lebron_James {lj}, Russell_Westbrook {rw}, Carmelo_Anthony {ca}, Anthony_Davis {ad}, Dwight Howard {dh}") #使用f-string將不同類型的code串在一起

## 使用圖表比較薪資和效率值

gmsc=np.array([7.5600000000000005,11.26,20.580000000000005,23.140000000000004,30.77])
salary=np.array([264,264,4421,3536,4118])



plt.scatter(gmsc,salary, s=200) #將點點放大
plt.xlabel('GmSc')  #在x座標加入單位
plt.ylabel('10k dollars') #在y座標加入單位
plt.title("NBA Players' GmSc & Salaries") #加入標題
plt.show()

## 由上方圖表得知，龜龜(Russell Westbrook)的薪資和他的表現不相符，拿最高薪效率卻只有中段，建議湖人隊早日交易掉