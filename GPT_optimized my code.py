import xmltodict
import json as tdfr8
from typing import Optional, List


def rss_parser(xml: str, limit: Optional[int] = None, json=True) -> List[str]:
    parsed_xml = xmltodict.parse(xml)
    channel = parsed_xml['rss']['channel']

    channel["Feed" if not json else "title"] = channel.pop('title')
    channel["Link" if not json else 'link'] = channel.get('link', '')
    channel["Last Build Date" if not json else "lastBuildDate"] = channel.get('lastBuildDate', '')
    channel["Publish Date" if not json else 'pubDate'] = channel.get('pubDate', '')
    channel["Language" if not json else 'language'] = channel.get('language', '')
    channel["Categories" if not json else 'category'] = channel.get('category', '')
    channel["Editor" if not json else 'managinEditor'] = channel.get('managinEditor', '')
    channel["Description" if not json else 'description'] = channel.get('description', '')

    items = channel.get('item', [])
    if type(items) == dict:
        items = list((items,))
    if limit == True:
        items = items[:limit]
    items3 = []
    for i in items:
        items2 = {}
        items2["Title" if not json else "title"] = i.get('title', '')
        items2["Author" if not json else 'author'] = i.get('author', '')
        items2["Published" if not json else 'pubDate'] = i.get('pubDate', '')
        items2["Link" if not json else 'link'] = i.get('link', '')
        items3.append(items2)

    if json:
        return [tdfr8.dumps(channel, indent=2, sort_keys=False)] + [tdfr8.dumps(i, indent=2, sort_keys=False) for i in
                                                                   items3]
    return [channel] + items3




xml = '<rss><channel><title>&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;...&gt;&gt;&gt;&gt;</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link></channel></rss>'
limit = None
json = False
output = rss_parser(xml, limit, json)
print(output)

print(" I dont know why it errors")
xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<item><author>__TITLE_0__</author></item></channel></rss>'
limit = None
# json = True
json = False
output = rss_parser(xml, limit, json)
print(output)

print("strange event")
xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<item><author>__TITLE_0__</author></item></channel></rss>'
limit = 1
json = False
output = rss_parser(xml, limit, json)
print(output)




xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<language>en</language></channel></rss>'
limit = None
json = False
output = rss_parser(xml, limit, json)
print(output)


xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<language>en</language></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)



xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<pubDate>Sat, 07 Sep 2002 00:00:01 GMT</pubDate></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<category>Newspapers</category><category>Some random category</category></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<lastBuildDate>Sat, 07 Sep 2002 09:42:31 GMT</lastBuildDate></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)


xml = '<rss><channel><title>&gt;</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)


xml = '<rss><channel><title>&lt;</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)


xml = '<rss><channel><title>&amp;</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)



xml = '<rss><channel><title>&#x27;</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)


xml = '<rss><channel><title>&quot;</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>&gt;</description>\n<link>https://dummy.com</link></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)


xml = '<rss><channel><title>Dummy</title>\n<description>&lt;</description>\n<link>https://dummy.com</link></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)


xml = '<rss><channel><title>Dummy</title>\n<description>&amp;</description>\n<link>https://dummy.com</link></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)


xml = '<rss><channel><title>Dummy</title>\n<description>&#x27;</description>\n<link>https://dummy.com</link></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>&quot;</description>\n<link>https://dummy.com</link></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;...&gt;&gt;&gt;&gt;</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link></channel></rss>'
limit = None
json = False
output = rss_parser(xml, limit, json)
print(output)


xml = '<rss><channel><title>&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;...&lt;&lt;&lt;&lt;</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link></channel></rss>'
limit = None
json = False
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&...;&amp;&amp;&amp;</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link></channel></rss>'
limit = None
json = False
output = rss_parser(xml, limit, json)
print(output)


xml = '<rss><channel><title>&#x27;&#x27;&#x27;&#x27;&#x27;&#x27;&#x27;&#x27;&#x27;&#x27;&#x27;&#x27;&#x27;&#x27;&#x27;&#x27;...x27;&#x27;&#x27;</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link></channel></rss>'
limit = None
json = False
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>&quot;&quot;&quot;&quot;&quot;&quot;&quot;&quot;&quot;&quot;&quot;&quot;&quot;&quot;&quot;&quot;...uot;&quot;&quot;</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link></channel></rss>'
limit = None
json = False
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;...&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;</description>\n<link>https://dummy.com</link></channel></rss>'
limit = None
json = False
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;...&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&lt;</description>\n<link>https://dummy.com</link></channel></rss>'
limit = None
json = False
output = rss_parser(xml, limit, json)
print(output)
#
xml = '<rss><channel><title>Dummy</title>\n<description>&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&am...;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;</description>\n<link>https://dummy.com</link></channel></rss>'
limit = None
json = False
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>&#x27;&#x27;&#x27;&#x27;&#x27;&#x27;&#x27;&#x27;&#x27;&#x27;&#x27;&#...7;&#x27;&#x27;&#x27;&#x27;&#x27;&#x27;&#x27;&#x27;&#x27;</description>\n<link>https://dummy.com</link></channel></rss>'
limit = None
json = False
output = rss_parser(xml, limit, json)
print(output)


xml="<title>Dummy</title>\n<description>&quot;&quot;&quot;&quot;&quot;&quot;&quot;&quot;&quot;&quot;&quot;&q...t;&quot;&quot;&quot;&quot;&quot;&quot;&quot;&quot;&quot;</description>\n<link>https://dummy.com</link></channel></rss>"
limit = None
json = False
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<item><title>&gt;</title></item></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)


xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<item><title>&lt;</title></item></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)   # TypeError: string indices must be integers
#                   # tasks/rss_reader.py:51: TypeError

xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<item><title>&amp;</title></item></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<item><title>&#x27;</title></item></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<item><title>&quot;</title></item></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<item><description>&gt;</description></item></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<item><description>&lt;</description></item></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<item><description>&amp;</description></item></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<item><description>&#x27;</description></item></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<item><description>&quot;</description></item></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)





xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<item><author>__TITLE_0__</author></item></channel></rss>'
limit = 6
json = False
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link></channel></rss>'
limit = 2
json = False
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link></channel></rss>'
limit = 1
json = False
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link></channel></rss>'
limit = 0
json = False
output = rss_parser(xml, limit, json)
print(output)




xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<item><author>__TITLE_0__</author></item><item><author>__TITLE_1__</author></item></channel></rss>'
limit = 1
json = True
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<it..._0__</author></item><item><author>__TITLE_1__</author></item><item><author>__TITLE_2__</author></item></channel></rss>'
limit = 1
json = True
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<it..._1__</author></item><item><author>__TITLE_2__</author></item><item><author>__TITLE_3__</author></item></channel></rss>'
limit = 1
json = True
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<item><author>__TITLE_0__</author></item></channel></rss>'
limit = 6
json = True
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link></channel></rss>'
limit = 2
json = True
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link></channel></rss>'
limit = 1
json = True
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link></channel></rss>'
limit = 0
json = True
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<it..._7__</author><item><author>__TITLE_8__</author></item><item><author>__TITLE_9__</author></item></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)


xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<item><title>__TITLE__</title></item></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)

