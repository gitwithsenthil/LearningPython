import os
import pandas

print ("Program Starts ........")

filepath = "D:\\Work\\NetApp OneDrive\\OneDrive - NetApp Inc\\294915 - ARCH-Identify the unused objects in the system\\BCO.csv"
path = "C:\\Users\\share\\Documents\\CopernicusIsolatedShell\\Projects\\NETAPP_DEV"
log = open("log.txt","w+")

df = pandas.read_csv(filepath)
#print(df[['Name']])
def searchterm(str,fname):
    ret = False
    with open(fname) as f:
        if str in f.read():
            ret = True
        f.close()
    return ret
        

for line in df['Name']:
    txt = line.replace(".bco","")
    log.write("Searching...."+ txt + "\n")
    #print("Searching ... " + txt)

    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith((".bo", ".bco",".uicomponent")):
                #print("Entering -> "+name)
                #log.write("\t Entering -> "+name + "\n")
                pos = name.find(".")
                mname = name[0:pos]
                #print(mname)
                result = searchterm(txt,os.path.join(root, name))
                if result == True:
                    print("\t" + txt + " is found in " + name)
                    log.write(txt + " is found in " + name+ "\n")


log.close()
print("Program ended")