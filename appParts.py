import wx
import wx.grid as  gridlib
from wx.core import HeaderCtrlSimple, Window
from formatData import FormatData


class AppParts(wx.Frame):
    def __init__(self, parent, title, size):
        wx.Frame.__init__(self, parent, title=title, size=size)
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.data = ''
        self.fd = ''
        self.xpos = 20
        self.ypos = 100 
        self.dropdownlist = []
        self.listboxlist = []
  
    def GetData(self, event):
        self.openFileDialog = wx.FileDialog(self, "Open", "", "", 'CSV files (*.csv)|*.csv|All files(*.*)|*.*', wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        self.openFileDialog.ShowModal()
        self.data = self.openFileDialog.GetPath()
        self.CreateDropDown(event)   
    
    def ExportData(self, event):
        with wx.FileDialog(self, "Save CSV file", wildcard='CSV files (*.csv)|*.csv|All files(*.*)|*.*',
                        style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind

            # save the current contents in the file
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'w', newline="") as file:
                    self.fd.SaveData(file)
            except IOError:
                wx.LogError("Cannot save current data in file '%s'." % pathname)

    def CreateDropDown(self, event):
        self.fd = FormatData(self.data)
        self.headers = self.fd.GetHeaders()
        self.dropDown = wx.ComboBox(self.panel,choices = self.fd.GetHeaders(), pos =(self.xpos , self.ypos), size =(150, 40))
        self.listboxValues = []
        self.listbox = wx.ListBox(self.panel, pos = (self.xpos, self.ypos+20),size=(150, 150), style=wx.LB_MULTIPLE, choices=self.listboxValues)
        self.xpos += 150
        self.dropdownlist.append(self.dropDown)
        self.listboxlist.append(self.listbox)
        if self.xpos == 920:
            self.xpos = 20
            self.ypos += 170
        self.UpdateListBox(event)

    def MakeButton(self, xpos, ypos, xSize, ySize, functionName, buttonText):
        self.button = wx.Button(self.panel, label=buttonText, pos =(xpos, ypos), size =(xSize, ySize))
        self.button.SetSize(100,50)
        self.button.Bind(wx.EVT_BUTTON, functionName)

    def UpdateListBox(self, event):
        count = 0
        for drop in self.dropdownlist:
            if drop.GetValue() != '':
                columnName = drop.GetValue()
                value = self.fd.GetUniqueValues(columnName)
                self.listboxlist[count].Set(value)
            count += 1

    def ClearDropDown(self, event):
        for drop in self.dropdownlist:
            drop.SetValue('')
        for list in self.listboxlist:
            list.Set([])
    
    def RemoveRows(self, event):
        values = []
        for x in range(len(self.dropdownlist)):
            if self.dropdownlist[x].GetValue() != '':
                for i in range(len(self.listboxlist[x].Selections)):
                    values.append(self.listboxlist[x].GetString(self.listboxlist[x].GetSelections()[i]))
                self.fd.FormatRows(self.dropdownlist[x].GetValue(), values)

    def RemoveDropDown(self, event):
        self.dropdownlist[-1].Destroy()
        self.listboxlist[-1].Destroy()
        self.dropdownlist.pop()
        self.listboxlist.pop()
        self.xpos -= 150
        if len(self.dropdownlist) % 6 == 0:
            self.ypos -= 170
            self.xpos = 20 + (150 * 6)
        if len(self.dropdownlist) == 0:
            self.xpos = 20
            self.ypos = 100
    def UpdateHeaders(self):
        return self.fd.GetHeaders()

    def onClose(self, event):
        self.Close(force=True)


class SecondWindow(wx.Frame):
    def __init__(self, parent, title, size, data):
        wx.Frame.__init__(self, parent, title=title, size=size)
        xCol = len(data)
        print(xCol)
        panel = wx.Panel(self)
        
        myGrid = gridlib.Grid(panel)
        myGrid.CreateGrid(12, xCol)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(myGrid, 1, wx.EXPAND)
        panel.SetSizer(sizer)
        

    # def showPopupMenu(self, event):
    #     """
    #     Create and display a popup menu on right-click event
    #     """
    #     if not hasattr(self, "popupID1"):
    #         self.popupID1 = wx.NewId()
    #         self.popupID2 = wx.NewId()
    #         self.popupID3 = wx.NewId()
    #         # make a menu
        
    #     menu = wx.Menu()
    #     # Show how to put an icon in the menu
    #     item = wx.MenuItem(menu, self.popupID1,"One")
    #     menu.AppendItem(item)
    #     menu.Append(self.popupID2, "Two")
    #     menu.Append(self.popupID3, "Three")
        
    #     # Popup the menu.  If an item is selected then its handler
    #     # will be called before PopupMenu returns.
    #     self.PopupMenu(menu)
    #     menu.Destroy()
        
        
    