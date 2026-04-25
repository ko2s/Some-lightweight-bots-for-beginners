import os
source_folder = (os.getcwd())
files = [f for f in os.listdir(source_folder) if f.endswith(('.py', '.json', '.env'))]
path = os.listdir(source_folder)
class Os_fildar:
    def __init__(self) -> None:
        pass
    def fldar_now (self):
        """
        دالة جلب اسماء الملفات في الملف المحلي
        """
        self.source_folder = (os.getcwd())
        self.path = os.listdir(self.source_folder)
        return self.path 
    def sarch_fldar_now(self,opaek):
        """دالة عرض اسماء الملفات المحدداده"""
        self.opaek = opaek
        self.source_folder = (os.getcwd())
        self.files = [f for f in os.listdir(source_folder) if f.endswith((self.opaek))]
        return self.files
    def sarch_path(self,path,opaek):
        self.path = path
        self.opaek = opaek
        self.files = [f for f in os.listdir(self.path) if f.endswith((self.opaek))]
        return self.files
    
c = Os_fildar()
f = c.sarch_fldar_now("")
for i in f:
    if i == "aqila.py":
        
        fl = open(i,"r")
        print(fl.read())
        fl.close()

