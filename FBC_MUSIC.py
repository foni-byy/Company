import customtkinter
import pyglet

app = customtkinter.CTk()
app.title("FBC_MUSIC")
app.geometry("600x400")
#app.grid_columnconfigure(0, weight = 1)
customtkinter.set_appearance_mode("dark")
app.resizable(False, False)

def play():
    sound = pyglet.media.load('METAN - Башня клинит.mp3', streaming=False)
    sound.play()

def play1():
    sound = pyglet.media.load('METAN - Банку качай.mp3', streaming=False)
    sound.play()

def play2():
    sound = pyglet.media.load('Metan - Пропаганда Спорта.mp3', streaming=False)
    sound.play()

def play3():
    sound = pyglet.media.load('METAN.mp3', streaming=False)
    sound.play()

def play4():
    sound = pyglet.media.load('METAN - Шнурки.mp3', streaming=False)
    sound.play()

def play5():
    sound = pyglet.media.load('Metan feat. AKIMBO69 - Рукосечка.mp3', streaming=False)
    sound.play()

def play6():
    sound = pyglet.media.load('Metan - Влюбился в боль.mp3', streaming=False)
    sound.play()

def play7():
    sound = pyglet.media.load('Metan - Перцовый баллон.mp3', streaming=False)
    sound.play()

def play8():
    sound = pyglet.media.load('METAN - Криминал Раша.mp3', streaming=False)
    sound.play()

def play9():
    sound = pyglet.media.load('Metan - Паутина.mp3', streaming=False)
    sound.play()

def play10():
    sound = pyglet.media.load('METAN - Нет страха.mp3', streaming=False)
    sound.play()

def play11():
    sound = pyglet.media.load('METAN - Не сломлен.mp3', streaming=False)
    sound.play()

def play12():
    sound = pyglet.media.load('METAN - Балаклавы.mp3', streaming=False)
    sound.play()

def play13():
    sound = pyglet.media.load('METAN - Не дам в обиду.mp3', streaming=False)
    sound.play()

def play14():
    sound = pyglet.media.load('METAN - Космонавт.mp3', streaming=False)
    sound.play()

def play15():
    sound = pyglet.media.load('Вектор А & METAN - Кровавый батут.mp3', streaming=False)
    sound.play()

def play16():
    sound = pyglet.media.load('METAN - Города.mp3')
    sound.play()

def play17():
    sound = pyglet.media.load('METAN - Нож.mp3')
    sound.play()

def one():
    Button_17.grid_remove()
    Button_18.grid_remove()
    Button_19.grid_remove()
    Button_20.grid_remove()
    Button_21.grid_remove()
    active()

def play18():
    sound = pyglet.media.load('METAN - Быть с тобой.mp3')
    sound.play()

def play19():
    sound = pyglet.media.load('METAN & ТЯЖЁЛАЯ АТЛЕТИКА - День наоборот.mp3')
    sound.play()

def play20():
    sound = pyglet.media.load('METAN - Злая молодёжь.mp3')
    sound.play()

def play21():
    sound = pyglet.media.load('Вектор А - Зависал.mp3')
    sound.play()

def play22():
    sound = pyglet.media.load('Вектор А - Один.mp3')
    sound.play()

def play23():
    sound = pyglet.media.load('Вектор А - Лирика.mp3')
    sound.play()

def play24():
    sound = pyglet.media.load('Вектор А - Снова.mp3')
    sound.play()

def play25():
    sound = pyglet.media.load('Вектор А - Жизнь.mp3')
    sound.play()

def play26():
    sound = pyglet.media.load('Вектор А - В Порядке.mp3')
    sound.play()

def play27():
    sound = pyglet.media.load('Вектор А - Не Вернусь.mp3')
    sound.play()

def play28():
    sound = pyglet.media.load('Вектор А - Новый День.mp3')
    sound.play()

def play29():
    sound = pyglet.media.load('Вектор А feat. Криминальный Бит - Выживать.mp3')
    sound.play()

def play30():
    sound = pyglet.media.load('SCIRENA feat. Вектор А - Темы.mp3')
    sound.play()

def play31():
    sound = pyglet.media.load('Вектор А - До Конца.mp3')
    sound.play()

def play32():
    sound = pyglet.media.load('Фогель feat. Вектор А - Пока.mp3')
    sound.play()

def play33():
    sound = pyglet.media.load('Вектор А - Далеко.mp3')
    sound.play()

def play34():
    sound = pyglet.media.load('Вектор А feat. Kiliana - Сон.mp3')
    sound.play()

def play35():
    sound = pyglet.media.load('Ramil feat. Вектор А - Нож На Земле.mp3')
    sound.play()

