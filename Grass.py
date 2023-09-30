import subprocess
import sys

a = int(sys.argv[1])

#iteration
for x in range(a):
	y = x
	s = f"echo '{y}' | cat > nueve.txt"

	#Seperate cases so it lets us push because is different each time.
	if(x%2)==0:
		subprocess.run("git pull", shell=True)
		subprocess.run(s, shell=True)
		subprocess.run("git add .", shell=True)
		subprocess.run("git commit -m 'Playa'", shell=True)
		subprocess.run("git push origin main", shell=True)
	else:
		subprocess.run("git pull", shell=True)
		subprocess.run("echo '2' | cat > nueve.txt", shell=True)
		subprocess.run("git add .", shell=True)
		subprocess.run("git commit -m 'Sol'", shell=True)
		subprocess.run("git push origin main", shell=True)