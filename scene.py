from manim import *
from math import sin, pi

class Triangle(object):
    def __init__(self, rt_vertices,side_lengths,scale):
        self.rt_vertices = rt_vertices
        self.scale = scale 
        for v in self.rt_vertices:
            for i in [0,1,2]:
                v[i] = v[i]/scale

        theta_vertices = [
            rt_vertices[1],
            rt_vertices[0],
            rt_vertices[2],
        ]
        theta_2_vertices = [
            rt_vertices[1],
            rt_vertices[2],
            rt_vertices[0],
        ]
        self.triangle = Polygon(*rt_vertices, color=YELLOW)
        self.rt_angle = RightAngle.from_three_points(*rt_vertices, elbow=True, radius=0.15)
        self.theta_angle = Angle.from_three_points(*theta_vertices, radius=0.25)
        self.theta_value = DecimalNumber(
            self.theta_angle.get_value(degrees=True),
            font_size = 10,
            num_decimal_places=0,
            unit = r"^{\circ}"
        ).next_to(self.theta_angle,RIGHT,buff=0.05).shift(UP*0.005)
        self.theta_value.set_value(abs(self.theta_value.number))

        self.theta_2_angle = Angle.from_three_points(*theta_2_vertices, radius=0.25, other_angle=True)
        self.theta_2_value = DecimalNumber(
            self.theta_2_angle.get_value(degrees=True),
            font_size = 10,
            num_decimal_places=0,
            unit = r"^{\circ}"
        ).next_to(self.theta_2_angle,DOWN,buff=0.05).shift(LEFT*0.005)
        self.theta_2_value.set_value(abs(self.theta_2_value.number))

        self.side_lengths = side_lengths
        self.side_lengths[0]
        self.side_lengths[1].next_to(self.triangle, RIGHT, buff=0.05)
        self.side_lengths[2].next_to(self.triangle,DOWN,buff=0.05)
    def write(self,scene):
        scene.play(
            Write(self.triangle),
            Write(self.theta_angle),
            Write(self.theta_value),
            Write(self.theta_2_angle),
            Write(self.theta_2_value),
            Write(self.rt_angle),
            Write(self.side_lengths[0]),
            Write(self.side_lengths[1]),
            Write(self.side_lengths[2]),
        )
    def unwrite(self,scene):
        scene.play(
            Unwrite(self.triangle),
            Unwrite(self.theta_angle),
            Unwrite(self.theta_value),
            Unwrite(self.theta_2_angle),
            Unwrite(self.theta_2_value),
            Unwrite(self.rt_angle),
            Unwrite(self.side_lengths[0]),
            Unwrite(self.side_lengths[1]),
            Unwrite(self.side_lengths[2]),
        )
    def shift(self,scene,direction):
        scene.play(
            self.triangle.animate.shift(direction),
            self.theta_angle.animate.shift(direction),
            self.theta_value.animate.shift(direction),
            self.theta_2_angle.animate.shift(direction),
            self.theta_2_value.animate.shift(direction),
            self.rt_angle.animate.shift(direction),
            self.side_lengths[0].animate.shift(direction),
            self.side_lengths[1].animate.shift(direction),
            self.side_lengths[2].animate.shift(direction),
    )
    def instant_shift(self,direction):
        self.triangle.shift(direction),
        self.theta_angle.shift(direction),
        self.theta_value.shift(direction),
        self.theta_2_angle.shift(direction),
        self.theta_2_value.shift(direction),
        self.rt_angle.shift(direction),
        self.side_lengths[0].shift(direction),
        self.side_lengths[1].shift(direction),
        self.side_lengths[2].shift(direction),
    def indicate(self,scene):
        scene.play(
            Indicate(self.triangle),
            Indicate(self.theta_angle),
            Indicate(self.theta_value),
            Indicate(self.theta_2_angle),
            Indicate(self.theta_2_value),
            Indicate(self.rt_angle),
            Indicate(self.side_lengths[0]),
            Indicate(self.side_lengths[1]),
            Indicate(self.side_lengths[2]),
        )

class Introduction(Scene):
    def construct(self):
        circle = Circle();
        square = Square();

        intro_text_1 = MarkupText(
                f'<span underline="double" underline_color="green">Jan-Hendrik Brink</span>',
                font_size=32,
                color=WHITE
        )
        
        intro_text_2 = Text("Grade 10 Trigonometry", font_size=24, color=YELLOW)
        intro_text_2.next_to(intro_text_1,DOWN,buff=0.2)
        
        self.play(Create(circle))
        self.play(Transform(circle,square))
        self.play(circle.animate.rotate(PI / 4))
        self.play(Transform(circle,intro_text_1), FadeIn(intro_text_2))
        
        self.wait(3)

        self.play(FadeOut(circle), FadeOut(intro_text_2))





class Overview(Scene):
    def construct(self):
        overview_text_1 = MarkupText(
            f'A Quick Overview',
                font_size=16,
                color=WHITE
        )

        line1 = Line(LEFT*0.5,RIGHT*0.5)
        line2 = Line(LEFT*0.5,(RIGHT+UP*(3/2))*0.5)
        line3 = Line(LEFT*1.5,(LEFT*0.5))
        angle1 = Angle(line1,line2,radius=0.4)
        value1 = DecimalNumber(
                angle1.get_value(degrees=True),
                font_size = 12,
                unit = r"^{\circ}"
        )
        angle2 = Angle(line2,line3,radius=0.4,quadrant=(1,-1))
        value2 = DecimalNumber(
                angle2.get_value(degrees=True),
                font_size = 12,
                unit = r"^{\circ}"
        )
        angle3 = Angle(line3,line2,radius=0.4,quadrant=(-1,1))
        value3 = DecimalNumber(
                angle3.get_value(degrees=True),
                font_size = 12,
                unit = r"^{\circ}"
        )

        value1.next_to(angle1,RIGHT)
        value2.next_to(angle2,LEFT)
        value3.next_to(angle3,RIGHT)

        self.play(Write(overview_text_1),runtime=1)
        self.play(ShowPassingFlash(Underline(overview_text_1)),run_time=2)
        self.play(overview_text_1.animate.shift(UP), buff=0.2, run_time=2)

        self.wait(1)

        self.play(Create(line1), Create(line2),runtime=2)
        self.play(Create(angle1), Create(value1),runtime=2)
        
        self.wait(1)

        self.play(FadeOut(angle1),FadeOut(value1),Transform(line1,line3), buff=0.2, runtime=2)

        self.play(Create(angle2), Create(value2), runtime=2)

        self.wait(1)

        self.play(FadeOut(angle2), FadeOut(value2), runtime=2)

        self.play(Create(angle3), Create(value3),runtime=2)
        
        self.wait(1)

        self.play(Unwrite(overview_text_1), Uncreate(line1),Uncreate(line2),Uncreate(angle3),Uncreate(value3))

        self.play(FadeOut(overview_text_1), FadeOut(line1), FadeOut(line2), FadeOut(angle3), FadeOut(value3)) 

        self.wait(1)

class TrigFunctions(Scene):
    def construct(self):

        title = Tex(r"\underline{\text{Trigonometric Functions}}", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.shift(UP))
        self.wait(1)

        rt_vertices = [

                np.array([0.5,0.5,0]),
                np.array([0.5,-0.5,0]),
                np.array([-0.5,-0.5,0]),
        ]
        theta_vertices = [
                rt_vertices[1],
                rt_vertices[2],
                rt_vertices[0],
        ]
        triangle = Polygon(*rt_vertices, color=BLUE)
        theta_angle = Angle.from_three_points(*theta_vertices, radius=0.25)
        theta_value = MathTex(r"\theta", font_size=16)
        theta_value.next_to(theta_angle, RIGHT)
 

        self.play(Write(triangle), run_time=2)

        r_angle = RightAngle.from_three_points(*rt_vertices, elbow=True, radius=0.15)
        self.play(Write(r_angle))

        self.play(Write(theta_angle), Write(theta_value))


        self.play(triangle.animate.shift(RIGHT), r_angle.animate.shift(RIGHT), theta_value.animate.shift(RIGHT), theta_angle.animate.shift(RIGHT))

        funcs_text = MathTex(r"\sin{\theta} = \frac{o}{s} \\ \cos{\theta} = \frac{a}{s} \\ \tan{\theta} = \frac{o}{a}", font_size=24)
        self.wait(1)
        funcs_text.next_to(triangle, LEFT)
        self.play(Write(funcs_text))
        self.wait(1)
        self.play(funcs_text.animate.shift(LEFT));

        txt_o = Text(r"o", font_size=16)
        txt_o.next_to(triangle,RIGHT)
        txt_a = Text(r"a",font_size=16)
        txt_a.next_to(triangle,DOWN)
        txt_s = Text(r"s",font_size=16)
        txt_s.next_to(triangle,UL,buff=-0.4)

        def_o = Text(r"o = opposite", font_size=12)
        def_o.next_to(funcs_text,DOWN)
        def_a = Text(r"a = adjacient", font_size=12)
        def_a.next_to(def_o,RIGHT)
        def_s = Text(r"o = hypotenuse", font_size=12)
        def_s.next_to(def_a,RIGHT)

        self.play(Write(txt_o), Write(txt_a), Write(txt_s))
        self.play(Write(def_o),Write(def_a),Write(def_s))
        
        self.wait(2)

        self.play(
                Unwrite(title), Unwrite(funcs_text), Unwrite(triangle),
                Unwrite(txt_o), Unwrite(txt_a), Unwrite(txt_s),
                Unwrite(r_angle), Unwrite(theta_angle), Unwrite(theta_value),
                Unwrite(def_o), Unwrite(def_s), Unwrite(def_a),
                run_time=3
        )

