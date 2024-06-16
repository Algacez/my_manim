from manimlib import *

class BallMoving(Scene):
    def construct(self):
        # 创建一个带有刻度和数字的坐标系
        plane = NumberPlane(
            x_range=[-2, 2, 1],  # x 轴范围和刻度
            y_range=[-2, 2, 1],  # y 轴范围和刻度
            axis_config={"color": BLUE},
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 2,
                "stroke_opacity": 0.6
            }
        )
        plane.add_coordinate_labels()  # 添加刻度和数字

        # 创建一个小球
        ball = Dot(color=RED).move_to(plane.c2p(-1, 0))

        # 添加坐标系和小球到场景中
        self.add(plane, ball)

        # 创建小球从 x = -1 到 x = 1 的动画
        ball_animation = ball.animate.move_to(plane.c2p(1, 0))

        # 播放动画
        self.play(ball_animation, run_time=4)  # 设置动画持续时间为 4 秒
        self.wait()

# 运行命令：python -m manim -pql example_scenes.py BallMoving

# manimgl 1.py BallMoving -ow