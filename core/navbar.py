#-*- coding:utf-8 -*-
#-*- coding:utf-8 -*-

from django.core.urlresolvers import reverse_lazy

from grappelli_navbar.nodes import CLNode


class Navbar(object):
    nodes = (
        # (u'Vendas', {'nodes': (
        #     CLNode('pedido', 'pedido'),
        #     CLNode('cliente', 'cliente'),
        # )}),
        (u'Inventários', {'nodes': (
            CLNode('pacote', 'pacote'),
        )}),
        (u'Configurações', {'nodes': (
            (u'Destinos', {
                'url': reverse_lazy('admin:destino_destino_add'),
                'perm': 'auth.add_destino',
            }),
            CLNode('configuracao', 'empresa'),
            CLNode('configuracao', 'formapagamento'),
        )}),
        (u'Usuários', {'nodes': (
            (u'Cadastrar', {
                'url': reverse_lazy('admin:auth_user_add'),
                'perm': 'auth.add_user',
            }),
            (u'Grupos de permissões', {
                'url': reverse_lazy('admin:auth_group_changelist'),
                'perm': 'auth.change_group',
            }),
        )}),
    )
