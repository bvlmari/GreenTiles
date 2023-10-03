import subprocess
import sys

def main():
	a = int(sys.argv[1])
	a += 1
	#iteration
	for x in range(a):
		y = x
		s = f"echo '{y}' | cat > nueve.txt"

		#Seperate cases so it lets us push because is different each time.
		if(x%2)==0:
			GreenScript(s)
		else:
			GreenScriptRev(s)

def GreenScript(s):
	subprocess.run("git pull", shell=True)
	subprocess.run(s, shell=True)
	subprocess.run("git add .", shell=True)
	subprocess.run("git commit -m 'Playa'", shell=True)
	subprocess.run("git push origin main", shell=True)

def GreenScriptRev(s):
	subprocess.run("git pull", shell=True)
	subprocess.run(s, shell=True)
	subprocess.run("git add .", shell=True)
	subprocess.run("git commit -m 'Sol'", shell=True)
	subprocess.run("git push origin main", shell=True)

if __name__ == "__main__":
	main()
