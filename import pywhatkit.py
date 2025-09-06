def choice():
    print('1.entry')
    print('2.view')
    print('3.update')
    print('4.delete')
    print('5.quit')
    
    entries={}
    my_choice=input('enter your choice:')
    if my_choice==1:
        print("enter your choice")
        name=input('name:')
        entries[name]=input('number:')
choice()