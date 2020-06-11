#encoding: utf-8
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

def render_pdf(url_template, contexto={}):
    """
    Esto renderiza un template de Django a pdf
    """
    template = get_template(url_template)
    html = template.render(contexto)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), context_type="application/pdf")
    return None