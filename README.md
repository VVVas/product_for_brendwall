# API для продуктов  
Позволяет добавить продукт и получить список продуктов через API.  

## Стек технологий  
Python 3.11.9, Django 5.1.1, Django REST framework 3.15.2, SQLite  

## Функциональность  
Реализовано API.  
Ограничения API настроены в моделях данных.  
Для доступа к API используются ограничения явно заданные в settings.py.  

Модели данных настроены в административном разделе.  

## Как развернуть 
Перейти в каталог backend  
```  
cd backend/  
```  

Создать окружение  
```  
python -m venv venv  
```  

Активировать окружение, обновить pip и установить зависимости  
```  
source venv/Scripts/activate  
python -m pip install --upgrade pip  
pip install -r requirements.txt  
```  

Применить миграции и запустить сервер  
```  
python manage.py migrate  
python manage.py runserver  
```  

Перейти в браузере по адресу  
```  
http://127.0.0.1:8000/api/v1/products/
```  

По окончании использования деактивировать окружение  
```  
deactivate  
```  

## Разработчик
[Мишустин Василий](https://github.com/vvvas), v@vvvas.ru  
