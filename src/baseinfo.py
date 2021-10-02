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


class Land(object):
    def __init__(self, owner, loc: int, point: int, desc, item: str, players):
        self.owner = owner  # 拥有者
        self.loc = loc  # 所在位置
        self.point = point  # 地产存成本，矿场存可获取点数
        self.desc = desc  # 描述，用于区分地形
        self.item = item  # 该地的道具
        self.players = players  # 当前在该位置上的玩家们


class Map(object):
    def __init__(self):
        lands = [Land("", 0, 0, "S", "", [])]
        for i in range(1, 14):
            lands.append(Land("", i, 200, "0", "", []))
        lands.append(Land("", 14, 0, "H", "", []))
        for i in range(15, 28):
            lands.append(Land("", i, 200, 0, "", []))
        lands.append(Land("", 28, 0, "T", "", []))
        for i in range(29, 35):
            lands.append(Land("", i, 500, 0, "", []))
        lands.append(Land("", 35, 0, "G", "", []))
        for i in range(36, 49):
            lands.append(Land("", i, 300, 0, "", []))
        lands.append(Land("", 49, 0, "P", "", []))
        for i in range(50, 63):
            lands.append(Land("", i, 300, 0, "", []))
        lands.append(Land("", 63, 0, "M", "", []))
        lands.append(Land("", 64, 60, "$", "", []))
        lands.append(Land("", 65, 80, "$", "", []))
        lands.append(Land("", 66, 40, "$", "", []))
        lands.append(Land("", 67, 100, "$", "", []))
        lands.append(Land("", 68, 80, "$", "", []))
        lands.append(Land("", 69, 20, "$", "", []))

    def move(self, player: Player, source, target):
        player.loc = target
        # TODO 处理移动过程中触发事件的逻辑都可以放在这里

# for x in Map.lands:
#     print(x.owner, x.loc, x.point, x.desc, x.item)
