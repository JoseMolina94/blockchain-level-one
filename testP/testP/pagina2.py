from django.http import HttpResponse

def webPlantilla (request):  #Vista 1  (V1.html)    

   #  plantilla_juan=open("H:/djangoProyectos/p2/p2/plantillas/plantillas1.html")

   # juanPLT=open("H:\djangoProyectos\p1\p1\p1\plantillas\plantillas1.html", encoding="utf8")

    juanPLT=open(r"Y:\4Rblockchain\Proyector4R\Proyecto2\Proyecto2\Plantillas\plantillas1.html", encoding="utf8")

 

    #juanPLT=open(r"Y:\4Rblockchain\Proyector4R\Proyecto2\Proyecto2\index.html", encoding="utf8")

    juan=Template(juanPLT.read())

    juanPLT.close()

    ctx=Context()

    juan1=juan.render(ctx)

 

    return HttpResponse(juan1)