"""minimal2."""
from Globals import package_home

from OFS import SimpleItem

from Products.PageTemplates.PageTemplateFile import PageTemplateFile

from Products.minimal2.Controllers.Controll import ClasseControll


import os

global product_path
product_path = os.path.join(package_home(globals())) + '/'


class Minimal2(SimpleItem.SimpleItem):
    """minimal2."""

    paginas = ClasseControll('paginas')

    meta_type = 'minimal2'

    manage_options = {'label': 'view', 'action': 'paginas/index_html'},

    def __init__(self, id):
        """minimal2."""
        self.id = id


def manage_add_minimal2(self, id):
    """Add minimal2 a uma pasta."""
    self._setObject(id, Minimal2(id))
    self.REQUEST.RESPONSE.redirect('index_html')

manage_add_minimal2_form = PageTemplateFile('zpt/manage_add_minimal2_form',
                                            globals())
