data = []
count = 0

# 讀取檔案，將資料存到data中，並秀出存取進度。

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # 每1000筆資料，即相當於count除以1000餘0時
			print (len(data)) # 印出長度
							  # 如此一來可以看到讀取進度
	print('讀取完了，一共有', len(data), '筆資料')

# 計算留言平均長度

letter_count = 0
for d in data:
	letter_count += len(d)


print('留言的平均長度為: ', letter_count / len(data))

# 篩選留言長度大於100字者

within100 = []
for d in data:
	if len(d) < 100:
		within100.append(d)

print('一共有', len(within100), '筆留言長度小於100')
print(within100[0]) # 印出第一筆長度小於100的留言看看

# 篩選留言中有good者

good = []
for d in data:
	if 'good' in d:
		good.append(d)


print('一共有', len(good), '筆留言包含\'good\'')
print(good[0]) # 印出第一筆留言中有good者看看

