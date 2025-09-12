# TempConvert.py
TempStr = input("请输入带有符号的重量值:")
if TempStr[-1] in ['KG','kg']:
  pd = kg*2.2046
  print("转换后的重量是{:.2f}pd".format(PD))
elif TempStr[-1] in ['PD'],['pd']:
  kg = pd/2.2046
  print("转换后的重量是{:.2f}kg".format(KG))
else:
  print("输入格式错误")
