#НЕ РЕКУРСИВНЫЙ ПРОХОД (ИЗМЕНЕНИЕ) НЕГЛУБОКОГО ДЖЕЙСОНА
#дикт!  лист!  дикт!  лист  дикт!  строка
#                     дикт!	
#                     строка	
def non_recursive(appearance_file):
	with open(appearance_file, 'r', encoding='utf-8') as file:
		data = json.load(file) #дикт!строго

	storables = []
	for storable in data["storables"]:	#лист!строго
		items = {}
		for k,v in storable.items(): 	#дикт!строго
			if isinstance(v, list): #list, dict, str
				substorables = []
				for value in v: 		
					if isinstance(value, dict): #лист!строго
						subitems = {}
						for k, v in value.items(): # str
							if ':/' in v:
								print(v) # тут подменяем перед записью!!!!!!!!!!!!!!!!!!!!!!
								subitems[k] = v
							else:
								subitems[k] = v
						substorables.append(subitems)
				items[k] = substorables
			elif isinstance(v, dict): #list, dict, str
				subitems = {}
				for k,v in v.items():
					if ':/' in v:
						print(v) # тут подменяем перед записью!!!!!!!!!!!!!!!!!!!!!!
						subitems[k] = v
					else:
						subitems[k] = v
				items[k] = subitems
			elif isinstance(v, str): #list, dict, str
				if ':/' in v:
					print(v) # тут подменяем перед записью!!!!!!!!!!!!!!!!!!!!!!
					items[k] = v
		storables.append(items)
