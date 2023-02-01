x={'item': {'author': '__TITLE_0__', 'item': {'author': '_EDY YA DOMOY NAP£££LA ZERNA_', 'item': {'language': '__JAPONSKY11111__'}}}}

# {'author': '__TITLE_0__', 'item': {'author': '_EDY YA DOMOY NAP£££LA ZERNA_', 'item': {'language': '__JAPONSKY11111__'}}}
n=str(x).count("{")
print(n)
# i=1
# while i!=n:
#
#     object1=x.get("item")
#     print(object1)
#     x=object1
#
#     i+=1
# values_list=[]

def fuck_to_real(x,n):
    defct=[]
    if n==2:
        return defct + [x.get("item"), ] + [fuck_to_real(x.get("item"), n - 1),]

    # else:
    #     # x = x.get("item")
    #     print(defct)
    #     return defct +


print(fuck_to_real(x,n))



# print(f"А  должен быть:"
#       f"{ {'title': 'Dummy', 'description': 'Dummy Description', 'link': 'https://dummy.com', 'item':[
# {'author': '__TITLE_0__'},  {'author': '_EDY YA DOMOY NAP£££LA ZERNA_'}, {'language': '__JAPONSKY11111__'}]}}")



