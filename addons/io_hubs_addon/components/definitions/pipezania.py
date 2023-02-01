from bpy.props import IntProperty, PointerProperty
from bpy.types import Object
from ..hubs_component import HubsComponent
from ..types import Category, PanelType, NodeType
from ...utils import delayed_gather

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

    unlock: PointerProperty(
        name="Object to unlock",
        description="",
        type=Object)
    
    @delayed_gather
    def gather(self, export_settings, object):
        from ...io.utils import gather_node_property
        return {
            'level': self.level,
            'unlock': gather_node_property(export_settings, object, self, 'unlock')
        }