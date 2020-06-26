import win32con
import win32gui
import win32api


'''
   通过句柄类名和标题名打开软件，定义鼠标位置进行一次单击
'''


#调用软件
hwnd=win32gui.FindWindowEx(0,0,"Chrome_WidgetWin_1","OAuth application authorized - 360极速浏览器 12.0")
win32gui.SetForegroundWindow (hwnd)

if(win32gui.IsIconic(hwnd)):
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 300,200,1200,800,win32con.SWP_SHOWWINDOW)


# 鼠标位置
win32api.SetCursorPos([557, 584])
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)