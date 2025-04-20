import tkinter as tk
from tkinter import simpledialog, scrolledtext

class TowerOfHanoi:
    def __init__(self, root, disks):
        self.root = root
        self.disks = disks
        self.colors = ["red", "green", "blue", "orange", "purple", "yellow", "pink", "cyan", "magenta", "lime"]
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack()
        
        self.move_list = []
        self.current_move = -1
        self.solve(disks, 0, 2, 1)

        self.poles = [[i for i in range(disks, 0, -1)], [], []]
        self.draw_poles()
        
        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack()

        self.prev_button = tk.Button(self.btn_frame, text="Previous", command=self.prev_move)
        self.prev_button.pack(side=tk.LEFT)

        self.next_button = tk.Button(self.btn_frame, text="Next", command=self.next_move)
        self.next_button.pack(side=tk.RIGHT)
        
        self.text_box = scrolledtext.ScrolledText(root, height=10)
        self.text_box.pack(fill=tk.BOTH, expand=True)
        self.display_moves()

    def draw_poles(self):
        self.canvas.delete("all")
        pole_height = 20 * (self.disks + 1)
        for i in range(3):
            self.canvas.create_line(200 * i + 100, 350 - pole_height, 200 * i + 100, 350, width=2)
        self.canvas.create_line(50, 350, 550, 350, width=2)
        for i in range(3):
            self.draw_disks(i)

    def draw_disks(self, pole):
        disk_height = 20
        for i, disk in enumerate(self.poles[pole]):
            color = self.colors[disk % len(self.colors)]
            x0 = 200 * pole + 100 - disk * 10
            y0 = 350 - disk_height * (i + 1)
            x1 = 200 * pole + 100 + disk * 10
            y1 = 350 - disk_height * i
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)

    def next_move(self):
        if self.current_move < len(self.move_list) - 1:
            self.current_move += 1
            from_pole, to_pole = self.move_list[self.current_move]
            disk = self.poles[from_pole].pop()
            self.poles[to_pole].append(disk)
            self.draw_poles()
            self.update_text_box()
            if self.current_move == len(self.move_list) - 1:
                self.next_button.config(text="Done", command=self.root.quit)

    def prev_move(self):
        if self.current_move >= 0:
            from_pole, to_pole = self.move_list[self.current_move]
            disk = self.poles[to_pole].pop()
            self.poles[from_pole].append(disk)
            self.current_move -= 1
            self.draw_poles()
            self.update_text_box()
            if self.next_button['text'] == "Done":
                self.next_button.config(text="Next", command=self.next_move)

    def solve(self, disks, from_pole, to_pole, aux_pole):
        if disks == 1:
            self.move_list.append((from_pole, to_pole))
            return
        self.solve(disks - 1, from_pole, aux_pole, to_pole)
        self.move_list.append((from_pole, to_pole))
        self.solve(disks - 1, aux_pole, to_pole, from_pole)

    def display_moves(self):
        self.text_box.delete('1.0', tk.END)
        for i, move in enumerate(self.move_list):
            self.text_box.insert(tk.END, f"Move disk from pole {move[0] + 1} to pole {move[1] + 1}\n")
        self.update_text_box()
        self.text_box.yview('1.0') 

    def update_text_box(self):
        self.text_box.tag_remove('highlight', '1.0', tk.END)
        if self.current_move >= 0:
            start_idx = f"{self.current_move + 1}.0"
            end_idx = f"{self.current_move + 2}.0"
            self.text_box.tag_add('highlight', start_idx, end_idx)
            self.text_box.tag_config('highlight', background='yellow')
            self.text_box.see(start_idx)  
        else:
            self.text_box.yview('1.0')  

root = tk.Tk()
root.withdraw()  
root.update()  
root.title("Tower of Hanoi Solver") 
num_disks = simpledialog.askinteger("Tower of Hanoi Solver", "How many disks?", minvalue=1, maxvalue=10)

if num_disks is not None:
    root.deiconify() 
    root.geometry("1000x600") 
    app = TowerOfHanoi(root, num_disks)
    root.mainloop()
else:
    root.destroy() 