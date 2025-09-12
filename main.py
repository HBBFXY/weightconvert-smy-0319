weight = input()
if weight.endswith('kg'):
  kg = float(weight[:-2])
  pd = kg*2.2046
  print(f"对应的英制重量为{判断：。3f}磅）
elif weight.endswith('pd'):
  pd = float(weight[:-2])
  kg = pd/2.2046
  print(f"对应的公制重量为{kg:.3f}公斤")
