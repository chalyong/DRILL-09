from pico2d import *

CANVAS_WIDTH, CANVAS_HEIGHT = 1280, 1024
FRAME_W, FRAME_H = 100, 100
FRAME_COUNT = 8

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


running = True
frame = 0
while running:
    clear_canvas()
    tuk_ground.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
    character.clip_draw(frame * FRAME_W, 0, FRAME_W, FRAME_H, CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
    update_canvas()

    handle_events()

    frame = (frame + 1) % FRAME_COUNT
    delay(0.05)

close_canvas()
