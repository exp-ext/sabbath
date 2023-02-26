<h2>Как запустить проект:</h2>

<p>Клонировать репозиторий и перейти в него в командной строке:</p>

<p><code>$ git clone https://github.com/exp-ext/yatube.git</code><br /><code>$ cd yatube</code></p>

<p>создать в корне и заполнить файл .env</p>

<p>
<sup>DEBUG=0</sup>
<br />
<sup>DJANGO_SECRET_KEY=Твой_ключ</sup>
<br />
<sup>DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 твой_хост</sup>
</p>
<p>
<sup>POSTGRES_ENGINE=django.db.backends.postgresql</sup>
<br />
<sup>POSTGRES_DB=db</sup>
<br />
<sup>POSTGRES_USER=db</sup>
<br />
<sup>POSTGRES_PASSWORD=Твой_ключ</sup>
<br />
<sup>POSTGRES_HOST=db</sup>
<br />
<sup>POSTGRES_PORT=5432</sup>
</p>

<p>Запустить проект в docker-compose командой:</p>

<p><code>$ docker-compose up --build</code></p>


## License
[MIT © Andrey Borokin](https://github.com/exp-ext/yatube/blob/main/LICENSE.txt)

[![Join Telegram](https://img.shields.io/badge/My%20Telegram-Join-blue)](https://t.me/Borokin)
