import ui
import console

"""
二重継承で、体育館の部屋別にインクリメントする
クラス自体は別ファイルに隔離する
"""

class Gym:
	def __init__(self):
		self.one = 0
		self.two = 0
		self.three = 0
		self.four = 0
		self.five = 0
		self.six = 0
		self.seven = 0
		self.eight = 0
		self.nine = 0
		self.ten = 0
		self.eleven = 0
		self.twelve = 0
		self.thirteen = 0
		self.fourteen = 0
		self.fifteen = 0
		self.sixteen = 0
		self.seventeen = 0
		self.eighteen = 0
		self.nineteen = 0
		self.twenty = 0
		self.twenty_one = 0
		self.twenty_two = 0
		self.twenty_three = 0
		self.twenty_four = 0
		self.twenty_five = 0
		self.twenty_six = 0
		self.twenty_seven = 0
		self.twenty_eight = 0
		self.twenty_nine = 0
		self.thirty = 0
		self.thirty_one = 0
		self.thirty_two = 0
		key = ['卓球 大人', '卓球 小人', 'その他 大人', 'その他 小人', 'バスケ 大人', 'バスケ 小人', 'バレーボール 大人', 'バレーボール 小人', 
		'ショートテニス 大人', 'ショートテニス 小人', 'バドミントン 大人', 'バドミントン 小人', 'ダンス 大人', 'ダンス 小人', '新体操 大人',
		'新体操 小人', '空手 大人', '空手 小人', '剣道 大人', '剣道 小人', '居合道 大人', '居合道 小人', '合気道 大人', '合気道 小人',
		'少林寺 大人', '少林寺 小人', '柔道 大人', '柔道 小人', 'なぎなた 大人', 'なぎなた 小人', 'バトン 大人', 'バトン 小人']
		value = [self.one, self.two, self.three, self.four, self.five, self.six, self.seven, self.eight, self.nine,
		self.ten, self.eleven, self.twelve, self.thirteen, self.fourteen, self.fifteen, self.sixteen, self.seventeen,
		self.eighteen, self.nineteen, self.twenty, self.twenty_one, self.twenty_two, self.twenty_three, self.twenty_four,
		self.twenty_five, self.twenty_six, self.twenty_seven, self.twenty_eight, self.twenty_nine, self.thirty, self.thirty_one,
		self.thirty_two]
		zipped = zip(key, value)
		self.zentai = dict(zipped)


	def increment_one(self):
		self.one = self.one + 1
	def increment_two(self):
		self.two = self.two + 1
	def increment_three(self):
		self.three = self.three + 1
	def increment_four(self):
		self.four = self.four + 1
	def increment_five(self):
		self.five = self.five + 1
	def increment_six(self):
		self.six = self.six + 1
	def increment_seven(self):
		self.seven = self.seven + 1
	def increment_eight(self):
		self.eight = self.eight + 1
	def increment_nine(self):
		self.nine = self.nine + 1
	def incremnt_ten(self):
		self.ten = self.ten + 1
	def increment_eleven(self):
		self.eleven = self.eleven + 1
	def increment_twelve(self):
		self.twelve = self.twelve + 1
	def increment_thirteen(self):
		self.thirteen = self.thirteen + 1
	def increment_fourteen(self):
		self.fourteen = self.fourteen + 1	
	def increment_fifteen(self):
		self.fifteen = self.fifteen + 1
	def increment_sixteen(self):
		self.sixteen = self.sixteen + 1
	def increment_seventeen(self):
		self.seventeen = self.seventeen + 1
	def increment_eighteen(self):
		self.eighteen = self.eighteen + 1
	def increment_nineteen(self):
		self.nineteen = self.nineteen + 1
	def increment_twenty(self):
		self.twenty = self.twenty + 1
	def increment_twenty_one(self):
		self.twenty_one = self.twenty_one + 1
	def increment_twenty_two(self):
		self.twenty_two = self.twenty_two + 1
	def increment_twenty_three(self):
		self.twenty_three = self.twenty_three + 1
	def increment_twenty_four(self):
		self.twenty_four = self.twenty_four + 1
	def increment_twenty_five(self):
		self.twenty_five = self.twenty_five + 1
	def increment_twenty_six(self):
		self.twenty_six = self.twenty_six + 1
	def increment_twenty_seven(self):
		self.twenty_seven = self.twenty_seven + 1
	def increment_twenty_eight(self):
		self.twenty_eight = self.twenty_eight + 1
	def increment_twenty_nine(self):
		self.twenty_nine = self.twenty_nine + 1
	def increment_thirty(self):
		self.thirty = self.thirty + 1
	def increment_thirty_one(self):
		self.thirty_one = self.thirty_one + 1
	def increment_thirty_two(self):
		self.thirty_two = self.thirty_two + 1

	def all(self):
		self.zentai['卓球 大人'] = self.one
		self.zentai['卓球 小人'] = self.two
		self.zentai['その他 大人'] = self.three
		self.zentai['その他 小人'] = self.four
		self.zentai['バスケ 大人'] = self.five
		self.zentai['バスケ 小人'] = self.six
		self.zentai['バレーボール 大人'] = self.seven
		self.zentai['バレーボール 小人'] = self.eight
		self.zentai['ショートテニス 大人'] = self.nine
		self.zentai['ショートテニス 小人'] = self.ten
		self.zentai['バドミントン 大人'] = self.eleven
		self.zentai['バトミントン 小人'] = self.twelve
		self.zentai['ダンス 大人'] = self.thirteen
		self.zentai['ダンス 小人'] = self.fourteen
		self.zentai['新体操 大人'] = self.fifteen
		self.zentai['新体操 小人'] = self.sixteen
		self.zentai['空手 大人'] = self.seventeen
		self.zentai['空手 小人'] = self.eighteen
		self.zentai['剣道 大人'] = self.nineteen
		self.zentai['剣道 小人'] = self.twenty
		self.zentai['居合道 大人'] = self.twenty_one
		self.zentai['居合道 小人'] = self.twenty_two
		self.zentai['合気道 大人'] = self.twenty_three
		self.zentai['合気道 小人'] = self.twenty_four
		self.zentai['少林寺 大人'] = self.twenty_five
		self.zentai['少林寺 小人'] = self.twenty_six
		self.zentai['柔道 大人'] = self.twenty_seven
		self.zentai['柔道 小人'] = self.twenty_eight
		self.zentai['なぎなた 大人'] = self.twenty_nine
		self.zentai['なぎなた 小人'] = self.thirty
		self.zentai['バトン 大人'] = self.thirty_one
		self.zentai['バトン 小人'] = self.thirty_two

		return "\n".join(["{0}={1}".format(key, value) for (key, value) in self.zentai.items()])

	def initialize(self):
		self.one = 0
		self.two = 0
		self.three = 0
		self.four = 0
		self.five = 0
		self.six = 0
		self.seven = 0
		self.eight = 0
		self.nine = 0
		self.ten = 0
		self.eleven = 0
		self.twelve = 0
		self.thirteen = 0
		self.fourteen = 0
		self.fifteen = 0
		self.sixteen = 0
		self.seventeen = 0
		self.eighteen = 0
		self.nineteen = 0
		self.twenty = 0
		self.twenty_one = 0
		self.twenty_two = 0
		self.twenty_three = 0
		self.twenty_four = 0
		self.twenty_five = 0
		self.twenty_six = 0
		self.twenty_seven = 0
		self.twenty_eight = 0
		self.twenty_nine = 0
		self.thirty = 0
		self.thirty_one = 0
		self.thirty_two = 0
		key = ['卓球 大人', '卓球 小人', 'その他 大人', 'その他 小人', 'バスケ 大人', 'バスケ 小人', 'バレーボール 大人', 'バレーボール 小人', 
		'ショートテニス 大人', 'ショートテニス 小人', 'バドミントン 大人', 'バドミントン 小人', 'ダンス 大人', 'ダンス 小人', '新体操 大人',
		'新体操 小人', '空手 大人', '空手 小人', '剣道 大人', '剣道 小人', '居合道 大人', '居合道 小人', '合気道 大人', '合気道 小人',
		'少林寺 大人', '少林寺 小人', '柔道 大人', '柔道 小人', 'なぎなた 大人', 'なぎなた 小人', 'バトン 大人', 'バトン 小人']
		value = [self.one, self.two, self.three, self.four, self.five, self.six, self.seven, self.eight, self.nine,
		self.ten, self.eleven, self.twelve, self.thirteen, self.fourteen, self.fifteen, self.sixteen, self.seventeen,
		self.eighteen, self.nineteen, self.twenty, self.twenty_one, self.twenty_two, self.twenty_three, self.twenty_four,
		self.twenty_five, self.twenty_six, self.twenty_seven, self.twenty_eight, self.twenty_nine, self.thirty, self.thirty_one,
		self.thirty_two]
		zipped = zip(key, value)
		self.zentai = dict(zipped)
