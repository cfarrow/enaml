from traits.api import HasStrictTraits, Instance

from .widgets.i_window import IWindow

  
class NamespaceProxy(object):
    
    def __init__(self, ns):
        self.__dict__ = ns
      

class View(HasStrictTraits)
    
    window = Instance(IWindow)

    ns = Instance(NamespaceProxy)

    def show(self, layout=False):
        self.window.show(layout=layout)
    
    def hide(self):
        self.window.hide()

