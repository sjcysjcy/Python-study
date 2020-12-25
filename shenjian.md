这是被沈坚修改的程序，解决了两个问题：
1、窗口大小可调整，会导致球走向看起来不正确，修改为第二十行self.windows.resizable(width=False,height=False)
2、修改调整退出时的操作，避免退出后，因为窗口销毁，导致animate函数运行循环时循环内容中的canvas已经销毁的错误，使退出为正常退出。
3、 本次修改仅修改为Ballgame.py
4、因为windows主窗口将会再其他地方用到，因此在此将局部变量windows变更为内部类内部变量
