import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((600,400))
font = pygame.font.SysFont(None, 60)

# 初期設定
current_num = random.randint(1, 10) # 今の数字
message = "H(High) or L(Low)" # 画面に出すメッセージ
score = 0

while True:
    screen.fill((30,30,30))

    # メッセージと数字の表示
    msg_disp = font.render(message, True, (255, 255, 255))
    num_disp = font.render(f"Number: {current_num}", True, (255, 215, 0))
    score_disp = font.render(f"Score: {score}", True, (0, 255, 127))

    screen.blit(msg_disp, (100, 50))
    screen.blit(num_disp, (200, 150))
    screen.blit(score_disp, (200, 250))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            print(f"Key pressed: {event.key}")
        # 判定のロジック
        if event.type == pygame.KEYDOWN:
            next_num = random.randint(1, 10) # 次の数字を裏で決める

            if event.key == pygame.K_h: # Highを選んだら
                if next_num >= current_num:
                    message = "WIN! (Next was higher)"
                    score += 1
                else:
                    message = "LOSE... (Next was lower)"
                    score = 0
                current_num = next_num # 次の数字を今の数字にする
            
            if event.key == pygame.K_l: # Lowを選んだら
                if next_num <= current_num:
                    message = "WIN! (Next was lower)"
                else:
                    message = "LOSE! (Next was higher)"
                    score = 0
                current_num = next_num

    pygame.display.update()