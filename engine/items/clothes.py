from engine.items.status_modifier import StatusModifier
from engine.items.wearable import Wearable
from protos import item_pb2


class Clothes(Wearable):
    def __init__(self, clothes_proto: item_pb2.Clothes):
        if not isinstance(clothes_proto, item_pb2.Clothes):
            raise ValueError('Incorrect object type; expected item_pb2.Clothes, got {}'.format(type(clothes_proto)))
        super().__init__(StatusModifier(kwargs={'status_modifier_proto': clothes_proto.stats}))
