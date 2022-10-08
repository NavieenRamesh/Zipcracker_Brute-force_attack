from termcolor import colored
from tqdm import tqdm
import zipfile

var =""
wordlist = [passwords.strip() for passwords in open("Passwords-dictionary.txt")]
zip_file = zipfile.Zipfile("Sample.zip")

for i in tqdm(wordlist,desc="Checking passwords in a wordlist"):
	try:
		zip_file.extractall(pwd=i.encode())
		var=1
		break
	except:
		continue
print(colored("[+] Password Found: {}".format(var),'green'))