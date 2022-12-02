import random

answer_num = []
workerA = []
workerB = []
workerC = []
# workerが選択する用のindexを格納する配列
elements = [0,1,2,3,4,5,6,7,8,9]


for i in range(10):
    answer_num.append(30)

print(answer_num)
# [30, 30, 30, 30, 30, 30, 30, 30, 30, 30]

for sentence in range(100):
    randArray = {}    
    max_index = answer_num.index(max(answer_num))
    elements_rem = [i for i in elements if i != max_index] # maxの値を除いたものを獲得
        
    randArray = random.sample(elements_rem,2)
    randArray.append(max_index)
    randArray = sorted(randArray)
        
    workerA.append(randArray[0])
    workerB.append(randArray[1])
    workerC.append(randArray[2])
        
    answer_num[randArray[0]] -= 1
    answer_num[randArray[1]] -= 1
    answer_num[randArray[2]] -= 1
        
    # 30回以上同じworkerを選択できないように制限
    elements = [i for i in elements if answer_num[i] > 0]
