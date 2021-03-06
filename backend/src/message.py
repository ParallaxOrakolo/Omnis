from bson import ObjectId
class Message:
    def __init__(
        self,
        sourceId,
        targetId,
        sourceName,
        targetName,
        sourceNodeId,
        targetNodeId,
        payload,
        additional=None,
    ):
        self.sourceId = sourceId
        self.targetId = targetId
        self.sourceName = sourceName
        self.targetName = targetName
        self.sourceNodeId = sourceNodeId
        self.targetNodeId = targetNodeId
        self.payload = payload
        self.additional = additional
        self._id = ObjectId()

    def __str__(self) -> str:
        return f"([{self.targetNodeId}|{self.targetName}]"
