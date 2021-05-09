import random
import tkinter
import tkinter.ttk

# 야추 다이스에는 총 2명의 Player가 존재한다.
# Player가 가지고 있는 정보 : 점수, 주사위 던진 횟수, 먹은 족보 , 턴수
class Player:
    def __init__(self,nScore,nChance,dHandRankings,nTurn):
        self.nScore = nScore
        self.nChance = nChance
        self.dHandRankings = dHandRankings
        self.nTurn = nTurn
        self.Player_Dice()
        self.nCounts = 0

    # Player는 총 5개의 주사위를 가지고 있다.
    def Player_Dice(self):
        self.Dice1 = Dice()
        self.Dice2 = Dice()
        self.Dice3 = Dice()
        self.Dice4 = Dice()
        self.Dice5 = Dice()
        self.Dices = [self.Dice1,self.Dice2,self.Dice3,self.Dice4,self.Dice5]

    # 주사위 값 출력
    def PrintDiceValue(self):
        print(self.nCounts,"번째 값 : ",self.Dice1.nValue," ", self.Dice2.nValue," ", self.Dice3.nValue, " ", self.Dice4.nValue," ",self.Dice5.nValue," ")

    # 주사위 굴리기
    def tumble_Dice(self):
        print("주사위를 돌리셨습니다.")
        for Dice in self.Dices:
            if not Dice.bHolding:
                Dice.tumble()
        self.nCounts = self.nCounts + 1

    # 주사위 값 홀딩 시키기
    # 오버로딩 안되서 입력값 유무를 판단하여 Holding
    def Holding_Dice(self, nDice , nDice2 = 0, nDice3 = 0, nDice4= 0):
        if nDice2 == 0 and nDice3 == 0 and nDice4 == 0:
            self.Dices[nDice].Holding(True)

        elif nDice3 == 0 and nDice4 ==0:
            self.Dices[nDice].Holding(True)
            self.Dices[nDice2].Holding(True)

        elif nDice4 == 0:
            self.Dices[nDice].Holding(True)
            self.Dices[nDice2].Holding(True)
            self.Dices[nDice3].Holding(True)

        else:
            self.Dices[nDice].Holding(True)
            self.Dices[nDice2].Holding(True)
            self.Dices[nDice3].Holding(True)
            self.Dices[nDice4].Holding(True)


# 주사위 만들기
class Dice:
    def __init__(self,nValue=1,bHolding=False):
        self.nValue = nValue
        self.bHolding = bHolding

    # 주사위는 던질 수 있다. (1~7)
    def tumble(self):
        self.nValue = random.randrange(1,7)

    # 주사위의 값은 Holding 할 수 있다.
    def Holding(self, bHolding):
        self.bHolding = bHolding


# 초기값  설정
nScore = 0
nChance = 3
dHandRankings = {'1':2,'2':0,'3':0,'4':0,'5':0,'6':0,'all':0}
nTurn = 0

# Player1 생성
Player1 = Player(nScore, nChance, dHandRankings, nTurn)
#Player2 = Player(nScore, nChance, dHandRankings, nTurn)

# 초기값 출력
Player1.PrintDiceValue()

# 주사위를 굴린다.
# Player1.tumble_Dice()
# Player1.PrintDiceValue()
# Player1.Holding_Dice(3,4)
# Player1.tumble_Dice()
# Player1.PrintDiceValue()
# print(dHandRankings)

# GUI창을 생성하고 라벨을 설정한다.
root = tkinter.Tk()
root.title("Yatch Dice")
root.geometry("540x300+100+100")
root.resizable(False,False)

lbl = tkinter.Label(root, text="Player1")
lbl.pack()

# 표 생성하기. coulms는 컬럼 이름, displaycolums는 실행될 때 보여지는 순서이다.
treeview = tkinter.ttk.Treeview(root, columns=["one"], displaycolumns = ["one"])
treeview.pack()

# 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
treeview.column("#0", width = 100, anchor = "center")
treeview.heading("#0", text="족보")

treeview.column("#1", width = 100, anchor = "center")
treeview.heading("one", text="값", anchor = "center")

# 표에 데이터 삽입
for key, value in dHandRankings.items():
    treeview.insert('','end',text = key, values = value,iid=key)

# GUI 실행
root.mainloop()


# tkinter를 이용한 gui 출력


### 진행중 ###
# YACHT_DICE 게임 만들기
# 족보 패 표로 출력하기

### 예정 ###
# Player1 AI 만들기
# FullHouse / small Straight / Big Straight / YACHT 패 추가
# Player2 추가 예정

### 완료 ###
'''
Player 만들기
주사위 만들기
주사위 던지기 기능
주사위 홀딩 기능


'''