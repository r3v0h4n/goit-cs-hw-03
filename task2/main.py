from pymongo import MongoClient, errors

client = MongoClient('mongodb+srv://larevoo:nSvIbGvHr9KPQpdg@cluster0.lhsgq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['cat_database']
collection = db['cats']

def show_all_cats():
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except errors.PyMongoError as e:
        print(f"Помилка при виведенні всіх котів: {e}")

def find_cat_by_name(name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f'Кіт з ім\'ям {name} не знайдений.')
    except errors.PyMongoError as e:
        print(f"Помилка при пошуку кота за ім'ям: {e}")

def add_cat(name, age, features):
    try:
        collection.insert_one({"name": name, "age": age, "features": features})
        print(f'Кота {name} додано до бази.')
    except errors.PyMongoError as e:
        print(f"Помилка при додаванні кота: {e}")

def update_cat_age(name, new_age):
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.modified_count > 0:
            print(f'Вік кота {name} оновлено до {new_age}.')
        else:
            print(f'Кіт з ім\'ям {name} не знайдений.')
    except errors.PyMongoError as e:
        print(f"Помилка при оновленні віку кота: {e}")

def add_feature_to_cat(name, new_feature):
    try:
        result = collection.update_one({"name": name}, {"$push": {"features": new_feature}})
        if result.modified_count > 0:
            print(f'До кота {name} додано характеристику: {new_feature}.')
        else:
            print(f'Кіт з ім\'ям {name} не знайдений.')
    except errors.PyMongoError as e:
        print(f"Помилка при додаванні характеристики коту: {e}")

def delete_cat_by_name(name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f'Кіт з ім\'ям {name} видалений.')
        else:
            print(f'Кіт з ім\'ям {name} не знайдений.')
    except errors.PyMongoError as e:
        print(f"Помилка при видаленні кота: {e}")

def delete_all_cats():
    try:
        result = collection.delete_many({})
        print(f'Видалено {result.deleted_count} записів.')
    except errors.PyMongoError as e:
        print(f"Помилка при видаленні всіх котів: {e}")

def main():
    while True:
        command = input("Введіть команду (show_all, find, add, update_age, add_feature, delete, delete_all, exit): ").strip().lower()
        if command == "exit":
            print("Завершення програми.")
            break
        elif command == "show_all":
            show_all_cats()
        elif command == "find":
            name = input("Введіть ім'я кота: ").strip()
            find_cat_by_name(name)
        elif command == "add":
            name = input("Введіть ім'я кота: ").strip()
            try:
                age = int(input("Введіть вік кота: "))
                features = input("Введіть характеристики кота через кому: ").strip().split(", ")
                add_cat(name, age, features)
            except ValueError:
                print("Вік має бути числом.")
        elif command == "update_age":
            name = input("Введіть ім'я кота: ").strip()
            try:
                new_age = int(input("Введіть новий вік кота: "))
                update_cat_age(name, new_age)
            except ValueError:
                print("Вік має бути числом.")
        elif command == "add_feature":
            name = input("Введіть ім'я кота: ").strip()
            new_feature = input("Введіть нову характеристику: ").strip()
            add_feature_to_cat(name, new_feature)
        elif command == "delete":
            name = input("Введіть ім'я кота: ").strip()
            delete_cat_by_name(name)
        elif command == "delete_all":
            delete_all_cats()
        else:
            print("Невідома команда. Спробуйте ще раз.")

if __name__ == '__main__':
    main()
