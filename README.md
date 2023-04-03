**###Описание проекта:**

Проект api_final_yatube предназначен для взаимодействия с социальной сетью Yatube.
С его помощью возможно получать, создавать, изменять и удалять информацию о постах, комментариях, группах и подписках.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Nikitriy/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:


```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

**###Примеры запросов**

Get http://127.0.0.1:8000/api/v1/posts выдаст список всех постов сайта

Get http://127.0.0.1:8000/api/v1/posts/{int:pk}/ выдаст конкретный пост по соответствующему id

Get http://127.0.0.1:8000/api/v1/posts/{int:pk}/comments выдаст список комментариев конкретного поста

Post http://127.0.0.1:8000/auth/users/ зарегестрирует пользователя (необходимо в теле запроса передать username и password)
