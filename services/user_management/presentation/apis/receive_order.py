from ...domain.usecases.receive_message_from_order import ReceiveMessageFromOrder


class ReceiveOrder:
    def __init__(self) -> None:
        self.receive_order_message = ReceiveMessageFromOrder()

    async def execute(self):
        result = self.receive_order_message.execute(topic="get_order_by_id_action")