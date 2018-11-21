from Info_v3 import Info
import tkinter as tk
import Info_to_csv
import Info_to_json
import Info_to_psql
from selenium import webdriver


class Start(Info):
    def __init__(self):
        self.all_info = []

        super(Start, self).__init__(self.all_info)

# Создание пользовательсокого интерфейса

        if __name__ == "__main__":
            self.window = tk.Tk()
            self.window.wm_title("Новости")
            self.window.resizable(width=False, height=False)
            b1 = tk.Button(self.window, text="Создать фаил csv", width=30, command=lambda: Info_to_csv.to_csv(self.all_info))
            b1.grid(row=0, column=0)

            b2 = tk.Button(self.window, text="Создать фаил json", width=30, command=lambda: Info_to_json.to_json(self.all_info))
            b2.grid(row=0, column=1)

            b3 = tk.Button(self.window, text="Записать информацию в датабазу", width=30, command=lambda: Info_to_psql.psql_record(self.all_info))
            b3.grid(row=1, column=0)

            b4 = tk.Button(self.window, text="Показать информацию на сайте", width=30, command=lambda: self.site_log())
            b4.grid(row=1, column=1)

            self.window.mainloop()

    @staticmethod
    def site_log():
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:5000/")


if __name__ == "__main__":
    window_start = Start()
