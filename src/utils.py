
def red(pattern: str):
    return '\033[31m {}'.format(pattern)


def blue(pattern: str):
    return '\033[34m {}'.format(pattern)


def green(pattern: str):
    return '\33[32m {}'.format(pattern)


def do_help():
    message = "帮助信息\n" \
              "\tstart         —— 开始游戏🎮\n" \
              "\troll          —— 掷骰子🎲\n" \
              "\tsell n        —— 卖房子🏠，n指的是房子所占地块的索引\n" \
              "\tblock n       —— 放路障🚧，n指的是与玩家当前位置的相对距离(-10,10)\n" \
              "\tbomb n        —— 放置炸弹💣，n表示炸弹与玩家当前位置的相对距离(-10,10)\n" \
              "\trobot         —— 使用机器人娃娃🤖\n️" \
              "\tquery         —— 查询当前玩家所有资产💰信息\n" \
              "\tquit          —— 推出游戏🎮\n" \
              "\thelp          —— 显示此帮助\n"
    print(message)

