import pygame

pygame.init() # 초기화 작업 (필수)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado game") # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/pc/Desktop/PythonWorkspace/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/pc/Desktop/PythonWorkspace/pygame_basic/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴 # rectalge = 직사각형
character_width = character_size[0] # 캐릭터 가로 크기
character_height = character_size[1] # 캐릭터 세로 크기
character_x_pos = screen_width / 2 - character_width / 2 # 화면 가로 크기 절반에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이동할 좌표 변수 선언
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.5

# 적 enemy 캐릭터
enemy = pygame.image.load("C:/Users/pc/Desktop/PythonWorkspace/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size # 이미지의 크기 구현 # rectalge = 직사각형
enemy_width = enemy_size[0] # 캐릭터 가로 크기
enemy_height = enemy_size[1] # 캐릭터 세로 크기
enemy_x_pos = screen_width / 2 - enemy_width / 2 # 화면 가로 크기 절반에 해당하는 곳에 위치
enemy_y_pos = screen_height / 2 - enemy_height / 2 # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 10 

# 시작 시간 정보
start_ticks = pygame.time.get_ticks() # 시작 tick을 받아옴

# 이벤트 루프가 있어야 창이 안꺼짐
# 이벤트 루프
running = True # 게임이 진행중인가 ?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수 설정, delta
    for event in pygame.event.get(): # 이벤트가 발생하였는가 ?
        if event.type == pygame.QUIT: # 만약 창이 닫히는 이벤트가 발생한다면
            running = False 
        if event.type == pygame.KEYDOWN: # 키 입력 확인 (이동 시작)
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed # to_x = to_x - character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP: # 캐릭터를 위쪽으로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # 캐릭터를 아래쪽으로
                to_y += character_speed
        
        if event.type == pygame.KEYUP: # 키 입력 마침 (이동 종료)
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect): # 사각형 기준으로 충돌을 했는가 ?
        print("충돌했어요.")
        running = False


    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 에너미 그리기

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 경과 시간(ms)을 1000으로 나누어서 초 단위로 표시
    
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255)) # 출력할 글자, True, 글자 색상
    screen.blit(timer, (10, 10))
    pygame.display.update() # 게임화면 다시 그리기
    if total_time - elapsed_time <= 0:
        print("타임 아웃")
        running = False

# 잠시 대기
pygame.time.delay(2000) # 2초 대기
# pygame 종료
pygame.quit()