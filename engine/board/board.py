from engine.characters.position import Position
from protos import board_pb2


class Board:
    def __init__(self, proto_board: board_pb2.Board):
        if not isinstance(proto_board, board_pb2.Board):
            raise ValueError('Incorrect object type; expected board_pb2.Board, got {}'.format(type(proto_board)))

        rows = proto_board.rows
        cols = proto_board.cols
        self.grid = []

        for r in range(rows):
            row = []
            for c in range(cols):
                row.append(proto_board.grid[r * c + c])
            self.grid.append(row)

        self.portals = []
        for i in range(len(proto_board.portals)):
            # TODO: implement Position
            self.portals.append(Position(proto_board.portals[i]))

    def get_grid(self):
        return self.grid

    def get_portals(self):
        return self.portals
