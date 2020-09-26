<h1 align="center">Welcome to SimpleFastapiProject 👋</h1>
<p>
</p>

> 本项目基于fastapi进行开发，采用encode orm完成数据库与项目的关系映射, 项目使用jwt验证进行鉴权，使用celery-rabbitmq分布式任务系统
>进行消费，项目使用alembic进行数据库迁移，大家可在此项目模板基础上进行开发拓展（大家有想要添加的功能可直接issue）。


### 🏠 [Homepage](wxq0309.github.io)

### ✨ [Demo](http://test.hjx.pub/docs) 网站已部署至 http://114.55.33.142:8002/docs   (学生机性能无视)

## 项目目录介绍
```
    此项目结构已近一步优化，用户可直接在此基础上进行修改开发。
    目前配置主要使用.env文件加载，正式上线安全性更高。
    app:
        api-视图接口
        core-celery配置、jwt基础校验
        migrations-alembic数据迁移管理
        models-数据关系对象
        schemas-base校验
        main-项目启动文件
```

## 已开发功能
```
    用户注册登录jwt鉴权
    celery-rabbitmq分布式任务集成
    
```

## 待开发功能
```
    邮件功能
    短信功能
```

## Install

* 项目拉取到本地后可进行依赖的安装,项目依赖可使用 requirements.txt 中的依赖进行安装

```sh
pipenv install  / pip install -r requirements.txt
```

## Usage

* 数据库迁移

```sh

进行迁移之前需要先将 alembic.ini 文件和 dao.db中的MySQL用户名和密码更改成本人的

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

* Github: [@wxq0309](https://github.com/wxq0309)

## Show your support

Give a ⭐️ if this project helped you!

***
<!-- _This README was generated with ❤️ by  -->
<!-- [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_ -->
