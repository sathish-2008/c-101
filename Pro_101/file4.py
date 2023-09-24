import random

res = input("Press y to roll a dice:   ") 

if res != 'y':
    print("!!! Invalid Input Try Again !!!")

while res == "y" :
    no = random.randint(1,6)
    no = int(no)
   
    if no == 1 :
        print(['     '])
        print(['  0  '])
        print(['     '], end = "  ")    
        que = input("Enter y to continue and n to exit:  ")
        res == que
        
    if no == 2 :
        print(['    0'])
        print(['     '])
        print(['0    '], end = "  ")  
        que = input("Enter y to continue and n to exit:  ")
        res == que

    if no == 3 :
        print(['    0'])
        print(['  0  '])
        print(['0    '], end = "  ")   
        que = input("Enter y to continue and n to exit:  ")
        res == que

    if no == 4 :
        print(['0   0'])
        print(['     '])
        print(['0   0'], end = "  ")   
        que = input("Enter y to continue and n to exit:  ")
        res == que

    if no == 5 :
        print(['0   0'])
        print(['  0  '])
        print(['0   0'], end = "  ")  
        que = input("Enter y to continue and n to exit:  ")
        res == que

    if no == 6 :
        print(['0 0 0'])
        print(['     '])
        print(['0 0 0'], end = "  ")    
        que = input("Enter y to continue and n to exit:  ")
        res == que

    if(res == 'n'):
        print("asdfc")
        break    
    


        
    
  



 

    
    
       



    

   

       
