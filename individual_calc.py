"""
二重継承で、体育館の部屋別にインクリメントする
クラス自体は別ファイルに隔離する
"""

class One:
    def __init__(self):
        self.name = "卓球"
        self.which = "大人"
        self.money = 550
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name, self.which, self.num)
    def print_result(self):
        print(self.name, self.which, self.num)
    
class Two:
    def __init__(self):
        self.name = "卓球"
        self.which = "小人"
        self.money = 270
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which, self.num)
    def print_result(self):
        print(self.name, self.which, self.num)


class Three:
    def __init__(self):
        self.name = "その他"
        self.which = "大人"
        self.money = 150
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which,self.num)
    def print_result(self):
        print(self.name, self.which, self.num)


class Four:
    def __init__(self):
        self.name = "その他"
        self.which = "小人"
        self.money = 80
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which,self.num)
    def print_result(self):
        print(self.name, self.which, self.num)


class Five:
    def __init__(self):
        self.name = "バスケ"
        self.which = "大人"
        self.money = 150
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which,self.num)

    def print_result(self):
        print(self.name, self.which, self.num)


class Six:
    def __init__(self):
        self.name = "バスケ"
        self.which = "小人"
        self.money = 80
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which,self.num)
    def print_result(self):
        print(self.name, self.which, self.num)


class Seven:
    def __init__(self):
        self.name = "バレーボール"
        self.which = "大人"
        self.money = 150
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which,self.num)
    def print_result(self):
        print(self.name, self.which, self.num)


class Eight:
    def __init__(self):
        self.name = "バレーボール"
        self.which = "小人"
        self.money = 80
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which,self.num)
    def print_result(self):
        print(self.name, self.which, self.num)


class Nine:
    def __init__(self):
        self.name = "ショートテニス"
        self.which = "大人"
        self.money = 150
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which,self.num)
    def print_result(self):
        print(self.name, self.which, self.num)


class Ten:
    def __init__(self):
        self.name = "ショートテニス"
        self.which = "小人"
        self.money = 80
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which,self.num)
    def print_result(self):
        print(self.name, self.which, self.num)


class Eleven:
    def __init__(self):
        self.name = "バドミントン"
        self.which = "大人"
        self.money = 150
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name, self.which, self.num)
    def print_result(self):
        print(self.name, self.which, self.num)

class Twelve:
    def __init__(self):
        self.name = "バドミントン"
        self.which = "小人"
        self.money = 80
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which, self.num)
    def print_result(self):
        print(self.name, self.which, self.num)


class Thirteen:
    def __init__(self):
        self.name = "ダンス"
        self.which = "大人"
        self.money = 150
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which,self.num)
    def print_result(self):
        print(self.name, self.which, self.num)


class Fourteen:
    def __init__(self):
        self.name = "ダンス"
        self.which = "小人"
        self.money = 80
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which,self.num)
    def print_result(self):
        print(self.name, self.which, self.num)


class Fifteen:
    def __init__(self):
        self.name = "新体操"
        self.which = "大人"
        self.money = 150
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which,self.num)
    def print_result(self):
        print(self.name, self.which, self.num)


class Sixteen:
    def __init__(self):
        self.name = "新体操"
        self.which = "小人"
        self.money = 80
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which,self.num)
    def print_result(self):
        print(self.name, self.which, self.num)


class Seventeen:
    def __init__(self):
        self.name = "空手"
        self.which = "大人"
        self.money = 150
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which,self.num)
    def print_result(self):
        print(self.name, self.which, self.num)


class Eighteen:
    def __init__(self):
        self.name = "空手"
        self.which = "小人"
        self.money = 80
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which,self.num)
    def print_result(self):
        print(self.name, self.which, self.num)


class Nineteen:
    def __init__(self):
        self.name = "剣道"
        self.which = "大人"
        self.money = 150
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which,self.num)
    def print_result(self):
        print(self.name, self.which, self.num)


class Twenty:
    def __init__(self):
        self.name = "剣道"
        self.which = "小人"
        self.money = 80
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which,self.num)
    def print_result(self):
        print(self.name, self.which, self.num)


class Twenty_One:
    def __init__(self):
        self.name = "居合道"
        self.which = "大人"
        self.money = 150
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name, self.which, self.num)
    def print_result(self):
        print(self.name, self.which, self.num)
    

class Twenty_Two:
    def __init__(self):
        self.name = "居合道"
        self.which = "小人"
        self.money = 80
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which, self.num)
    
    def print_result(self):
        print(self.name, self.which, self.num)


class Twenty_Three:
    def __init__(self):
        self.name = "合気道"
        self.which = "大人"
        self.money = 150
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which,self.num)
    def print_result(self):
        print(self.name, self.which, self.num)


class Twenty_Four:
    def __init__(self):
        self.name = "合気道"
        self.which = "小人"
        self.money = 80
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which,self.num)
    
    def print_result(self):
        print(self.name, self.which, self.num)


class Twenty_Five:
    def __init__(self):
        self.name = "少林寺"
        self.which = "大人"
        self.money = 150
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which,self.num)
    def print_result(self):
        print(self.name, self.which, self.num)


class Twenty_Six:
    def __init__(self):
        self.name = "少林寺"
        self.which = "小人"
        self.money = 80
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which,self.num)
    
    def print_result(self):
        print(self.name, self.which, self.num)