class TrigFunctionsExample_1(Scene):
    def construct(self):
        title = Tex(r"\underline{\text{Example 1}}",font_size=36)
        self.play(Write(title))
        self.play(Circumscribe(title))
        #self.play(Circumscribe(title, Circle))
        #self.play(Circumscribe(title, fade_out=True))
        #self.play(Circumscribe(title, time_width=2))
        #self.play(Circumscribe(title, Circle, True))
        self.wait(1)
        self.play(FadeOut(title))
        self.wait(1)

        question = Tex(r"Use the given angle and hypotenuse length along with trigonometric functions \\ to determine the length of the opposite and adjacent sides", font_size=12)

        self.play(Write(question))
        self.play(Indicate(question))
        self.play(question.animate.shift(UP), buff=0.2, run_time=2)
        self.wait(1)

        rt_vertices = [

                np.array([0.5,0.366,0]),
                np.array([0.5,-0.5,0]),
                np.array([-1.0,-0.5,0]),
        ]
        theta_vertices = [
                rt_vertices[1],
                rt_vertices[2],
                rt_vertices[0],
        ]
        triangle = Polygon(*rt_vertices, color=YELLOW)
        theta_angle = Angle.from_three_points(*theta_vertices, radius=0.25)
        theta_value = DecimalNumber(
                theta_angle.get_value(degrees=True),
                font_size = 12,
                num_decimal_places=0,
                unit = r"^{\circ}=\theta"
        ).shift(UP*0.1)

        theta_value.next_to(theta_angle, RIGHT)

        self.play(Write(triangle), run_time=2)

        r_angle = RightAngle.from_three_points(*rt_vertices, elbow=True, radius=0.15)
        self.play(Write(r_angle))

        self.play(Write(theta_angle), Write(theta_value))

        txt_s = Text(r"2",font_size=12)
        txt_s.next_to(triangle,UL,buff=-0.4)
        txt_o = Text(r"o", font_size=12)
        txt_o.next_to(triangle,RIGHT)
        txt_a = Text(r"a",font_size=12)
        txt_a.next_to(triangle,DOWN)

        self.play(Write(txt_o), Write(txt_a), Write(txt_s))

        self.play(
            triangle.animate.shift(RIGHT),
            theta_angle.animate.shift(RIGHT),
            theta_value.animate.shift(RIGHT),
            txt_s.animate.shift(RIGHT),
            txt_a.animate.shift(RIGHT),
            txt_o.animate.shift(RIGHT),
            r_angle.animate.shift(RIGHT),
        )
        
        txt_count = Tex(r"\text{answer will be reveiled in:}",font_size=10, color=BLUE)
        txt_count.next_to(triangle,LEFT,buff=0.5)
        txt_count.shift(UP*0.5)
        self.play(Create(txt_count))

        for i in range(5):
            count_down = Text(str(5-i), color=BLUE)
            count_down.next_to(triangle,LEFT,buff=1)
            self.play(FadeIn(count_down),run_time=0.5)
            self.wait(1)
            self.play(FadeOut(count_down),run_time=0.5)

        self.play(FadeOut(txt_count))

        txt_sin_1 = MathTex(r" \text{getting opposite side with } \sin(\theta) \\ " +
            r"\text{we know: } \sin({\theta}) = \frac{o}{s} "
        ,font_size=13,color=BLUE).next_to(triangle,LEFT,buff=0.3).shift(UP*0.5)
        txt_sin_2= MathTex(r"\text{calculate} \sin({30^{\circ}})"
                           ,font_size=13,color=BLUE).next_to(txt_sin_1,DOWN,buff=0.01)
        txt_sin_3 = MathTex(r" \sin({30^{\circ}}) = \frac{1}{2} \\ " +
            r"\frac{1}{2} = \frac{o}{s} \\ " +
            r"\frac{1}{2} = \frac{o}{2} \\ " +
            r"o \ = \ 1 "
            ,font_size=13,color=BLUE).next_to(txt_sin_2,DOWN,buff=0.1)
        
        self.play(Create(txt_sin_1))
        self.wait(1)
        self.play(Create(txt_sin_2))
        self.wait(1)
        self.play(Create(txt_sin_3), run_time=4)
        self.wait(5)
        self.play(Uncreate(txt_sin_1), Uncreate(txt_sin_2), Uncreate(txt_sin_3))

        txt_cos_1 = MathTex(r" \text{getting adjacent side with } \cos(\theta) \\ " +
            r"\text{we know: } \cos({\theta}) = \frac{a}{s}"
        ,font_size=13,color=BLUE).next_to(triangle,LEFT,buff=0.3).shift(UP*0.5)
        txt_cos_2 = MathTex(r"\text{calculate}\cos(30^{\circ}}) "
                            ,font_size=13,color=BLUE).next_to(txt_cos_1,DOWN,buff=0.01)
        txt_cos_3 = MathTex(r" \cos({30^{\circ}}) = \frac{\sqrt{3}}{2} \\ " +
            r"\frac{\sqrt{3}}{2} = \frac{a}{s} \\ " +
            r"\frac{\sqrt{3}}{2} = \frac{a}{2} \\ " +
            r"a \ = \ \sqrt{3} "
        ,font_size=13,color=BLUE).next_to(txt_cos_2,DOWN,buff=0.1)

        self.play(Create(txt_cos_1))
        self.wait(1)
        self.play(Create(txt_cos_2))
        self.wait(1)
        self.play(Create(txt_cos_3), run_time=4)
        self.wait(5)
        self.play(Uncreate(txt_cos_1), Uncreate(txt_cos_2), Uncreate(txt_cos_3))

        self.play(Unwrite(question), Unwrite(triangle),
                  Unwrite(txt_o), Unwrite(txt_s),
                  Unwrite(txt_a), Unwrite(r_angle),
                  Unwrite(theta_angle), Unwrite(theta_value)
        )

