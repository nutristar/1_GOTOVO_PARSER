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
    di={}
    it=""
    it2=""
    tht=""
    i=0
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
            it2=""
            it=""
            tht=""
        if it =="item":
            di.update({"item":sm_xmltodict((z[i:len(z)].replace("</item>","")))})
            it=""
            i=len(z)
    try: di.pop('')
    except: pass
    return di

# def json_formater(x):
#     try: x_keys=list(x.keys())
#     except: pass
#     try: x_keys.remove('item')
#     except: pass
#     try: x_keys.append('item')
#     except: pass
#     result={}
#     for key in x_keys:
#         try:
#             result[key] = x[key]
#         except: pass
#     return(tdfr8.dumps(result, indent=2, sort_keys=False))


x =  {'title': 'Dummy', 'description': 'Dummy Description', 'link': 'https://dummy.com', 'item':[ {'author': '__TITLE_0__'},  {'author': '_EDY YA DOMOY NAP£££LA ZERNA_'}, {'link': '__JAPONSKY11111__'}]}

# print(json_formater(x))

xml = '<title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<language>en</language>'
xml = '<rss><channel><title>Dummy</title>\n<description>Dummy Description</description>\n<link>https://dummy.com</link>\n<item><author>__TITLE_0__</author></item> <item><author>_EDY YA DOMOY NAP£££LA ZERNA_</author></item><item><language>__JAPONSKY11111__</language></item></channel></rss>'
xml = (((xml.replace("<rss>", "")).replace("</rss>", "")).replace("<channel>", "")).replace("</channel>", "")
limit = None
json = False
output = sm_xmltodict(xml)
print(output)

























