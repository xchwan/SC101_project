"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    """
    program of breakout brick game
    """
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    vx = graphics.get_ball_vx()
    vy = graphics.get_ball_vy()
    # Add the animation loop here!
    while lives > 0:
        pause(FRAME_RATE)
        if graphics.click:
            graphics.ball.move(vx, vy)
            if graphics.ball_out():
                lives -= 1
                graphics.ball_initial()
            if graphics.ball_reflect_left():
                vx *= -1
            if graphics.ball_reflect_right():
                vx *= -1
            if graphics.ball_reflect_top():
                vy *= -1
            if graphics.obj_ball_hit():
                if graphics.obj_ball_hit() == graphics.paddle:
                    graphics.ball.y = graphics.paddle.y - graphics.ball.height
                else:
                    graphics.window.remove(graphics.obj_ball_hit())
                    graphics.brick_count -= 1
                vy *= -1
            if graphics.brick_count == 0:
                graphics.ball_initial()


if __name__ == '__main__':
    main()
