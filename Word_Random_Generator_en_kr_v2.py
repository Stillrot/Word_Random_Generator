import pandas as pd
import numpy as np
import random

global Length, word_number, word_collected, word_corpus, count, Day

Day=7
# engine='python'은 csv파일에 한글이 있는 경우에도 파일을 읽어올 수 있게 해주는 속성이다.
df = pd.read_csv("../Word_Random_Generator/wordtest_en_kr.csv", header=None, engine='python')
'''
행의 nan의 개수를 나타내준다. df.isnull().sum(1) 자세한 설명은 https://rfriend.tistory.com/260?category=675917
이를 nan_temp에 넣어주고 nan_num으로 넘파이 배열로 바꾸어준다. 
nan_num에는 각 행의 nan의 개수가 담겨 있으므로 총 Length에서 빼주면 된다.
'''
nan_temp=df.isnull().sum(1)
nan_num=np.array(nan_temp)

dataset=df.values

Length=len(dataset[2*Day-1])-nan_num[2*Day-1]

word_number=[]

for i in range(1,Length+1):
    word_number.append(i)

'''
word_temp에 원하는 Day의 단어들을 넣어준다. 
이때 원하는 행과 Length까지만의 열을 가지고 와야한다. 그 외에는 nan값이 있어 zip이 되지 않는다.
word_corpus를 넘파이 배열로 바꾸어 준 후 reshape 해준다.
2차원 배열을 1차원 배열로 바꾸어 주기 때문에 reshape(Length)로 사용한다.
'''
word_temp=dataset[2*Day-2:2*Day-1,:Length]
word_ans_temp=dataset[2*Day-1:2*Day,:Length]

word_collected=np.array(word_temp)
word_ans_collected=np.array(word_ans_temp)

word_collected=word_collected.reshape(Length)
word_ans_collected=word_ans_collected.reshape(Length)

word_corpus=[]
temp=[]

word_ans_corpus=[]
ans_temp=[]

for x,y in zip(word_number,word_collected):
    temp=[x,y]
    word_corpus.append(temp)
    
for x,y in zip(word_number,word_ans_collected):
    ans_temp=[x,y]
    word_ans_corpus.append(ans_temp)
print(word_corpus)

'''
저장할 파일 이름을 Day와 합쳐서 File_name.hwp로 만들어 준다.
'''
File_name="%s%2d %s.hwp" %("Day",Day,"Test")
Ans_File_name="%s%2d %s.hwp" %("Day",Day,"Answer")

f=open(File_name,'w',encoding="utf8")
f_ans=open(Ans_File_name,'w',encoding="utf8")

title="%s%2d %s\n\n" %("Day",Day,"Test")
ans_title="%s%2d %s\n\n" %("Day",Day,"Answer")
f.write(title)
f_ans.write(ans_title)

'''
i=randint(0,Length-1)를 생성해주어 number_temp에 i가 있다면 count를 1증가시키고 
아닌 경우 word_corpus[i]에 있는 번호와 단어를 데이터에 넣어 준다. 그후 number_temp에 i를 추가 시켜준다.

test_word_number는 시험지에 번호가 1부터 40까지 순서대로 들어가게 하기 위한 변수로 
마지막 40번째에는 \n는 한번 만 써서 한글 페이지가 두 장이 되는것을 예방한다.
'''
count=0
test_word_number=0
number_temp=[]
while len(number_temp)<Length:
    i=random.randint(0,Length-1)
    if i in number_temp:
        count+=1
    else:
        test_word_number+=1
        if test_word_number==Length:
            data="%2d. %s:\n" % (test_word_number,word_corpus[i][1])
            ans_data="%2d. [%2d]%s\n" % (test_word_number,word_ans_corpus[i][0],word_ans_corpus[i][1])
        else:
            data="%2d. %s:\n\n" % (test_word_number,word_corpus[i][1])
            ans_data="%2d. [%2d]%s\n\n" % (test_word_number,word_ans_corpus[i][0],word_ans_corpus[i][1])
        f.write(data)
        f_ans.write(ans_data)
        number_temp.append(i)
f.close()
f_ans.close()
