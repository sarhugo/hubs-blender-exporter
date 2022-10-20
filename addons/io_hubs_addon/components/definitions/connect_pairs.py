from bpy.props import IntProperty, EnumProperty
from ..hubs_component import HubsComponent
from ..types import Category, PanelType, NodeType

PIECE_ORIENTATIONS = [("0", "Left", "Left Side"), ("1", "Right", "Right Side")]

class ConnectPairsConstraint(HubsComponent):
    _definition = {
        'name': 'connect-pairs-constraint',
        'display_name': 'Connect Pairs Puzzle Board Constraint',
        'category': Category.MEDIA,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'AXIS_FRONT'
    }

class ConnectPairs(HubsComponent):
    _definition = {
        'name': 'connect-pairs',
        'display_name': 'Connect Pairs Puzzle',
        'category': Category.MEDIA,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'PACKAGE'
    }

    pair: IntProperty(
        name="Pair ID",
        description="Id of the pair",
        default=0
    )

    side: EnumProperty(
        name="Piece orientation",
        items=PIECE_ORIENTATIONS,
        default="0")