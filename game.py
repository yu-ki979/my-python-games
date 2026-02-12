import pygame
import sys

# 1.初期化
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My First Game")
clock = pygame.time.Clock()

x = 0 # 四角形の横の位置
y = 200
# 2.ゲームループ
while True:
    # A.イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # ロジック
    # x += 5
    # if x > 640:
    #     x = -50

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: x -= 5   
    if keys[pygame.K_RIGHT]: x += 5
    if keys[pygame.K_UP]: y -= 5
    if keys[pygame.K_DOWN]: y += 5

        

    # B.描画処理
    screen.fill((0,0,100)) # 背景を濃い青に

    # 白い四角形を描く（画面, 色, [x座標, y座標, 幅, 高さ]）
    pygame.draw.rect(screen, (255,255,255), [x, y,50,50])

    # 3. 画面更新
    pygame.display.update()
    clock.tick(60) 

