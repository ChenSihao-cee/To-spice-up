import os  
import time  

def clear_screen(width):  # 清屏函数
    os.system('cls' if os.name == 'nt' else 'clear') 
    print("西安" +" " * width +"南京") #地图

def print_plane(position, ShaoShuai=False):  # 飞机和少帅
    # 打印飞机和少帅
    if ShaoShuai:  # 如果有少帅
        print(" " * position + "✈️💺少帅" + " " * (30 - position - 6))  # 飞机带少帅
    else:  # 如果没有少帅
        print(" " * position + "🛬" + " " * (30 - position - 1))  

def print_guards(offset, width, ShaoShuai=False):  # 卫兵和少帅
    if ShaoShuai:  # 少帅下飞机
        print("\n" * offset + " " * width + "👮少帅👮")
    else:  # 等少帅
        print("\n" * offset +" " * width + "👮        👮")

def main():  
    plane_position = 5  # 飞机初始位置
    width = 60  # 距离
    offset = 1  #卫兵初始行
    
    # 初始化位置
    clear_screen(width)  
    print_plane(plane_position)  # 打印飞机
    print_guards(offset, width)  # 打印卫兵
    time.sleep(2) 
    
    # 少帅上飞机
    for i in range(6):  
        clear_screen(width) 
        print_plane(plane_position)  
        print(" " * i + "少帅")  # 少帅走
        print_guards(offset-1, width) 
        time.sleep(0.2)  # 等待0.2秒
    
    # 飞机飞行
    for i in range(width-3):  # 飞机飞行
        clear_screen(width) 
        print_plane(plane_position, ShaoShuai=True)  # 飞机带少帅
        print_guards(offset, width)
        time.sleep(0.1)  
        plane_position += 1  # 飞机飞
    
    # 飞机到达中间位置后，等待一段时间
    clear_screen(width)  
    print_plane(plane_position, ShaoShuai=True)  # 飞机带少帅
    print_guards(offset, width)
    time.sleep(1)  # 等待1秒
    
    # 少帅下飞机
    clear_screen(width) 
    print_plane(plane_position, ShaoShuai=False)  
    print_guards(offset-1,width+2,ShaoShuai=True)  # 卫兵接少帅
    time.sleep(0.8)
    
    # 少帅和卫兵一起向下移动
    for i in range(5):  # 循环5次
        clear_screen(width)  
        print_plane(plane_position)  
        print_guards(i, width+i+2,ShaoShuai=True)  # 卫兵押少帅
        time.sleep(0.8)  #没病走两步

if __name__ == "__main__":  
    main()  # 调用主函数