def play36():
    sound = pyglet.media.load('Вектор А feat. BRANYA - Золотой Звук.mp3')
    sound.play()

def play37():
    sound = pyglet.media.load('Вектор А - Напоследок.mp3')
    sound.play()

def two():
    Button_1.grid_remove()
    Button_2.grid_remove()
    Button_3.grid_remove()
    Button_4.grid_remove()
    Button_5.grid_remove()
    Button_6.grid_remove()
    Button_7.grid_remove()
    Button_8.grid_remove()
    Button_9.grid_remove()
    Button_10.grid_remove()
    Button_11.grid_remove()
    Button_12.grid_remove()
    Button_13.grid_remove()
    Button_14.grid_remove()
    Button_15.grid_remove()
    Button_16.grid_remove()
    Button_17.grid(row=0, column=1, padx=10, pady=20)
    Button_18.grid(row=1, column=1, padx=10, pady=0)
    Button_19.grid(row=2, column=1, padx=10, pady=20)
    Button_20.grid(row=3, column=1, padx=10, pady=0)
    Button_21.grid(row=4, column=1, padx=10, pady=20)

def three():
    Button_1.grid_remove()
    Button_2.grid_remove()
    Button_3.grid_remove()
    Button_4.grid_remove()
    Button_5.grid_remove()
    Button_6.grid_remove()
    Button_7.grid_remove()
    Button_8.grid_remove()
    Button_9.grid_remove()
    Button_10.grid_remove()
    Button_11.grid_remove()
    Button_12.grid_remove()
    Button_13.grid_remove()
    Button_14.grid_remove()
    Button_15.grid_remove()
    Button_16.grid_remove()
    Button_17.grid_remove()
    Button_18.grid_remove()
    Button_19.grid_remove()
    Button_20.grid_remove()
    Button_21.grid_remove()
    Button_22.grid_remove()
    Button_23.grid_remove()
    Button_24.grid_remove()
    Button_25.grid_remove()
    Button_26.grid_remove()
    Button_27.grid_remove()
    Button_28.grid_remove()
    Button_29.grid_remove()
    Button_30.grid_remove()
    Button_31.grid_remove()
    Button_32.grid_remove()
    Button_33.grid_remove()
    Button_34.grid_remove()
    Button_35.grid_remove()
    Button_36.grid_remove()
    Button_37.grid_remove()
    Button_F_1.grid_remove()
    Button_F_2.grid_remove()

Button_1 = customtkinter.CTkButton(app, text='Башня клинит', command=play)
Button_2 = customtkinter.CTkButton(app, text='Банку качай', command=play1)
Button_3 = customtkinter.CTkButton(app, text='Пропаганда Спорта', command=play2)
Button_4 = customtkinter.CTkButton(app, text='Андеграунд', command=play3)
Button_5 = customtkinter.CTkButton(app, text='Шнурки', command=play4)
Button_6 = customtkinter.CTkButton(app, text='Рукосечка', command=play5)
Button_7 = customtkinter.CTkButton(app, text='Влюбился в боль', command=play6)
Button_8 = customtkinter.CTkButton(app, text='Перцовый баллон', command=play7)
Button_9 = customtkinter.CTkButton(app, text='Криминал Раша', command=play8)
Button_10 = customtkinter.CTkButton(app, text='Паутина', command=play9)
Button_11 = customtkinter.CTkButton(app, text='Нет страха', command=play10)
Button_12 = customtkinter.CTkButton(app, text='Не сломлен', command=play11)
Button_13 = customtkinter.CTkButton(app, text='Балаклавы', command=play12)
Button_14 = customtkinter.CTkButton(app, text='Не дам в обиду', command=play13)
Button_15 = customtkinter.CTkButton(app, text='Космонавт', command=play14)
Button_16 = customtkinter.CTkButton(app, text='Кровавый батут', command=play15)
Button_F_1 = customtkinter.CTkButton(app, text='1', command=one, width=20, height=20)
Button_F_2 = customtkinter.CTkButton(app, text='2', command=two, width=10, height=10)
Button_17 = customtkinter.CTkButton(app, text='Города', command=play16)
Button_18 = customtkinter.CTkButton(app, text='Нож', command=play17)
Button_19 = customtkinter.CTkButton(app, text='Быть с тобой', command=play18)
Button_20 = customtkinter.CTkButton(app, text='День наоборот', command=play19)
Button_21 = customtkinter.CTkButton(app, text='Злая молодёжь', command=play20)
Button_22 = customtkinter.CTkButton(app, text='Зависал', command=play21)
Button_23 = customtkinter.CTkButton(app, text='Один', command=play22)
Button_24 = customtkinter.CTkButton(app, text='Лирика', command=play23)
Button_25 = customtkinter.CTkButton(app, text='Cнова', command=play24)
Button_26 = customtkinter.CTkButton(app, text='Жизнь', command=play25)
Button_27 = customtkinter.CTkButton(app, text='В Порядке', command=play26)
Button_28 = customtkinter.CTkButton(app, text='Не вернусь', command=play27)
Button_29 = customtkinter.CTkButton(app, text='Новый день', command=play28)
Button_30 = customtkinter.CTkButton(app, text='Выживать', command=play29)
Button_31 = customtkinter.CTkButton(app, text='Темы', command=play30)
Button_32 = customtkinter.CTkButton(app, text='До конца', command=play31)
Button_33 = customtkinter.CTkButton(app, text='Пока', command=play32)
Button_34 = customtkinter.CTkButton(app, text='Далеко', command=play33)
Button_35 = customtkinter.CTkButton(app, text='Сон', command=play34)
Button_36 = customtkinter.CTkButton(app, text='Нож на земле', command=play35)
Button_37 = customtkinter.CTkButton(app, text='Золотой звук', command=play36)
Button_38 = customtkinter.CTkButton(app, text='Напоследок', command=play37)
Button_F_3 = customtkinter.CTkButton(app, text='1', command=three)
Button_39 = customtkinter.CTkButton(app, text='')

