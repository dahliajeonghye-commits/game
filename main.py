import pygame
import sys
import random

# 초기화
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("둘리 vs 고길동")

# 색상
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)   # 둘리
RED = (255, 0, 0)     # 고길동
BLUE = (0, 0, 255)    # 냉장고

# 캐릭터 설정
player_size = 50
enemy_size = 50
fridge_size = 60

# 이미지 로드
dooly_img = pygame.image.load("./images/dooly.png")
gogildong_img = pygame.image.load("./images/go.png")
ref_img = pygame.image.load("./images/ref.png")
background_img = pygame.image.load("./images/back.png")



# 크기 조절 (선택)
dooly_img = pygame.transform.scale(dooly_img, (100, 100))
gogildong_img = pygame.transform.scale(gogildong_img, (120, 120))
ref_img = pygame.transform.scale(ref_img, (150, 150))
background_img = pygame.transform.scale(background_img, (800, 600))

player_pos = [100, 100]
enemy_pos = [WIDTH - 100, HEIGHT - 100]
fridge_pos = [WIDTH // 2, HEIGHT // 2]

player_speed = 5
enemy_speed = 2

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def draw_text(text, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def move_enemy():
    if enemy_pos[0] < player_pos[0]:
        enemy_pos[0] += enemy_speed
    elif enemy_pos[0] > player_pos[0]:
        enemy_pos[0] -= enemy_speed
    if enemy_pos[1] < player_pos[1]:
        enemy_pos[1] += enemy_speed
    elif enemy_pos[1] > player_pos[1]:
        enemy_pos[1] -= enemy_speed

def check_collision(pos1, size1, pos2, size2):
    rect1 = pygame.Rect(*pos1, size1, size1)
    rect2 = pygame.Rect(*pos2, size2, size2)
    return rect1.colliderect(rect2)

# 게임 루프
running = True
while running:
    screen.blit(background_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - player_size:
        player_pos[1] += player_speed

    # 고길동 이동
    move_enemy()

    # 충돌 체크
    if check_collision(player_pos, player_size, enemy_pos, enemy_size):
        draw_text("game over! you are dead!", RED, 150, HEIGHT // 2)
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False

    if check_collision(player_pos, player_size, fridge_pos, fridge_size):
        draw_text("Achievement! ", GREEN, 150, HEIGHT // 2)
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False

    # 그리기
    screen.blit(dooly_img, player_pos)       # 둘리 이미지 표시
    screen.blit(gogildong_img, enemy_pos)    # 고길동 이미지 표시
    screen.blit(ref_img, fridge_pos)    # 냉장고 이미지 표시
    #pygame.draw.rect(screen, GREEN, (*player_pos, player_size, player_size))  # 둘리
    #pygame.draw.rect(screen, RED, (*enemy_pos, enemy_size, enemy_size))       # 고길동
    #pygame.draw.rect(screen, BLUE, (*fridge_pos, fridge_size, fridge_size))   # 냉장고

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
