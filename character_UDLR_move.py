from pico2d import *

# 캔버스 크기 (배경 이미지 크기와 동일)
CANVAS_WIDTH, CANVAS_HEIGHT = 1280, 1024

# 스프라이트 프레임 정보
FRAME_W, FRAME_H = 100, 100
FRAME_COUNT = 8

# 스프라이트 시트 행(clip_y)
CLIP_Y_IDLE_RIGHT = 0
CLIP_Y_IDLE_LEFT = 100
CLIP_Y_RUN_RIGHT = 200
CLIP_Y_RUN_LEFT = 300

# 이동 속도(px/frame), 프레임 지연(초)
MOVE_SPEED = 10
FRAME_DELAY = 0.05

# 스프라이트가 화면 밖으로 잘리지 않게 하는 경계 여유분
MARGIN_X = FRAME_W // 2 - 15
MARGIN_Y = FRAME_H // 2 - 15

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def get_clip_y(dir_x, dir_y, face_dir):
    # 좌우 이동이 상하보다 우선, 상하로만 이동 시 직전 좌우 방향 유지
    if dir_x > 0:
        return CLIP_Y_RUN_RIGHT
    if dir_x < 0:
        return CLIP_Y_RUN_LEFT
    if dir_y != 0:
        return CLIP_Y_RUN_RIGHT if face_dir == 1 else CLIP_Y_RUN_LEFT
    return CLIP_Y_IDLE_RIGHT if face_dir == 1 else CLIP_Y_IDLE_LEFT


def handle_events():
    global running, dir_x, dir_y, face_dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
                face_dir = 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
                face_dir = -1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1


running = True
frame = 0
x, y = CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2
dir_x, dir_y = 0, 0  # 현재 입력 중인 이동 방향
face_dir = 1         # 마지막으로 바라본 좌/우 방향 (1: 우, -1: 좌)

while running:
    clear_canvas()
    tuk_ground.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
    character.clip_draw(frame * FRAME_W, get_clip_y(dir_x, dir_y, face_dir), FRAME_W, FRAME_H, x, y)
    update_canvas()

    handle_events()

    frame = (frame + 1) % FRAME_COUNT
    x += dir_x * MOVE_SPEED
    y += dir_y * MOVE_SPEED

    # 화면 경계 이탈 방지
    x = max(MARGIN_X, min(x, CANVAS_WIDTH - MARGIN_X))
    y = max(MARGIN_Y, min(y, CANVAS_HEIGHT - MARGIN_Y))
    delay(FRAME_DELAY)

close_canvas()
