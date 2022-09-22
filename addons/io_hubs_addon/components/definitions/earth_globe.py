from pprint import pprint
from inspect import getmembers


from bpy.props import FloatVectorProperty, PointerProperty, StringProperty
from ..hubs_component import HubsComponent
from ..types import Category, PanelType, NodeType
from ..utils import has_component
from bpy.types import Object
from ...io.utils import gather_node_property, delayed_gather, gather_color_property, gather_color_opacity


def filter_on_component(self, ob):
    from .text import Text
    dep_name = Text.get_name()
    if hasattr(ob, 'type') and ob.type == 'ARMATURE':
        if ob.mode == 'EDIT':
            ob.update_from_editmode()

        for bone in ob.data.bones:
            if has_component(bone, dep_name):
                return True
    return has_component(ob, dep_name)

class EarthGlobe(HubsComponent):
    _definition = {
        'name': 'earth-globe',
        'display_name': 'Earth Globe',
        'category': Category.ELEMENTS,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT, PanelType.BONE],
        'icon': 'SPHERE'
    }

    textNode: PointerProperty(
        name="Text Node",
        description="Node with the text to display the info",
        type=Object,
        poll=filter_on_component)

    src: StringProperty(
        name="JSON URL", description="JSON file with the countries info", default='https://')

    sideColor: FloatVectorProperty(name="Side Material Color",
                                    description="Side Material Color",
                                    subtype='COLOR_GAMMA',
                                    default=(0, 1.0, 0.96, 0.7),
                                    size=4,
                                    min=0,
                                    max=1)
    bottomCapColor: FloatVectorProperty(name="Bottom Cap Material Color",
                                    description="Bottom Cap Material Color",
                                    subtype='COLOR_GAMMA',
                                    default=(0, 1.0, 0.96, 0.7),
                                    size=4,
                                    min=0,
                                    max=1)
    topCapColor: FloatVectorProperty(name="Top Cap Material Color",
                                    description="Top Cap Material Color",
                                    subtype='COLOR_GAMMA',
                                    default=(0, 1.0, 0.96, 0.7),
                                    size=4,
                                    min=0,
                                    max=1)

    activeSideColor: FloatVectorProperty(name="Active Side Material Color",
                                    description="Active Side Material Color",
                                    subtype='COLOR_GAMMA',
                                    default=(0, 1.0, 0.96, 0.7),
                                    size=4,
                                    min=0,
                                    max=1)
    activeBottomCapColor: FloatVectorProperty(name="Active Bottom Cap Material Color",
                                    description="Active Bottom Cap Material Color",
                                    subtype='COLOR_GAMMA',
                                    default=(0, 1.0, 0.96, 0.7),
                                    size=4,
                                    min=0,
                                    max=1)
    activeTopCapColor: FloatVectorProperty(name="Active Top Cap Material Color",
                                    description="Active Top Cap Material Color",
                                    subtype='COLOR_GAMMA',
                                    default=(0.604, 0.239, 0.216, 1.0),
                                    size=4,
                                    min=0,
                                    max=1)

    @delayed_gather
    def gather(self, export_settings, object):

        return {
            'src': self.src,
            'text': gather_node_property(export_settings, object, self, 'textNode'),
            'sideColor': gather_color_property(export_settings, object, self, 'sideColor', 'COLOR_GAMMA'),
            'sideColorOpacity': gather_color_opacity(export_settings, object, self, 'sideColor'),
            'bottomCapColor': gather_color_property(export_settings, object, self, 'bottomCapColor', 'COLOR_GAMMA'),
            'bottomCapColorOpacity': gather_color_opacity(export_settings, object, self, 'bottomCapColor'),
            'topCapColor': gather_color_property(export_settings, object, self, 'topCapColor', 'COLOR_GAMMA'),
            'topCapColorOpacity': gather_color_opacity(export_settings, object, self, 'topCapColor'),
            'activeSideColor': gather_color_property(export_settings, object, self, 'activeSideColor', 'COLOR_GAMMA'),
            'activeSideColorOpacity': gather_color_opacity(export_settings, object, self, 'activeSideColor'),
            'activeBottomCapColor': gather_color_property(export_settings, object, self, 'activeBottomCapColor', 'COLOR_GAMMA'),
            'activeBottomCapColorOpacity': gather_color_opacity(export_settings, object, self, 'activeBottomCapColor'),
            'activeTopCapColor': gather_color_property(export_settings, object, self, 'activeTopCapColor', 'COLOR_GAMMA'),
            'activeTopCapColorOpacity': gather_color_opacity(export_settings, object, self, 'activeTopCapColor'),
        }

