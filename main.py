import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from meat_fuzzy import (
    predict_cooking,
    meat_type, cooking_method, cooking_pref,
    fat_level, thickness, time, temp
)

def main():
    root = tk.Tk()
    root.title("Akıllı Et Pişirme Asistanı")
    root.resizable(False, False)

    meat_types = ["Dana", "Kuzu", "Tavuk"]
    cooking_methods = ["Izgara", "Tavada", "Fırında"]
    all_cooking_prefs = ["Az Pişmiş", "Orta Pişmiş", "Çok Pişmiş"]
    fat_levels = ["Yağsız", "Orta Yağlı", "Yağlı"]

    selected_meat = tk.StringVar()
    selected_method = tk.StringVar()
    selected_pref = tk.StringVar()
    selected_fat = tk.StringVar()
    et_thickness = tk.DoubleVar(value=3.0)
    selected_unit = tk.StringVar(value="C")
    temp_c_global = {'value': None}

    # UI Elemanları
    ttk.Label(root, text="Et Türü:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    ttk.OptionMenu(root, selected_meat, meat_types[0], *meat_types).grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(root, text="Pişirme Şekli:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
    ttk.OptionMenu(root, selected_method, cooking_methods[0], *cooking_methods).grid(row=1, column=1, padx=5, pady=5)

    ttk.Label(root, text="Pişirme Tercihi:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
    cooking_pref_menu = ttk.OptionMenu(root, selected_pref, all_cooking_prefs[0], *all_cooking_prefs)
    cooking_pref_menu.grid(row=2, column=1, padx=5, pady=5)

    def update_cooking_prefs(*args):
        current_meat = selected_meat.get()
        prefs = all_cooking_prefs.copy()
        if current_meat == "Tavuk":
            prefs.remove("Az Pişmiş")
        selected_pref.set(prefs[0])
        menu = cooking_pref_menu["menu"]
        menu.delete(0, "end")
        for option in prefs:
            menu.add_command(label=option, command=lambda value=option: selected_pref.set(value))

    selected_meat.trace_add("write", update_cooking_prefs)

    ttk.Label(root, text="Yağ Oranı:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
    ttk.OptionMenu(root, selected_fat, fat_levels[0], *fat_levels).grid(row=3, column=1, padx=5, pady=5)

    ttk.Label(root, text="Et Kalınlığı (cm):").grid(row=4, column=0, sticky="w", padx=5, pady=5)
    tk.Scale(root, from_=1.0, to=6.0, orient="horizontal", resolution=0.1,
             variable=et_thickness, length=200).grid(row=4, column=1, padx=5, pady=5, sticky="w")

    ttk.Label(root, text="Sıcaklık Birimi:").grid(row=6, column=0, sticky="w", padx=5, pady=5)
    unit_frame = ttk.Frame(root)
    unit_frame.grid(row=6, column=1, sticky="w", padx=5, pady=5)
    tk.Radiobutton(unit_frame, text="°C", variable=selected_unit, value="C", command=lambda: update_displayed_temp()).pack(side="left")
    tk.Radiobutton(unit_frame, text="°F", variable=selected_unit, value="F", command=lambda: update_displayed_temp()).pack(side="left")

    result_label = ttk.Label(root, text="")
    result_label.grid(row=7, column=0, columnspan=2, pady=10)

    def update_displayed_temp():
        temp_c = temp_c_global['value']
        current_text = result_label.cget("text")
        if temp_c is None or "Tahmini Süre" not in current_text:
            return
        time_line = current_text.split("\n")[0]
        unit = selected_unit.get()
        temp_display = temp_c * 1.8 + 32 if unit == "F" else temp_c
        result_label.config(text=f"{time_line}\nTahmini Sıcaklık: {temp_display:.0f}°{unit}")

    def calculate():
        inputs = {
            "meat_type": meat_types.index(selected_meat.get()),
            "cooking_method": cooking_methods.index(selected_method.get()),
            "cooking_pref": all_cooking_prefs.index(selected_pref.get()),
            "fat_level": fat_levels.index(selected_fat.get()),
            "thickness": et_thickness.get()
        }
        time, temp = predict_cooking(**inputs)
        if time is None or temp is None:
            result_label.config(text="Bu kombinasyon için yeterli kural tanımlı değil.")
            temp_c_global['value'] = None
        else:
            temp_c_global['value'] = temp
            unit = selected_unit.get()
            temp_display = temp * 1.8 + 32 if unit == "F" else temp
            result_label.config(text=f"Tahmini Süre: {time:.1f} dk\nTahmini Sıcaklık: {temp_display:.0f}°{unit}")

    def show_graphs():
        if temp_c_global['value'] is None:
            tk.messagebox.showwarning("Uyarı", "Lütfen önce 'Hesapla' butonuna basın.")
            return

        graph_window = tk.Toplevel()
        graph_window.title("Fuzzy Üyelik Fonksiyonları")
        graph_window.geometry("1200x800")

        fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(10, 10))
        fig.tight_layout(pad=5.0)

        temp_value = temp_c_global['value']
        result_text = result_label.cget("text")
        if "Tahmini Süre" in result_text:
            try:
                time_line = result_text.split("\n")[0]
                time_value = float(time_line.replace("Tahmini Süre:", "").replace("dk", "").strip())
            except:
                time_value = None
        else:
            time_value = None

        variables = [
            (meat_type, "Et Türü", meat_types.index(selected_meat.get())),
            (cooking_method, "Pişirme Yöntemi", cooking_methods.index(selected_method.get())),
            (cooking_pref, "Pişirme Tercihi", all_cooking_prefs.index(selected_pref.get())),
            (fat_level, "Yağ Oranı", fat_levels.index(selected_fat.get())),
            (thickness, "Et Kalınlığı (cm)", et_thickness.get()),
            (time, "Pişirme Süresi (dk)", time_value),
            (temp, "Sıcaklık (°C)", temp_value),
        ]

        for ax, (var, title, input_val) in zip(axes.flatten(), variables):
            x_vals = var.universe
            for term in var.terms:
                y_vals = var[term].mf
                ax.plot(x_vals, y_vals, label=term)
                ax.fill_between(x_vals, 0, y_vals, alpha=0.3)

            if input_val is not None:
                ax.axvline(x=input_val, color='red', linestyle='--', linewidth=2, label="Giriş Değeri")

            ax.set_title(title)
            ax.legend()
            ax.grid(True)

        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


    ttk.Button(root, text="Hesapla", command=calculate).grid(row=5, column=0, columnspan=2, pady=10)
    ttk.Button(root, text="Grafikleri Göster", command=show_graphs).grid(row=8, column=0, columnspan=2, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
