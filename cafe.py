# 模拟程序员用咖啡提神的过程

class Programmer:
    def __init__(self, name):
        self.name = name
        self.energy_level = 50  # 初始能量水平，最大为100
    
    def drink_coffee(self):
        # 喝咖啡提高能量
        if self.energy_level <= 90:
            self.energy_level += 10
            print(f"{self.name} 喝了一杯咖啡。能量水平提高到 {self.energy_level}%.")
        else:
            print(f"{self.name} 能量已经很高，不需要再喝咖啡。")
    
    def code(self, hours):
        # 编程消耗能量
        energy_consumed = hours * 10
        if self.energy_level >= energy_consumed:
            self.energy_level -= energy_consumed
            print(f"{self.name} 编程 {hours} 小时。能量水平降低到 {self.energy_level}%.")
        else:
            print(f"{self.name} 能量不足，无法编程 {hours} 小时。")

# 创建一个程序员对象
programmer = Programmer("小陈")

# 模拟一天的工作
programmer.code(2)
programmer.drink_coffee()
programmer.code(3)
programmer.drink_coffee()
programmer.code(5)
