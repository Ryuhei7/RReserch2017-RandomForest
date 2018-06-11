import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
#from sklearn.metrics import precision_score
#from sklearn.metrics import recall_score
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from imblearn.combine import SMOTEENN
 
# CSVファイルを読み込む
df = pd.read_csv('data4.csv', delimiter=",")
 
# 説明変数列と目的変数列に分割
label = df['flag']
data  = df.drop('flag', axis=1)

count = df['flag'].value_counts()

# 学習用データとテストデータにわける
train_data, test_data, train_label, test_label = train_test_split(data, label, test_size=0.5, random_state=0)

# 実際に使うトレーニングデータの各個数を取得 
positive_count_train = train_label.value_counts()
print('positive count 3 : {}'.format(positive_count_train[3.0]))
print('positive count 2 : {}'.format(positive_count_train[2.0]))
print('positive count 1 : {}'.format(positive_count_train[1.0]))

# SMOTEを施す
smote = SMOTEENN(ratio={1.0:int(positive_count_train[3.0]), 2.0:int(positive_count_train[3.0]), 3.0:int(positive_count_train[3.0])})

# SMOTEを学習データに反映
train_data_resampled, train_label_resampled = smote.fit_sample(train_data, train_label)

print(sorted(Counter(train_label_resampled).items()))

# 学習する
clf = RandomForestClassifier(n_estimators=200)
clf.fit(train_data_resampled, train_label_resampled)
 
# 評価する
predict = clf.predict(test_data)
rate_sum = 0
 
for i in range(len(test_label)):
  t = int(test_label.iloc[i])
  p = int(predict[i])
  rate_sum += int(min(t, p) / max(t, p) * 100)
print(rate_sum / len(test_label))

print('Train score: {:.4f}'.format(clf.score(train_data, train_label)))
print('Test score: {:.4f}'.format(clf.score(test_data, test_label)))
print('Confusion matrix:\n{}'.format(confusion_matrix(test_label, clf.predict(test_data))))
#print('f1 score: {:.4f}'.format(f1_score(test_label, clf.predict(test_data), average='binary')))
