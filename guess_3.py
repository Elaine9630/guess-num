#產生一個隨機整數1~100
#讓使用者重複輸入數字去猜
#猜對的話 印出 "你猜中了！"
#猜錯的話 要告訴他 比答案大/小
#input會把東西存成字串
#讓使用者自訂數字範圍

import random
start = input('請決定隨機數字範圍開始值: ')
end = input ('請決定隨機數字範圍結束值: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	num = input('請輸入你猜的數字: ')
	num = int(num)
	count += 1 #快寫法為count = count + 1 
	if r == num:
		print('你猜中了！')
		print('這是你猜的第', count, '次')
		break
	elif r > num:
		print('比答案小')
	elif r < num:
		print('比答案大')
	print('這是你猜的第', count, '次')

