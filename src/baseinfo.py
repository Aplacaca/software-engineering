import utils


class Player(object):
    def __init__(self, name, loc: int, fund: int, credit: int, bomb_num: int, barrier_num: int, robot_num: int,
                 rich_god_num: int, stay_num: int):
        self.name = name  # 玩家名称
        self.loc = loc  # 玩家所处位置
        self.fund = fund  # 资金
        self.credit = credit  # 点数
        self.bomb_num = bomb_num  # 拥有炸弹数量
        self.barrier_num = barrier_num  # 拥有障碍数量
        self.robot_num = robot_num  # 拥有机器人数量
        self.rich_god_num = rich_god_num  # 财神附身剩余次数
        self.stay_num = stay_num  # 在医院或监狱停留的轮数


class Node(object):
    def __init__(self, owner, loc: int, color, point, desc, item, players):
        self.owner = owner  # 拥有者
        self.loc = loc  # 序号
        self.color = color  # 颜色
        self.point = point  # 地产存成本，矿场存可获取点数
        self.desc = desc  # 描述，用于区分地形
        self.item = item  # 该地的道具
        self.players = players  # 当前在该位置上的玩家们


class Map(object):
    def __init__(self):
        self.start = Node(None, 0, 'red', None, 'S', None, None)
        self.tool_house = Node(None, 28, 'red', None, 'T', None, None)
        self.gift_house = Node(None, 35, 'red', None, 'G', None, None)
        self.magic_house = Node(None, 63, 'red', None, 'M', None, None)
        self.hospital = Node(None, 14, 'red', None, 'H', None, None)
        self.prison = Node(None, 49, 'red', None, 'P', None, None)

        self.map = [Node(None, i, 'black', None, 0, None, None) for i in range(70)]
        self.map[0] = self.start
        self.map[14] = self.hospital
        self.map[28] = self.tool_house
        self.map[35] = self.gift_house
        self.map[49] = self.prison
        self.map[63] = self.magic_house
        self.map.append(Node(None, 64, 'black', 60, "$", None, None))
        self.map.append(Node(None, 65, 'black', 80, "$", None, None))
        self.map.append(Node(None, 66, 'black', 40, "$", None, None))
        self.map.append(Node(None, 67, 'black', 100, "$", None, None))
        self.map.append(Node(None, 68, 'black', 80, "$", None, None))
        self.map.append(Node(None, 69, 'black', 20, "$", None, None))

    def __len__(self):
        return len(self.map)

    def display(self):
        print(self)

    def __str__(self):
        length, width = 30, 8
        self.map2str = [*list(range(length - 1)),
                        *[length * i - 2 for i in range(2, width)],
                        *list(range(length * width - 2, length * (width - 1) - 1, -1)),
                        *list(range(length * (width - 2), 0, -length))]

        lst = [' ' if i % length else '\n' for i in range(1, length * width + 1)]
        for i, j in enumerate(self.map2str):
            desc = self.map[i].desc
            if isinstance(desc, int):
                desc = str(desc)
            lst[j] = desc
            # lst[j] = getattr(utils, self.map[i].color)(self.map[i].desc)
            # print(self.map[i].color)
        return ''.join(lst)

    def move(self, player: Player, source, target):
        player.loc = target
        # TODO 处理移动过程中触发事件的逻辑都可以放在这里


if __name__ == '__main__':
    map = Map()
    map.start.color = 'red'
    map.magic_house.color = 'blue'
    map.prison.color = 'green'
    map.display()
