from datetime import datetime

from elasticsearch import Elasticsearch

es = Elasticsearch()

def check():
    return es.ping()

def create_index():
    mappings = {
        "mappings":{
            "properties":{
                "id": {
                    "type": "long",
                    "index": "true"
                },
                "publish_time": {
                    "type": "keyword",
                },
                "content": {
                    "type": "text",
                    "index": "false"
                },
                "group": {
                    "type": "keyword"
                },
                "title": {
                    "type": "text",
                    "analyzer": "ik_smart"
                },
                "is_activated": {
                    "type": "keyword"
                }
            }
        }
    }
    es.indices.create(
        index="mw",
        body=mappings
    )

def insert_values(info):
    if not check():
        return False

    if not es.indices.exists(index="mw"):
        create_index()

    try:
        # es.index 可添加创建  es.create 可创建 但是数据存在则是添加 否则报错
        # es.count 统计数量
        # es.delete_by_query 擦删除查询出的数据
        # es.esists
        # es.indices.put_alias() 添加别名
        # es.indices.get_alias
        # es.indices.delete_alias
        # es弃用一个index下多个type 因此使用默认 doc_type
        es.index(
            # doc_type=datetime.now().strftime("%Y-%m-%d"),
            index='mw',
            id=info['id'],
            body=info
            )

    except Exception as e:
        print(e, info)

def match_info(keywords):
    body = {
        "size": 50,
        "query":{
            "match": {
                "title": keywords
            }
        },
        "highlight": {
            "pre_tags": "<b class='key' style='color:red'>",
            "post_tags": "</b>",
            "fields": {
                "title": {}
            }
        }
    }
    return es.search(
        body=body,
        # doc_type=datetime.now().strftime("%Y-%m-%d"),
        index="mw",
        filter_path=['hits.hits._source']
    )

def match_alls():
    if not check():
        return "ES 未启动！！！"

    body = {
        "query":{
            "match_all":{}
        },
        "sort":[
            {"publish_time":"desc"}
        ],
        "highlight": {
            "pre_tags": "<b style='color:red'> ",
            "post_tags": "</b>",
            "fields": {
                "title": {}
            }
        }
    }
    return es.search(
        # doc_type=datetime.now().strftime("%Y-%m-%d"),
        body=body,
        index="mw",
        filter_path=['hits.hits._source']
    )

def suggest_search(keys):
    body = {
        "size": 20,
        "query":{
            "match":{
                "title": keys
            }
        },
        "sort":[
            {"publish_time":"desc"}
        ],
        "suggest":{
            "my_suggest":{
                "text": keys,
                "phrase":{ # 词项建议器，为每个词进行模糊查询 纠正错误
                         # phrase 词组建议器 对多个term进行关联 打分
                         # completion 自动补全 
                    "field": "title"
                }
            }
        }
    }

    return es.search(index="mw", body=body, filter_path=['hits.hits._source'])


