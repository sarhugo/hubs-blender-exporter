from bpy.props import StringProperty
from ..hubs_component import HubsComponent
from ..types import Category, PanelType, NodeType


class SimpleLink(HubsComponent):
    _definition = {
        'name': 'simple-link',
        'display_name': 'Simple Link',
        'category': Category.ELEMENTS,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT, PanelType.BONE],
        'icon': 'LINKED'
    }

    href: StringProperty(name="Link URL", description="Link absolute url",
                         default="")

