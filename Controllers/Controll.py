"""minimal2."""
from OFS import SimpleItem
from Products.minimal2.Models.MinhaModel import ClasseModel
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.ZSQLMethods.SQL import SQL
from Globals import package_home

import os

global product_path
product_path = os.path.join(package_home(globals())) + '/'


class ClasseControll(SimpleItem.SimpleItem):
    """minimal2."""

    def __init__(self, id):
        """minimal2."""
        self.id = id
        self.model = ClasseModel('model')

    def pagina_artigos(self, artigo):
        """Retorna o conteudo de exibicao vinda de models."""
        return self.model.pagina(artigo=artigo)

    def edit_sql(self, artigo):
        """Retorna o conteudo vindo de models para modificar a pagina."""
        return self.model.edit(artigo=artigo)

    def chama_pagina(self, titulos, autorform, areatexto, titulo, titulopag):
        """Retorna o conteudo editado pela pagina de selecao de edicao.

        Contida em models.
        """
        return self.model.chama(titulos=titulos, autorform=autorform,
                                areatexto=areatexto, titulo=titulo,
                                titulopag=titulopag)

    def del_page(self, artigo):
        """Remove uma pagina(linha da tabela do banco)."""
        return self.model.delete(artigo=artigo)

    def adiciona_pag(self, titulo_geral, titulo_pagina,
                     area_texto, autor_pagina):
        """Adiciona uma pagina ao site(uma linha na tabela sql)."""
        return self.model.adiciona(titulo_geral=titulo_geral,
                                   titulo_pagina=titulo_pagina,
                                   area_texto=area_texto,
                                   autor_pagina=autor_pagina)

    index_html = PageTemplateFile('zpt/index_html', globals())

    fill_index = PageTemplateFile('zpt/fill_index', globals())

    manage_edit_page = PageTemplateFile('zpt/manage_edit_page', globals())

    select_edit = PageTemplateFile('zpt/select_edit', globals())

    msg_altera = PageTemplateFile('zpt/msg_altera', globals())

    manage_select_del_page = PageTemplateFile('zpt/manage_select_del_page',
                                              globals())

    msg_del = PageTemplateFile('zpt/msg_del', globals())

    manage_add_page = PageTemplateFile('zpt/manage_add_page', globals())

    msg_add = PageTemplateFile('zpt/msg_add', globals())

    manage_site = PageTemplateFile('zpt/manage_site', globals())

    style_css = PageTemplateFile('zpt/style_css', globals())

    menuZ = SQL(id='menuZ', title='', connection_id='conexaoBanco',
                arguments='',
                template=open(product_path + 'sql/menuZ.sql').read()
                )
