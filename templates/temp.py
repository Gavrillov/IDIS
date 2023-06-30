from pymongo import *

def update_document(collection, query_elements, new_values):
    """ Function to update a single document in a collection.
    """
    collection.update_one(query_elements, {'$set': new_values})
def find_document(collection, elements, multiple=False):
    """ Для извлечения одного или нескольких документов,
    с использованием словаря, содержащего элементы документа.
    """
    if multiple:
        results = collection.find(elements)
        return [r for r in results]
    else:
        return collection.find_one(elements)

# Создание клиента
client = MongoClient('localhost', 27017)

# Подключение к базе
db = client['Documents']

# Наша коллекцию
series_collection = db['Employees']

print("Фамилия сотрудника: ")
employeer_surname = input()

print("Имя сотрудника: ")
employeer_name = input()

print("Отчество сотрудника: ")
employeer_patronymic = input()

print("телефон: ")
employeer_telephone = input()

print("Электронная почта: ")
employeer_mail = input()
documents = []
for a in range (2,0,-1):
    print("Тип документа: ")
    type_document = input()

    print("Документ: ")
    document = input()


    documents.append({"type_documents": type_document,"document": document})
#print(documents)


employeer = {
    "surname": employeer_surname,
    "name": employeer_name,
    "name": employeer_patronymic,
    "telephone": employeer_telephone,
    "mail" : employeer_mail,
    "documents" : documents
    }


# Кидаем в базу
series_collection.insert_one(employeer).inserted_id


for channale in series_collection.find():
    print(channale)
    emp_len = len(channale)

print("")

#pri = find_document(series_collection,{'surname': 'w','name' : 'w'} )

#print(pri)

print("Фамилия сотрудника: ")
employeer_surname = input()

print("Имя сотрудника: ")
employeer_name = input()

print("Отчество сотрудника: ")
employeer_patronymic = input()

print("телефон: ")
employeer_telephone = input()

print("Электронная почта: ")
employeer_mail = input()
documents = []
for a in range (2,0,-1):
    print("Тип документа: ")
    type_document = input()

    print("Документ: ")
    document = input()


    documents.append({"type_documents": type_document,"document": document})
#print(documents)


employeer = {
    "surname": employeer_surname,
    "name": employeer_name,
    "name": employeer_patronymic,
    "telephone": employeer_telephone,
    "mail" : employeer_mail,
    "documents" : documents
    }

update_document(series_collection,{'surname': 'zzz','name' : 'zzz'},{'mail': '789456123'})
