def html_tag_checker("dosya.html"):
    return tag_checker(html_filtrele("dosya.html"))

def html_filtrele(dosya.html):
    yeni=open("dosya.html")
    dList=yeni.readlines()
    tagFiltre=[]
    tag = ['<html>','<head>','<title>','</title>','</head>','<body>','<div>','<h1>','</h1>','</div>','</body>','</html>']
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    for i in dList:
        list1 = i.split(" ")
        for j in list1:
            list2.append(j.lower())
    for tag in list2:
        if tag.strip() in tag:
            tagFiltre.append(tag.strip())
    for k in tagFiltre:
        list3.append(k.strip("<"))
    for l in list3:
        list4.append(l.strip(">"))
    return list4

class Stack():
    def __init__(self):
        self.items=[]
        def isEmpty(self):
            return self.items=[]
        def push(self,item):
            self.items.insert(0,item)
        def pop(self):
            return self.items.pop(0)
        def peek(self):
            return self.items[0]
        def size(self):
            return len(self.items)

def tag_checker(html_filtrele):
    open_tag=['html','head','title','body','div','h1']
    s=Stack()
    denge=True
    indis=0
    while indis < len(list4) and denge:
        tagler=list4[indis]
        if tagler in open_tag:
            s.push(tagler)
        else:
            top=s.pop()
            if not eslesme(top,tagler):
                denge=False
        indis=indis+1
    if denge and s.isEmpty():
        return true
    else:
        return false
    
def esleme(ac,kapa):
    ac_tag=['html','head','title','body','div','h1']
    kapa_tag=['/title','/head','/h1','/div','/body','/html']
    return ac_tag.index(ac)== kapa_tag.index(kapa)


    
