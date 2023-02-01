from bpy.props import FloatProperty, EnumProperty
from ..hubs_component import HubsComponent
from ..types import Category, PanelType, NodeType

class Rotation(HubsComponent):
    _definition = {
        'name': 'rotation-loop',
        'display_name': 'Rotation',
        'category': Category.ANIMATION,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT, PanelType.BONE],
        'icon': 'FORCE_MAGNETIC',
        'version': (1, 0, 0)
    }

    speed: FloatProperty(
        name="Speed",
        description="In seconds",
        default=1.0
    )

    axis: EnumProperty(
        name="Axis",
        description="Rotate on axis",
        items=[("x", "X", "X Axis"), ("y", "Y", "Y Axis"), ("z", "Z", "Z Axis")],
        default="z")
    