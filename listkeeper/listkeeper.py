import os

def main():
	dirty = False
	filename, items = choose_file()
	show_list(items)

	while True:
		choice = get_choise(items, dirty)
		if choice in "Aa":
			dirty = add_item(items, dirty)
		elif choice in "Dd":
			dirty = delete_item(items, dirty)
		elif choice in "Ss":
			dirty = save_file(filename, items, dirty)
		elif choice in "Qq":
			break
		
		if dirty:
			show_list(items)



#########
def choose_file():
	items = []
	filename = input("choose_file:      ")

	for item in open(filename, encoding="utf-8"):
		items.append(item.strip())
	
	return filename, items


def show_list(items):
	if not items:
		print("--no items are in the list--\n")
	else:
		for lineno, item in enumerate(items, start = 1):
			print(lineno, item)
		print()


#######
def get_choise(items, dirty):
	message = ""
	valid_choice = "AaQq"
	if dirty:
		valid_choice += "Ss"
		if items:
			valid_choice += "Dd"
			message = "[A]dd [D]elete [S]ave [Q]uit [a]:"
		else:
			message = "[A]dd [S]ave [Q]uit [a]:"
	else:
		if items:
			valid_choice += "Dd"
			message = "[A]dd [D]elete [Q]uit [a]:"
		else:
			message = "[A]dd [Q]uit [a]:"
	
	while True:
		choice = input(message)
		if choice in valid_choice:
			return choice
		else:
			print("ERROR: invalid choice.")

			

#######
def add_item(items, dirty):
	item = input("Add item:")
	items.insert(0, item)
	dirty = True

	return dirty

######
def delete_item(items, dirty):
	assert items, "The list is empty."

	lineno = input("Delete item number (or 0 or just enter to cancel):")
	try:
		lineno = int(lineno)
		if lineno > 0 or lineno <= len(items):
			items.pop(lineno - 1)
			dirty = True
	except ValueError as err:
		print("Error {0} must be an integer.")
	
	
	return dirty

######
def save_file(filename, items, dirty):
	if not dirty:
		print("It is already newest.")
		return dirty
	else:
		fh = open(filename, "w", encoding="utf-8")
		for item in items:
			fh.write(item + "\n")
		fh.close()
	
	return False
	

main()

