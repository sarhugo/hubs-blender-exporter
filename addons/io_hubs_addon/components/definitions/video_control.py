from bpy.props import PointerProperty, IntProperty, EnumProperty, StringProperty
from ..hubs_component import HubsComponent
from ..utils import has_component
from bpy.types import Object
from ..types import Category, PanelType, NodeType
from ...io.utils import gather_node_property, delayed_gather

BUTTON_TYPES = [("play", "Play", "Play video"),
               ("pause", "Pause", "Pause video"),
               ("previous", "Previous", "Previous chapter"),
               ("next", "Next", "Next chapter"),
               ("chapter", "Chapter link", "Seek to the chapter position"),
               ("src", "Change video", "Changes the source of the video")]

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


class VideoControl(HubsComponent):
    _definition = {
        'name': 'video-control',
        'display_name': 'Video Control',
        'category': Category.MEDIA,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT, PanelType.BONE],
        'icon': 'MOD_PARTICLE_INSTANCE'
    }

    targetNode: PointerProperty(
        name="Video",
        description="Video to manage",
        type=Object,
        poll=filter_on_component)

    buttonType: EnumProperty(
        name="Type",
        description="Button Type",
        items=BUTTON_TYPES,
        default="play")
    
    chapter: IntProperty(
        name="Chapter", description="Chapter to link", subtype="UNSIGNED", default=0)
    
    src: StringProperty(
        name="Video URL", description="Video URL", default='https://')

    def draw(self, context, layout, panel):
        layout.prop(data=self, property="targetNode")
        layout.prop(data=self, property="buttonType")

        if self.buttonType == "chapter":
            layout.prop(data=self, property="chapter")

        if self.buttonType == "src":
            layout.prop(data=self, property="src")

    @delayed_gather
    def gather(self, export_settings, object):

        return {
            'type': self.buttonType,
            'target': gather_node_property(export_settings, object, self, 'targetNode'),
            'chapter': self.chapter if self.buttonType == "chapter" else None,
            'src': self.src if self.buttonType == "src" else None
        }
