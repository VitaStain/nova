## Установка
Cклонируйте проект с gitlab.
  ```bash
  git clone git@github.com:VitaStain/nova.git
  ```
Установите с помощью `pip` все пакеты.
  ```bash
  $ pip install -r requirements.txt
 ```


## Быстрый старт
Создайте `.env`. Пример представлен в файле `.env.example`.

Проведите все миграции.
  ```bash
  $ python manage.py migrate
 ```

## Или через Docker
 ```bash
 docker compose up -d --build
 ```