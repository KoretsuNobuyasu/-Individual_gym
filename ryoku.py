import ui
import console

class Hunter:
	def __init__(self):
		self.head = 'nothing'
		self.chest = 'nothing'
		self.arm = 'nothing'
		self.leggings = 'nothing'
		key = ['head','chest','arm','leggings']
		value = [self.head, self.chest, self.arm, self.leggings]
		zipped = zip(key, value)
		self.zenshin = dict(zipped)

	def change_head(self,head_name):
		self.head = head_name
	def change_head_non(self):
		self.head = 'nothing'

	def change_chest(self,chest_name):
		self.chest = chest_name
	def change_chest_non(self):
		self.chest = 'nothing'
		
	def change_arm(self,arm_name):
		self.arm = arm_name
	def change_arm_non(self):
		self.arm = 'nothing'
		
	def change_leggings(self,leggings_name):
		self.leggings = leggings_name
	def change_leggingd_non(self):
		self.leggings = 'nothing'
		
		
	def initialize(self):
		self.head = 'nothing'
		self.chest = 'nothing'
		self.arm = 'nothing'
		self.leggings = 'nothing'
		key = ['head','chest','arm','leggings']
		value = [self.head, self.chest, self.arm, self.leggings]
		zipped = zip(key, value)
		self.zenshin = dict(zipped)
		
		
		
		
	def all(self):
		self.zenshin['head'] = self.head
		self.zenshin['chest'] = self.chest
		self.zenshin['arm'] = self.arm
		self.zenshin['leggings'] = self.leggings
		return "\n".join(["{0}={1}".format(key, value) for (key, value) in self.zenshin.items()])




	





hunter = Hunter()

def button_tapped_all(sender):
	console.alert(hunter.all())
	



def button_change_reus_head(sender):
	if hunter.head == 'レウスヘルメット':
		hunter.change_head_non()
		console.alert('レウスヘルメットを脱ぎました')
	else:
		hunter.change_head('レウスヘルメット')
		console.alert('レウスヘルメットに変更しました。')
	
	
def button_change_reus_chest(sender):
	if hunter.chest == 'レウスチェスト':
		hunter.change_chest_non()
		console.alert('レウスチェストを脱ぎました')
	else:
		hunter.change_chest('レウスチェスト')
		console.alert('レウスチェストに変更しました。')


def button_change_reus_arm(sender):
	if hunter.arm == 'レウスアーム':
		hunter.change_arm_non()
		console.alert('レウスアームを脱ぎました')
	else:
		hunter.change_arm('レウスアーム')
		console.alert('レウスアームに変更しました。')


def button_change_reus_leggings(sender):
	if hunter.leggings == 'レウスレギンス':
		hunter.change_leggingd_non()
		console.alert('レウスレギンスを脱ぎました')
	else:
		hunter.change_leggings('レウスレギンス')
		console.alert('レウスレギンスに変更しました。')

def button_change_reia_head(sender):
	if hunter.head == 'レイアヘルメット':
		hunter.change_head_non()
		console.alert('レイアヘルメットを脱ぎました')
	else:
		hunter.change_head('レイアヘルメット')
		console.alert('レイアヘルメットに変更しました。')
	
	
def button_change_reia_chest(sender):
	if hunter.chest == 'レイアチェスト':
		hunter.change_chest_non()
		console.alert('レイアチェストを脱ぎました')
	else:
		hunter.change_chest('レイアチェスト')
		console.alert('レイアチェストに変更しました。')


def button_change_reia_arm(sender):
	if hunter.arm == 'レイアアーム':
		hunter.change_arm_non()
		console.alert('レイアアームを脱ぎました')
	else:
		hunter.change_arm('レイアアーム')
		console.alert('レイアアームに変更しました。')


def button_change_reia_leggings(sender):
	if hunter.leggings == 'レイアレギンス':
		hunter.change_leggingd_non()
		console.alert('レイアレギンスを脱ぎました')
	else:
		hunter.change_leggings('レイアレギンス')
		console.alert('レイアレギンスに変更しました。')

def initialize(sender):
	hunter.initialize()
	console.alert('初期化します。')
	
	


v = ui.load_view()
v.present('sheet')
