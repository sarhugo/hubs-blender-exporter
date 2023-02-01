from bpy.props import BoolProperty, StringProperty
from ..hubs_component import HubsComponent
from ..types import Category, PanelType, NodeType


class InfoPanel(HubsComponent):
    _definition = {
        'name': 'info-panel',
        'display_name': 'Information Panel',
        'category': Category.MEDIA,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT, PanelType.BONE],
        'icon': 'INFO',
        'version': (1, 0, 0)
    }

    group: StringProperty(
        name="Panel group", description="Group where this panel belongs")
    
    default: BoolProperty(
        name="Default panel", description="Show this panel when there is no one selected", default=False)
