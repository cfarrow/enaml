#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from traits.api import Bool, Enum, Instance, Property

from .dialog import Dialog

from ..enums import DialogResult, Modality
from ..util.trait_types import EnamlEvent


class FileDialog(Dialog):
    """ A file selection dialog widget.

    """
    #: The type of file dialog: open or save
    type = Enum("open", "save")
    
    
    #--------------------------------------------------------------------------
    # Abstract Method Implementations
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    # Auxiliary Methods
    #--------------------------------------------------------------------------

