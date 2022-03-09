import pygame

# 初始设置
pygame.init() # 初始化pygame
screen = pygame.display.set_mode((800,600)) # Pygame窗口
pygame.display.set_caption("Pygame绘制图形") # 标题
keep_going = True
RED = (255,0,0)  # 红色，使用RGB颜色
radius = 50 # 半径
RED2 = (0,255,0)  # 红色，使用RGB颜色
radius2 = 20 # 半径

print("hello world 2 !")

# 游戏循环
while keep_going:
    for event in pygame.event.get():  # 遍历事件
        if event.type == pygame.QUIT:  # 退出事件
            keep_going = False
    pygame.draw.circle(screen,RED,(200,300),radius)
    pygame.draw.circle(screen,RED2,(100,500),radius2)
    pygame.draw.line(screen,RED2, (11,20),(111,222))
    pygame.draw.polygon(screen,RED2,[(50,200),(55,135),(44,233),(30,149)])
    pygame.display.update()  # 刷新屏幕

# 退出程序
pygame.quit()
