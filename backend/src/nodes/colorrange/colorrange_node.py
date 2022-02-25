from src.nodes.node_manager import NodeManager
from src.nodes.base_node import BaseNode
from api import logger, exception

NODE_TYPE = "COLORRANGE"


class ColorrangeNode(BaseNode):
    """
    Group two colors in a dictionary
    """

    @exception(logger)
    def __init__(self, name, id, options, outputConnections, inputConnections) -> None:
        super().__init__(name, NODE_TYPE, id, options, outputConnections)
        self.inputConnections = inputConnections
        self.lower = None
        self.upper = None
        # self.auto_run = options["auto_run"]
        NodeManager.addNode(self)

    @exception(logger)
    def execute(self, message=None):
        if message["targetName"] in ["lower", "upper"]:
            setattr(self, message["targetName"], message["lower"])

        if self.lower and self.upper:
            self.onSuccess({"lower": self.lower, "upper": self.upper})
            self.lower, self.upper = None, None

    @staticmethod
    @exception(logger)
    def get_info():
        return {
            "options": {
                "option_name": "option_accepted_values",
            }
        }


