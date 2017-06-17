#Author: tripp
#Desc: takes in a bunch of hashes and will attempt to decrypt them

import sys, getopt, hashlib,time

def main(argv):

	print
	
	charset	 	= ""
	encryption 	= ""
	hashFile 	= ""
	outputFile 	= ""
	minLength 	= 0
	maxLength 	= 0
	variedChars = 0
	userCharset = False
	verbrose 	= False
	userHash 	= []
	supportedAlgorithims = []

	#Getting the date to make the output file more identifiable
	outputFileName = time.strftime("%a::%H:%M:%S.txt")
	
	#Command line argument crap
	try:
		opts, args = getopt.getopt(argv, "h:i:e:c:m:l:o:v", ["if=", "of=","charset=", "help"])
		
	except getopt.GetoptError as e:
		print(("Option {} not recognised, please use '--help' for program usage").format(e))
		sys.exit(2)
		
	for opt, arg in opts:
		if opt == "--help":
			print
			print("Smash The Hash   [v1.0]")
			print("_______________________")
			print("Options:")
			print("--help			To display help information")
			print("-h				Hash to be broken")
			print("-e				Encryption type")
			print("-v				To set output mode to verbrose (useful for debugging)")
			print("-i --if			Input file for hashes")
			print("-o --of			Output file for cracked hashes")
			print("-c --charset		To define a custom charset")
			print("-m --min			To set the min length of the password")
			print("-l --max 		To set the max length of the password")
			print
			print("Usage:")
			print("STH.py if=passwords/hashes.txt of=cracked.txt -v")
			print("STH.py -h 5f4dcc3b5aa765d61d8327deb882cf99 -e md5")
			print
			print("Developed by: Tripp")
			print("For additional information visit http://www.utterdinosaur.com")
			print
			
			sys.exit(2)
		elif opt == "-h":
			userHash.append(arg)
			
		elif opt in ("-i, --if"):
			hashFile = arg
		
		elif opt == "-e":
			encryption = arg.lower
			
		elif opt in ("-c", "--charset"):
			charset = arg
			userCharset = True
			
		elif opt == "-m":
			minLength = int(arg)
		
		elif opt == "-l":
			maxLength = int(arg)
		
		elif opt in ("-o", "--of"):
			outputFile = arg
			
		elif opt == "-v":
			verbrose = True
	
	
	#Header
	print("---------------------------------------------------------------")
	print("- ___               _      _____ _          _  _         _    -")    
	print("-/ __|_ __  __ _ __| |_   |_   _| |_  ___  | || |__ _ __| |_  -")  
	print("-\__ \ '  \/ _` (_-< ' \    | | | ' \/ -_) | __ / _` (_-< ' \\ -") 
	print("-|___/_|_|_\__,_/__/_||_|   |_| |_||_\___| |_||_\__,_/__/_||_|-")
	print("---------------------------------------------------------------")                                                              
	print
	
	# Checking if all options are valid
	if not userHash and not hashFile:
		print("Error - no hash(es) supplied, use -h or -i\nfor more information use --help")
		sys.exit(2)
	
	elif not encryption:
		print("Error - no encryption type supplied, use -e\nfor more information use --help")
		sys.exit(2)
	
	elif not minLength or not maxLength:
		print("Error - either no minimum length or maximum length supplied, use -m and -l\nfor more information use --help")
		sys.exit(2)
	
	#Alerting user of non vital options
	if not userCharset:
		print("[!]   No custom charset supplied using predefined alphanumeric list")
	
	if not outputFile:
		print("[!]   No output file supplied, outputting to terminal and 'cracked/{}'").format(outputFileName)
		
	print
	print("[*]   Cracking...")
	print
	
	#Calcuating the length of the desired password	
	variedChars = maxLength - minLength
	
	#Getting supported Algorithims
	fi = open("resources\\supported_algorithims.txt","r")
	for line in fi:
		supportedAlgorithims.append(line)
	fi.close()
	
	#Getting hashes from userdefined hash file
	if hashFile:
		fi = open(hashFile,"r")
		for line in fi:	
			userHash.append(line)
		fi.close()
	
	fo = open(outputFile,"w")
	
	#Is algorithm supported?
	for encryption in supportedAlgorithims:
		if encryption == "md5":
			md5Crack(charset, userHash, variedChars, minLength, maxLength, verbrose)
			
		elif encryption == "sha128":
			sha128Crack(charset, userHash, variedChars, minLength, maxLength, verbrose)
			
		elif encryption == "sha256":
			sha256Crack(charset, userHash, variedChars, minLength, maxLength, verbrose)
			
		elif encryption == "base64":
			base64Decode(charset, userHash, variedChars, minLength, maxLength, verbrose)
		
		else:
			print(("Error - {} is not supported by STH").format(encryption))
			

#def md5Crack(charset, userHash, variedChars, minLength, maxLength, verbrose):
#	 generate_array(charset, variedChars)
	
if __name__ == "__main__":
	main(sys.argv[1:])