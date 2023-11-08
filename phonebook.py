def show_menu():
    print('1. Распечатать справочник \n'
    '2. Найти телефон по фамилии \n'
    '3. Изменить номер телефона \n'
    '4. Удалить запись \n'
    '5. Найти абонента по номеру телефона \n'
    '6. Добавить абонента в справочник \n'
    '7. Закончить работу \n')
    choice=int(input())
    return choice

def work_with_phonebook():
    
    choice=show_menu()

    phone_book = read_csv('phonebook.csv')

    while (choice!=7):

        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('Фамилия ')
            res = find_by_lastname(phone_book,last_name)
            print_result(res)
        elif choice==3:
            last_name=input('Фамилия ')
            new_number=input('Новый номер телефона ')
            res = change_number(phone_book,last_name,new_number)
            print_result(res)
        elif choice==4:
            lastname=input('Фамилия ')
            res = delete_by_lastname(phone_book,lastname)
            print_result(res)
        elif choice==5:
            number=input('Номер телефона ')
            res = find_by_number(phone_book,number)
            print_result(res)
        elif choice==6:
            user_data=input('Новый контакт ')
            add_user(phone_book,user_data)
            write_csv('phonebook.csv',phone_book)
        choice=show_menu()

def read_csv(filename):

    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename,'r', encoding='utf-8') as phb:
        
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)

    return phone_book

def write_csv(filename , phone_book):

    with open(filename,'w',encoding='utf-8') as phout:

        for i in range(len(phone_book)):

            s=''  
            for v in phone_book[i].values():
                s+=v+','
            
            phout.write(f'{s[:-1]}')

def print_result(phone_book):
    for i in range(len(phone_book)):
        print(*[f"{x}" for x in phone_book[i].values()], sep = ' ', end = '')
    print('\n')

def find_by_lastname(phone_book, last_name):
    res = []
    for i in range(len(phone_book)):
        if phone_book[i].get('Фамилия')==last_name:
            res.append(phone_book[i])
    return (res)

def change_number(phone_book, last_name, new_number):
    for i in range(len(phone_book)):
        if phone_book[i].get('Фамилия')==last_name:
            phone_book[i]['Телефон']=new_number
    write_csv('phonebook.csv',phone_book)
    return phone_book

def delete_by_lastname(phone_book, last_name):
    a = len(phone_book)-1
    for i in range(len(phone_book)):
        if phone_book[a-i].get('Фамилия')==last_name:
            phone_book.pop(a-i)
    write_csv('phonebook.csv',phone_book)
    return phone_book

def find_by_number (phone_book, number):
    res = []
    for i in range(len(phone_book)):
        if phone_book[i].get('Телефон')==number:
            res.append(phone_book[i])
    return (res)

def add_user(phone_book, user_data):
    filds = ["Фамилия", "Имя", "Телефон", "Примечания"]
    record=dict(zip(filds,user_data.split(',')))
    record['Примечания']+='\n'
    phone_book.append(record)
    return phone_book

work_with_phonebook()