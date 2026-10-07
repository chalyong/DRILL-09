from pico2d import *

CANVAS_WIDTH, CANVAS_HEIGHT = 1280, 1024
FRAME_W, FRAME_H = 100, 100
FRAME_COUNT = 8

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running, dir_x
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1


running = True
frame = 0
x = CANVAS_WIDTH // 2
dir_x = 0
while running:
    clear_canvas()
    tuk_ground.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)

    if dir_x > 0:
        clip_y = 200
    else:
        clip_y = 0
    character.clip_draw(frame * FRAME_W, clip_y, FRAME_W, FRAME_H, x, CANVAS_HEIGHT // 2)
    update_canvas()

    handle_events()

    frame = (frame + 1) % FRAME_COUNT
    x += dir_x * 10
    delay(0.05)

close_canvas()
