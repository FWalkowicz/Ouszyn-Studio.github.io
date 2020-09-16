import os
os.chdir("Animations")
for fi in os.listdir():
	if os.path.isdir(fi):
		print(fi)

