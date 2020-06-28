import win32con
import win32gui
import win32api

#鼠标点击态
MOUNSE_CLICK = 1
MOUNSE_DOUBLE_CLICK = 2


#在xy坐标处单机或双击
def mounse_click_xy(clicktype,x = 0,y = 0):
    # 鼠标位置
    if x != 0 or y != 0:
        win32api.SetCursorPos([x, y])
    #鼠标点击
    #单机
    if clicktype == MOUNSE_CLICK :
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP |  win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    #双击
    if clicktype == MOUNSE_DOUBLE_CLICK:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP |  win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP |  win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)