import os
import re
File = os.listdir(("C:/Users/Daniela/Desktop/SecretKey"))
os.chdir("C:/Users/Daniela/Desktop/SecretKey")
for i in range(len(File)):
    nombres=File[i]
    s=File[i]
    s1= re.sub("[0-9]","",s)
    os.rename(File[i],s1)
    File[i]=s1

print(File)
