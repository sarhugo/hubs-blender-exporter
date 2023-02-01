from bpy.props import PointerProperty
from bpy.types import Object
from ..hubs_component import HubsComponent
from ..types import Category, PanelType, NodeType
from ..utils import has_component
from ...utils import delayed_gather

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
        'icon': 'FILE_MOVIE',
        'version': (1, 0, 0)
    }

    targetNode: PointerProperty(
        name="Video",
        description="Video to project",
        type=Object,
        poll=filter_on_component)

    @delayed_gather
    def gather(self, export_settings, object):
        from ...io.utils import gather_node_property
        return {
            'target': gather_node_property(export_settings, object, self, 'targetNode'),
        }
