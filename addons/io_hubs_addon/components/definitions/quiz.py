from bpy.props import BoolProperty, StringProperty
from ..hubs_component import HubsComponent
from ..types import Category, PanelType, NodeType


class QuizAnswer(HubsComponent):
    _definition = {
        'name': 'quiz-answer',
        'display_name': 'Quiz Answer',
        'category': Category.MEDIA,
        'node_type': NodeType.NODE,
        'panel_type': [PanelType.OBJECT, PanelType.BONE],
        'icon': 'QUESTION'
    }

    quiz: StringProperty(
        name="Quiz identifier", description="Quiz where this answer belongs")
    
    correct: BoolProperty(
        name="Is correct", description="It's the correct answer", default=False)
