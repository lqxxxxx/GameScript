import win32gui

hwnd_title = {}

'''

    获得句柄hwnd，再通过句柄查询对应的句柄类名和标题名
    
'''
def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


win32gui.EnumWindows(get_all_hwnd, 0)

for h, t in hwnd_title.items():
    if t is not "":
        print( win32gui.GetWindowText(h),'   ',win32gui.GetClassName(h))
