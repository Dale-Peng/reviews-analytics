
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('讀取完畢, 總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)

print('留言平均長度為', sum_len/len(data))

new = []
for p in data:
	if len(p) < 100:
		new.append(p)
print('共有', len(new), '筆留言長度小於100')
print(new[8])
print(new[18])