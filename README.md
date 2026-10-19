# Notes App UI tests — Playwright + POM

Проект содержит три последовательных UI-теста для публичного учебного приложения
[Notes App](https://practice.expandtesting.com/notes/app/):

1. регистрация нового пользователя, вход и проверка интерфейса заметок;
2. создание заметки и проверка её текста в карточке;
3. редактирование заметки, проверка нового текста, удаление и проверка отсутствия карточки.

Каждый запуск создаёт уникального пользователя. Тесты 2 и 3 используют состояние
предыдущих шагов, поэтому запускайте весь файл последовательно, без `pytest-xdist`.

## Структура

- `pages/` — Page Object-ы для регистрации, входа и заметок;
- `tests/conftest.py` — общая фикстура пользователя и страницы;
- `tests/test_notes_workflow.py` — три теста;
- `tests/test_api.py` — три независимых API-теста: регистрация, повторная
  регистрация и удаление пользователя;
- `pytest.ini` — порядок тестов через `pytest-order`.

## Codegen

Playwright Codegen использован для создания стартового сценария; его локаторы
проверены в браузере и перенесены в Page Object-ы. Чтобы повторно записать шаги
вручную, выполните:

```bash
./.venv-mac12/bin/python -m playwright codegen --target python-pytest --test-id-attribute data-testid https://practice.expandtesting.com/notes/app/register
```

## Установка и запуск

```bash
./.venv-mac12/bin/python -m pip install -r requirements.txt
./.venv-mac12/bin/python -m playwright install chromium
./.venv-mac12/bin/python -m pytest tests/test_notes_workflow.py -v
./.venv-mac12/bin/python -m pytest tests/test_api.py -v
```
