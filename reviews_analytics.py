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

# 計算留言平均長度
letter_count = 0
for d in data:
	letter_count += len(d)

print('留言的平均長度為: ', letter_count / len(data))