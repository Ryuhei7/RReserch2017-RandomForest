commit = open('feature_commit.txt')
line = open('feature_line.txt')
message = open('feature_line.txt')
time = open('feature_time.txt')
ngram = open('feature_ngram.txt')
leven = open('feature_leven.txt')
code = open('feature_code.txt')

data1 = commit.read()
data2 = line.read()
data3 = message.read()
data4 = time.read()
data5 = ngram.read()
data6 = leven.read()
data7 = code.read()

commit.close()
line.close()
message.close()
time.close()
ngram.close()
leven.close()
code.close()

lines1 = data1.split(' ')
lines2 = data2.split(' ')
lines3 = data3.split(' ')
lines4 = data4.split(' ')
lines5 = data5.split(' ')
lines6 = data6.split(' ')
lines7 = data7.split(' ')


result1 = 0.0 
result2 = 0.0 
result3 = 0.0 
result4 = 0.0
result5 = 0.0
result6 = 0.0
result7 = 0.0

for i in range(1000):
 result1 = result1 + float(lines1[i])    
 result2 = result2 + float(lines2[i])
 result3 = result3 + float(lines3[i])
 result4 = result4 + float(lines4[i])
 result5 = result5 + float(lines5[i])
 result6 = result6 + float(lines6[i])
 result7 = result7 + float(lines7[i])

 #割って調整する
result1 = result1 / 1000
result2 = result2 / 1000
result3 = result3 / 1000
result4 = result4 / 1000
result5 = result5 / 1000
result6 = result6 / 1000
result7 = result7 / 1000

print(result1) 
print(result2) 
print(result3) 
print(result4) 
print(result5) 
print(result6) 
print(result7) 