from django.http import HttpResponse
from django.template import Template, Context
def pagina1(resquest): #vista http

    from datetime import datetime

    time1 = datetime.now()

    t1 = datetime.timestamp(time1)

    t3 = "si es"

    yj=5
    
    paginita=open(r"C:\Users\jose-\OneDrive\Documentos\Blockchain level 1\Init\blockchain-level-one\testP\testP\views\html-bc.html", encoding="utf8")

    panginaRender=Template(paginita.read())
    
    paginita.close()
    
    ctx=Context({"time1": time1 })

    render=panginaRender.render(ctx)
    
    return HttpResponse(render % (t1, t3, time1, yj, t3, yj))