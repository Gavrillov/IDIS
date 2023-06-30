from flask import Flask, request, redirect
from flask import render_template
from pymongo import MongoClient
from bson import ObjectId
import base64

app = Flask(__name__)


# Подключение к MongoDB
client = MongoClient('localhost', 27017)
db = client['Documents']  #имя вашей базы данных
collection = db['Employees']  #имя вашей коллекции


@app.route('/')
def index():
    # Получение данных из базы данных
    users = collection.find()

    # Передача данных в шаблон для отображения
    return render_template('main.html', users=users)

@app.route('/user/<string:user_id>')
def user(user_id):
    # Поиск пользователя по object _id
    user = collection.find_one({'_id': ObjectId(user_id)})

    if user:
        return render_template('user.html', user=user)
    else:
        return 'Пользователь не найден'


@app.route('/user/<user_id>/edit', methods=['POST'])
def edit_user(user_id):
    # Получение данных из формы
    surname = request.form['surname']
    name = request.form['name']
    telephone = request.form['telephone']
    mail = request.form['mail']

    # Обновление данных пользователя в базе данных
    collection.update_one({'_id': ObjectId(user_id)}, {'$set': {
        'surname': surname,
        'name': name,
        'telephone': telephone,
        'mail': mail
    }})

    return redirect('/user/' + user_id)


@app.route('/user/<user_id>/remove', methods=['POST'])
def remove_employee(user_id):

    # Преобразуем строковый user_id в ObjectId
    employee_id = ObjectId(user_id)

    # Удаляем пользователя
    collection.delete_one({'_id': employee_id})

    users = collection.find()
    return render_template('main.html', users=users)


@app.route('/user/<user_id>/delete', methods=['POST'])
def delete_document(user_id):
    type_documents_to_delete = request.form['type_documents']
    document_to_delete = request.form['document']

    # Поиск пользователя по user_id
    user = collection.find_one({'_id': ObjectId(user_id)})
    if user:
        # Поиск и удаление документа по заданным значениям
        for document in user['documents']:
            if document['type_documents'] == type_documents_to_delete and document['document'] == document_to_delete:
                user['documents'].remove(document)
                break

        #file_path = os.path.join(app.config['UPLOAD_FOLDER'], document_to_delete)  # Полный путь к файлу
        #os.remove(file_path)  # Удалить файл

        # Обновление документа в базе данных
        collection.update_one({'_id': ObjectId(user_id)}, {'$set': user})


    return redirect('/user/' + user_id)


@app.route('/user/<user_id>/append', methods=['POST'])
def upload(user_id):
    type_documents = request.form['type_documents']
    document = request.files['document']

    # Читаем содержимое файла и сохраняем его в MongoDB
    file_content = document.read()
    encoded_content = base64.b64encode(file_content)

    data = {
        'type_documents': type_documents,
        'document': encoded_content.decode('utf-8')  # Сохраняем закодированное содержимое файла
    }

    collection.update_one({'_id': ObjectId(user_id)}, {'$push': {'documents': data}})

    return redirect('/user/' + user_id)

@app.route('/add_employee', methods=['POST'])
def add_employee():
    data = request.form  # Получение данных из POST-запроса

    # Извлечение данных о сотруднике
    surname = data.get('surname')
    name = data.get('name')
    telephone = data.get('telephone')
    mail = data.get('mail')
    documents = []

    employeer = {
        "surname": surname,
        "name": name,
        "telephone": telephone,
        "mail": mail,
        "documents": documents
    }

    # Кидаем в базу
    collection.insert_one(employeer).inserted_id

    users = collection.find()

    return render_template('main.html', users=users)

# Страница "Сотрудники"
@app.route('/main')
def employees():
    users = collection.find()

    # Передача данных в шаблон для отображения
    return render_template('main.html', users=users)

# Страница "Договора"
@app.route('/contracts')
def contracts():
    # Дополнительная логика для страницы "Договора"
    # ...

    return render_template('contracts.html')

# Страница "Партнёры"
@app.route('/partners')
def partners():
    # Дополнительная логика для страницы "Партнёры"
    # ...

    return render_template('partners.html')

# Страница "Торги"
@app.route('/trading')
def trading():
    # Дополнительная логика для страницы "Торги"
    # ...

    return render_template('trading.html')

# Страница "Данные на изменения"
@app.route('/data_for_changes')
def data_for_changes():
    # Дополнительная логика для страницы "Данные на изменения"
    # ...

    return render_template('data_for_changes.html')

if __name__ == '__main__':
    app.run()
