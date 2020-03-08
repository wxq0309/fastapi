<h1 align="center">Welcome to fastapi 👋</h1>
<p>
</p>

> 本项目基于Fastapi进行开发，采用encode orm完成数据库与项目的关系映射,model管理上使用了alembic。
项目主要集成了celery-redis分布式任务队列， ElasticSearch 和 JWT(基于scopes) 认证的用户系统，
以及一个简单的基于 requests 库的 羊毛线报网站的爬虫，本项目主要是提供了一个项目基础模板,
其他项目可在本项目的基础上进行功能开发完善。


### 🏠 [Homepage](wxq0309.github.io)

<!-- ### ✨ [Demo](123) -->

## 项目目录介绍
```
    -controller   控制层文件
        - actions crud操作文件
        - api     视图层文件
    -dao          数据库配置和数据表文件
    -migrations   数据库迁移文件
    -model        pydantic model文件
    -service      其他功能组件
    -utils        es及爬虫文件
    -alembic.ini  alembic启动文件
    -main.py      项目入口文件
    -Pipfile      项目依赖文件
```

## Install

* 项目拉取到本地后可进行依赖的安装

```sh
pipenv install 
```

## Usage

* 数据库迁移

```sh
alembic revision --autogenerate -m '本次操作信息'
alembic upgrade head
```

* 项目运行

```sh
uvicorn main:app --reload
```
* 浏览器输入 `127.0.0.1:8000/docs` 即可进入 Swagger 交互文档

* 其中爬虫部分功能需要先开启 Elasticsearch Kibana后才能进行数据的存储和检索

## Author

👤 **wxq0309**

* Github: [@wwxxq0309](https://github.com/wxq0309)

## Show your support

Give a ⭐️ if this project helped you!

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_