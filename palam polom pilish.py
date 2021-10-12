import sys
import random
print('welcome!!')
while True:
    pc1 = random.randint(2,3 )
    pc2 = random.randint(2,3 )
    karbar = int(input())
    if pc1==pc2==karbar:
        print("har 3 yeksan")
    elif pc1 !=pc2 and karbar==pc1:
        print("pc2 loser")
    elif pc1 !=karbar and pc1==pc2:
        print("karbar loser") 
    elif pc1 !=pc2 and karbar==pc2:
        print("pc1 loser")
    elif karbar!=2 or karbar!=3 :
        print("not found")
        sys.exit(0)      
