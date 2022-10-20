from bpy.props import PointerProperty, EnumProperty
from ..hubs_component import HubsComponent
from ..utils import has_component
from bpy.types import Object
from ..types import Category, PanelType, NodeType
from ...io.utils import gather_node_property, delayed_gather

BUTTON_TYPES = [("show", "Show", "Show Panel")]

def filter_on_component(self, ob):
    from .info_panel import InfoPanel
    dep_name = InfoPanel.get_name()
    if hasattr(ob, 'type') and ob.type == 'ARMATURE':
        if ob.mode == 'EDIT':
            ob.update_from_editmode()

        for bone in ob.data.bones:
            if has_component(bone, dep_name):
                return True
    return has_component(ob, dep_name)


class InfoPanelControl(HubsComponent):
    _definition = {
        'name': 'info-panel-control',
        'display_name': 'Information Panel Control',
        'category': Category.MEDIA,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT, PanelType.BONE],
        'icon': 'MOD_PARTICLE_INSTANCE'
    }

    targetNode: PointerProperty(
        name="Panel",
        description="Information panel to manage",
        type=Object,
        poll=filter_on_component)

    buttonType: EnumProperty(
        name="Type",
        description="Button Type",
        items=BUTTON_TYPES,
        default="show")
    
    @delayed_gather
    def gather(self, export_settings, object):

        return {
            'type': self.buttonType,
            'target': gather_node_property(export_settings, object, self, 'targetNode')
        }