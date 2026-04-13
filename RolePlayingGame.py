#RolePlayingGame.py

class Character:
	def __init__(self,name,hp,level):
		self.name = name
		self.hp = hp
		self.level = level


class NPC(Character):
	def speak():
		return f"the {character} says {lang}"




villager = NPC("Bob", 100, 12)
villager.name  # Bob
villager.hp  # 100
villager.level  # 12
villager.speak()  # "I heard there were monsters running around last night!".
