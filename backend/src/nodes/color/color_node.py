from src.nodes.node_manager import NodeManager
from src.nodes.base_node import BaseNode
from src.nodes.color.color_obj import ColorOBJ as color
from api import logger, exception
from api.decorators import for_all_methods

NODE_TYPE = "COLOR"

color_modes = [color.RGB, color.HEX, color.HSV, color.CV2_HSV]


@for_all_methods(exception(logger))
class ColorNode(BaseNode):
    """
    insert_node_description_here
    """

    def __init__(self, name, id, options, output_connections, input_connections):
        super().__init__(name, NODE_TYPE, id, options, output_connections)
        self.input_connections = input_connections

        self.color_code = options["color_code"]
        self.color_mode = options["color_name"]

        self.color = color(self.color_code, self.color_mode)
        self.auto_run = options["auto_run"]["value"]

        NodeManager.addNode(self)

    def execute(self, message=None):
        if message:
            self.color = color(message.payload, self.color_mode)
        for output in color_modes:
            self.on(output, self.color.get(output))

    @staticmethod
    def get_info():
        return {
            "options": {
                "color_modes": color_modes,
            }
        }
