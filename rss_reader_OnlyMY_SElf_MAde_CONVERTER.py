from argparse import ArgumentParser

from typing import List, Optional, Dict, Sequence
import json as tdfr8
def sm_xmltodict(z):
    try:
        z=z.replace('&amp;',"&")
    except: pass
    try:
        z=z.replace('&#x27;',"'")
    except: pass
    try:
        z=z.replace('&quot;', '"')
    except: pass
    di, it, it2, i, tht = {}, "", "", 0, ""
    while i<len(z):
        if z[i]=="<":
            if len(it)>0:
                while z[i] != ">":
                    i += 1
                    it2 += z[i]
            else:
                while z[i]!=">":
                    i+=1
                    it += z[i]
        tht+=z[i]
        i += 1
        it =it.replace(">","").replace("/","")
        it2 = it2.replace(">","").replace("/","")
        if it==it2:
            di[it.replace(">","").replace("/","")]=tht[1:-1]
            it2, it, tht = "", "", ""
        if it =="item":
            di.update({"item":sm_xmltodict((z[i:len(z)].replace("</item>","")))})
            it=""
            i=len(z)
    try: di.pop('')
    except: pass
    print(di)
    return di

def json_formater(x):
    try: x_keys=list(x.keys())
    except: pass
    try: x_keys.remove('item')
    except: pass
    try: x_keys.append('item')
    except: pass
    result={}
    for key in x_keys:
        try:
            result[key] = x[key]
        except: pass
    return(tdfr8.dumps(result, indent=2, sort_keys=False))

class UnhandledException(Exception):
    pass


def rss_parser(xml: str, limit: Optional[int] = None, json=True) -> List[str]:

    parsed_xml = (((xml.replace("<rss>", "")).replace("</rss>", "")).replace("<channel>", "")).replace("</channel>", "")
    channel = sm_xmltodict(parsed_xml)
    try:
        channel["Feed" if json == False else "title"] = channel.pop('title')
    except: pass
    try:
        channel["Link" if json == False else 'link'] = channel.pop('link')
    except:
        pass
    try:
        channel["Last Build Date" if json == False else "lastBuildDate"] = channel.pop('lastBuildDate')
    except:
        pass
    try:
        channel["Publish Date" if json == False else 'pubDate'] = channel.pop('pubDate')
    except:
        pass
    try:
        channel["Language" if json == False else 'language'] = channel.pop('language')
    except:
        pass
    try:
        channel["Categories" if json == False else 'category'] = channel.pop('category')
    except:
        pass
    try:
        channel["Editor" if json == False else 'managinEditor'] = channel.pop('managinEditor')
    except:
        pass
    try:
        channel["Description" if json == False else 'description'] = channel.pop('description')
    except:
        pass
    items = channel.get('item')
    if items:
        if type(items) == dict:
            items = list((items,))
        if limit == True:
            items = items[:limit]
        items3 = []
        for i in items:
            items2 = {}
            try:
                items2["Title" if json == False else "title"] = i.pop('title')
            except:
                pass
            try:
                items2["Author" if json == False else 'author'] = i['author']
            except:
                pass
            try:
                items2["Published" if json == False else 'pubDate'] = i['pubDate']
            except:
                pass
            try:
                items2["Link" if json == False else 'link'] = i['link']
            except:
                pass
            try:
                items2["Categories" if json == False else 'category'] = i['category']
            except:
                pass
            try:
                items2['description' if json == False else 'description'] = i['description']
            except:
                pass
            items3.append(items2)
        channel.update({'item': items3})
    if json == True:
        return json_formater(channel)
    else:
        for each in channel:
            if each != "item":
                print(f"{each}: {channel.get(each)}")
        print("\n")
        try:
            for every in channel["item"]:
                for each in every:
                    if each != "description":
                        print(f"{each}: {every.get(each)}")
                    if "description" in each:
                        print("\n")
                        print(every["description"])
                print("\n")
        except:
            pass
        return

#
# def main(argv: Optional[Sequence] = None):
#     parser = ArgumentParser(prog="rss_reader", description="Pure Python command-line RSS reader.", )
#     parser.add_argument("source", help="RSS URL", type=str, nargs="?")
#     parser.add_argument("--json", help="Print result as JSON in stdout", action="store_true")
#     parser.add_argument("--limit", help="Limit news topics if this parameter provided", type=int)
#     args = parser.parse_args()
#     try:
#         output = rss_parser(args.source, args.limit, args.json)
#         print(output)
#         return 0
#     except Exception as e:
#         raise UnhandledException(e)
#
# if __name__ == "__main__":
#     main()

print(" I dont know why it errors")

xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<item><author>__TITLE_0__</author></item> <item><author>_EDY YA DOMOY NAP£££LA ZERNA_</author></item><item><language>__JAPONSKY11111__</language></item></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(f"А  должен быть:{ {'title': 'Dummy', 'description': 'Dummy Description', 'link': 'https://dummy.com', 'item':[ {'author': '__TITLE_0__'},  {'author': '_EDY YA DOMOY NAP£££LA ZERNA_'}, {'language': '__JAPONSKY11111__'}]}}")
print(output)
print(output== {'title': 'Dummy', 'description': 'Dummy Description', 'link': 'https://dummy.com', 'item':[ {'author': '__TITLE_0__'},  {'author': '_EDY YA DOMOY NAP£££LA ZERNA_'}, {'language': '__JAPONSKY11111__'}]})

print("    ")
print("    ")
print("    ")
print("    ")
print(" I dont know why it errors")
xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<item><author>__TITLE_0__</author></item></channel></rss>'
limit = None
json = True
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

xml = "<title>Dummy</title>\n<description>&quot;&quot;&quot;&quot;&quot;&quot;&quot;&quot;&quot;&quot;&quot;&q...t;&quot;&quot;&quot;&quot;&quot;&quot;&quot;&quot;&quot;</description>\n<link>https://dummy.com</link></channel></rss>"
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
print(output)  # TypeError: string indices must be integers
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

xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<item><description>__DESCRIPTION__</description></item></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<item><author>__AUTHOR__</author><title>__TITLE__</title></item></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<item><category>__CATEGORY__</category><title>__TITLE__</title></item></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)

xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<item><pubDate>Sat, 07 Sep 2002 09:42:31 GMT</pubDate><title>__TITLE__</title></item></channel></rss>'
limit = None
json = True
output = rss_parser(xml, limit, json)
print(output)
