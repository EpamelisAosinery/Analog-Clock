"""     Phần 1: Sử dụng thư viện Turtle để setup  đồng hồ
B1: import turtle
          B2: Create a screen/window
          B3: Create a pen tool to draw
B4: Tạo mặt đồng hồ
B5: Thêm chi tiết cho mặt đồng hồ (tạo vặt giờ tương ứng với các con số trên đồng hồ và vặt giây tương ứng với từng nấc kim giờ chạy)
B6: tạo kim Giờ, Phút, Giây

 Phần 2: tạo kim Giờ,Phút, Giây làm đồng hồ hoạt động
B7: làm 3 kim Giờ Phút Giây hoạt động như 1 đồng hồ bình thường
B9: thêm chút chỉnh sửa màu mè theo phong cách của bạn và hoàn chỉnh """

import turtle
import time
from datetime import date, datetime

# Create a window/screen
wn = turtle.Screen()
wn.title("Turtle clock by Epamelis")
wn.setup(width = 600, height = 600)
wn.bgcolor("black")
wn.tracer(0)
# tracer is a function turn on/off the animation and it goes with wn.update()

# Create a pen to draw
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)
pen.hideturtle()
pen.color("white")

def clock(h, m, s, pen):
          pen.up()
          pen.goto(0,260)
          pen.setheading(180)
          pen.color("white")
          pen.down()
          pen.circle(180) #180 is the radius

          # Create 12 numbers around  the clock
          num =0 
          for i in range(12):
                    num+=1
                    pen.up()
                    pen.setheading(-30*(i+3)+75)
                    pen.forward(100)
                    pen.write(str(num), align="center", font=("Arial", 12, "normal"))

          # Create the hour lines
          pen.goto(0,80)
          pen.setheading(90)
          for i in range(12):
                    pen.forward(160)
                    pen.down()
                    pen.forward(10)
                    pen.up()
                    pen.goto(0,80)
                    pen.rt(30)

          # Create the second lines
          # There are 5 dashes between each number 5x12 = 60. The second hand stop at these dashes
          for i in range(60):
                    pen.forward(175)
                    pen.down()
                    pen.forward(4)
                    pen.up()
                    pen.goto(0,80)
                    pen.rt(6)

          # Create Hour hand
          pen.setposition(0,80)
          pen.setheading(90)
          pen.pensize(4)
          pen.color("yellow")
          angle = (h/12)*360
          pen.rt(angle)
          pen.down()
          pen.forward(95)

          # Create Minute hand
          pen.setposition(0,80)
          pen.setheading(90)
          pen.pensize(4)
          pen.color("blue")
          angle = (m/60)*360
          pen.rt(angle)
          pen.down()
          pen.forward(160)

          # Create Second hand
          pen.setposition(0,80)
          pen.setheading(90)
          pen.pensize(2)
          pen.color("red")
          angle = (s/60)*360
          pen.rt(angle)
          pen.down()
          pen.forward(175)

          #Create Name inside the clock
          pen.up()
          pen.color("orange")
          pen.setpos(0,-30)
          pen.write("Epamelis", align="center", font=("Arial", 15, "italic"))

#Create an infinite loop to Get Time and pass it in the User Define Function 
while True:
          h = int(time.strftime("%I"))
          m = int(time.strftime("%M"))
          s = int(time.strftime("%S"))
          pen.up()
          pen.color("orange")
          today = date.today()
          today_now = today.strftime("%B, %d, %Y")
          pen.goto(0,-175)
          pen.write("Today is: " + today_now, align="center", font=("Arial", 15, "italic"))

          duisplay_time = datetime.now()
          time_now  = duisplay_time.strftime("%H %p %M minutes %S seconds")
          pen.goto(0,-220)
          pen.write("Up time:" + time_now, align="center", font=("Arial", 15, "italic"))
          clock(h, m, s, pen)

          wn.update()
          time.sleep(1)
          pen.clear()

wn.mainloop()