def active():
    Button_1.grid(row=0, column=1, padx=10, pady=20)
    Button_2.grid(row=1, column=1, padx=10,pady=0)
    Button_3.grid(row=2, column=1, padx=10, pady=20)
    Button_4.grid(row=3, column=1, padx=10, pady=0)
    Button_5.grid(row=4, column=1, padx=10, pady=20)
    Button_6.grid(row=5, column=1, padx=10, pady=0)
    Button_7.grid(row=6, column=1, padx=10, pady=20)
    Button_8.grid(row=7, column=1, padx=10, pady=0)
    Button_9.grid(row=0, column=2, padx=10, pady=20)
    Button_10.grid(row=1, column=2, padx=10, pady=0)
    Button_11.grid(row=2, column=2, padx=10, pady=20)
    Button_12.grid(row=3, column=2,padx=10, pady=0)
    Button_13.grid(row=4, column=2, padx=10, pady=20)
    Button_14.grid(row=5, column=2, padx=10, pady=0)
    Button_15.grid(row=6, column=2, padx=10, pady=20)
    Button_16.grid(row=7, column=2, padx=10, pady=0)
    Button_F_1.grid(row=7, column=3, padx=10, pady=0)
    Button_F_2.grid(row=7, column=4, padx=10, pady=0)

def active1():
    Button_1.grid_remove()
    Button_2.grid_remove()
    Button_3.grid_remove()
    Button_4.grid_remove()
    Button_5.grid_remove()
    Button_6.grid_remove()
    Button_7.grid_remove()
    Button_8.grid_remove()
    Button_9.grid_remove()
    Button_10.grid_remove()
    Button_11.grid_remove()
    Button_12.grid_remove()
    Button_13.grid_remove()
    Button_14.grid_remove()
    Button_15.grid_remove()
    Button_16.grid_remove()
    Button_17.grid_remove()
    Button_18.grid_remove()
    Button_19.grid_remove()
    Button_20.grid_remove()
    Button_21.grid_remove()
    Button_22.grid(row=0, column=1, padx=10, pady=20)
    Button_23.grid(row=1, column=1, padx=10, pady=0)
    Button_24.grid(row=2, column=1, padx=10, pady=20)
    Button_25.grid(row=3, column=1, padx=10, pady=0)
    Button_26.grid(row=3, column=1, padx=10, pady=0)
    Button_27.grid(row=4, column=1, padx=10, pady=20)
    Button_28.grid(row=5, column=1, padx=10, pady=0)
    Button_29.grid(row=6, column=1, padx=10, pady=20)
    Button_30.grid(row=7, column=1, padx=10, pady=0)
    Button_31.grid(row=0, column=2, padx=10, pady=0)
    Button_32.grid(row=1, column=2, padx=10, pady=0)
    Button_33.grid(row=2, column=2, padx=10, pady=20)
    Button_34.grid(row=3, column=2, padx=10, pady=0)
    Button_35.grid(row=4, column=2, padx=10, pady=0)
    Button_36.grid(row=5, column=2, padx=10, pady=0)
    Button_37.grid(row=6, column=2, padx=10, pady=0)
    Button_38.grid(row=7, column=2, padx=10, pady=0)

Button = customtkinter.CTkButton(app, text='METAN',command=active)
Button.grid(row=0, column=0, padx=10, pady=20)

Button1 = customtkinter.CTkButton(app, text='Вектор А', command=active1)
Button1.grid(row=1, column=0, padx=20, pady=0)

app.mainloop()