from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askyesno, showinfo, showwarning
from app.actor  import *
from app.base  import *
def shellSort(a, n, isNumber):
    c = n // 2
    while c>0:
        for i in range(c, n):
            t1 = a[i][0]
            t2 = a[i][1]
            j = i
            if isNumber:
                while j >= c and float(a[j - c][0]) > float(t1):
                    a[j] = a[j - c]
                    j -= c
                a[j]= (t1,t2)
            else:
                while j >= c and a[j - c][0] > t1:
                    a[j] = a[j - c]
                    j -= c
                a[j]= (t1,t2)
        c //= 2

class Win:
    def __init__(self,b):
       self.win =Tk() 
       self.win.geometry("500x300")
       self.win.resizable(True, True)
       self.base = b
       self.menu()
       self.win.mainloop()

    def menu(self):
        self.win.title("Киноактёры")
        self.win.button1 = Button(self.win, text = "Вывести таблицу актёров", command=lambda:[self.sneak1(), self.printA(1)])
        self.win.button2 = Button(self.win, text = "Вывести таблицу актёров с гонорарами в евро", command=lambda:[self.euro(True)])
        self.win.button3 = Button(self.win, text = "Ввести в базу данных нового актёра", command=lambda:[self.addA()])
        self.win.button4 = Button(self.win, text = "Вывести актёров с гонораром не менее указанного числа", command=lambda:[self.honorar()])
        self.win.button5 = Button(self.win, text = "Выход", command=self.terminate)
        self.win.button1.pack(padx=5, pady=5)
        self.win.button2.pack(padx=5, pady=5)
        self.win.button3.pack(padx=5, pady=5)
        self.win.button4.pack(padx=5, pady=5) 
        self.win.button5.pack(padx=5, pady=5)

    def terminate(self):
        l=askyesno(title="Выход", message="Вы точно хотите выйти из программы?")
        if l:
            self.win.destroy()
            quit( )
    def sneak1(self):
        self.win.button1.destroy()
        self.win.button2.destroy()
        self.win.button3.destroy()
        self.win.button4.destroy()
        self.win.button5.destroy()
    def cw(self, string):
        k=0
        t=False
        for i in range(0,len( string)):
            if not((string[i]>='a' and string[i]<='z') or (string>='A' and string<='Z') or (string>='А' and string[i]<='Я') or (string[i]>='а' and string[i]<='я')):
                showwarning(title="Предупреждение", message='Некорректный ввод. Введите корретно имя или фамилию')
                t=True
                break
            if ((string[i]>='A' and string[i]<='Z') or (string[i]>='А' and string[i]<='Я')) and k==0:
                k=1
            elif ((string[i]>='A' and string[i]<='Z') or (string[i]>='А' and string[i]<='Я')):
               showwarning(title="Предупреждение", message='Некорректный ввод. Требуется корректный ввод заглавных букв')
               t=True
               break
            if ((string[i]>='a' and string[i]<='z') or (string[i]>='а' and string[i]<='я')) and k==0:
               showwarning(title="Предупреждение", message='Некорректный ввод. Введите с заглавной буквы')
               t=True
               break
        return not t
    def cn(self, string):
        t=False
        for i in range(0,len(string)):
            if not(ord(string[i])>=48 and ord(string[i])<=57):
                showwarning(title="Предупреждение", message='Некорректный ввод. Введите натуральное число фильмов')
                t=True
                break
        return not t
    def cf(self, string):
        t=False
        k=0
        for i in range(0,len(string)):
            if not((ord(string[i])>=48 and ord(string[i])<=57) or string[i]=='.' or string[i]==','):
                showwarning(title="Предупреждение", message='Некорректный ввод. Введите вещественное число')
                t=True
                break
            elif ((string[i]=='.' or string[i]==',') and i==0):
                showwarning(title="Предупреждение", message='Некорректный ввод. Введите корретно вещественное число')
                t=True
                break
            elif ((string[i]=='.' or string[i]==',') and k==0):
                b = string[:i]+'.' +string[i+1:]
                k=1           
            elif ((string[i]=='.' or string[i]==',') and k==1):
                showwarning(title="Предупреждение", message='Некорректный ввод. Введите корретно вещественное число')
                t=True
                break        
        return not t
    def floating(self, string):
        for i in range(0,len(string)):
            if (string[i]=='.' or string[i]==','):
                self.base = string[:i]+'.' +string[i+1:]
                break        
        return float(string)
    def addA(self):
        def restartA(t):
            s1=e1.get()
            s2=e2.get()
            s3=e3.get()
            s4=e4.get()
            l.destroy()
            l1.destroy()
            l2.destroy()
            l3.destroy()
            l4.destroy()
            e1.destroy()
            e2.destroy()
            e3.destroy()
            e4.destroy()
            btn1.destroy()
            btn2.destroy()
            if t:
                self.menu()
            else:
                if self.cw(s1) and self.cw(s2) and self.cn(s3) and self.cf(s4) and self.base.c<=12:
                    b = self.base.add(Actor(s1,s2,int(s3),self.floating(s4)))
                    if not b:
                        showwarning(title="Предупреждение", message='База заполнена')
                    else:
                        showinfo(title="Информация", message='Актёр удачно внесён в базу данных')
                    self.menu()
                else:
                    self.addA(self.base)
        self.sneak1()
        self.win.title('Ввод нового актёра')
        l=Label(self.win, text='Введите данные нового актёра')
        e1=Entry(self.win) 
        e2=Entry(self.win)
        e3=Entry(self.win)
        e4=Entry(self.win)
        l1=Label(self.win, text='Фамилия')
        l2=Label(self.win, text='Имя')
        l3=Label(self.win, text='Число фильмов')
        l4=Label(self.win, text='Гонорар')
        l.pack(anchor=NW, padx=5, pady=0)
        l1.pack(anchor=NW, padx=5, pady=0)
        e1.pack(anchor=NW, padx=5, pady=1)
        l2.pack(anchor=NW, padx=5, pady=0)
        e2.pack(anchor=NW, padx=5, pady=1)
        l3.pack(anchor=NW, padx=5, pady=0)
        e3.pack(anchor=NW, padx=5, pady=1)
        l4.pack(anchor=NW, padx=5, pady=0)
        e4.pack(anchor=NW, padx=5, pady=1)
        btn1 = Button(self.win,  text="Ввод", command=lambda:restartA(False))
        btn1.pack(anchor=NW, padx=5, pady=5)
        btn2 = Button(self.win,  text="Вернуться в меню", command=lambda:restartA(True))
        btn2.pack(anchor=SW, padx=5, pady=5)
    def printA(self, f):
        def restart():
            tree.destroy()
            bl.destroy()
            self.menu()
            bd.destroy()
        def delete():
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                person = item["values"]
            for i in range(0,self.base.c):
                if person[0]==self.base.a[i].fn and person[1]==self.base.a[i].pn:
                    self.base.a.pop(i)
                    self.base.c -= 1
                    break
            bd.destroy()
            bl.destroy()
            tree.destroy()
            self.printA(self.base)
        def sort(col, rev):
            l = [(tree.set(k, col), k) for k in tree.get_children("")]
            if col>1:
                t=True
            else:
                t=False
            shellSort(l,self.base.c, t)
            if rev:
                l=reversed(l)
            for index,(_, k) in enumerate(l):
                tree.move(k, "", index)
            tree.heading(col, command=lambda: sort(col, not rev))
        def item_selected(event):
            bd["state"]="normal"
        eu=float(f)
        columns = ("fn", "pn", "n", "s")
        tree = ttk.Treeview(columns=columns, show="headings")
        tree.pack(fill=BOTH, expand=1)
        tree.heading("fn", text="Фамилия",command=lambda: sort(0, rev=False))
        tree.heading("pn", text="Имя", command=lambda:  sort(1, rev=False))
        tree.heading("n", text="Число фильмов", command=lambda:  sort(2, rev=False))
        tree.heading("s", text="Гонорар", command=lambda:  sort(3, rev=False))
        tree.column("#1", stretch=YES, width=70)
        tree.column("#2", stretch=YES, width=20)
        tree.column("#3", stretch=YES, width=40)
        tree.column("#4", stretch=YES, width=20)
        for i in range(0,self.base.c):
            tree.insert("",  END, values=(self.base.a[i].fn, self.base.a[i].pn,self.base.a[i].n, round(eu*self.base.a[i].s, 2)))
        bl = Button(text="Вернуться в меню", command=restart)
        bl.pack(anchor=S, padx=5, pady=5)
        bd= Button(text="Удалить", state=["disabled"], command=lambda:[delete()])
        bd.pack(anchor=S, padx=5, pady=5 )
        tree.bind("<<TreeviewSelect>>", item_selected)
    def printB(self, base: Base, f):
        def restart():
            tree.destroy()
            bl.destroy()
            self.menu()
            bd.destroy()
        def delete():
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                person = item["values"]
            for i in range(0,base.c):
                if person[0]==base.a[i].fn and person[1]==base.a[i].pn:
                    base.a.pop(i)
                    base.c -= 1
                    break
            bd.destroy()
            bl.destroy()
            tree.destroy()
            self.printB(base, f)
        def sort(col, rev):
            l = [(tree.set(k, col), k) for k in tree.get_children("")]
            if col>1:
                t=True
            else:
                t=False
            shellSort(l,base.c, t)
            if rev:
                l=reversed(l)
            for index,(_, k) in enumerate(l):
                tree.move(k, "", index)
            tree.heading(col, command=lambda: sort(col, not rev))
        def item_selected(event):
            bd["state"]="normal"
        eu=float(f)
        columns = ("fn", "pn", "n", "s")
        tree = ttk.Treeview(columns=columns, show="headings")
        tree.pack(fill=BOTH, expand=1)
        tree.heading("fn", text="Фамилия",command=lambda: sort(0, rev=False))
        tree.heading("pn", text="Имя", command=lambda:  sort(1, rev=False))
        tree.heading("n", text="Число фильмов", command=lambda:  sort(2, rev=False))
        tree.heading("s", text="Гонорар", command=lambda:  sort(3, rev=False))
        tree.column("#1", stretch=YES, width=70)
        tree.column("#2", stretch=YES, width=20)
        tree.column("#3", stretch=YES, width=40)
        tree.column("#4", stretch=YES, width=20)
        for i in range(0,base.c):
            tree.insert("",  END, values=(base.a[i].fn, base.a[i].pn,base.a[i].n, round(eu*base.a[i].s, 2)))
        bl = Button(text="Вернуться в меню", command=restart)
        bl.pack(anchor=S, padx=5, pady=5)
        bd= Button(text="Удалить", state=["disabled"], command=lambda:[delete()])
        bd.pack(anchor=S, padx=5, pady=5 )
        tree.bind("<<TreeviewSelect>>", item_selected)


    def euro(self,t):
        def restart(t):
            s=e.get()
            l.destroy()
            e.destroy()
            btn1.destroy()
            btn2.destroy()
            if t:
                self.menu()
            else:
                if self.cf(s):
                    nb=Base([])
                    j=0
                    for i in range(0,self.base.c):
                        nb.add(self.base.a[i])
                    self.sneak1()
                    self.printB(nb, self.floating(s))     
                else:
                    self.euro(False)
        self.sneak1()
        self.win.title("Ввод курса евро")
        l=Label(self.win,  text='Введите курс евро')
        l.pack(anchor=NW, padx=5, pady=5)
        e=Entry(self.win)
        e.pack(anchor=NW, padx=5, pady=5)
        btn1 = Button(self.win,  text="Ввод", command=lambda:restart(False))
        btn1.pack(anchor=NW, padx=5, pady=5)
        btn2 = Button(self.win,  text="Вернуться в меню", command=lambda:restart(True))
        btn2.pack(anchor=SW, padx=5, pady=5)
    def honorar(self):
        def restart(t):
            s=e.get()
            l.destroy()
            e.destroy()
            btn1.destroy()
            btn2.destroy()
            if t:
                self.menu()
            else:
                if self.cf(s):
                    nb=Base([])
                    j=0
                    for i in range(0,self.base.c):
                        if self.base.a[i].s >= self.floating(s):
                            nb.add(self.base.a[i])
                    self.sneak1()
                    self.printB(nb, 1)     
                else:
                    self.honorar(self.base)
        self.sneak1()
        self.win.title("Ввод порог гонорара")
        l=Label(self.win,  text="Ввод порог гонорара")
        l.pack(anchor=NW, padx=5, pady=5)
        e=Entry(self.win)
        e.pack(anchor=NW, padx=5, pady=5)
        btn1 = Button(self.win,  text="Ввод", command=lambda:restart(False))
        btn1.pack(anchor=NW, padx=5, pady=5)
        btn2 = Button(self.win,  text="Вернуться в меню", command=lambda:restart(True))
        btn2.pack(anchor=SW, padx=5, pady=5)