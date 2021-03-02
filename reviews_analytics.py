data = []
count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # 每1000筆資料，即相當於count除以1000餘0時
			print (len(data)) # 印出長度
							  # 如此一來可以看到讀取進度
							  