class TrigFunctionsExample_2(Scene):
    def construct(self):
        title = Tex(r"\underline{\text{Example 2}}",font_size=36)
        self.play(Write(title))
        self.play(Circumscribe(title))
        #self.play(Circumscribe(title, Circle))
        #self.play(Circumscribe(title, fade_out=True))
        #self.play(Circumscribe(title, time_width=2))
        #self.play(Circumscribe(title, Circle, True))
        self.wait(1)
        self.play(FadeOut(title))
        self.wait(1)

        question = Tex(r"Use the given angle and adjacient length along with trigonometric functions \\ to determine the length of the hypotenuse and opposite sides", font_size=12)

        self.play(Write(question))
        self.play(Indicate(question))
        self.play(question.animate.shift(UP), buff=0.2, run_time=2)
        self.wait(1)

        rt_vertices = [

                np.array([0.5,0.7,0]),
                np.array([0.5,-0.8,0]),
                np.array([-0.366,-0.8,0]),
        ]
        theta_vertices = [
                rt_vertices[1],
                rt_vertices[2],
                rt_vertices[0],
        ]
        triangle = Polygon(*rt_vertices, color=YELLOW)
        theta_angle = Angle.from_three_points(*theta_vertices, radius=0.25)
        theta_value = DecimalNumber(
                theta_angle.get_value(degrees=True),
                font_size = 11,
                num_decimal_places=0,
                unit = r"^{\circ}=\theta"
        ).shift(UP*0.1)

        theta_value.next_to(theta_angle, RIGHT,buff=0.02)

        self.play(Write(triangle), run_time=2)

        r_angle = RightAngle.from_three_points(*rt_vertices, elbow=True, radius=0.15)
        self.play(Write(r_angle))

        self.play(Write(theta_angle), Write(theta_value))

        txt_s = Text(r"s",font_size=12)
        txt_s.next_to(triangle,UL,buff=-0.4)
        txt_o = Text(r"o", font_size=12)
        txt_o.next_to(triangle,RIGHT)
        txt_a = Text(r"3",font_size=12)
        txt_a.next_to(triangle,DOWN)

        self.play(Write(txt_o), Write(txt_a), Write(txt_s))

        self.play(
            triangle.animate.shift(RIGHT),
            theta_angle.animate.shift(RIGHT),
            theta_value.animate.shift(RIGHT),
            txt_s.animate.shift(RIGHT),
            txt_a.animate.shift(RIGHT),
            txt_o.animate.shift(RIGHT),
            r_angle.animate.shift(RIGHT),
        )
        
        txt_count = Tex(r"\text{answer will be reveiled in:}",font_size=10, color=BLUE)
        txt_count.next_to(triangle,LEFT,buff=0.5)
        txt_count.shift(UP*0.5)
        self.play(Create(txt_count))

        for i in range(5):
            count_down = Text(str(5-i), color=BLUE)
            count_down.next_to(triangle,LEFT,buff=1)
            self.play(FadeIn(count_down),run_time=0.5)
            self.wait(1)
            self.play(FadeOut(count_down),run_time=0.5)

        self.play(FadeOut(txt_count))

        txt_cos_1 = MathTex(r" \text{getting hypotenuse side with } \cos(\theta) \\ " +
            r"\text{we know: } \cos({\theta}) = \frac{a}{s}"
        ,font_size=13,color=BLUE).next_to(triangle,LEFT,buff=0.3).shift(UP*0.5)
        txt_cos_2 = MathTex(r"\text{calculate} \ \cos(60^{\circ}}) "
                            ,font_size=13,color=BLUE).next_to(txt_cos_1,DOWN,buff=0.01)
        txt_cos_3 = MathTex(r" \cos({60^{\circ}}) = \frac{1}{2} \\ " +
            r"\frac{1}{2} = \frac{a}{s} \\ " +
            r"\frac{1}{2} = \frac{3}{s} \\ " +
            r"s \ = \ 6 "
        ,font_size=13,color=BLUE).next_to(txt_cos_2,DOWN,buff=0.1)

        self.play(Create(txt_cos_1))
        self.wait(1)
        self.play(Create(txt_cos_2))
        self.wait(1)
        self.play(Create(txt_cos_3), run_time=4)
        self.wait(5)
        self.play(Uncreate(txt_cos_1), Uncreate(txt_cos_2), Uncreate(txt_cos_3))


        txt_tan_1 = MathTex(r" \text{getting opposite side with } \tan(\theta) \\ " +
            r"\text{we know: } \tan({\theta}) = \frac{o}{a}"
        ,font_size=13,color=BLUE).next_to(triangle,LEFT,buff=0.3).shift(UP*0.5)
        txt_tan_2 = MathTex(r"\text{calculate} \ \tan(60^{\circ}}) "
                            ,font_size=13,color=BLUE).next_to(txt_tan_1,DOWN,buff=0.01)
        txt_tan_3 = MathTex(r" \tan({60^{\circ}}) = \sqrt{3} \\ " +
            r"\sqrt{3} = \frac{o}{a} \\ " +
            r"\sqrt{3} = \frac{o}{3} \\ " +
            r"o \ = \ 3\sqrt{3} "
        ,font_size=13,color=BLUE).next_to(txt_tan_2,DOWN,buff=0.1)

        self.play(Create(txt_tan_1))
        self.wait(1)
        self.play(Create(txt_tan_2))
        self.wait(1)
        self.play(Create(txt_tan_3), run_time=4)
        self.wait(5)
        self.play(Uncreate(txt_tan_1), Uncreate(txt_tan_2), Uncreate(txt_tan_3))

        self.play(Unwrite(question), Unwrite(triangle),
                  Unwrite(txt_o), Unwrite(txt_s),
                  Unwrite(txt_a), Unwrite(r_angle),
                  Unwrite(theta_angle), Unwrite(theta_value)
        )


