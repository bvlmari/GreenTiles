import os

#iteration
for x in range(10):
	#Seperate cases so it lets us push because is different each time.
	if(x%2)==0:
		os.system("git pull")
		os.system("echo '1' | cat > nueve.txt")
		os.system("git add .")
		os.system("git commit -m 'Playa'")
		os.system("git push origin main")
	else:
		os.system("git pull")
		os.system("echo '2' | cat > nueve.txt")
		os.system("git add .")
		os.system("git commit -m 'Sol'")
		os.system("git push origin main")