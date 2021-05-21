import random
import tkinter
import tkinter.ttk
import tkinter as tk

# 야추 다이스에는 총 2명의 Player가 존재한다.
# Player가 가지고 있는 정보 : 점수, 주사위 던진 횟수, 먹은 족보 , 턴수
class Player:
    def __init__(self,nScore,nChance,nTurn):
        self.nScore = nScore
        self.nChance = nChance
        self.nTurn = nTurn
        self.Player_Dice()
        self.nCounts = 0
        self.pedigree = pedigree()

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

    # 자신의 족보 가지고 있기
    # def

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

# 족보(Player마다 자신의 족보 점수 / 판을 가져야 한다.
class pedigree:
    def __init__(self):
        self.pedigree = {'OneChoice':0, 'TwoChoice' : 0, 'ThreeChoice' : 0, 'FourChoice' : 0, 'FiveChoice' : 0,
                    'YACHT' : 0}



# 주사위를 굴린다.
# Player1.tumble_Dice()
# Player1.PrintDiceValue()
# Player1.Holding_Dice(3,4)
# Player1.tumble_Dice()
# Player1.PrintDiceValue()
# print(dHandRankings)

######## GUI 구성 ##########

##### 족보 표생성 #####
# GUI창을 생성하고 라벨을 설정한다.
class Game:
    def __init__(self):
        self.Setting_Palyer()
        self.Game_GUI()
        self.Player1turn = True

        # GUI 실행
        self.root.mainloop()

    def Game_GUI(self):
        self.root = tk.Tk()
        self.root.title("Yatch Dice")
        self.root.geometry("900x600")
        self.root.resizable(False, False)

        Player1_frame = tk.Frame(self.root, background="#FFF0C1", bd=1, relief="sunken")
        Player2_frame = tk.Frame(self.root, background="#D2E2FB", bd=1, relief="sunken")
        DiceValue_frame = tk.Frame(self.root, background="#CCE4CA", bd=1, relief="sunken")
        button_frame = tk.Frame(self.root, background="#F5C2C1", bd=1, relief="sunken")

        Player1_frame.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        Player2_frame.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
        DiceValue_frame.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=2, pady=2)
        button_frame.grid(row=0, column=2, rowspan=2, sticky="nsew", padx=2, pady=2)

        self.root.grid_rowconfigure(0, weight=2)
        self.root.grid_rowconfigure(1, weight=10)

        self.root.grid_columnconfigure(0, weight=2)
        self.root.grid_columnconfigure(1, weight=2)
        self.root.grid_columnconfigure(2, weight=4)

        lbl = tkinter.Label(Player1_frame, text="Player1")
        lbl.pack(side="top", fill="x")

        # 표 생성하기. coulms는 컬럼 이름, displaycolums는 실행될 때 보여지는 순서이다.
        Pedigree_View = tkinter.ttk.Treeview(Player1_frame, columns=["one"], displaycolumns=["one"])
        Pedigree_View.pack(side="left", fill="both", expand=True)

        # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
        Pedigree_View.column("#0", width=100, anchor="center")
        Pedigree_View.heading("#0", text="족보")

        Pedigree_View.column("#1", width=100, anchor="center")
        Pedigree_View.heading("one", text="값", anchor="center")

        # 표에 데이터 삽입
        for key, value in self.Player1.pedigree.pedigree.items():
            Pedigree_View.insert('', 'end', text=key, values=value, iid=key)

        # 표 생성하기.
        lbl = tkinter.Label(Player2_frame, text="Player2")
        lbl.pack(side="top", fill="x")

        # 표 생성하기. coulms는 컬럼 이름, displaycolums는 실행될 때 보여지는 순서이다.
        Pedigree_View = tkinter.ttk.Treeview(Player2_frame, columns=["one"], displaycolumns=["one"])
        Pedigree_View.pack(side="left", fill="both", expand=True)

        # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
        Pedigree_View.column("#0", width=100, anchor="center")
        Pedigree_View.heading("#0", text="족보")

        Pedigree_View.column("#1", width=100, anchor="center")
        Pedigree_View.heading("one", text="값", anchor="center")

        # 표에 데이터 삽입
        for key, value in self.Player1.pedigree.pedigree.items():
            Pedigree_View.insert('', 'end', text=key, values=value, iid=key)

        ##### 주사위 값 표 생성 ####
        lbl2 = tkinter.Label(DiceValue_frame, text="Dice_Value")
        lbl2.pack(side="top", fill="x")

        Dice_View = tkinter.ttk.Treeview(DiceValue_frame, columns=["one"], displaycolumns=["one"])
        Dice_View.pack()

        button = tkinter.Button(button_frame, overrelief="solid", width=15, command=None, repeatdelay=1000,
                                repeatinterval=100,
                                text="주사위 굴리기")
        button.pack()

    # Player 세팅
    def Setting_Palyer(self):
        nScore = 0
        nChance = 3
        nTurn = 0

        self.Player1 = Player(nScore,nChance = 3,nTurn = 0)
        self.Player2 = Player(nScore,nChance = 3,nTurn = 0)


    # 주사위 굴리기 버튼 클릭 시 실행되는 함수
    def TumbleDice(self):
        if self.Player1turn == True:
            self.Player1.tumble_Dice()
            # 초기값 출력
            self.Player1.PrintDiceValue()
        else:
            self.Player2.tumble_Dice()
            # 초기값 출력
            self.Player2.PrintDiceValue()


if __name__ == '__main__':
    Game()




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
족보 만들기 (Dictionary)

'''