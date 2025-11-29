# E-commerce

## Описание:

E-commerce  — ядро для электронной торговли/коммерции основанное на ООП. В дальнейшем для этого ядра возможно будет реализовать любой интерфейс — от сайта до телеграм-бота.

## Установка:

1. клонируйте репозиторий:
```
git clone https://github.com/lengvin/e-commerce-project.git
```

## Тестирование:

Все модули покрыты тестами на 100%

## Модуль classes.py

### Класс Category

Класс для создания объекта категории, который хранит в себе информацию о категории и список продуктов данной категории, пример использования:
```
from classes import Category

category = Category(name, description, products)
```

### Класс Product

Класс для создания объекта продукта, который хранит в себе информацию о продукте, пример использования:
```
from classes import Product

product = Product(name, description, price, quantity)
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
