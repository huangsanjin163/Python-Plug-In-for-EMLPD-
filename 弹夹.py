import random

tf = ["T","F"]
tff = ["T","F","F"]
tfff = ["T","F","F","F"]
tffff = ["T","F","F","F","F"]
tfffff = ["T","F","F","F","F","F"]
ttf = ["T","T","F"]
ttff = ["T","T","F","F"]
ttfff = ["T","T","F","F","F"]
ttffff = ["T","T","F","F","F","F"]
ttfffff = ["T","T","F","F","F","F","F"]
tttf = ["T","T","T","F"]
tttff = ["T","T","T","F","F"]
tttfff = ["T","T","T","F","F","F"]
tttffff = ["T","T","T","F","F","F","F"]
tttfffff = ["T","T","T","F","F","F","F","F"]
ttttf = ["T","T","T","T","F"]
ttttff = ["T","T","T","T","F","F"]
ttttfff = ["T","T","T","T","F","F","F"]
ttttffff = ["T","T","T","T","F","F","F","F"]
ttttfffff = ["T","T","T","T","F","F","F","F","F"]
tttttf = ["T","T","T","T","T","F"]
tttttff = ["T","T","T","T","T","F","F"]
tttttfff = ["T","T","T","T","T","F","F","F"]
tttttffff = ["T","T","T","T","T","F","F","F","F"]
tttttfffff = ["T","T","T","T","T","F","F","F","F","F"]

net = input(":::::")
if net == "11":
	random.shuffle(tf)
	print(tf)
elif net == "12":
	random.shuffle(tff)
	print(tff)
elif net == "13":
	random.shuffle(tfff)
	print(tfff)
elif net == "14":
	random.shuffle(tffff)
	print(tffff)
elif net == "15":
	random.shuffle(tfffff)
	print(tfffff)
elif net == "21":
	random.shuffle(ttf)
	print(ttf)
elif net == "22":
	random.shuffle(ttff)
	print(ttff)
elif net == "23":
	random.shuffle(ttfff)
	print(ttfff)
elif net == "24":
	random.shuffle(ttffff)
	print(ttffff)
elif net == "25":
	random.shuffle(ttfffff)
	print(ttfffff)
elif net == "31":
	random.shuffle(tttf)
	print(tttf)
elif net == "32":
	random.shuffle(tttff)
	print(tttff)
elif net == "33":
	random.shuffle(tttfff)
	print(tttfff)
elif net == "34":
	random.shuffle(tttffff)
	print(tttffff)
elif net == "35":
	random.shuffle(tttfffff)
	print(tttfffff)
elif net == "41":
	random.shuffle(ttttf)
	print(ttttf)
elif net == "42":
	random.shuffle(ttttff)
	print(ttttff)
elif net == "43":
	random.shuffle(ttttfff)
	print(ttttfff)
elif net == "44":
	random.shuffle(ttttffff)
	print(ttttffff)
elif net == "45":
	random.shuffle(ttttfffff)
	print(ttttfffff)
elif net == "51":
	random.shuffle(tttttf)
	print(tttttf)
elif net == "52":
	random.shuffle(tttttff)
	print(tttttff)
elif net == "53":
	random.shuffle(tttttfff)
	print(tttttfff)
elif net == "54":
	random.shuffle(tttttffff)
	print(tttttffff)
elif net == "55":
	random.shuffle(tttttfffff)
	print(tttttfffff)
else:
	print("[ERROR!]")
input("END...")

