import shared as sh
import re
sh.afunction()


def space_compress(str_in:str):
	"""
	Take a spring and return a string with no whitespaces

	Args:
		- str_in(str): string to remove whitespace
	"""
	if type(str_in) != str:
		return "Expected string but got {}".format(dtype(str_in))

	else:
		# replace multiline string with one-line string
		str_out = str_in.replace('\n',"")

		# reduce multiple whitespaces into one white space
		str_out = " ".join(str_out.split())

		return str_out

# if __name__=="__main__":
# 	txt = input("test inputs: ")
# 	print(space_compress(txt))
