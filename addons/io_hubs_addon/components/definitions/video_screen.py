from bpy.props import PointerProperty
from ..hubs_component import HubsComponent
from ..utils import has_component
from bpy.types import Object
from ..types import Category, PanelType, NodeType
from ...io.utils import gather_node_property, delayed_gather

def filter_on_component(self, ob):
    from .video import Video
    dep_name = Video.get_name()
    if hasattr(ob, 'type') and ob.type == 'ARMATURE':
        if ob.mode == 'EDIT':
            ob.update_from_editmode()

        for bone in ob.data.bones:
            if has_component(bone, dep_name):
                return True
    return has_component(ob, dep_name)

class VideoScreen(HubsComponent):
    _definition = {
        'name': 'video-screen',
        'display_name': 'Video Custom Projection',
        'category': Category.MEDIA,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'deps': ['video'],
        'icon': 'FILE_MOVIE'
    }

    targetNode: PointerProperty(
        name="Video",
        description="Video to project",
        type=Object,
        poll=filter_on_component)

    @delayed_gather
    def gather(self, export_settings, object):

        return {
            'target': gather_node_property(export_settings, object, self, 'targetNode'),
        }
