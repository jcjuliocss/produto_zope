"""minimal2."""
from OFS import SimpleItem
from Products.ZSQLMethods.SQL import SQL
from Globals import package_home

import os

global product_path
product_path = os.path.join(package_home(globals())) + '/'


class ClasseModel(SimpleItem.SimpleItem):
    """minimal2."""

    def __init__(self, id):
        """minimal2."""
        self.id = id

    def pagina(self, artigo):
        """Acessa banco e retorna os valores encontrados."""
        conteudo = self.banco(artigo=artigo)

        for i in conteudo:
            tit = i.titulo
            pag = i.titulopag
            par = i.p1
            aut = i.autor

        return self.fill_index(tit=tit, pag=pag, par=par, aut=aut)

    def edit(self, artigo):
        """Edita a pagina."""
        conteudo = self.banco(artigo=artigo)

        for i in conteudo:
            titulo = i.titulo
            titulopag = i.titulopag
            p1 = i.p1
            autor = i.autor
            dbid = i.dbid

        return self.select_edit(titulo=titulo, titulopag=titulopag, p1=p1,
                                autor=autor, dbid=dbid)

    def chama(self, titulos, autorform, areatexto, titulo, titulopag):
        """Chama pagina do banco para alterar."""
        teste = self.altera_pagina(titulos=titulos, autorform=autorform,
                                   areatexto=areatexto, titulo=titulo,
                                   titulopag=titulopag)

        for i in teste:
            titulo = i.titulo

        return self.msg_altera(titulo=titulo)

    def delete(self, artigo):
        """Funcao para excluir uma pagina."""
        delet = self.manage_del_page(artigo=artigo)

        for i in delet:
            pass

        return self.msg_del(artigo=artigo)

    def adiciona(self, titulo_geral, titulo_pagina,
                 area_texto, autor_pagina):
        """Adiciona uma pagina ao minimal2, criando uma linha na tabela Sql."""
        add = self.add_page(titulo_geral=titulo_geral,
                            titulo_pagina=titulo_pagina, area_texto=area_texto,
                            autor_pagina=autor_pagina)

        for i in add:
            titulo_geral = i.titulo_geral

        return self.msg_add(titulo_geral=titulo_geral)

    altera_pagina = SQL(id='altera_pagina', title='',
                        connection_id='conexaoBanco',
                        arguments='titulos autorform areatexto titulo\
                        titulopag',
                        template=open(product_path +
                                      'sql/altera_pagina.sql').read()
                        )

    banco = SQL(id='banco', title='', connection_id='conexaoBanco',
                arguments='artigo',
                template=open(product_path + 'sql/banco.sql').read()
                )

    manage_del_page = SQL(id='manage_del_page', title='',
                          connection_id='conexaoBanco', arguments='artigo',
                          template=open(product_path +
                                        'sql/manage_del_page.sql').read())

    add_page = SQL(id='add_page', title='', connection_id='conexaoBanco',
                   arguments='titulo_geral titulo_pagina area_texto\
                   autor_pagina',
                   template=open(product_path + 'sql/add_page.sql').read())
