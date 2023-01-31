from bpy.props import IntProperty, EnumProperty, PointerProperty
from ..hubs_component import HubsComponent
from bpy.types import Object
from ..types import Category, PanelType, NodeType
from ...io.utils import gather_node_property, delayed_gather

PIECE_ORIENTATIONS = [("0", "Left", "Left Side"), ("1", "Right", "Right Side")]

class ConnectPairsPuzzle(HubsComponent):
    _definition = {
        'name': 'connect-pairs-puzzle',
        'display_name': 'Connect Pairs Puzzle',
        'category': Category.MEDIA,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT],
        'icon': 'PACKAGE'
    }

    unlock: PointerProperty(
        name="Object to unlock",
        description="",
        type=Object)
    
    @delayed_gather
    def gather(self, export_settings, object):

        return {
            'unlock': gather_node_property(export_settings, object, self, 'unlock')
        }

class ConnectPairs(HubsComponent):
    _definition = {
        'name': 'connect-pairs',
        'display_name': 'Connect Pairs Puzzle Pair',
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