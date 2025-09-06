def choice():
    print('1.entry')
    print('2.view')
    print('3.update')
    print('4.delete')
    print('5.quit')
    
    
my_choice=0
         
entries={}
choice()
while my_choice!=5:

    my_choice=int(input('enter your choice:'))

    if my_choice == 1:
         print("enter your choice")
         name=input('name:')
     
         entries[name]=int(input('number:'))
         
    elif my_choice== 2:
         print("enter your choice")
         name=input('name:')
         if name in entries:
             print('---------------------------------')
             print(name  ,  '||',entries[name])
         else:
             print(name,'was not found')
   
    elif my_choice==3:
        print("enter number to update")
        entries[name]=int(input('number:'))
        
    elif my_choice==4:
        print('enter name to delete')
        name=input("name:")
        if name in entries:
            del entries[name]
        else:
            print(name,'was not found')
    elif my_choice==5:
        exit()
        
