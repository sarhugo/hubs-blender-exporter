from bpy.props import IntProperty
from ..hubs_component import HubsComponent
from ..types import Category, PanelType, NodeType


class Pipezania(HubsComponent):
    _definition = {
        'name': 'pipezania',
        'display_name': 'Pipezania Game',
        'category': Category.MEDIA,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'PACKAGE'
    }

    level: IntProperty(
        name="Level",
        description="In seconds",
        default=0
    )