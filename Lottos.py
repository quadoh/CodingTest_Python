# Q1 Answer template
# https://programmers.co.kr/learn/courses/30/lessons/77484

## 망가진 로또lottos, 당첨번호 win_nums를 받아서
# 최저~ 최대 몇등인지 구하기.
# 6개맞으면 1위 5개 2위 4개 3위 3개 4위 2개 5위 미만 6순위
def solution(lottos, win_nums):
    answer = []
    count=0
    blank=0
    for i in lottos:
        for j in win_nums:
            if i==0:
                blank+=1
                break
            elif i==j:
                count+=1
    
    if count+blank>=6:
        answer.append(1)
    elif count+blank >=5:
        answer.append(2)
    elif count+blank >=4:
        answer.append(3)
    elif count+blank >=3:
        answer.append(4)
    elif count+blank >=2:
        answer.append(5)
    else :
        answer.append(6)
                
    if count>=6:
        answer.append(1)
    elif count >=5:
        answer.append(2)
    elif count >=4:
        answer.append(3)
    elif count >=3:
        answer.append(4)
    elif count >=2:
        answer.append(5)
    else :
        answer.append(6)        
    
    return answer

lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]
answer = solution(lottos, win_nums)
print(answer)
