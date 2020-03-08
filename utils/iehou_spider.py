import requests
from lxml import etree

class IeHouSpider:
    def __init__(self):
        self.url = "http://iehou.com/"

    def get_list_info(self):
        resp = requests.get(self.url)
        assert resp.status_code == 200

        html = etree.HTML(resp.text)
        uls = html.xpath('//div[@class="post-body"]/ul[2]//li')

        infos = []
        for li in uls[1:]:
            group = "某网"
            title = li.xpath("./div/h2/a/text()")[0]
            publish_time = li.xpath("./span/text()")[0].strip()
            detail_uri = li.xpath("./div/h2/a/@href")[0]
            content = self.get_detail_info(detail_uri)
            # print(content)
            infos.append({"title": title, "publish_time": publish_time, "content": content, "group": group})
        return infos

    def get_detail_info(self, uri):
        resp = requests.get(uri)
        assert resp.status_code == 200

        html = etree.HTML(resp.text)
        element = html.xpath('//*[@id="body"]/div/div[3]/div[3]')[0]

        text = [i for i in [i.strip() for i in  element.xpath(".//text()")] if len(i) !=0]
        imgs = element.xpath(".//img/@src")
        hrefs = element.xpath(".//a/@href")

        if imgs or hrefs:
            for i, t in enumerate(text):
                # if t.endswith("jpg"):
                #     text[i] = imgs.pop(0)
                if "..." in t:
                    href = hrefs.pop(0)
                    text[i] = href.split("url=")[1] if "iehou" in href else href
        text.extend(imgs)
        ' '.join([i for i in text])
        return str(text)


# if __name__ == '__main__':
#     IeHouSpider().get_list_info()
    