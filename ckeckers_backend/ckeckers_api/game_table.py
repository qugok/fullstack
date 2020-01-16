import itertools as it
import numpy as np
import re
import json
import logging

# logger = logging.getLogger("logggg.txt")
logger = logging.getLogger('myproject.custom')


class Table:
    class Position:
        def __init__(self, x=0, y=0, player=0, kinged=False):
            self.x = x
            self.y = y
            self.player = player
            self.kinged = kinged

        def __str__(self):
            return '(' + str(self.x) + ';' + str(self.y) + ') - ' + str(self.player) + ' k:' + str(self.kinged)

        def __repr__(self):
            return '(' + str(self.x) + ';' + str(self.y) + ') - ' + str(self.player) + ' k:' + str(self.kinged)

        def serialize(self):
            return str(self.x) + ':' + str(self.y) + '@' + str(int(self.kinged))

        def deserialize(self, s: str):
            x, y, k = re.split(r'[:@]', s, maxsplit=2)
            self.x = int(x)
            self.y = int(y)
            self.kinged = k != 0
            return self

        def to_json_like(self, player=False):
            ans = {
                'x': self.x,
                'y': self.y,
                'kinged': self.kinged,
            }
            if player:
                ans['player'] = self.player
            return ans

        def to_json(self, player=False):
            return json.dumps(self.to_json_like(player))

        def set_kinged(self, kinged=True):
            self.kinged = kinged

    def __init__(self, size=8, turn=1, table=None):
        logger.info("created table")
        self.size = size
        self.table = table
        self.turn = turn
        if self.table is None:
            self.table = Table.__generate_field(self.size)

    def test(self):
        # return str(self.to_json_like())
        return Table.__generate_field()
        # return '\n'.join(self.serialize()) + '\n\n' + str(self.deserialize(*self.serialize()))

    def __str__(self):
        return '\n'.join([str(i) for i in self.table])

    def __int__(self):
        return self.size

    def __check_turn(self, pos):
        return self.turn == self.table[pos[0]][pos[1]].player

    def __generate_field(size: int = 8, empty=False):
        get_player = lambda y, x: 1 if not empty and (x + y) % 2 == 0 and x < 3 else 2 if not empty and (
                x + y) % 2 == 0 and (size - x) < 4 else 0
        # first_p = [(i, j) for i, j in it.product(np.arange(8), np.arange(8)) if (i + j) % 2 == 0 and j < 3]
        # second_p = [(i, j) for i, j in it.product(np.arange(8), np.arange(8)) if (i + j) % 2 == 0 and size - j < 4]
        table = [[Table.Position(i, j, get_player(i, j)) for j in range(size)] for i in range(size)]
        # for i, j in it.product(np.arange(8), np.arange(8)):
        #     if (i + j) % 2 == 0:
        #         if j < 3:
        #             first_p.append((i, j))
        #         if size - j < 4:
        #             second_p.append((i, j))
        return table

    def serialize(self):
        logger.info(str(self.__dict__))
        first_player_positions = '#'.join([p.serialize() for line in self.table for p in line if p.player == 1])
        second_player_positions = '#'.join([p.serialize() for line in self.table for p in line if p.player == 2])
        return first_player_positions, second_player_positions

    def deserialize(self, first: str, second: str):
        self.table = Table.__generate_field(self.size, empty=True)
        first_positions = [Table.Position().deserialize(pos) for pos in first.split('#')]
        logger.info(first)
        logger.info(str([pos for pos in first.split('#')]))
        logger.info(str(first_positions))
        second_positions = [Table.Position().deserialize(pos) for pos in second.split('#')]
        logger.info(second)
        logger.info(str([pos for pos in second.split('#')]))
        logger.info(str(second_positions))
        for pos in first_positions:
            self.table[pos.x][pos.y].player = 1
        for pos in second_positions:
            self.table[pos.x][pos.y].player = 2
        return self

    def to_json_like(self):
        ans = {
            'first_player_positions':
                [p.to_json_like() for line in self.table for p in line if p.player == 1],
            'second_player_positions':
                [p.to_json_like() for line in self.table for p in line if p.player == 2],
            'turn': self.turn,
            'size': self.size
        }
        return ans

    def to_json_like_with_table(self):
        ans = {
            'table': [[p.to_json_like(True) for p in line] for line in self.table],
            'turn': self.turn,
            'size': self.size
        }
        return ans

    def to_json(self):
        return json.dumps(self.to_json_like())

    def __is_on_table(self, x, y):
        return not (x >= self.size or y >= self.size or x < 0 or y < 0)

    def __check_line(self, start, step):
        can_go = []
        prev = self.table[start[0]][start[1]]
        player = prev.player
        enemy = 1 if player == 2 else 2
        x, y = start[0] + step[0], start[1] + step[1]
        while self.__is_on_table(x, y):
            if self.table[x][y].player == enemy:
                if prev.player == enemy:
                    break
            if self.table[x][y].player == player:
                break
            if self.table[x][y].player == 0:
                can_go.append((x, y))

            prev = self.table[x][y]
            x += step[0]
            y += step[1]
        return can_go

    def __can_go_king(self, pos):
        can_go = []
        can_go.extend(self.__check_line(pos, (1, 1)))
        can_go.extend(self.__check_line(pos, (1, 0)))
        can_go.extend(self.__check_line(pos, (1, -1)))
        can_go.extend(self.__check_line(pos, (0, 1)))
        can_go.extend(self.__check_line(pos, (0, -1)))
        can_go.extend(self.__check_line(pos, (-1, 1)))
        can_go.extend(self.__check_line(pos, (-1, 0)))
        can_go.extend(self.__check_line(pos, (-1, -1)))
        return can_go

    def __can_go_checker(self, pos):
        can_go = []
        player = self.table[pos[0]][pos[1]].player
        enemy = 1 if player == 2 else 2
        delta = it.product([1, -1], [1, -1])
        for dx, dy in delta:
            x, y = pos[0] + dx, pos[1] + dy
            if not self.__is_on_table(x, y):
                continue
            if self.table[x][y].player == 0:
                can_go.append((x, y))
            if self.table[x][y].player == player:
                continue
            if self.table[x][y].player == enemy and self.__is_on_table(x + dx, y + dy) and self.table[x + dx][
                y + dy].player == 0:
                can_go.append((x + dx, y + dy))
        return can_go

    def can_go(self, pos):
        if self.table[pos[0]][pos[1]].player == 0:
            return []
        if self.table[pos[0]][pos[1]].kinged:
            return self.__can_go_king(pos)
        return self.__can_go_checker(pos)

    def __eats(self, fro, to):
        eated = []
        if tuple(to) not in self.can_go(fro):
            return None
        player = self.table[fro[0]][fro[1]].player
        enemy = 1 if player == 2 else 2
        x, y = tuple(fro)
        xx, yy = tuple(to)
        dx = int((xx - x) / abs(xx - x))
        dy = int((yy - y) / abs(yy - y))
        x += dx
        y += dy
        while (x, y) != (xx, yy) and self.__is_on_table(x, y):
            logger.info(str((x, y, xx, yy)))
            if self.table[x][y].player == enemy:
                eated.append((x, y))
        return eated

    def become_kinged(self, pos):
        player = self.table[pos[0]][pos[1]].player
        if player == 1 and pos[1] == self.size - 1:
            self.table[pos[0]][pos[1]].set_kinged()
            return True
        if player == 2 and pos[1] == 0:
            self.table[pos[0]][pos[1]].set_kinged()
            return True
        return False

    def go(self, fro, to):
        if tuple(to) not in self.can_go(fro):
            return False
        eats = self.__eats(fro, to)
        if eats is None:
            return False
        logger.info(str(eats))
        player = self.table[fro[0]][fro[1]].player

        self.table[to[0]][to[1]].player = player
        self.table[to[0]][to[1]].set_kinged(self.table[fro[0]][fro[1]].kinged)
        self.become_kinged(to)

        self.table[fro[0]][fro[1]].player = 0
        self.table[fro[0]][fro[1]].set_kinged(False)

        for x, y in eats:
            self.table[x][y].player = 0
            self.table[x][y].set_kinged(False)

        self.turn = 1 if player == 2 else 2
        if self.is_ended():
            self.turn = 0
        return True

    def is_ended(self):
        for p in [p for line in self.table for p in line if p.player == self.turn]:
            if self.can_go((p.x, p.y)):
                return False
        return True

    def get_score(self):
        first = 0
        second = 0
        for line in self.table:
            for p in line:
                if p.player == 1:
                    first += 1
            for p in line:
                if p.player == 2:
                    second += 1
        return (first, second)
