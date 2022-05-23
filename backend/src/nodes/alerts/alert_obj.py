from datetime import datetime
from api.store import alerts
from api import logger, exception
from api.decorators import for_all_methods
from api.subscriptions import SubscriptionFactory

AlertLevel = {"INFO": "INFO", "WARNING": "WARNING", "ERROR": "ERROR", "LOG": "LOG"}

AlertManager = SubscriptionFactory(alerts, 'alerts')


@for_all_methods(exception(logger))
class Alert:
    """
    Add an alert object to all subscribed queue's.
    """

    def __init__(
        self,
        level,
        title,
        description,
        how2solve="",
        buttonText="Ok",
        buttonAction="Ok",
    ):
        """
        Create a new Alert object.
        """
        self.level = level 
        self.date = float(datetime.now().timestamp())
        self.title = title
        self.description = description
        self.how2solve = how2solve
        self.buttonText = buttonText
        self.buttonAction = buttonAction
        getattr(logger, self.level)(self.dict())
        AlertManager.put(self)

    def __str__(self) -> str:
        """
        Return a string representation of the Alert object.
        """
        message = ""
        for k, v in self.__dict__.items():
            message += f"{k[0].upper()}{k[1:]}:\t{v}\n"
        return message

    def __repr__(self) -> str:
        return str(self)

    @classmethod
    def dict(self):
        """
        Return a dictionary representation of the Alert object.
        """
        return self.__dict__
