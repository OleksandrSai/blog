# Django Docker Application

## Установка и запуск

### Сборка Docker-образа

Выполните в терминале из корневой папки проекта:

```bash
docker build -t django-app .
```

```bash
docker run -p 8000:8000 --name django-containss django-app
```

Доступ к приложению
После запуска приложение будет доступно по адресу:

http://localhost:8000