from pico2d import *

CANVAS_WIDTH, CANVAS_HEIGHT = 1280, 1024
FRAME_W, FRAME_H = 100, 100
FRAME_COUNT = 8

CLIP_Y_IDLE_RIGHT = 0
CLIP_Y_IDLE_LEFT = 100
CLIP_Y_RUN_RIGHT = 200
CLIP_Y_RUN_LEFT = 300

MARGIN_X = FRAME_W // 2 - 15
MARGIN_Y = FRAME_H // 2 - 15

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def get_clip_y(dir_x, dir_y, face_dir):
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
dir_x, dir_y = 0, 0
face_dir = 1
while running:
    clear_canvas()
    tuk_ground.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
    character.clip_draw(frame * FRAME_W, get_clip_y(dir_x, dir_y, face_dir), FRAME_W, FRAME_H, x, y)
    update_canvas()

    handle_events()

    frame = (frame + 1) % FRAME_COUNT
    x += dir_x * 10
    y += dir_y * 10

    x = max(MARGIN_X, min(x, CANVAS_WIDTH - MARGIN_X))
    y = max(MARGIN_Y, min(y, CANVAS_HEIGHT - MARGIN_Y))
    delay(0.05)

close_canvas()
