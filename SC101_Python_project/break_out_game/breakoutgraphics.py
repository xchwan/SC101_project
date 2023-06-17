"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle_start_x = self.window_width/2-paddle_width/2
        self.paddle_start_y = self.window_height-paddle_offset
        self.window.add(self.paddle, x=self.paddle_start_x, y=self.paddle_start_y)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball_start_x = self.window_width/2-ball_radius
        self.ball_start_y = self.window_height/2-ball_radius
        self.window.add(self.ball, x=self.ball_start_x, y=self.ball_start_y)
        # Default initial velocity for the ball
        self.__dx = random.uniform(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED
        # Initialize our mouse listeners
        onmousemoved(self.paddle_position)
        onmouseclicked(self.ball_start)
        self.click = False
        # Draw bricks
        self.brick_count = brick_rows*brick_cols
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if j == 0 or j == 1:
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'
                elif j == 2 or j == 3:
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'
                elif j == 4 or j == 5:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'
                elif j == 6 or j == 7:
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green'
                else:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'
                self.window.add(self.brick, x=(brick_width+brick_spacing)*i,
                                y=brick_offset+(brick_height+brick_spacing)*j)

    def paddle_position(self, mouse):
        """
        set up paddle on mouse move function
        :param mouse:
        :return: None
        """
        if mouse.x - self.paddle.width / 2 > 0 and mouse.x + self.paddle.width / 2 < self.window.width:
            self.paddle.x = mouse.x - self.paddle.width / 2

    def ball_start(self, mouse):
        """
        update click to True while on mouse click
        :param mouse:
        :return: None
        """
        self.click = True

    def get_ball_vx(self):
        """
        get ball velocity of x direction
        :return: ball velocity of x direction
        """
        return self.__dx

    def get_ball_vy(self):
        """
        get ball velocity of y direction
        :return: ball velocity of y direction
        """
        return self.__dy

    def ball_initial(self):
        """
        set up initial parameter before ball start
        :return: None
        """
        self.ball.x = self.ball_start_x
        self.ball.y = self.ball_start_y
        self.click = False

    def ball_out(self):
        """
        check ball drop or not
        :return: True/False of ball drop
        """
        return self.ball.y >= self.window_height - self.ball.height

    def ball_reflect_left(self):
        """
        check ball touch window left
        :return: True/False when ball touch window left
        """
        return self.ball.x <= 0

    def ball_reflect_right(self):
        """
        check ball touch window right
        :return: True/False when ball touch window right
        """
        return self.ball.x + self.ball.width >= self.window_width

    def ball_reflect_top(self):
        """
        check ball touch window top
        :return: True/False when ball touch window top
        """
        return self.ball.y <= 0

    def obj_ball_hit(self):
        """
        get objects when ball hit
        :return: objects of ball hit
        """
        obj1 = self.window.get_object_at(self.ball.x, self.ball.y)
        obj2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        obj3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        obj4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        if obj1:
            return obj1
        elif obj2:
            return obj2
        elif obj3:
            return obj3
        else:
            return obj4
