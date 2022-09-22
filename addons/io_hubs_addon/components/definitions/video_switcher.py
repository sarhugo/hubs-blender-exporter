from pprint import pprint
from inspect import getmembers


from bpy.props import EnumProperty, PointerProperty, StringProperty
from ..hubs_component import HubsComponent
from ..types import Category, PanelType, NodeType
from ..utils import has_component
from bpy.types import Object
from ..consts import TRANSPARENCY_MODE
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

class VideoSwitcher(HubsComponent):
    _definition = {
        'name': 'video-switcher',
        'display_name': 'Video Switcher',
        'category': Category.MEDIA,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT, PanelType.BONE],
        'icon': 'IMAGE_DATA'
    }

    targetNode: PointerProperty(
        name="Video Node",
        description="Node with the video to manage",
        type=Object,
        poll=filter_on_component)

    src: StringProperty(
        name="Video URL", description="Video URL", default='https://')

    @delayed_gather
    def gather(self, export_settings, object):

        return {
            'src': self.src,
            'target': gather_node_property(export_settings, object, self, 'targetNode'),
        }

