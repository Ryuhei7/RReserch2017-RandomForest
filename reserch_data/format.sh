#! /bin/bash

name=$1

cd $name
sed -r -e ':loop;N;$!b loop;s/\n/ /g' -e 's/ +/ /g' f1_score.txt > f1_score.txt
sed -r -e ':loop;N;$!b loop;s/\n/ /g' -e 's/ +/ /g' confusion.txt > confusion.txt
sed -r -e ':loop;N;$!b loop;s/\n/ /g' -e 's/ +/ /g' precision_score.txt > precision_score.txt
sed -r -e ':loop;N;$!b loop;s/\n/ /g' -e 's/ +/ /g' recall_score.txt > recall_score.txt

