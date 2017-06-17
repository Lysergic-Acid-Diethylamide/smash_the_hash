##example
import sys
import hashlib
import time

def success(passwd):
	print(f"\n Hash smashed:   {passwd}")
	print(" Time completed: {}".format(time.strftime("%H:%M:%S")))
	quit()
#program output
def fail():
	print(f"\n Unable to break {userHash}")
	print(" Time completed: {}".format(time.strftime("%H:%M:%S")))
	quit()

def main(argv):
	charset = "abcdefghijklmnopqrstuvABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
	passwd = ""
	userHash = argv[0] #get hash from user argument

	print(f" Attemping to break {userHash}...")
	print(" Time initiated: {}\n".format(time.strftime("%H:%M:%S")))
	for char in charset:
		for char1 in charset:
			for char2 in charset:
				for char3 in charset:
					for char4 in charset:
						for char5 in charset: #all these loops will cycle through the charset resulting however,
							                #the goal is to use recursion instead of iteration to vary
								        #the number of loops and times the characters will iterate
							passwd=char1+char2+char3+char4+char5
							hash=hashlib.md5(passwd.encode("utf-8")).hexdigest()
							t=time.strftime("%H:%M:%S")
							sys.stdout.write(f"\r |{t}| [{userHash}] : {hash} : {passwd}") #trust me, this
							                                                             #looks 1337 as fuck
							sys.stdout.flush()
							if hash == userHash:
								success(passwd)
	fail()

if __name__ == "__main__":
	main(sys.argv[1:])
