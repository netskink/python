#!/usr/bin/python3

import sys
import os.path


entry_list=[]

## option flags ######################
option_print_classification=False
option_print_long=False


def parse_args():
	for i in range(len(sys.argv)):
		if (i == 0):
			# skip the ls command
			continue
		if (sys.argv[i].startswith("-")):
			parse_option(sys.argv[i])
			continue
		entry_list.append(sys.argv[i])


#           S_IRWXU    00700     mask for file owner permissions
#           S_IRUSR    00400     owner has read permission
#           S_IWUSR    00200     owner has write permission
#           S_IXUSR    00100     owner has execute permission
#           S_IRWXG    00070     mask for group permissions
#           S_IRGRP    00040     group has read permission
#
#           S_IWGRP    00020     group has write permission
#           S_IXGRP    00010     group has execute permission
#           S_IRWXO    00007     mask for permissions for others (not in group)
#           S_IROTH    00004     others have read permission
#           S_IWOTH    00002     others have write permission
#           S_IXOTH    00001     others have execute permission


def print_prefix(entry):
	if (option_print_long):
		stat_info = os.stat(entry)
		print("%o " % stat_info.st_mode,end="")
		print("\t%s " % stat_info.st_size,end="")
		print("\t ",end="")

def print_suffix(entry):
	if (option_print_classification):
		if (os.path.isfile(entry)):
			print("",end="")
		elif (os.path.isdir(entry)):
			print("/",end="")



def print_lists():
	# a way to do this is build up a suffix based upon the type 
	# and then always print the suffix.
	for i in range(len(entry_list)):
		print_prefix(entry_list[i])
		print("%s" % entry_list[i],end="")
		print_suffix(entry_list[i])
		if (option_print_long):
			print(" ")
		else:
			print(" ",end="")



def parse_option(option_str):
	global option_print_classification
	global option_print_long
	#just_the_option=option_str.lstrip('-')	# we dont need to use this since, we can use "in" operator
	if ("F" in option_str):
		option_print_classification=True
	if ("l" in option_str):
		option_print_long=True
		

def print_usage():
    print('Usage {:s}, [-options] [file]'.format(sys.argv[0]))
    print('\t-h\t prints help text')
    print('\t-F\t prints classification')
    print('\t-l\t prints long list')


## main ##############################

if (len(sys.argv) == 1):
	entry_list.append(".")


if (len(sys.argv) > 1):
	parse_args()





print_lists()




# this will list all files and directories in the current
# directory. It can be called with a parameter for 
# specific directory.
#for entries in os.listdir():
#	print(entries)

#for i in range(len(entry_list)):
#	print("xxxx %s " % entry_list[i],end="")
#



#print()
#http://docs.python.org/3/library/os.html
#for dirname, dirnames, filenames in os.walk('.'):
#	for filename in filenames:
#		print(os.path.join(dirname,filename))


sys.exit()


# get list of files in directory
os.listdir(path)

os.path.isfile()
os.path.isdir()



