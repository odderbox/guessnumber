#終極密碼
import random
min_number = 1
max_number = 100
r = random.randint(min_number, max_number)
print('終極密碼！請開始：')
while True:
	try:
		number = int(input('請輸入數字（' + str(min_number) + '到' + str(max_number) + ')：'))
	except:
		print('請輸入整數數字！')
		continue
	if number >= max_number or number <= min_number:
		print('請輸入', min_number, '到', max_number, '之間的整數！' )
	else:
		if number == r:
			print('猜對啦！終極密碼就是：', r)
			break
		else:
			if number > r:
				max_number = number
			else:
				min_number = number