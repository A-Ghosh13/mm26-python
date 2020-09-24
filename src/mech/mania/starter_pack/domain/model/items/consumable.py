from mech.mania.engine.domain.model import item_pb2
from mech.mania.starter_pack.domain.model.items.item import Item
from mech.mania.starter_pack.domain.model.items.temp_status_modifier import TempStatusModifier


class Consumable(Item):
    def __init__(self, max_stack: int, consumable_proto: item_pb2.Consumable):
        if not isinstance(consumable_proto, item_pb2.Shoes):
            raise ValueError(
                'Incorrect object type; expected item_pb2.Consumable, got {}'.format(
                    type(consumable_proto)))
        super().__init__(max_stack)
        self.effect = TempStatusModifier(consumable_proto.effect)
        self.stacks = consumable_proto.stacks

    def get_stacks(self):
        return self.stacks

    def get_effect(self):
        return self.effect
