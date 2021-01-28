import pygame

pygame.init()

win = pygame.display.set_mode((1200,400))
track = pygame.image.load('track6.png')
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car , (30,60))

car_x = 150
car_y = 300
focal_dis = 25
cam_x_offset = 0
cam_y_offset = 0
direction = 'up'
clock = pygame.time.Clock()

loop = True

while loop:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            loop = False

    clock.tick(60)
    cam_x = car_x + cam_x_offset + 15
    cam_y = car_y + cam_y_offset + 15

    up_px =  win.get_at((cam_x,cam_y-focal_dis))[0]
    ri_px =  win.get_at((cam_x+focal_dis+10,cam_y))[0]
    lf_px =  win.get_at((cam_x-focal_dis-10,cam_y))[0]
    dw_px =  win.get_at((cam_x,cam_y+focal_dis))[0]
    
    print(up_px, ri_px, dw_px, lf_px)

    if direction == 'up' and ri_px == 255 and up_px != 255:
        direction = 'right'
        cam_x_offset = 30
        car = pygame.transform.rotate(car , -90)

    if direction == 'right' and dw_px == 255 and ri_px != 255:
        direction = 'down'
        cam_x_offset = 0
        cam_y_offset = 30
        car_x = car_x + 35
        car = pygame.transform.rotate(car , -90)
        
                
    if direction == 'down' and ri_px == 255 and dw_px != 255:
        direction = 'right'
        cam_y_offset = 0
        cam_x_offset = 30
        car_y = car_y + 30
        car = pygame.transform.rotate(car , 90)

    if direction == 'right' and up_px == 255 and ri_px != 255:
        direction = 'up'
        car = pygame.transform.rotate(car , 90)
        car_x = car_x + 40
        cam_x_offset = 0


               

    if direction == 'up' and up_px == 255:
        car_y = car_y-2
        
    elif direction == 'right' and ri_px == 255:
        car_x = car_x + 2

    elif direction == 'down' and dw_px ==255:
        car_y = car_y + 2

    elif direction == 'left' and ri_px == 255:
        car_x = car_x - 2
    
    win.blit(track,(0,0))
    win.blit(car,(car_x,car_y))
    pygame.draw.circle(win,(0,255,0),(cam_x,cam_y),5,5)
    
    pygame.display.update()