gym = Gym()
def button_tapped_all(sender):
	console.alert(gym.all())
def button_one(sender):
	gym.increment_one()
	console.alert('卓球大追加')
def button_two(sender):
	gym.increment_two()
	console.alert('卓球小追加')
def button_three(sender):
	gym.increment_three()
	console.alert('その他大追加')
def button_four(sender):
	gym.increment_four()
	console.alert('その他小追加')
def button_five(sender):
	gym.increment_five()
	console.alert('バスケ大追加')
def button_six(sender):
	gym.increment_six()
	console.alert('バスケ小追加')
def button_seven(sender):
	gym.increment_seven()
	console.alert('バレーボール大追加')
def button_eight(sender):
	gym.increment_eight()
	console.alert('バレーボール小追加')
def button_nine(sender):
	gym.increment_nine()
	console.alert('ショートテニス大追加')
def button_ten(sender):
	gym.increment_ten()
	console.alert('ショートテニス小追加')
def button_eleven(sender):
	gym.increment_eleven()
	console.alert('バドミントン大追加')
def button_twelve(sender):
	gym.increment_twelve()
	console.alert('バドミントン小追加')
def button_thirteen(sender):
	gym.increment_thirteen()
	console.alert('ダンス大追加')
def button_fourteen(sender):
	gym.increment_fourteen()
	console.alert('ダンス小追加')
