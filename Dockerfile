# 1. Используем образ с Python 3.12
FROM python:3.12-slim

ENV DB_HOST=192.168.1.100

# 2. Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# 3. Копируем зависимости
COPY requirements.txt .

# Обновляем pip
RUN pip install --upgrade pip

# 4. Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# 5. Копируем весь код проекта внутрь контейнера
COPY . .

# 6. Открываем порт (например, 8000)
EXPOSE 8000

# 7. Команда при запуске контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]