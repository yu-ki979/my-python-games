import pygame
import sys
import random

# 初期化
pygame.init()
screen = pygame.display.set_mode((600,400))
font = pygame.font.SysFont(None, 50)

#【論理の定義】自分の手(key)に対して、勝てる相手(value)を定義
rules = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper"
}

player_hand = ""
computer_hand = ""
result = "Press R, P, or S"

while True:
    screen.fill((40,40,60))

    # 描画処理
    msg_disp = font.render(result, True, (255,255,255))
    player_disp = font.render(f"You: {player_hand}", True, (0,255,255))
    comp_disp = font.render(f"CPU: {computer_hand}", True, (255,100,100))

    screen.blit(msg_disp, (50,50))
    screen.blit(player_disp, (100,150))
    screen.blit(comp_disp, (100,220))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            # 入力受付
            if event.key == pygame.K_r: player_hand = "Rock"
            elif event.key == pygame.K_p: player_hand = "Paper"
            elif event.key == pygame.K_s: player_hand = "Scissors"
            else: continue # 指定以外のキーは無視

            # CPUの手を「定義済みリスト」から選ぶ
            computer_hand = random.choice(list(rules.keys()))

            #【判定の型】ifの羅列を辞書一発で解決
            if player_hand == computer_hand:
                result = "DRAW"
            elif rules[player_hand] == computer_hand: # 自分の勝てる相手か？
                result = "YOU WIN!"
            else:
                result = "YOU LOSE..."
    
    pygame.display.update()