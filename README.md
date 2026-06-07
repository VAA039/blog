# Запуск проекта

### Установка и настройка виртуального окружения
```bash
python -m venv venv
```
**Что делает:**
- `python -m venv venv` - создает виртуальное окружение Python в папке `venv`. Это изолирует зависимости проекта глобальных пакетов.


### Активация окружения
```
# Windows
source venv/Scripts/activate
# Linux MacOS
source venv/bin/activate
```
**Что делает:**
- Активирует виртуальное окружение. После активации в терминале появится `(venv)`.

## Установка зависимостей
```bash
pip install -r requirements.txt
```
**Что делает:**
- Устанавливает все пакеты из файла `requirements.txt` (Django и др.).

## Как запустить сервер
```bash
python manage.py runserver
```



## Миграции базы данных
```bash
python manage.py makemigrations
python manage.py migrate
```

**Что делает:**
- 'makemigrations' - создёт файлы миграций на основе моделей Django
- 'migrate' - применяет миграции к базе данных


## Создание суперпользователя (опционально)
```bash
python manage.py createsuperuser
```

**Что делает:**
- Создаёт администратора для доступа к панели Django ('/admin').