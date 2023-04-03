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
