# -*- coding:utf-8 -*-

from configuracao.models import Empresa


def global_context(request):
    empresa = Empresa.objects.get_singleton()
    return {"empresa": empresa}
