import argparse
import os
import datetime

def parse_arg():
	order_choice = ['name','n', 'modified', 'm', 'size', 's']
	parser = argparse.ArgumentParser(description='list item in directory')
	parser.add_argument('-H', '--hidden', action='store_true')
	parser.add_argument('-m', '--modified', action='store_true')
	parser.add_argument('-o', '--order',  type=str, choices=order_choice, default='name')
	parser.add_argument('-r', '--recursive', action='store_true')
	parser.add_argument('-s', '--size', action='store_true')
	parser.add_argument("directory", type=str, nargs="*")

	args = parser.parse_args()
	return args


def get_list(args):
	items = []

	if args.recursive:
		pass
	else:
		for d in args.directory:
			for item in os.listdir(d):
				fullname = os.path.join(d, item)
				if fullname.startswith('./'):
					fullname = fullname[2:]	
				items.append(fullname)
	return items

def process_list(items, args):
	count = [0, 0]
	for item in items:
		line = ""
		modified = ""
		size = ""
	
		if os.path.isfile(item):
			if args.modified:
				modified = (datetime.datetime.fromtimestamp(os.path.getmtime(item)).isoformat(" ")[:19] + " ")
			if args.size:
				size = "{0:>15n}".format(os.path.getsize(item))
			if os.path.islink(item):
				item += "-> " + os.path.realpath(item)
			line = modified + size + " " + item
			count[0] += 1
		else:
			count[1] += 1
			modified = "" if not args.modified else " " * 20
			size = "" if not args.size else " " * 15
			line = modified + size + " " + item
		
		print(line)
	
	




def main():
	args = parse_arg()
	if not len(args.directory):
		args.directory += ['.']
		
	items = get_list(args)
	process_list(items, args)


main()
