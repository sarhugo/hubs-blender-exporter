from bpy.props import StringProperty
from ..hubs_component import HubsComponent
from ..types import Category, PanelType, NodeType


class RoomLink(HubsComponent):
    _definition = {
        'name': 'room-link',
        'display_name': 'Room Link',
        'category': Category.ELEMENTS,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT, PanelType.BONE],
        'icon': 'LINKED',
        'version': (1, 0, 0)
    }

    src: StringProperty(name="Room URL", description="Room absolute url",
                         default="")

    text: StringProperty(name="Label", description="Text to display on hover",
                         default="Exit")
