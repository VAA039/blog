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
