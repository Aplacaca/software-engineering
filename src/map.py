import utils


class Node(object):
    def __init__(self, color, content, default, owner):
        self.color = color
        self.content = content
        self.default = default
        self.owner = owner


class Map(object):
    """Naive map block"""

    def __init__(self, length: int = 70):
        self.start = Node('black', None, 'S', None)
        self.tool_house = Node('black', None, 'T', None)
        self.gift = Node('black', None, 'G', None)
        self.magic_house = Node('black', None, 'M', None)
        self.hospital = Node('black', None, 'H', None)
        self.prison = Node('black', None, 'P', None)

        self.map = [Node('black', None, '0', None) for i in range(length)]
        self.map[0] = self.start
        self.map[14] = self.hospital
        self.map[28] = self.tool_house
        self.map[35] = self.gift
        self.map[49] = self.prison
        self.map[63] = self.magic_house
        self.map[64:] = [Node('black', None, '$', None) for _ in range(6)]

    def __len__(self):
        return len(self.map)

    def display(self):
        print(self)

    def __str__(self):
        """Split one-dimensional map to two-dimensional str.

        :return: str
        """
        length, width = 30, 8
        self.map2str = [*list(range(length-1)),
                        *[length*i-2 for i in range(2, width)],
                        *list(range(length*width-2, length * (width-1)-1, -1)),
                        *list(range(length * (width-2), 0, -length))]

        lst = [' ' if i % length else '\n' for i in range(1, length*width+1)]
        for i, j in enumerate(self.map2str):
            lst[j] = getattr(utils, self.map[i].color)(self.map[i].default)
            # print(self.map[i].color)
        return ''.join(lst)


if __name__ == '__main__':
    map = Map()
    map.start.color='red'
    map.magic_house.color='blue'
    map.prison.color='green'
    map.display()
