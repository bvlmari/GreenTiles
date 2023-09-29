import subprocess

#iteration
for x in range(10):
	#Seperate cases so it lets us push because is different each time.
	if(x%2)==0:
		subprocess.run(["git","pull"])
		subprocess.run(["echo","1","|","cat",">","nueve.txt"])
		subprocess.run(["git","add","."])
		subprocess.run(["git","commit","-m",'"playa"'])
		subprocess.run(["git","push","origin",'main'])
	else:
		subprocess.run(["git","pull"])
		subprocess.run(["echo","2","|","cat",">","nueve.txt"])
		subprocess.run(["git","add","."])
		subprocess.run(["git","commit","-m",'"sol"'])
		subprocess.run(["git","push","origin",'main'])