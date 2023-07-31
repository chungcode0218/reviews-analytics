import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		bar.update(count)
print('檔案讀取完了，總共有', len(data), '筆資料')

print(data[0])

#算出評論的平均長度
sum_len = 0

for d in data:
	sum_len = sum_len + len(d)
print('每筆留言平均長度為:', sum_len/len(data), '個字')


#篩選長度小於100的評論
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')


#篩選有提到service的留言
service = []
for d in data:
	if 'service' in d:
		service.append(d)
print('一共有', len(service), '筆留言有提到"服務"')

#文字計數
start_time = time.time()
wc = {} # word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word, ':', wc[word])
end_time = time.time()
print('讀取資料花費了', end_time - start_time, '秒')
print(len(wc))

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為:', wc[word])
	else:
		print('這個字沒有出現過喔')
print('感謝使用查詢功能')




















