import random
import arff

w, h = 5, 50
Res=[0]*50
Matrix = [[0 for x in range(w)] for t in range(h)]

for x in range(0,50):
    for z in range(0, 5):
       Matrix[x][z]=random.randint(0,1)



for p in range(0,50):
   Res[p]=(Matrix[p][0]&Matrix[p][1])|(Matrix[p][1]&Matrix[p][2])|(Matrix[p][2]&Matrix[p][3])





fileName='result.arff'
strs = ["" for x in range(50)]

for x in range (0,50):
    if Res[x]==1:
        strs[x]="yes"
        print(strs[x])
    else:
        strs[x]="no"



arff_writer = arff.Writer(fileName, relation='whatever', names=['pattern1', 'pattern2','pattern3','pattern4','pattern5', 'Label'])
arff_writer.pytypes[arff.Nominal] = '{yes,no}'
for y in range(0, 50):
 arff_writer.write([Matrix[y][0],Matrix[y][1],Matrix[y][2],Matrix[y][3],Matrix[y][4],arff.Nominal(strs[y])])

