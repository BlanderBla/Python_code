import datetime
from django.http import HttpResponse
from django.template import Template, Context

# Función vista
def saludo(request):

    name = "Brayan"
    lastName = "Galvan"

    document_ext = open("C:/Users/Brayan/Documents/Programas/University Proyects/Programs_Python/Django/Proyect_1/Proyect_1/Templates/Hello_Template.html")
    plt = Template(document_ext.read())
    document_ext.close()

    ctx = Context({"nombre_persona":name,"apellido_persona":lastName,"temas":["Plantillas","Modelos","Formularios","Vistas","Despliegue"]})
    document = plt.render(ctx)
    return HttpResponse(document)

# Función vista
def despedida(request):
    document = """ 
        <html>
            <body>
                <h1>Good bye to everyone :D</h1>
            </body>
        </html>"""
    return HttpResponse(document);

# Functión vista
def fecha(request):
    fecha_actual = datetime.datetime.now()
    document = """ 
        <html>
            <body>
                <h1>Date and current time: %s</h1>
            </body>
        </html>""" % fecha_actual
    return HttpResponse(document)