class Extendto360degrees(Scene):
    def construct(self):
        pure_blue = ManimColor.from_hex(0x0000ff)
        title = MathTex(r"\underline{ \text{Trigonometric Definitions on } 0^{\circ} \le x \le 360^{\circ}",
                     font_size=20
        )
        self.play(Write(title), run_time=2)
        self.wait(1)
        self.play(title.animate.shift(UP*1.15))
        self.wait(1)

        rt_vertices = [

                np.array([0.5,0.7,0]),
                np.array([0.5,-0.8,0]),
                np.array([-0.366,-0.8,0]),
        ]
        theta_vertices = [
                rt_vertices[1],
                rt_vertices[2],
                rt_vertices[0],
        ]
        triangle = Polygon(*rt_vertices, color=YELLOW)
        theta_angle = Angle.from_three_points(*theta_vertices, radius=0.25)
        theta_value = DecimalNumber(
                theta_angle.get_value(degrees=True),
                font_size = 11,
                num_decimal_places=0,
                unit = r"^{\circ}=\theta"
        ).shift(UP*0.1)

        theta_value.next_to(theta_angle, RIGHT,buff=0.02)

        self.play(Write(triangle), run_time=2)

        r_angle = RightAngle.from_three_points(*rt_vertices, elbow=True, radius=0.15)
        self.play(Write(r_angle))

        self.play(Write(theta_angle), Write(theta_value))

        txt_s = Text(r"s",font_size=12)
        txt_s.next_to(triangle,UL,buff=-0.4).shift(DOWN*0.3 + LEFT*0.3)
        txt_o = Text(r"o", font_size=12)
        txt_o.next_to(triangle,RIGHT)
        txt_a = Text(r"a",font_size=12)
        txt_a.next_to(triangle,DOWN)

        self.play(Write(txt_s), Write(txt_o), Write(txt_a))
        self.wait(1)

        txt_ser = Text(r"s = r",font_size=12)
        txt_ser.next_to(triangle,UL,buff=-0.4).shift(DOWN*0.3 + LEFT*0.3)
        txt_oey = Text(r"o = y", font_size=12)
        txt_oey.next_to(triangle,RIGHT)
        txt_aex = Text(r"a = x",font_size=12)
        txt_aex.next_to(triangle,DOWN)

        self.play(Transform(txt_s, txt_ser), Transform(txt_o, txt_oey), Transform(txt_a, txt_aex))
        self.wait(1)
        
        self.play(
            triangle.animate.shift(LEFT),
            theta_angle.animate.shift(LEFT),
            theta_value.animate.shift(LEFT),
            txt_s.animate.shift(LEFT),
            txt_o.animate.shift(LEFT),
            txt_a.animate.shift(LEFT),

            r_angle.animate.shift(LEFT),
        )


        txt_snorm = Text(r"s",font_size=12)
        txt_snorm.next_to(triangle,UL,buff=-0.4).shift(DOWN*0.3 + LEFT*0.3)
        txt_onorm = Text(r"o", font_size=12)
        txt_onorm.next_to(triangle,RIGHT)
        txt_anorm = Text(r"a",font_size=12)
        txt_anorm.next_to(triangle,DOWN)

        self.play(Transform(txt_s, txt_snorm), Transform(txt_o, txt_onorm), Transform(txt_a, txt_anorm))
        self.wait(1)

        self.next_section("next_triangle")

        rt_vertices = [

                np.array([0.5,0.7,0]),
                np.array([0.5,-0.8,0]),
                np.array([-0.366,-0.8,0]),
        ]
        theta_vertices = [
                rt_vertices[1],
                rt_vertices[2],
                rt_vertices[0],
        ]
        triangle1 = Polygon(*rt_vertices, color=YELLOW).shift(LEFT)
        theta_angle1 = Angle.from_three_points(*theta_vertices, radius=0.25).shift(LEFT)
        theta_value1 = DecimalNumber(
                theta_angle1.get_value(degrees=True),
                font_size = 11,
                num_decimal_places=0,
                unit = r"^{\circ}=\theta"
        ).shift(UP*0.1).shift(LEFT)
        theta_value1.next_to(theta_angle, RIGHT,buff=0.02)
        r_angle1 = RightAngle.from_three_points(*rt_vertices, elbow=True, radius=0.15).shift(LEFT)
        txt_r = Text(r"r",font_size=12)
        txt_r.next_to(triangle,UL,buff=-0.4).shift(DOWN*0.3 + LEFT*0.3)
        txt_y = Text(r"y", font_size=12)
        txt_y.next_to(triangle,RIGHT)
        txt_x = Text(r"x",font_size=12)
        txt_x.next_to(triangle,DOWN)
        self.play(FadeIn(triangle1), FadeIn(theta_angle1),
                  FadeIn(r_angle1), FadeIn(theta_value1),
        )
        
        self.play(
            triangle1.animate.shift(RIGHT*2),
            theta_angle1.animate.shift(RIGHT*2),
            theta_value1.animate.shift(RIGHT*2),
            txt_r.animate.shift(RIGHT*2),
            txt_y.animate.shift(RIGHT*2),
            txt_x.animate.shift(RIGHT*2),
            r_angle1.animate.shift(RIGHT*2),

        )
        self.play(Indicate(txt_r, color=pure_blue), Indicate(txt_x, color=pure_blue),
                  Indicate(txt_y, color=pure_blue), Indicate(txt_s, color=pure_blue),
                  Indicate(txt_o, color=pure_blue), Indicate(txt_a, color=pure_blue),
                  run_time=3)

        self.wait(1)
        self.play(FadeOut(triangle), FadeOut(triangle1),
                  FadeOut(theta_angle), FadeOut(theta_angle1),
                  FadeOut(theta_value), FadeOut(theta_value1),
                  FadeOut(r_angle), FadeOut(r_angle1),
                  FadeOut(txt_a), FadeOut(txt_o), FadeOut(txt_s),
                  FadeOut(txt_x), FadeOut(txt_y), FadeOut(txt_r),
        )
        

        funcs_text_org = MathTex(r"\sin{\theta} = \frac{o}{s} \\ \cos{\theta} = \frac{a}{s} \\ \tan{\theta} = \frac{o}{a}", font_size=24).shift(LEFT)
        implies_text = MathTex(r"\implies", font_size=26)
        funcs_text_cart = MathTex(r"\sin{\theta} = \frac{y}{r} \\ \cos{\theta} = \frac{x}{r} \\ \tan{\theta} = \frac{y}{x}", font_size=24).shift(RIGHT)


        self.play(Write(funcs_text_org), Write(implies_text) , Write(funcs_text_cart))
        self.wait(3.5)
        self.play(Unwrite(funcs_text_org), Unwrite(implies_text) , Unwrite(funcs_text_cart))


        y_vertices = [
                np.array([0,0.8,0]),
                np.array([0,-0.8,0]),
        ]
        axis_y = DoubleArrow(y_vertices[0],y_vertices[1], buff=0, tip_length=0.05,
                             color=BLUE, max_stroke_width_to_length_ratio=1)
        x_vertices = [
                np.array([1,0,0]),
                np.array([-1,0,0]),
        ]
        axis_x = DoubleArrow(x_vertices[0],x_vertices[1], buff=0, tip_length=0.05,
                             color=BLUE, max_stroke_width_to_length_ratio = 1)

        self.play(Write(axis_y), Write(axis_x))

        theta_values = [
            Tex(r"x",font_size=9, color=RED),
            Tex(r"180-x",font_size=9, color=RED),
            Tex(r"180+x",font_size=9, color=RED),
            Tex(r"360-x or 0-x",font_size=9, color=RED)
        ]

        below_note = MathTex(r"\text{Going Anti-Clockwise is positive}",
                                    font_size=12,color=BLUE).next_to(axis_y,DOWN*2,buff=0.1)

        self.play(Write(below_note)) 
       
        deg0 = MathTex(r"x \ 0^{\circ};360^{\circ}", font_size=10).next_to(axis_x,RIGHT,buff=0)
        deg90 = MathTex(r"90^{\circ}",font_size=10).next_to(axis_y,UP,buff=0)
        deg180 = MathTex(r"180^{\circ}",font_size=10).next_to(axis_x, LEFT, buff=0)
        deg270 = MathTex(r"270^{\circ}",font_size=10).next_to(axis_y,DOWN, buff=0)
   
        self.play(Write(deg0))
        self.play(Write(deg90))
        self.play(Write(deg180))
        self.play(Write(deg270))
        
        for i in range(0,4):
            x_sign = 1 
            y_sign = 1
            if i in (1,2):
                x_sign = -1 
            if i in (2,3):
                y_sign = -1 

            theta_vertices = [
                np.array([0.8,0,0]),
                np.array([0,0,0]),
                np.array([-0.8*(sin(pi/2*i-pi/5)), 0.8*(sin(pi/2*i+pi/2-pi/5)),0]),
            ]
            indication_line = Line(start=theta_vertices[1], end=theta_vertices[2],buff=-0.01, color=YELLOW)
            theta_angle = Angle.from_three_points(*theta_vertices, radius=0.15, color=RED)
            theta_num = DecimalNumber(
                theta_angle.get_value(degrees=True),
                font_size = 9,
                num_decimal_places=0,
                unit = r"^{\circ}",
                color=WHITE
            ).shift(RIGHT*0.25 + UP*0.2)
            theta_values[i].shift(RIGHT*0.55*(x_sign) + UP*0.1*(y_sign))
            self.play(Write(indication_line))
            self.play(Write(theta_angle), Write(theta_num), Write(theta_values[i]))
            self.wait(2)
            self.play(FadeOut(theta_angle), Unwrite(theta_num), Unwrite(indication_line))
        
        self.play(Unwrite(below_note),
                  FadeOut(deg0), FadeOut(deg90),
                  FadeOut(deg180), FadeOut(deg270),
                  FadeOut(theta_values[0]), FadeOut(theta_values[1]),
                  FadeOut(theta_values[2]), FadeOut(theta_values[3]),
        )
        

        theta_values = [
            Tex(r"-360+x or x",font_size=10),
            Tex(r"-180-x or \\ 180-x",font_size=10),
            Tex(r"-180+x or \\ 180+x",font_size=10),
            Tex(r"+360-x or -x",font_size=10, color=RED)
        ]
        for i in range(0,len(theta_values)):
            theta_values[i][0][0:6].set_color(RED)
            theta_values[i][0][6:9].set_color(WHITE)
            theta_values[i][0][8:].set_color(pure_blue)

        below_note = MathTex(r"\text{Going Clockwise is negative}",
                                    font_size=12,color=BLUE).next_to(axis_y,DOWN*2,buff=0.1)
        self.play(Write(below_note)) 

        deg0 = MathTex(r"x \ 0^{\circ};360^{\circ}", font_size=10).next_to(axis_x,RIGHT,buff=0)
        deg90 = MathTex(r"-270^{\circ}",font_size=10).next_to(axis_y,UP,buff=0)
        deg180 = MathTex(r"-180^{\circ}",font_size=10).next_to(axis_x, LEFT, buff=0)
        deg270 = MathTex(r"-90^{\circ}",font_size=10).next_to(axis_y,DOWN, buff=0) 
        self.play(Write(deg0))
        self.play(Write(deg270))
        self.play(Write(deg180))
        self.play(Write(deg90))

        for i in range(0,4):
            x_sign = 1 
            y_sign = 1
            if i in (0,1):
                y_sign = -1
            if i in (1,2):
                x_sign = -1

            theta_vertices = [
                np.array([0.8,0,0]),
                np.array([0,0,0]),
                np.array([-0.8*(sin(pi/2*i-pi/5)), -0.8*(sin(pi/2*i+pi/2-pi/5)),0]),
            ]
            indication_line = Line(start=theta_vertices[1], end=theta_vertices[2],buff=-0.01, color=YELLOW)
            theta_angle = Angle.from_three_points(*theta_vertices, radius=0.15, color=pure_blue)
            other_angle = Angle.from_three_points(*theta_vertices, radius=0.15, color=RED, other_angle=True)
            theta_num = DecimalNumber(
                theta_angle.get_value(degrees=True),
                font_size = 9,
                num_decimal_places=0,
                unit = r"^{\circ}",
                color=WHITE
            ).shift(RIGHT*0.25 + UP*0.05) 
            other_num = DecimalNumber(
                other_angle.get_value(degrees=True),
                font_size = 9,
                num_decimal_places=0,
                unit = r"^{\circ}",
                color=WHITE
            ).shift(RIGHT*0.25 + -UP*0.05)
            theta_values[3-i].shift(RIGHT*0.60*(x_sign) + UP*0.15*(y_sign))
            self.play(Write(indication_line))
            self.play(Write(theta_angle), Write(theta_num), Write(other_num), Write(theta_values[3-i]))
            self.wait(1)
            self.play(Write(other_angle))
            self.wait(2)
            self.play(Unwrite(theta_angle), Unwrite(other_angle),
                      Unwrite(theta_num), Unwrite(other_num),
                      Unwrite(indication_line)
            )
        
        self.play(Unwrite(below_note),
                  FadeOut(deg0), FadeOut(deg90),
                  FadeOut(deg180), FadeOut(deg270),
                  FadeOut(theta_values[0]), FadeOut(theta_values[1]),
                  FadeOut(theta_values[2]), FadeOut(theta_values[3]),
        )
        
        deg0 = MathTex(r"x \ 0^{\circ};360^{\circ}", font_size=10).next_to(axis_x,RIGHT,buff=0)
        deg90 = MathTex(r"90^{\circ}",font_size=10).next_to(axis_y,UP,buff=0)
        deg180 = MathTex(r"180^{\circ}",font_size=10).next_to(axis_x, LEFT, buff=0)
        deg270 = MathTex(r"270^{\circ}",font_size=10).next_to(axis_y,DOWN, buff=0)
   
        self.play(Write(deg0))
        self.play(Write(deg90))
        self.play(Write(deg180))
        self.play(Write(deg270))
        
        s_always_positive = MathTex(r"\text{Remember hypotenuse always positive} \implies r \ge 0",
                                    font_size=12,color=BLUE).next_to(axis_y,DOWN*2,buff=0.1)
        self.play(Write(s_always_positive))

        free_later_objs = [[]]
        free_later_tex = []
        quadrant_label = []
     
        for quad in range(1,5):
            x_sign = 1 
            y_sign = 1 
            x_char = ''
            y_char = ''
            other_bool = True
            if quad in (2,3):
                x_sign = -1 
                x_char = '-'
            if quad in (3,4):
                y_sign = -1
                y_char = '-'
            if quad in (2,4):
                other_bool=False
            
            Quadrant_string = "I"*quad if quad < 4 else "IV"
            Quadrat_Num = Text(Quadrant_string,font_size=10,color=YELLOW).shift(RIGHT*0.11*x_sign + UP*0.11*y_sign)
            quadrant_label.append(Quadrat_Num)
            self.play(Write(Quadrat_Num))

            theta_vertices = [
                np.array([0.6*x_sign, 0.6*y_sign, 0]),
                np.array([0.2*x_sign, 0.2*y_sign, 0]),
                np.array([0.6*x_sign, 0.2*y_sign, 0]),
            ]
            triangle = Polygon(*theta_vertices, color=BLUE)
            theta_angle = Angle.from_three_points(*theta_vertices, radius=0.15, color=RED, other_angle=other_bool)
            theta_num = MathTex(r"\theta",font_size=9, color=RED).shift(RIGHT*0.42*x_sign + UP*0.26*y_sign)

            txt_r = Text("r",font_size=9).shift(UP*0.55*y_sign + RIGHT*0.35*x_sign)
            txt_y = Text(y_char + "y", font_size=9).shift(UP*0.4*y_sign + RIGHT*0.75*x_sign)
            txt_x = Text(x_char + "x",font_size=9).shift(UP*0.1*y_sign + RIGHT*0.4*x_sign)

            self.play(Write(triangle),Write(theta_angle), Write(theta_num))
            self.play(Write(txt_r), Write(txt_y), Write(txt_x))

            free_later_objs.append([])
            free_later_objs[quad-1].append(triangle)
            free_later_objs[quad-1].append(theta_angle)
            free_later_objs[quad-1].append(theta_num)
            free_later_objs[quad-1].append(txt_r)
            free_later_objs[quad-1].append(txt_y)
            free_later_objs[quad-1].append(txt_x)
            self.wait(1)
            

            tan_sign = '+' if (y_sign*x_sign > 0) else '-'
            sin_sign = '+' if (y_sign > 0) else '-'
            cos_sign = '+' if (x_sign > 0) else '-'


           
            funcs = MathTex(r"\sin(\theta) = \frac{" + y_char + r"y}{r} \text{ is } " + sin_sign + r"\\" + r"\cos(\theta) = \frac{" + x_char + r"x}{r} \text{ is } " + cos_sign + r"\\" + r"\tan(\theta) = \frac{" + y_char + r"y}{" + x_char + r"x} \text{ is } " + tan_sign + r"\\",
                            font_size = 10, 
                            color=BLUE,
            ).shift(RIGHT*1.3*x_sign + UP*0.5*y_sign)


            self.play(Write(funcs))

            free_later_tex.append(funcs)

            self.wait(1)
            
            #self.play(Unwrite(triangle), Unwrite(theta_angle), Unwrite(theta_num),
            #          Unwrite(txt_r), Unwrite(txt_x), Unwrite(txt_y),
            #)
        for quad in range(0,4):
            for obj in range(0,6): 
                self.play(Unwrite(free_later_objs[quad][obj]), run_time=0.07)

        theta_values = [
            Tex(r"x",font_size=9, color=RED),
            Tex(r"180-x",font_size=9, color=RED),
            Tex(r"180+x",font_size=9, color=RED),
            Tex(r"360-x or 0-x",font_size=9, color=RED)
        ]
        astc = [
            Text(r"A",font_size=12, color=pure_blue),
            Text(r"S",font_size=12, color=pure_blue),
            Text(r"T",font_size=12, color=pure_blue),
            Text(r"C",font_size=12, color=pure_blue)
        ]
        for quad in range(0,4):
            x_sign = 1 
            y_sign = 1
            if quad in (1,2):
                x_sign = -1
            if quad in (2,3):
                y_sign = -1

            theta_values[quad].shift(RIGHT*0.60*(x_sign) + UP*0.15*(y_sign))
            astc[quad].shift(RIGHT*0.6*(x_sign) + UP*0.45*(y_sign))

            self.play(Write(theta_values[quad]), Write(astc[quad]))
            self.wait(2)

        for quad in range(0,4):
            self.play(Unwrite(theta_values[quad]), Unwrite(astc[quad]))
            
 
        for quad in range(0,4):
            self.play(Unwrite(free_later_tex[quad]), Unwrite(quadrant_label[quad]), run_time=0.5)


        self.play(Unwrite(deg0),
                  Unwrite(deg90),
                  Unwrite(deg180),
                  Unwrite(deg270),
                  Unwrite(axis_x),
                  Unwrite(axis_y),
                  Unwrite(title),
                  Unwrite(s_always_positive),
        )
        self.wait(1)
