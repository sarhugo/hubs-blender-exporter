from ..hubs_component import HubsComponent
from ..types import Category, PanelType, NodeType


class Portal(HubsComponent):
    _definition = {
        'name': 'portal',
        'display_name': 'Portal',
        'category': Category.ELEMENTS,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT, PanelType.BONE],
        'icon': 'LINKED',
        'version': (1, 0, 0)
    }
