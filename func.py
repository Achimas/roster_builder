class Detachment ():
	all_types = ['HQ', 'Troops', 'Elites', 'FA', 'HS', 'DT', 'LoW', 'Flyer']
	def __init__(self, name='Patrol', faction='Leagues of Votann', CP=0, restricts=patrol):
		self.detachment_name = name
		self.detachment_faction = faction
		self.detachment_CP_count = CP
		self.detachment_restricts = restricts		
		self.detachment_units = []
		self.detachment_units_types = []
		self.restrictions = ''
		self.notifications = {}

	def add_unit(self, unit_class_object)
		self.detachment_units.append(unit_class_object)
		self.detachment_units_types.append(unit_class_object.type)

	def display_all_units(self):
		with open(f'{self.detachment_name}new.txt', 'w') as file:
			for searcheable_type in all_types:
				for unit in self.detachment_units:
					if unit.type == searcheable_type:
						unit_description = unit.display()
						file.write(unit_description)
				file.write('\n')

	def check_restricts(self):
		for type in all_types:
			if detachment_units_types.count(type) < self.restrictions[f'min_{type}']:
				self.notifications.add(f'{type} is less than needed')
			elif detachment_units_types.count(type) > self.restrictions[f'max_{type}']:
				self.notifications.add(f'{type} is more than needed')

	def display_notifications(self):
		with open(f'{self.detachment_name}new.txt', 'w') as file:
			for n in self.notifications:
				file.write(n)
			file.write('\n')

class Unit ():
	def __init__(self, count=0, name='', total_points=0, type='Troops'):
		self.name = name
		self.count = count
		self.wargear = []
		self.type = type
		self.total_points = total_points

	def set_wargear(self, wargear_name, num=1, cost=0):
		if count == 1:
			wargear = wargear_name
		else:
			wargear = str(count) + wargear_name
		self.wargear.append(wargear)
		self.total_points += num*cost

	def display(self):
		shown_wargear = ', '.join(self.wargear)
		unit_displaying = f'{self.type}: {self.count} {self.name}, {shown_wargear} [{self.total_points}]'
		return unit_displaying

def main():
	...

if __name__ == '__main__':
	main()
