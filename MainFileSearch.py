import os

path = "C:\\Users\\share\\Documents\\CopernicusIsolatedShell\\Projects\\NETAPP_DEV"

for root, dirs, files in os.walk(path):
    for name in files:
        if name.endswith((".bo", ".bco", ".uicomponent")):
            #print(name)
            result = searchterm("THIRDPARTYPRODUCT",os.path.join(root, name))
            if result == True:
                print("THIRDPARTYPRODUCT" + " is found in " + name)

    def searchterm(str,fname):
        with open(fname) as f:
            if str in f.read():
                return True
            else:
                return False
