import wx
import time
from appParts import AppParts
from appParts import SecondWindow

def MakeNewWindow(event):
    sw = SecondWindow(None, 'Preview Data', (1200, 500), ap.UpdateHeaders())
    sw.Show()

print('App Started')
print('App Loading...')

app = wx.App()
print('App Loaded!')
ap = AppParts(None, 'Data Formatter', (1200, 500))

ap.Show()
openFile = ap.MakeButton(20, 20, 300, 40, ap.GetData, 'Open File')
appDropDown = ap.MakeButton(120, 20, 300, 40, ap.CreateDropDown, 'Add Fliter')
removeDropDown = ap.MakeButton(220, 20, 100, 40, ap.RemoveDropDown, 'Remove Fliter')
update = ap.MakeButton(320, 20, 100, 40, ap.ClearDropDown, 'Clear')
remove = ap.MakeButton(420, 20, 100, 40, ap.UpdateListBox, 'Update')
save = ap.MakeButton(520, 20, 100, 40, ap.RemoveRows, 'Format Data')
save = ap.MakeButton(620, 20, 100, 40, ap.ExportData, 'Save')
preview = ap.MakeButton(720, 20, 100, 40, MakeNewWindow, 'Preview')
app.MainLoop()