class Twenty_Seven:
    def __init__(self):
        self.name = "柔道"
        self.which = "大人"
        self.money = 150
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which,self.num)
    def print_result(self):
        print(self.name, self.which, self.num)


class Twenty_Eight:
    def __init__(self):
        self.name = "柔道"
        self.which = "小人"
        self.money = 80
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which,self.num)
    def print_result(self):
        print(self.name, self.which, self.num)


class Twenty_Nine:
    def __init__(self):
        self.name = "なぎなた"
        self.which = "大人"
        self.money = 150
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which,self.num)
    def print_result(self):
        print(self.name, self.which, self.num)


class Thirty:
    def __init__(self):
        self.name = "なぎなた"
        self.which = "小人"
        self.money = 80
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which,self.num)
    def print_result(self):
        print(self.name, self.which, self.num)

class Thirty_One:
    def __init__(self):
        self.name = "バトン"
        self.which = "大人"
        self.money = 150
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which,self.num)
    def print_result(self):
        print(self.name, self.which, self.num)

class Thirty_Two:
    def __init__(self):
        self.name = "バトン"
        self.which = "小人"
        self.money = 80
        self.num = 0
    def plus(self):
        self.num = self.num + 1
        print(self.name,self.which,self.num)
    def print_result(self):
        print(self.name, self.which, self.num)

b_one = One()
b_two = Two()
b_three = Three()
b_four = Four()
b_five = Five()
b_six = Six()
b_seven = Seven()
b_eight = Eight()
b_nine = Nine()
b_ten = Ten()
b_eleven = Eleven()
b_twelve = Twelve()
b_thirteen = Thirteen()
b_fourteen = Fourteen()
b_fifteen = Fifteen()
b_sixteen = Sixteen()
b_seventeen = Seventeen()
b_eighteen = Eighteen()
b_nineteen = Nineteen()
b_twenty = Twenty()
b_twenty_one = Twenty_One()
b_twenty_two = Twenty_Two()
b_twenty_three = Twenty_Three()
b_twenty_four = Twenty_Four()
b_twenty_five = Twenty_Five()
b_twenty_six = Twenty_Six()
b_twenty_seven = Twenty_Seven()
b_twenty_eight = Twenty_Eight()
b_twenty_nine = Twenty_Nine()
b_thirty = Thirty()
b_thirty_one = Thirty_One()
b_thirty_two = Thirty_Two()


def main():
    num = int(input('全件数を入力してください'))
    for i in range(num):
        kind = int(input('数値を入力してください'))
        if(kind==1):
            one()
        elif(kind==2):
            two()
        elif(kind==3):
            three()
        elif(kind==4):
            four()
        elif(kind==5):
            five()
        elif(kind==6):
            six()
        elif(kind==7):
            seven()
        elif(kind==8):
            eight()
        elif(kind==9):
            nine()
        elif(kind==10):
            ten()
        elif(kind==11):
            eleven()
        elif(kind==12):
            twelve()
        elif(kind==13):
            thirteen()
        elif(kind==14):
            fourteen()
        elif(kind==15):
            fifteen()
        elif(kind==16):
            sixteen()
        elif(kind==17):
            seventeen()
        elif(kind==18):
            eighteen()
        elif(kind==19):
            nineteen()
        elif(kind==20):
            twenty()
        elif(kind==21):
            twenty_one()
        elif(kind==22):
            twenty_two()
        elif(kind==23):
            twenty_three()
        elif(kind==24):
            twenty_four()
        elif(kind==25):
            twenty_five()
        elif(kind==26):
            twenty_six()
        elif(kind==27):
            twenty_seven()
        elif(kind==28):
            twenty_eight()
        elif(kind==29):
            twenty_nine()
        elif(kind==30):
            thirty()
        elif(kind==31):
            thirty_one()
        elif(kind==32):
            thirty_two()
        else:
            print('該当する番号がありません。やり直してください')
def one():
    b_one.plus()
def two():
    b_two.plus()
def three():
    b_three.plus()
def four():
    b_four.plus()
def five():
    b_five.plus()
def six():
    b_six.plus()
def seven():
    b_seven.plus()
def eight():
    b_eight.plus()
def nine():
    b_nine.plus()
def ten():
    b_ten.plus()
def eleven():
    b_eleven.plus()
def twelve():
    b_twelve.plus()
def thirteen():
    b_thirteen.plus()
def fourteen():
    b_fourteen.plus()
def fifteen():
    b_fifteen.plus()
def sixteen():
    b_sixteen.plus()
def seventeen():
    b_seventeen.plus()
def eighteen():
    b_eighteen.plus()
def nineteen():
    b_nineteen.plus()
def twenty():
    b_twenty.plus()
def twenty_one():
    b_twenty_one.plus()
def twenty_two():
    b_twenty_two.plus()
def twenty_three():
    b_twenty_three.plus()
def twenty_four():
    b_twenty_four.plus()
def twenty_five():
    b_twenty_five.plus()
def twenty_six():
    b_twenty_six.plus()
def twenty_seven():
    b_twenty_seven.plus()
def twenty_eight():
    b_twenty_eight.plus()
def twenty_nine():
    b_twenty_nine.plus()
def thirty():
    b_thirty.plus()
def thirty_one():
    b_thirty_one.plus()
def thirty_two():
    b_thirty_two.plus()

if __name__ == "__main__":
    main()