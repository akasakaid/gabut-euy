import os
from concurrent.futures import ThreadPoolExecutor

# ribet ye kan :v 
save = lambda x:open("remove_subdo_result.txt","a+").write(f"{x}\n")

def remove(target):
	subdo = open("subdo.txt").read().splitlines()
	target = target.split(".")
	if target[0] == "www":
		del target[0]
	if target[0] in subdo:
		del target[0]
	save(".".join(target))

os.system("cls" if os.name == "nt" else "clear")
print("""
######################
### AkasakaID Gans ###
######################
	""")
try:
	sitelist = open(input("# list site : ")).read().splitlines()
	with ThreadPoolExecutor(max_workers=int(input("# thread : "))) as pepek:
		for site in sitelist:
			pepek.submit(remove,site)
except FileNotFoundError:
	exit("File Not Found !")
except KeyboardInterrupt:
	exit()
except ValueError:
	exit("input only number for thread !")