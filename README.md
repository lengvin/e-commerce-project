# E-commerce

## Описание:

E-commerce  — ядро для электронной торговли/коммерции основанное на ООП. В дальнейшем для этого ядра возможно будет реализовать любой интерфейс — от сайта до телеграм-бота.

## Установка:

1. клонируйте репозиторий:
```
git clone https://github.com/lengvin/e-commerce-project.git
```

## Тестирование:

Все модули покрыты тестами на 85%

## Модуль classes.py

### Класс Category

Класс для создания объекта категории, который хранит в себе информацию о категории и список продуктов данной категории, пример использования:
```
from classes import Category

category = Category(name, description, products)
```

#### Метод add_product

Метод для добавления нового продукта в уже созданную категорию, пример использования:
```
from classes import Category

category = Category(name, description, [product1])
category.add_product(product2)
```

### Класс Product

Класс для создания объекта продукта, который хранит в себе информацию о продукте, пример использования:
```
from classes import Product

product = Product(name, description, price, quantity)
```

#### Метод new_product

Метод для создания нового продукта, позволяющий в случае создания уже существуючего продукта заменить в нём информацию на новую, вместо создания нового продукта, пример использования:
```
from classes import Product

product1 = Product.new_product(name, description, price1, quantity1)
product2 = Product.new_product(name, desctiption, price2, quantity2)
```

### Класс Smartphone

Подкласс класса Product. Класс для создания объекта продукта смартфона, который хранит в себе информацию о смартфоне, пример испоьзования:
```
from classes import Smartphone

smartphone = Smartphone(name, description, price, quantity, efficiency, model, memory, color)
```

### Класс LawGrass

Подкласс класса Product. Класс для создания объекта продукта травы газонной, который хранит в себе информацию о траве газоне, пример использования:
```
from classes import LawGras

law_grass = LawGrass(name, description, price, quantity, country, germination_period, color)
```

## Модуль utils.py

### Функция read_json_file

Функция для преобразования JSON-файла в Python-объект, пример использования:
```
from utils import read_json_file

dict_ = read_json_file(file_path)
```

### Функция create_product

Функция для создания объекта класса Product из словаря, пример использования:
```
from utils import create_product

product = create_product(data)
```

### Функция create_category
Функция для создания объекта класса Category из словаря, пример использования:
```
from utils import create_category

category = create_category(data)
```
