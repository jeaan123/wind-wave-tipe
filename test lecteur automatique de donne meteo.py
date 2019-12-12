import csv
#import urllib.request



#url = "https://www.ndbc.noaa.gov/data/realtime2/62163.txt"
#url = "https://www.ndbc.noaa.gov/view_text_file.php?filename=42039h2018.txt.gz&dir=data/historical/stdmet/"
directory='/Users/jean/Desktop/tipe2/donne/satt2.csv'
direc='/Users/jean/Desktop/tipe2/donne/station2.csv'
#urllib.request.urlretrieve(url,directory)
file = open(directory, "r")
windD,windS,taillevague,periode,pression,temperature=[],[],[],[],[],[]
L=[]

reader = csv.reader(file)
for row in reader:
   #print(row)
   a=str(row).split()
   #print('wind dir(deg)=',a[5],'wind speed(m/s)=',a[6],'taille vague(m)=',a[8],'periode(sec)=',a[10],'pression(hpa)=',a[12])
   windD.append((a[5]))
   windS.append((a[6]))
   taillevague.append((a[8]))
   periode.append((a[10]))
   pression.append((a[12]))
   temperature.append((a[14]))
   L.append([a[6],a[8],a[10],a[12],a[14],a[5]])
   #[vitesse vent, taille, peridoe, pression, temp,direction]
file.close()

with open(direc, 'w', newline='') as f:
   writer = csv.writer(f)
   writer.writerows(L[2:])

   

