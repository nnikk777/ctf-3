# SSRF Vulnerability Demo

Учебное приложение для демонстрации уязвимости Server-Side Request Forgery (SSRF) в веб-приложениях.

## 📖 Описание уязвимости

**SSRF (Server-Side Request Forgery)** — уязвимость, позволяющая злоумышленнику заставить сервер выполнять произвольные HTTP-запросы к внутренним ресурсам.

### Почему возникает:
- Сервер без проверок принимает URL от пользователя.
- Внутренние сервисы не защищены от запросов изнутри сети.
- Фильтрация входных данных отсутствует или неполная.

## 🔒 Способ защиты

### Валидация URL:
```python
ALLOWED_DOMAINS = ['example.com']
if not any(url.startswith(f'https://{d}') for d in ALLOWED_DOMAINS):
    return "Forbidden", 403
```

## 🚀 Установка и запуск

### Клонируйте репозиторий:
```sh
git clone https://github.com/nnikk777/ctf-3.git
cd ctf-3
```

### Соберите и запустите контейнеры:
```sh
docker-compose build
docker-compose up
```

### Приложение будет доступно по адресу:
```
http://localhost:5000
```

## 🛠 POC (Proof of Concept)

1. Посмотрите статьи на сайте, это может помочь.
2. Найдите уязвимый эндпоинт `/share`.
3. Отправьте запрос к внутреннему сервису:
    ```
    http://localhost:5000/share?url=http://backend:8080/flag.txt
    ```
4. В ответе получите флаг:
    ```
    CTF{ssrf_backend_exploit}
