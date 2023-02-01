from bpy.props import StringProperty
from ..hubs_component import HubsComponent
from ..types import Category, PanelType, NodeType


class VideoChapters(HubsComponent):
    _definition = {
        'name': 'video-chapters',
        'display_name': 'Video Chapters Info',
        'category': Category.MEDIA,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT, PanelType.BONE],
        'deps': ['video'],
        'icon': 'FILE_MOVIE',
        'version': (1, 0, 0)
    }

    src: StringProperty(
        name="JSON Url", description="JSON file with the chapters info", default='https://mozilla.org')
