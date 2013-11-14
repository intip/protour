#-*- coding:utf-8 -*-

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    template = 'grappelli/dashboard/dashboard_4_cols.html'

    def init_with_context(self, context):
        get_admin_site_name(context)

        url = lambda m: reverse("admin:%s_%s_changelist" % (m, m))

        self.children.append(modules.AppList(
            _(u'Conteúdos'),
            column=1,
            collapsible=True,
            models=(
                'pacote.models.Pacote',
                'destino.models.Destino',
                'fiber.models.Page'
            ),
        ))

        self.children.append(modules.LinkList(
            _(u'Vendas'),
            collapsible=True,
            column=2,
            children=[
                {'title': 'Pedidos',
                 'url': reverse('admin:pedido_pedido_changelist')},
                {'title': 'Clientes',
                 'url': reverse('admin:cliente_cliente_changelist')},
            ]
        ))

        url = lambda m: reverse("admin:configuracao_%s_changelist" % m)
        self.children.append(modules.LinkList(
            title=_(u'Configurações'),
            collapsible=True,
            column=3,
            children=[
                {'title': "Empresa", 'url': url("empresa")},
                {'title': "Formas de Pagamento", 'url': url("formapagamento")},
            ]
        ))

        self.children.append(modules.RecentActions(
            _(u'Ações recentes'),
            limit=10,
            collapsible=True,
            css_classes=('collapse closed grp-closed',),
            column=3,
        ))
