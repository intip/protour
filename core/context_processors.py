# -*- coding:utf-8 -*-

from configuracao.models import Empresa
from destino.models import Destino


def global_context(request):
    empresa = Empresa.objects.get_singleton()
    destinos = Destino.objects.exclude(pacote_set=None)
    return {
        "empresa": empresa,
        "destinos": destinos,
    }