class Extendto360degrees_Example(Scene):
    def construct(self):
        pure_blue = ManimColor.from_hex(0x0000ff)

        title = Tex(r"\underline{\text{Example 1}}",font_size=36)
        self.play(Write(title))
        self.play(Circumscribe(title))
        self.wait(1)
        self.play(FadeOut(title))
        self.wait(1)
        

        question_def = MathTex(r"\text{Use The Definitions of } 0^{\circ} \le x \le 360^{\circ}", font_size = 13)
        question = MathTex(r"\text{to convert the following trigonometric functions to sharp angles} ",
                           font_size=13
        ).next_to(question_def,DOWN,buff=0.05)

        self.play(Write(question), Write(question_def))
        self.play(Indicate(question), Indicate(question_def))
        self.play(question.animate.shift(UP*1.2), question_def.animate.shift(UP*1.2), buff=0.2, run_time=2)
        self.wait(1)

        y_vertices = [
                np.array([-1.4,0.9,0]),
                np.array([-1.4,0.3,0]),
        ]
        axis_y = DoubleArrow(y_vertices[0],y_vertices[1], buff=0, tip_length=0.05,
                             color=BLUE, max_stroke_width_to_length_ratio=1)
        x_vertices = [
                np.array([-1.4+0.3,0.6,0]),
                np.array([-1.4-0.3,0.6,0]),
        ]
        axis_x = DoubleArrow(x_vertices[0],x_vertices[1], buff=0, tip_length=0.05,
                             color=BLUE, max_stroke_width_to_length_ratio = 1)

        self.play(Write(axis_y), Write(axis_x))

        deg = [ MathTex(r"x \ 0^{\circ};360^{\circ}", font_size=7).next_to(axis_x,RIGHT,buff=0),
                MathTex(r"90^{\circ}",font_size=7).next_to(axis_y,UP,buff=0),
                MathTex(r"180^{\circ}",font_size=7).next_to(axis_x, LEFT, buff=0),
                MathTex(r"270^{\circ}",font_size=7).next_to(axis_y,DOWN, buff=0),
        ]
        theta_values = [
            Tex(r"x",           font_size=7, color=RED).shift(LEFT*1.15).shift(UP*0.7),
            Tex(r"180-x",       font_size=7, color=RED).shift(LEFT*1.65).shift(UP*0.7),
            Tex(r"180+x",       font_size=7, color=RED).shift(LEFT*1.65).shift(UP*0.5),
            Tex(r"360-x or 0-x",font_size=7, color=RED).shift(LEFT*1.15).shift(UP*0.5),

        ]
        astc = [
            Text(r"A",font_size=6, color=pure_blue).shift(LEFT*1.2).shift(UP*0.8),
            Text(r"S",font_size=6, color=pure_blue).shift(LEFT*1.6).shift(UP*0.8),
            Text(r"T",font_size=6, color=pure_blue).shift(LEFT*1.6).shift(UP*0.4),
            Text(r"C",font_size=6, color=pure_blue).shift(LEFT*1.2).shift(UP*0.4),
        ]
 
        for quad in range(0,4):
            self.play(Write(theta_values[quad]), Write(astc[quad]), Write(deg[quad]) )
        
        self.wait(1)

        def ask_question(self, q_tex, timer, a_tex, indic):
            self.play(Write(q_tex))
            for i in range(0,timer):
                count_down = Text(str(timer-i), color=BLUE)
                count_down.next_to(q_tex,DOWN,buff=0.1)
                self.play(FadeIn(count_down),Indicate(astc[indic]), Indicate(theta_values[indic]),run_time=0.5)
                self.wait(1)
                self.play(FadeOut(count_down),run_time=0.5)
            
            a_tex.next_to(q_tex,DOWN,buff=1)
            self.play(Write(a_tex))
            self.wait(3)
            self.play(Unwrite(q_tex), Unwrite(a_tex))


        

        ask_question(self,
                     MathTex(r"\text{convert to a sharp angle: }\sin(240^{\circ})",font_size=14).next_to(deg[0],RIGHT,buff=0.5),
                     5,
                     MathTex(r"\text{answer: }\sin(180^{\circ} + 60^{\circ}) \\ = -\sin(60^{\circ})",font_size=14),
                     2
        )
        ask_question(self,
                     MathTex(r"\text{convert to a sharp angle: }\cos(-30^{\circ})",font_size=14).next_to(deg[0],RIGHT,buff=0.5),
                     5,
                     MathTex(r"\text{answer: }\cos(0^{\circ} - 30^{\circ}) \\ = \cos(30^{\circ})",font_size=14),
                     3
        )
        ask_question(self,
                     MathTex(r"\text{convert to a sharp angle: }\sin(-405^{\circ})",font_size=14).next_to(deg[0],RIGHT,buff=0.5),
                     5,
                     MathTex(r"\text{answer: }\sin(-45^{\circ} - 360^{\circ}) \\ = \sin(-45^{\circ}) \\ = -\sin(45^{\circ})",font_size=14),
                     3
        )
        ask_question(self,
                     MathTex(r"\text{convert to a sharp angle: }\tan(480^{\circ})",font_size=14).next_to(deg[0],RIGHT,buff=0.5),
                     5,
                     MathTex(r"\text{answer: }\tan(120^{\circ} + 360^{\circ}) \\ = \tan(180^{\circ} - 60^{\circ}) \\ = -\tan(60^{\circ})",font_size=14),
                     1
        )

        for i in range(0,4):
            self.play(Unwrite(deg[i]), Unwrite(theta_values[i]), Unwrite(astc[i]), run_time=0.1)
        self.play(Unwrite(question), Unwrite(question_def), Unwrite(axis_y), Unwrite(axis_x))



