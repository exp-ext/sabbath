<h2>YaTube, cоциальная сеть для авторов и подписчиков (Яндекс Практикум)</h2>

![статус](https://github.com/exp-ext/yatube/actions/workflows/yatube_workflow.yml/badge.svg?event=push)

<p align="center">
<img src="https://www.affde.com/uploads/article/13525/J0ypLxCKzjX12HIF.jpg" width="1200">
</p>
<p>Социальная сеть для авторов и подписчиков. Пользователи могут подписываться на избранных авторов, оставлять и удалять комментарии к постам, оставлять новые посты на главной странице и в тематических группах, прикреплять изображения к публикуемым постам.
Проект реализован на MVT-архитектуре, реализована система регистрации новых пользователей, восстановление паролей пользователей через почту, система тестирования проекта на unittest, пагинация постов и кэширование страниц. Проект имеет верстку с адаптацией под размер экрана устройства пользователя.</p>
<hr />
<h3>Стек технологий</h3>
<ul>
<li>Python</li>
<li>Django</li>
<li>Unittest</li>
<li>Bootstrap</li>
<li>CSS</li>
<li>HTML</li>
<li>PostgreSQL</li>
<li>Docker</li>
<li>Github Actions</li>
</ul>
<hr />
<h3>Зависимости</h3>
<ul>
<li>Перечислены в файле yatube/requirements.txt</li>
</ul>
<hr />
<h3>Особенности реализации</h3>
<ul>
<li>Проект запускается в Docker контейнерах;</li>
<li>Образ yatube запушен на DockerHub;</li>
<li>Реализован CI/CD;</li>
</ul>
<hr />
<h3>Развертывание на сервере c получением сертификата</h3>
<ul>
<li>Установите на сервере docker и docker-compose-plugin;</li>
<li>Клонируйте на локальный компьютер репозиторий;</li>
<li>Создайте файл /infra/.env. Шаблон для заполнения файла находится в /infra/.env.example;</li>
<li>В файле ./infra/nginx/default.conf.template закомментируйте строки 14:18 для получения сертификата.</li>
<li>Скопируйте папку infra со всем содержимым на сервер `scp -r ~/yatube/infra name@IP.ad.re.ss:~/`
</li>
<li>На сервере, перейдите в папку infra/ и получите сертификаты в Let's Encrypt запустив скрипт `sudo ./init-letsencrypt.sh`</li>
<li>Остановите сервер `docker compose down` </li>
<li>Раскомментируйте строки 14:18 в файле ./infra/nginx/default.conf.template</li>
<li>В папке infra выполните команду `docker compose up -d --build`;</li>
<li>Создайте суперюзера `docker compose exec web python manage.py createsuperuser`</li>
<br /><br />
</ul>
<hr />
<h3>Автор проекта:</h3>
<p>Борокин Андрей</p>

GITHUB: [exp-ext](https://github.com/exp-ext)

[![Join Telegram](https://img.shields.io/badge/My%20Telegram-Join-blue)](https://t.me/Borokin)