def button_fifteen(sender):
	gym.increment_fifteen()
	console.alert('新体操大追加')
def button_sixteen(sender):
	gym.increment_sixteen()
	console.alert('新体操小追加')
def button_seventeen(sender):
	gym.increment_seventeen()
	console.alert('空手大追加')
def button_eighteen(sender):
	gym.increment_eighteen()
	console.alert('空手小追加')
def button_nineteen(sender):
	gym.increment_nineteen()
	console.alert('剣道大追加')
def button_twenty(sender):
	gym.increment_twenty()
	console.alert('剣道小追加')
def button_twenty_one(sender):
	gym.increment_twenty_one()
	console.alert('居合道大追加')
def button_twenty_two(sender):
	gym.increment_twenty_two()
	console.alert('居合道小追加')
def button_twenty_three(sender):
	gym.increment_twenty_three()
	console.alert('合気道大追加')
def button_twenty_four(sender):
	gym.increment_twenty_four()
	console.alert('合気道小追加')
def button_twenty_five(sender):
	gym.increment_twenty_five()
	console.alert('少林寺大追加')
def button_twenty_six(sender):
	gym.increment_twenty_six()
	console.alert('少林寺小追加')
def button_twenty_seven(sender):
	gym.increment_twenty_seven()
	console.alert('柔道大追加')
def button_twenty_eight(sender):
	gym.increment_twenty_eight()
	console.alert('柔道小追加')
def button_twenty_nine(sender):
	gym.increment_twenty_nine()
	console.alert('なぎなた大追加')
def button_thirty(sender):
	gym.increment_thirty()
	console.alert('なぎなた小追加')
def button_thirty_one(sender):
	gym.increment_thirty_one()
	console.alert('バトン大追加')
def button_thirty_two(sender):
	gym.increment_thirty_two()
	console.alert('バトン小追加')
def initialize(sender):
	gym.initialize()
	console.alert('初期化します。')
	
	


v = ui.load_view()
v.present('sheet')
