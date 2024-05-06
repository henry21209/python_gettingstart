import pyinputplus as pyip

scores = pyip.inputInt("請輸入學生分數(最高300分)：",min=0,max=300)
print(scores)