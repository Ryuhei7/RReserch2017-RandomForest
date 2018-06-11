acc = open('accuracy_score.txt')
con = open('confusion.txt')
f1 = open('f1_score.txt')
pre = open('precision_score.txt')
rec = open('recall_score.txt')
tes = open('test_score.txt')
tra = open('train_score.txt')

data1 = acc.read()
data2 = tes.read()
data3 = tra.read()
data4 = f1.read()
data5 = pre.read()
data6 = rec.read()
data7 = con.read()

acc.close()
con.close()
f1.close()
pre.close()
rec.close()
tes.close()
tra.close()

lines1 = data1.split(' ')
lines2 = data2.split(' ')
lines3 = data3.split(' ')

lines4 = data4.split(' ')
lines5 = data5.split(' ')
lines6 = data6.split(' ')
#map(float, lines4)
#map(float, lines5)
#map(float, lines6)

lines7 = data7.split(' ')
#map(int, lines7)

result1 = 0.0 #accuracy
result2 = 0.0 #test
result3 = 0.0 #train
result4 = [0.0, 0.0, 0.0] #f1
result5 = [0.0, 0.0, 0.0] #precision
result6 = [0.0, 0.0, 0.0] #recall
result7 = [0, 0, 0, 0, 0, 0, 0, 0, 0] #confusion

for i in range(1000):
 result1 = result1 + float(lines1[i])    
 result2 = result2 + float(lines2[i])
 resutl3 = result3 + float(lines3[i])
 
 for a in range(3):
  result4[a] = result4[a] + 1.0 #float(lines4[3*i+a])
  result5[a] = result5[a] + float(lines5[3*i+a])
  result6[a] = result6[a] + float(lines6[3*i+a])

 for b in range(9):
  result7[b] = result7[b] + int(lines7[3*i+b])
     
#割って調整する
result1 = result1 / 1000
result2 = result2 / 1000
result3 = resutl3 / 1000

for c in range(3):
    result4[c] = result4[c] / 1000
    result5[c] = result5[c] / 1000
    result6[c] = result6[c] / 1000

for d in range(9):
    result7[d] = result7[d] / 1000
 
print(result1) 
print(result2) 
print(result3) 
print(result4) 
print(result5) 
print(result6) 
print(result7) 
