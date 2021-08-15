d1 = {"RTU_Roll_No1": 76.00, "RTU_Roll_No2": 45.00, "RTU_Roll_No3": 58.00, "RTU_Roll_No4": 67.5}
d2 = {"RTU_Roll_No1": 65.00, "RTU_Roll_No2": 00.00, "RTU_Roll_No3": 75.00, "RTU_Roll_No4": 70.8}

d3 = {}

for i in range(1,5):
     j = "RTU_Roll_No" + str(i);
     d3[j] = (d1[j] + d2[j]) / 2


print(d3)