class SpecialAngles(Scene):
    def construct(self):
        pure_blue = ManimColor.from_hex(0x0000ff)
        title = MathTex(r"\underline{ \text{Special Angles} }",
                     font_size=20
        )
        self.play(Write(title), run_time=2)
        self.wait(1)
        self.play(title.animate.shift(UP*1.15))
        self.wait(1)

        rt_vertices = [
            np.array([0.0,-0.0,0]),
            np.array([1.0,0.0,0]),
            np.array([1.0,1.0,0]),
        ]

        side_lengths = [
            MathTex(r"\sqrt{2}",font_size=11).shift(UP*0.65+RIGHT*0.4),
            MathTex(r"1",font_size=11),
            MathTex(r"1",font_size=11),
        ]

        deg45_triangle = Triangle(rt_vertices,side_lengths,1)
        deg45_triangle.instant_shift(LEFT*2)
        deg45_triangle.write(self)
        deg45_text = MathTex(r"\sin(45^{\circ}) = \frac{1}{\sqrt{2}} \\" +
                             r"\cos(45^{\circ}) = \frac{1}{\sqrt{2}} \\" +
                             r"\tan(45^{\circ}) = 1",
                             font_size = 12, color=BLUE,
        ).next_to(deg45_triangle.side_lengths[2],DOWN,buff=0.1)
        self.play(Write(deg45_text))



        rt_vertices = [
            np.array([0.0,0,0]),
            np.array([1.7,0,0]),
            np.array([1.7,1.0,0]),
        ]
        side_lengths = [
            MathTex(r"2",font_size=11).shift(UP*0.5+RIGHT*0.55),
            MathTex(r"1",font_size=11),
            MathTex(r"\sqrt{3}",font_size=11),
        ]                   

        deg30_triangle = Triangle(rt_vertices,side_lengths,1.5)

        deg30_triangle.instant_shift(LEFT*0.75)
        deg30_triangle.write(self)
        deg30_text = MathTex(r"\sin(30^{\circ}) = \frac{1}{2} \\" +
                             r"\cos(30^{\circ}) = \frac{\sqrt{3}}{2} \\" +
                             r"\tan(30^{\circ}) = \frac{1}{\sqrt{3}}",
                             font_size = 12, color=BLUE,
        ).next_to(deg30_triangle.side_lengths[2],DOWN,buff=0.1)
        self.play(Write(deg30_text))

        rt_vertices = [
            np.array([0.0,0.0,0]),
            np.array([1.0,0,0]),
            np.array([1.0,1.7,0]),
        ]
        side_lengths = [
            MathTex(r"2",font_size=11).shift(UP*0.70+RIGHT*0.25),
            MathTex(r"\sqrt{3}",font_size=11),
            MathTex(r"1",font_size=11),
        ]

        deg60_triangle = Triangle(rt_vertices,side_lengths,1.5)
        deg60_triangle.instant_shift(RIGHT*0.75)
        deg60_triangle.write(self)
        deg60_text = MathTex(r"\sin(60^{\circ}) = \frac{\sqrt{3}}{2} \\" +
                             r"\cos(60^{\circ}) = \frac{1}{2} \\" +
                             r"\tan(60^{\circ}) = \frac{\sqrt{3}}{1}",
                             font_size = 12, color=BLUE,
        ).next_to(deg60_triangle.side_lengths[2],DOWN,buff=0.1)
        self.play(Write(deg60_text))

        self.wait(5)
        self.play(Circumscribe(deg30_triangle.triangle,color=pure_blue), Circumscribe(deg60_triangle.triangle,color=pure_blue))
        self.wait(5)
        self.play(Unwrite(deg30_text), Unwrite(deg45_text), Unwrite(deg60_text))
        deg45_triangle.unwrite(self)
        deg30_triangle.unwrite(self)
        deg60_triangle.unwrite(self)
        self.play(Unwrite(title))
        self.wait(1)


class ReciprocalFunctions(Scene):
    def construct(self):
        pure_blue = ManimColor.from_hex(0x0000ff)
        title = MathTex(r"\underline{ \text{Reciprocal Functions} }",
                     font_size=20
        )
        self.play(Write(title), run_time=2)
        self.wait(1)
        self.play(title.animate.shift(UP*1.15))
        self.wait(1)

        rt_vertices = [
            np.array([1.0,-0.5,0]),
            np.array([2.0,-0.5,0]),
            np.array([2.0,1.2,0]),
        ]
        for v in rt_vertices:
            for i in [0,1,2]:
                v[i] = v[i]/1.2

        theta_vertices = [
                rt_vertices[1],
                rt_vertices[0],
                rt_vertices[2],
        ]
        triangle = Polygon(*rt_vertices, color=YELLOW)
        rt_angle = RightAngle.from_three_points(*rt_vertices, elbow=True, radius=0.15)
        theta_angle = Angle.from_three_points(*theta_vertices, radius=0.15)
        theta_value = MathTex(r"\theta",font_size=11).next_to(theta_angle, RIGHT,buff=0.05).shift(UP*0.05)
        side_lengths = [
            MathTex(r"s = 2",font_size=11).next_to(triangle,LEFT,buff=-0.2).shift(UP*0.1),
            MathTex(r"o = \sqrt{3}",font_size=11).next_to(triangle,RIGHT, buff=0.1),
            MathTex(r"a = 1",font_size=11).next_to(triangle,DOWN,buff=0.1),
        ]

 
        self.play(
                Write(triangle),
                Write(theta_angle),
                Write(theta_value),
                Write(rt_angle),
                Write(side_lengths[0]),
                Write(side_lengths[1]),
                Write(side_lengths[2]),
        )

        inverse_fn = MathTex(
            r"\sin^{-1}(\frac{o}{s}) = \theta \\ " +
            r"\cos^{-1}(\frac{a}{s}) = \theta \\ " +
            r"\tan^{-1}(\frac{o}{a}) = \theta \\",
            font_size = 13,
            color=BLUE,
        ).next_to(title,DOWN,buff=0.1).shift(LEFT*1.5)

        self.play(Write(inverse_fn))

        self.wait(5)

        self.play(Unwrite(inverse_fn))
        
        self.wait(1)

        inverse_fn = MathTex(
            r"\sin^{-1}(\frac{o}{s}) = \theta \\ " +
            r"\sin^{-1}(\frac{\sqrt{3}}{2}) = 60^{\circ} \\ \\ " +
            r"\cos^{-1}(\frac{a}{s}) = \theta \\ " +
            r"\cos^{-1}(\frac{1}{2}) = 60^{\circ} \\ \\ " +
            r"\tan^{-1}(\frac{o}{a}) = \theta \\" +
            r"\tan^{-1}(\frac{\sqrt{3}}{1}) = 60^{\circ} \\ \\ ",
            font_size = 11,
            color=BLUE,
        ).next_to(title,DOWN,buff=0.1).shift(LEFT*1.5)

        self.play(Write(inverse_fn))

        self.play(Circumscribe(inverse_fn))

        self.wait(5)

        self.play(Circumscribe(theta_value))
        self.play(Indicate(theta_value, color=BLUE))
        self.play(Unwrite(theta_value))
        theta_value = MathTex(r"60^{\circ}",font_size=11).next_to(theta_angle, RIGHT,buff=0.05).shift(UP*0.05)
        self.play(Write(theta_value))
        self.play(Indicate(theta_value, color=BLUE))


        self.play(
                Unwrite(title),
                Unwrite(inverse_fn),
                Unwrite(triangle),
                Unwrite(theta_angle),
                Unwrite(theta_value),
                Unwrite(rt_angle),
                Unwrite(side_lengths[0]),
                Unwrite(side_lengths[1]),
                Unwrite(side_lengths[2]),
        )

        self.wait(1)


