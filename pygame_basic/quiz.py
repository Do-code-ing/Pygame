import pygame
import random
#######################################################
# 기본 초기화 (필수)
pygame.init() # 초기화 작업 (필수)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Avoid The Ddong") # 게임 이름

# FPS
clock = pygame.time.Clock()
#######################################################
# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
background = pygame.image.load("C:/Users/pc/Desktop/PythonWorkspace/pygame_basic/background.png")

character = pygame.image.load("C:/Users/pc/Desktop/PythonWorkspace/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0] # [0] = 첫 번째 값, 즉 앞서 렉트한 값이 70 * 70인데 70의 값을 의미
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height
to_x = 0
character_speed = 10

enemy = pygame.image.load("C:/Users/pc/Desktop/PythonWorkspace/pygame_basic/enemy.png")
enemy_size = enemy.get_rect()
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
# e_to_x = 0
enemy_speed = 10
# plus_speed = 2

total_time = 0 
start_ticks = pygame.time.get_ticks() # 시간 측정 행위
game_font = pygame.font.Font(None, 40)

# 이벤트 루프가 있어야 창이 안꺼짐
# 이벤트 루프
running = True # 게임이 진행중인가 ?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수 설정, delta
    
    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x
    enemy_y_pos += enemy_speed
    # enemy_y_pos += enemy

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): # 이벤트가 발생하였는가 ?
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                to_x -= character_speed
            elif event.key == pygame.K_d:
                to_x += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                to_x = 0

        if event.type == pygame.QUIT: # 만약 창이 닫히는 이벤트가 발생한다면
            running = False 

    # 에너미 낙하 후 리셋

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)
        # enemy_speed += plus_speed

    # 4. 경계값 및 충돌처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌했어요.")
        running = False

    # 타이머

    elapsed_time = (pygame.time.get_ticks() + start_ticks) / 1000
    timer = game_font.render(str(int(total_time + elapsed_time)), True, (255, 255, 255)) # 출력할 글자, True, 글자 색상

    # 5. 화면에 그리기

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(timer, (10, 10))
    
    pygame.display.update() # 게임화면 다시 그리기



pygame.quit()