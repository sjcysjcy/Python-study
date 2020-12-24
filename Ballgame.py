from tkinter import *
from Sca import *


class Boll:  # 创建球类型
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 2
        self.dy = 2
        self.radius = 3
        self.color = getColor()


class BounceBolls:  # 创建窗口对象
    def __init__(self):
        self.bollList = []

        windows = Tk()
        windows.title("BounceBalls game")
        self.width = 600
        self.height = 400
        self.canvas = Canvas(windows, bg="white", width=self.width, height=self.height)
        self.canvas.pack()

        self.frame = Frame()
        self.frame.pack()

        btStop = Button(self.frame, text="stop", command=self.stop)
        btStop.pack(side=LEFT)
        btResume = Button(self.frame, text="resume", command=self.resume)
        btResume.pack(side=LEFT)
        btAdd = Button(self.frame, text="+", command=self.add)
        btAdd.pack(side=LEFT)
        btRemove = Button(self.frame, text="_", command=self.remove)
        btRemove.pack(side=LEFT)

        self.sleepTime = 10
        self.isStopped = False
        self.animate()

        windows.mainloop()

    def stop(self):
        self.isStopped = True

    def resume(self):
        self.isStopped = False
        self.animate()

    def add(self):
        self.bollList.append(Boll())

    def remove(self):
        self.bollList.pop()

    def animate(self):
        while not self.isStopped:
            self.canvas.after(self.sleepTime)
            self.canvas.update()
            self.canvas.delete("ball")

            for ball in self.bollList:
                self.redisplayball(ball)

    def redisplayball(self, ball):
        if ball.x > self.width or ball.x < 0:
            ball.dx = -ball.dx

        if ball.y > self.height or ball.y < 0:
            ball.dy = -ball.dy

        ball.x += ball.dx
        ball.y += ball.dy

        self.canvas.create_oval(ball.x - ball.radius, ball.y - ball.radius, ball.x + ball.radius,
                                ball.y + ball.radius, fill=ball.color, tags="ball")
