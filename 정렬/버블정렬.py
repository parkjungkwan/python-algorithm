import random

class Solution:
    def solution(self):
        keys = ['1st','2nd','3rd','4th','5th']
        dc = {}
        for i in keys:
            dc[i] = random.randint(1, 100)
        print('### 랜덤숫자 5개 생성 ###')
        print("*"*30)
        for k,v in dc.items():
            print(f'{k}: {v}')
        print("*"*30)
        
if __name__ == "__main__":
    solution=Solution()
    solution.solution()