class FinalExample(Scene):
    def construct(self):
        pure_blue = ManimColor.from_hex(0x0000ff)
        
        
        title = Tex(r"\underline{\text{Final Example}}",font_size=36)
        self.play(Write(title))
        self.play(Circumscribe(title))
        self.wait(1)
        self.play(FadeOut(title))
        self.wait(1)

        question_text = [ 
            Tex(r"\text{During the zombie apocalypse, on your way to the secret lab}",font_size=12),
            Tex(r"\text{You and your friend get separated in the forest.}",font_size=12),
            Tex(r"\text{Luckily your engineer friend constucted you both walkie talkies.}",font_size=12),
            Tex(r"\text{These walki-talkie's have the unique ability to measure}",font_size=12),
            Tex(r"\text{the distance to the nearest cell tower,}",font_size=12),
            Tex(r"\text{But due to your friend needing to make them in such a hurry",font_size=12),
            Tex(r"\text{they are incomplete and report their distances as trigonometric functions}",font_size=12),
            Tex(r"\text{Your friend start to panic, you tell him to calm down!}",font_size=12),
            Tex(r"\text{as a renowned mathmatician you know you can solve this problem}",font_size=12),
            Tex(r"\text{and calculate the exact angle and distance both you and your friend}",font_size=12),
            Tex(r"\text{need to walk so you can both reach the secret lab and}\underline{\text{ save the world!}",font_size=12)
        ]
        for i in range(0,len(question_text)):
            question_text[i].shift((DOWN*-1.15)+DOWN*0.2*i)
            self.play(Write(question_text[i]), run_time=2)
        self.wait(5)

        self.play(
            Unwrite(question_text[0]),
            Unwrite(question_text[1]),
            Unwrite(question_text[2]),
            Unwrite(question_text[3]),
            Unwrite(question_text[4]),
            Unwrite(question_text[5]),
            Unwrite(question_text[6]),
            Unwrite(question_text[7]),
            Unwrite(question_text[8]),
            Unwrite(question_text[9]),
            Unwrite(question_text[10]),
        )

        question_text = Tex(
            r"\text{After carfully considering the area around the secret lab} \\ " +
            r"\text{you and your friend come up with the following model of the area}",
            font_size=12
        ).shift(UP*1.1)

        self.play(Write(question_text))
 
        desc_text = MathTex(r"F = Friend \\ M = Me \\ T_1=Tower \ 1 \\ T_2=Tower \ 2 \\ L=Secret \ Laboratory",
                            font_size=12,
                            color=BLUE
        ).next_to(question_text,DOWN).shift(LEFT*1.2)
        self.play(Write(desc_text))

        vertices = [
                np.array([-1.4,0.9,0]),
                np.array([-1.4,0.3,0]),
        ]

        lines = [
            Line(np.array([ -0.5,-0.5, 0]),np.array([  0.5,  0.5, 0]),buff=0,color=RED),
            Line(np.array([  0.5, 0.5, 0]),np.array([  0.5, -0.5, 0]),buff=0,color=RED),
            Line(np.array([  0.5,-0.5, 0]),np.array([ -0.5, -0.5, 0]),buff=0,color=RED),
            Line(np.array([  0.5, 0.5, 0]),np.array([2.232, -0.5, 0]),buff=0,color=RED),
            Line(np.array([2.232,-0.5, 0]),np.array([  0.5, -0.5, 0]),buff=0,color=RED),
            Line(np.array([  0.5,-0.5, 0]),np.array([0.933,  0.25, 0]),buff=0,color=RED),
        ]

        for l in lines:
            l.shift(LEFT*0.3)
       
        angles = [
            Angle(lines[0],lines[2],radius=0.15, quadrant=(1,-1), other_angle=True), #0
            Angle(lines[1],lines[0],radius=0.15,quadrant=(1,-1), other_angle=True), #1
            Angle(lines[2],lines[1], elbow=True, radius=0.15,quadrant=(1,-1)), #2

            Angle(lines[3],lines[4],radius=0.15, quadrant=(-1,1)), #3
            Angle(lines[1],lines[5],radius=0.2,quadrant=(-1,1), other_angle=True), #4
            Angle(lines[3],lines[5], elbow=True, radius=0.15,quadrant=(1,-1)), #5
        ]

        values = [
            MathTex(r"\alpha",font_size=11).next_to(angles[0], RIGHT,buff=0.05).shift(UP*0.05),
            MathTex(r"\beta",font_size=11).next_to(angles[3], LEFT,buff=0.1).shift(UP*0.03),
            MathTex(r"30^{\circ}",font_size=11).next_to(angles[4], UP,buff=0.1).shift(RIGHT*0.05),

            MathTex(r"F",font_size=11).next_to(angles[0],LEFT,buff=0.15),
            MathTex(r"M",font_size=11).next_to(angles[3],RIGHT,buff=0.15),
            MathTex(r"T_2",font_size=11).next_to(angles[5],UP,buff=0.1),
            MathTex(r"T_1",font_size=11).next_to(angles[2],DOWN,buff=0.1).shift(RIGHT*0.1),
            MathTex(r"L",font_size=11).next_to(lines[1],UP,buff=0.05),

            MathTex(r"6\sin(150)",font_size=11).next_to(lines[3],UP,buff=-0.45).shift(RIGHT*0.25), 
            MathTex(r"-2\tan(-225)",font_size=11).next_to(lines[2],DOWN,buff=0.1), 
        ]

        for l in lines:
            self.play(Write(l), run_time=0.25)
            #self.add(l)
        for a in angles:
            self.play(Write(a), run_time=0.25)
            #self.add(a)
        for v in values:
            self.play(Write(v), run_time=0.25)
            #self.add(v)


        question_final = MathTex(
            r"\text{You copy this mental model on a piece of paper} \\ " +
            r"\text{calculate } \alpha, \beta, \text{distance from both " +
            r"you and your friend to the Laboratory}",
            font_size=12,
        ).shift(DOWN*1.1)
        self.play(Write(question_final))

        self.wait(1)

        for i in range(10):
            count_down = Text(str(10-i), color=GOLD)
            count_down.next_to(desc_text,DOWN,buff=0.1).shift(LEFT*0.1)
            self.play(FadeIn(count_down),run_time=0.5)
            self.wait(1)
            self.play(FadeOut(count_down),run_time=0.5)

        self.play(Unwrite(question_final), Unwrite(desc_text), Unwrite(question_text))

        shift = 0.63
        right = 0.2
        self.play(
            lines[0].animate.shift(UP*shift).shift(RIGHT*right),
            lines[1].animate.shift(UP*shift).shift(RIGHT*right),
            lines[2].animate.shift(UP*shift).shift(RIGHT*right),
            lines[3].animate.shift(UP*shift).shift(RIGHT*right),
            lines[4].animate.shift(UP*shift).shift(RIGHT*right),
            lines[5].animate.shift(UP*shift).shift(RIGHT*right),
            angles[0].animate.shift(UP*shift).shift(RIGHT*right),
            angles[1].animate.shift(UP*shift).shift(RIGHT*right),
            angles[2].animate.shift(UP*shift).shift(RIGHT*right),
            angles[3].animate.shift(UP*shift).shift(RIGHT*right),
            angles[4].animate.shift(UP*shift).shift(RIGHT*right),
            angles[5].animate.shift(UP*shift).shift(RIGHT*right),
            values[0].animate.shift(UP*shift).shift(RIGHT*right),
            values[1].animate.shift(UP*shift).shift(RIGHT*right),
            values[2].animate.shift(UP*shift).shift(RIGHT*right),
            values[3].animate.shift(UP*shift).shift(RIGHT*right),
            values[4].animate.shift(UP*shift).shift(RIGHT*right),
            values[5].animate.shift(UP*shift).shift(RIGHT*right),
            values[6].animate.shift(UP*shift).shift(RIGHT*right),
            values[7].animate.shift(UP*shift).shift(RIGHT*right),
            values[8].animate.shift(UP*shift).shift(RIGHT*right),
            values[9].animate.shift(UP*shift).shift(RIGHT*right),
        )

        MT_2 = [
            MathTex(r"6\sin(180-30)", color=GOLD, font_size=11).next_to(values[8],LEFT*0) ,
            MathTex(r"6\sin(30)", color=GOLD, font_size=11).next_to(values[8],LEFT*0) ,
            MathTex(r"6\frac{1}{2}", color=GOLD, font_size=11).next_to(values[8],LEFT*0) ,
            MathTex(r"3", color=GOLD, font_size=11).next_to(values[8],LEFT*0) ,
        ]
        MT_1 = [
            MathTex(r"-2\tan(-225+360)", color=GOLD, font_size=11).next_to(values[9],LEFT*0), 
            MathTex(r"-2\tan(135)", color=GOLD, font_size=11).next_to(values[9],LEFT*0), 
            MathTex(r"-2\tan(180-45)", color=GOLD, font_size=11).next_to(values[9],LEFT*0), 
            MathTex(r"2\tan(45)", color=GOLD, font_size=11).next_to(values[9],LEFT*0), 
            MathTex(r"\text{2}", color=GOLD, font_size=11).next_to(values[9],LEFT*0),
        ]
        for v in MT_2:
            self.play(Transform(values[8],v))
            self.wait(1)
        for v in MT_1:
            self.play(Transform(values[9],v))
            self.wait(1)

        indication_rt_angle = Angle(lines[1],lines[4], elbow=True, radius=0.25,quadrant=(-1,-1),color=GOLD)
        deg60_angle = Angle(
            lines[4],lines[5],radius=0.15,quadrant=(-1,1), color=GOLD
        )
        deg60_value =  MathTex(
                r"90^{\circ} - 30^{\circ}",font_size=11, color=GOLD
        ).next_to(deg60_angle,RIGHT,buff=0.15).shift(UP*0.05)

        self.play(Write(indication_rt_angle), Write(deg60_value))

        self.wait(1)
        self.play(Unwrite(indication_rt_angle))
        self.wait(1)
        del indication_rt_angle

        deg60_answer =  MathTex(
                r"60^{\circ}",font_size=11, color=GOLD
        ).next_to(deg60_angle,RIGHT,buff=0.1).shift(UP*0.05)


        self.play(Write(deg60_angle), Transform(deg60_value,deg60_answer))
        self.wait(3)

        desc_text = MathTex(
            r"\tan(60^{\circ}) = \frac{\sqrt{3}}{1} = \frac{MT_2}{T_1T_2} \\" +
            r"\frac{\sqrt{3}}{1} = \frac{3}{T_1T_2} \\",
            r"\sqrt{3}T_1T_2 = 3 \\",
            r"T_1T_2 = \frac{3}{\sqrt{3}} \\",
            r"T_1T_2 = \sqrt{3}",
            font_size=10,
            color=GOLD_A
        ).next_to(values[9],DOWN,buff=0).shift((LEFT*1.2)+(UP*0.2))

        T_1T_2 = MathTex(
            r"\sqrt{3}",font_size=11,color=GOLD
        ).next_to(lines[5],RIGHT,buff=-0.15).shift(UP*0.05)

        self.play(
                Indicate(deg60_angle,color=BLUE,scale_factor=1),
                Indicate(deg60_value,color=BLUE,scale_factor=1),
                Indicate(lines[3],color=BLUE,scale_factor=1),
                Indicate(lines[5],color=BLUE,scale_factor=1),
                run_time=2,
        )
        self.play(Write(desc_text),run_time=3)
        self.wait(3)
        self.play(Write(T_1T_2))
        self.play(Unwrite(desc_text))

        self.play(
            Indicate(angles[4],color=BLUE,scale_factor=1),
            Indicate(values[3],color=BLUE,scale_factor=1),
            Indicate(lines[1],color=BLUE,scale_factor=1),
            Indicate(lines[5],color=BLUE,scale_factor=1),
            run_time=2,
        )

        desc_text = MathTex(
            r"\cos(30^{\circ}) = \frac{\sqrt{3}}{2} = \frac{T_1T_2}{T_1L} \\" +
            r"\frac{\sqrt{3}}{2} = \frac{\sqrt{3}}{T_1L} \\",
            r"\frac{\sqrt{3}}{2}T_1L = \sqrt{3} \\",
            r"T_1L = 2",
            font_size=10,
            color=GOLD_A
        ).next_to(values[9],DOWN,buff=0).shift((LEFT*1.2)+(UP*0.2))
        T_1L = MathTex(
            r"2",font_size=11,color=GOLD
        ).next_to(lines[1],LEFT,buff=0.1).shift(UP*0.05)
        self.play(Write(desc_text),run_time=3)
        self.wait(3)
        self.play(Write(T_1L))
        self.play(Unwrite(desc_text))


        self.play(
            Indicate(angles[0],color=BLUE,scale_factor=1),
            Indicate(values[0],color=BLUE,scale_factor=1),
            Indicate(lines[1],color=BLUE,scale_factor=1),
            Indicate(lines[2],color=BLUE,scale_factor=1),
            run_time=2,
        )

        desc_text = MathTex(
            r"\tan^{-1}(\frac{T_1L}{FT_1}) = \alpha \\" +
            r"\tan^{-1}(\frac{2}{2}) = \alpha\\",
            r"\tan^{-1}(1) = \alpha \\",
            r"45^{\circ} = \alpha",
            font_size=10,
            color=GOLD_A
        ).next_to(values[9],DOWN,buff=0).shift((LEFT*1.2)+(UP*0.2))
        alpha = MathTex(
            r"45^{\circ}",font_size=11,color=GOLD
        ).next_to(angles[0],RIGHT,buff=0.1).shift(UP*0.05)
        self.play(Write(desc_text),run_time=3)
        self.wait(3)
        self.play(Transform(values[0],alpha))
        self.play(Unwrite(desc_text))

        self.play(
            Indicate(lines[0],color=BLUE,scale_factor=1),
            Indicate(lines[1],color=BLUE,scale_factor=1),
            Indicate(lines[2],color=BLUE,scale_factor=1),
            run_time=2,
        )

        desc_text = MathTex(
            r"\text{Pythagoras:} \\" +
            r"FL = \sqrt{FT_1^2 + T_1T_2^2} \\",
            r"FL = \sqrt{2^2 + 2^2} \\",
            r"FL = \sqrt{8} = 2.8284",
            font_size=10,
            color=GOLD_A
        ).next_to(values[9],DOWN,buff=0).shift((LEFT*1.2)+(UP*0.2))
        FL = MathTex(
            r"2.8284",font_size=11,color=GOLD
        ).next_to(lines[0],LEFT,buff=-0.35).shift(UP*0.05)
        self.play(Write(desc_text),run_time=3)
        self.wait(3)
        self.play(Write(FL))
        self.play(Unwrite(desc_text))


        self.play(
            Indicate(lines[1],color=BLUE,scale_factor=1),
            Indicate(lines[3],color=BLUE,scale_factor=1),
            Indicate(lines[5],color=BLUE,scale_factor=1),
            Indicate(angles[4],color=BLUE,scale_factor=1),
            Indicate(values[3],color=BLUE,scale_factor=1),
            run_time=2,
        )
        desc_text = MathTex(
            r"\sin(30^{\circ}) = \frac{1}{2} = \frac{T_2L}{T_1L} \\" +
            r"\frac{1}{2} = \frac{T_2L}{2} \\",
            r"2\frac{1}{2} = T2_L \\",
            r"T_2L = 1",
            font_size=10,
            color=GOLD_A
        ).next_to(values[9],DOWN,buff=0).shift((LEFT*1.2)+(UP*0.2))
        T_2L = MathTex(
            r"1",font_size=11,color=GOLD
        ).next_to(values[7],RIGHT,buff=0.15).shift(DOWN*0.05)
        self.play(Write(desc_text),run_time=3)
        self.wait(3)
        self.play(Write(T_2L))
        self.play(Unwrite(desc_text))



        self.play(
            Indicate(lines[1],color=BLUE,scale_factor=1),
            Indicate(lines[3],color=BLUE,scale_factor=1),
            Indicate(lines[4],color=BLUE,scale_factor=1),
            Indicate(angles[3],color=YELLOW,scale_factor=1),
            Indicate(values[1],color=YELLOW,scale_factor=1),
            run_time=2,
        )
        desc_text = MathTex(
            r"\sin^{-1}(\frac{T_1L}{ML}) = \beta \\" +
            r"\sin^{-1}(\frac{2}{3+1}) = \beta \\",
            r"\sin^{-1}(\frac{1}{2}) = \beta \\",
            r"\beta = 30^{\circ}",
            font_size=10,
            color=GOLD_A
        ).next_to(values[9],DOWN,buff=0).shift((LEFT*1.2)+(UP*0.2))
        beta = MathTex(
            r"30^{\circ}",font_size=11,color=GOLD
        ).next_to(angles[3],LEFT,buff=0.15).shift(UP*0.05)
        self.play(Write(desc_text),run_time=3)
        self.wait(3)
        self.play(Transform(values[1],beta))
        self.play(Unwrite(desc_text))
        
        self.wait(2)

        desc_text = Tex(
            r"\text{You now know you must turn } \textbf{30 degrees clockwise} \text{ and walk } \textbf{4 meters} \\" +
            r"\text{You call your friend on the walkie talkie and} \\",
            r"\text{tell him to turn } \textbf{45 degrees counter clockwise} \text{ and walk } \textbf{2.8284 meters} \\",
            r"\text{due to your quick thinking and mathmatical expertise} \\",
            r"\text{you both reach the secret laboratory !}\\ ",
            r"\underline{ \textbf{you successfully saved the world !}}",
            font_size=10,
            color=GOLD_A
        ).next_to(values[9],DOWN,buff=0).shift((DOWN*0.2))

        self.play(Write(desc_text), run_time=10)

        self.wait(3)

        self.play(
            Unwrite(desc_text),
            Unwrite(T_1T_2),
            Unwrite(T_1L),
            Unwrite(FL),
            Unwrite(T_2L),
            Unwrite(deg60_value),
            Unwrite(deg60_angle),
            Unwrite(lines[0]),
            Unwrite(lines[1]),
            Unwrite(lines[2]),
            Unwrite(lines[3]),
            Unwrite(lines[4]),
            Unwrite(lines[5]),
            Unwrite(angles[0]),
            Unwrite(angles[1]),
            Unwrite(angles[2]),
            Unwrite(angles[3]),
            Unwrite(angles[4]),
            Unwrite(angles[5]),
            Unwrite(values[0]),
            Unwrite(values[1]),
            Unwrite(values[2]),
            Unwrite(values[3]),
            Unwrite(values[4]),
            Unwrite(values[5]),
            Unwrite(values[6]),
            Unwrite(values[7]),
            Unwrite(values[8]),
            Unwrite(values[9]),
        )
        self.wait(1)

class Outroduction(Scene):
    def construct(self):
        circle = Circle();
        square = Square();

        intro_text_1 = MarkupText(
                f'<span underline="double" underline_color="green">Jan-Hendrik Brink</span>',
                font_size=32,
                color=WHITE
        )
        
        intro_text_2 = Text("Grade 10 Trigonometry", font_size=24, color=YELLOW)
        intro_text_2.next_to(intro_text_1,DOWN,buff=0.2)
        
        self.play(Create(circle))
        self.play(Transform(circle,square))
        self.play(circle.animate.rotate(PI / 4))
        self.play(Transform(circle,intro_text_1), FadeIn(intro_text_2))
        
        self.wait(3)

        self.play(FadeOut(circle), FadeOut(intro_text_2))








        





        


        

        


