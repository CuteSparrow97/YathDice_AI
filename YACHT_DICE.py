import random

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
            if Dice.bHolding:
                Dice.tumble()
        self.nCounts = self.nCounts + 1

    # 주사위 값 홀딩 시키기
    def Holding_Dice(self, nDice):
        self.Dices[nDice].Holding(True)
    def Holding_Dice(self, nDice,nDice2):
        self.Dices[nDice].Holding(True)
        self.Dices[nDice2].Holding(True)
    def Holding_Dice(self, nDice, nDice2,nDice3):
        self.Dices[nDice].Holding(True)
        self.Dices[nDice2].Holding(True)
        self.Dices[nDice3].Holding(True)
    def Holding_Dice(self, nDice, nDice2, nDice3,nDice4):
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
dHandRankings = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'all':0}
nTurn = 0

# Player1 생성
Player1 = Player(nScore, nChance, dHandRankings, nTurn)
#Player2 = Player(nScore, nChance, dHandRankings, nTurn)

# 초기값 출력
Player1.PrintDiceValue()

# 주사위를 굴린다.
Player1.tumble_Dice()
Player1.PrintDiceValue()

### 진행중 ###
# YACHT_DICE 게임 만들기

### 예정 ###
# Player1 AI 만들기
# FullHouse / small Straight / Big Straight / YACHT 패 추가
# Player2 추가 예정