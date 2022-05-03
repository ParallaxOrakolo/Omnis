from src.nodes.node_manager import NodeManager
from src.nodes.base_node import BaseNode

from cv2 import GaussianBlur, blur, medianBlur
from api import logger, exception
from api.decorators import for_all_methods

NODE_TYPE = "BLUR"


blur_types = {"GAUSSIAN": GaussianBlur, "MEDIAN": medianBlur, "DEFAULT": blur}


@for_all_methods(exception(logger))
class BlurNode(BaseNode):
    """
    Node to smoothing an image
    """

    def __init__(self, name, id, options, output_connections, input_connections):
        super().__init__(name, NODE_TYPE, id, options, output_connections)
        self.input_connections = input_connections
        self.type = options["blur_type"]
        self.k_size = options["blur_intensity"]
        self.auto_run = options["auto_run"]["value"]
        NodeManager.addNode(self)

    def execute(self, message=""):
        self.image = message.payload
        try:
            _ = blur_types[self.type](
                self.image,
                self.k_size if self.type == "MEDIAN" else (self.k_size, self.k_size),
            )
            self.onSuccess(_)
        except Exception as e:
            self.onFailure(f"{self._id} cant execute.", pulse=True, errorMessage=str(e))

    def get_frame(self):
        return self.image

    @staticmethod
    def get_info():
        return {
            "options": {
                "blur_types": list(blur_types.keys()),
            }
        }
