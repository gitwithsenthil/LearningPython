import os
import pandas as pd
import xlsxwriter

print ("Program Starts ........")

filepath = "D:\\Work\\NetApp OneDrive\\OneDrive - NetApp Inc\\294915 - ARCH-Identify the unused objects in the system\\BCO.csv"
path = "C:\\Users\\share\\Documents\\CopernicusIsolatedShell\\Projects\\NETAPP_DEV"

df = pd.read_csv(filepath)
#print(df[['Name']])
sname=[]
bo=[]
ui=[]
absl=[]
tempname=' '
for line in df['Name']:
    txt = line.replace(".bco","")
    bo.append('.')
    ui.append('.')
    sname.append('.')
    absl.append('.')
    if(txt == 'TYPE'):
        txt = 'SUBTYPE_1'
    for root, dirs, files in os.walk(path):
        for name in files:
            valid = False
            if name.endswith(".bo"):
                result = searchterm(txt,os.path.join(root, name))
                if result == True:
                    valid = True
                    bo.append(name)
                    ui.append(' ')
                    absl.append(' ')
            elif name.endswith(".uicomponent"):
                result = searchterm(txt,os.path.join(root, name))
                if result == True:
                    valid = True
                    ui.append(name)
                    bo.append(' ')
                    absl.append(' ')
            elif name.endswith(".absl"):
                result = searchterm(txt,os.path.join(root, name))
                if result == True:
                    valid = True
                    absl.append(name)
                    bo.append(' ')
                    ui.append(' ')
            if name.endswith((".bo",".uicomponent",".absl")) and valid:
                if (tempname != txt):
                    sname.append(txt)
                    tempname = txt
                else:
                    sname.append(' ')

        def searchterm(str,fname):
            with open(fname,encoding="mbcs") as f:
                if str in f.read():
                    return True
                else:
                    return False

d = {'Name':sname,'BO': bo,"UI":ui,"Script File":absl}
#df = pd.DataFrame.from_dict(comps, oreint='index')

df = pd.DataFrame.from_dict(d, orient='index')
df = df.transpose()
writer = pd.ExcelWriter('BCO Analysis V1.xlsx', engine='xlsxwriter')  # pylint: disable=abstract-class-instantiated
df.to_excel(writer, sheet_name='Sheet1')
writer.save()

print("gig")