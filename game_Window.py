import win32con
import win32gui
import win32api
import setting

class GameWindow():
    def __init__(self,title):
        self.title = title

    def getGameWindow(self):
        # 查询软件hwnd
        hwnd = win32gui.FindWindow(0, self.title)
        win32gui.SetForegroundWindow(hwnd)
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        # 调用软件，设置坐标，设置大小
        if (win32gui.IsIconic(hwnd)):
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, setting.WINDOW_POS_X, setting.WINDOW_POS_Y,
                              setting.WINDOW_LENGTH, setting.WINDOW_WIDTH, win32con.SWP_SHOWWINDOW)