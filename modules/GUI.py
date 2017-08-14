import tkinter as tk
import tkinter.font as tkFont

bg_color = "black"
border_color = "white"
txt_color = "white"
header_color = "yellow"

main_font = "helvetica"


root = tk.Tk()

fl_tire_temp = tk.IntVar()
fr_tire_temp = tk.IntVar()
rl_tire_temp = tk.IntVar()
rr_tire_temp = tk.IntVar()

aero_dmg = tk.IntVar()
engine_dmg = tk.IntVar()
water_temp = tk.IntVar()
oil_temp = tk.IntVar()

fuel = tk.DoubleVar()
fuel_laps_remain = tk.DoubleVar()

def update_variables(gData):
	fl_tire_temp.set(gData.FL_tire_temp_c())
	fr_tire_temp.set(gData.FR_tire_temp_c())
	rl_tire_temp.set(gData.RL_tire_temp_c())
	rr_tire_temp.set(gData.RR_tire_temp_c())

	water_temp.set(gData.waterTemp)
	oil_temp.set(gData.oilTemp)

	aero_dmg.set(gData.aero_damage)
	engine_dmg.set(gData.engine_damage)

	fuel.set(gData.fuel)

def quit(event):
	import sys
	sys.exit()

def root_setup(root):
	root.bind('<Escape>', quit)
	
	#Making background a grid of 1x1 (Space just for a frame)
	tk.Grid.rowconfigure(root, 0, weight=1)
	tk.Grid.columnconfigure(root, 0, weight=1)

	# Make it cover the entire screen (http://effbot.org/zone/tkinter-toplevel-fullscree$
	w, h = root.winfo_screenwidth(), root.winfo_screenheight()
	root.overrideredirect(1)
	root.geometry("%dx%d+0+0" % (w, h))

	#root.focus_set() # <-- move focus to this widget

class screenPCars:
	def __init__(self, master):
		frame = tk.Frame(master, borderwidth=1, bg=bg_color, highlightbackground=border_color, highlightthickness=1, relief=tk.SOLID, bd=0) #width=master.width, height=master.height,
		frame.grid(row=0, column=0, sticky='nsew')

		self.relief = tk.GROOVE
		self.font = main_font
		self.font = tkFont.Font(size = 15)

		#Configuring the grid in the frame
		for row_index in range(9):
			tk.Grid.rowconfigure(frame, row_index, weight=1)
			for col_index in range(16):
				tk.Grid.columnconfigure(frame, col_index, weight=1)
				#lbl = tk.Label(frame, text=str(col_index), font=self.font, bg=bg_color, fg=txt_color, borderwidth=1, highlightbackground=border_color, highlightthickness=1, relief=self.relief)
				#lbl.grid(row=row_index, column=col_index, sticky='nsew')

		#Setting up labels
		lbl_water_header = tk.Label(frame, text="Water T", font=self.font, bg=bg_color, fg=header_color, borderwidth=2)
		lbl_water_temp = tk.Label(frame, textvariable=water_temp, font=self.font, bg=bg_color, fg=txt_color, borderwidth=1, relief=self.relief)
		lbl_oil_header = tk.Label(frame, text="Oil T", font=self.font, bg=bg_color, fg=header_color, borderwidth=2)
		lbl_oil_temp = tk.Label(frame, textvariable=oil_temp, font=self.font, bg=bg_color, fg=txt_color, borderwidth=1, relief=self.relief)

		lbl_aero_header = tk.Label(frame, text="Aero Dmg", font=self.font, bg=bg_color, fg=header_color, borderwidth=2)
		lbl_aero_dmg = tk.Label(frame, textvariable=aero_dmg, font=self.font, bg=bg_color, fg=txt_color, borderwidth=1, relief=self.relief)
		lbl_engine_header = tk.Label(frame, text="Eng Dmg", font=self.font, bg=bg_color, fg=header_color, borderwidth=2)
		lbl_engine_dmg = tk.Label(frame, textvariable=engine_dmg, font=self.font, bg=bg_color, fg=txt_color, borderwidth=1, relief=self.relief)

		lbl_fuel_header = tk.Label(frame, text="Fuel", font=self.font, bg=bg_color, fg=header_color, borderwidth=2)
		lbl_fuel = tk.Label(frame, textvariable=fuel, font=self.font, bg=bg_color, fg=txt_color, borderwidth=1, relief=self.relief)
		lbl_fuel_remain_header = tk.Label(frame, text="Laps left", font=self.font, bg=bg_color, fg=header_color, borderwidth=2)
		lbl_fuel_remain = tk.Label(frame, textvariable=fuel_laps_remain, font=self.font, bg=bg_color, fg=txt_color, borderwidth=1, relief=self.relief)

		lbl_tire_temp_header = tk.Label(frame, text="Tire temps", font=self.font, bg=bg_color, fg=header_color, borderwidth=2)
		lbl_fl_tyre_temp = tk.Label(frame, textvariable=fl_tire_temp, font=self.font, bg=bg_color, fg=txt_color, borderwidth=1, relief=self.relief)
		lbl_fr_tyre_temp = tk.Label(frame, textvariable=fr_tire_temp, font=self.font, bg=bg_color, fg=txt_color, borderwidth=1, relief=self.relief)
		lbl_rl_tyre_temp = tk.Label(frame, textvariable=rl_tire_temp, font=self.font, bg=bg_color, fg=txt_color, borderwidth=1, relief=self.relief)
		lbl_rr_tyre_temp = tk.Label(frame, textvariable=rr_tire_temp, font=self.font, bg=bg_color, fg=txt_color, borderwidth=1, relief=self.relief)


		#Gridding the labels
		lbl_water_header.grid(row=0, column=13, columnspan=3, sticky='nsew')
		lbl_water_temp.grid(row=1, column=13, rowspan=2, columnspan=3, sticky='nsew')
		lbl_oil_header.grid(row=3, column=13, columnspan=3, sticky='nsew')
		lbl_oil_temp.grid(row=4, column=13, rowspan=2, columnspan=3, sticky='nsew')

		lbl_aero_header.grid(row=0, column=10, columnspan=3, sticky='nsew')
		lbl_aero_dmg.grid(row=1, column=10, rowspan=2, columnspan=3, sticky='nsew')
		lbl_engine_header.grid(row=3, column=10, columnspan=3, sticky='nsew')
		lbl_engine_dmg.grid(row=4, column=10, rowspan=2, columnspan=3, sticky='nsew')

		lbl_fuel_header.grid(row=0, column=0, columnspan=3, sticky='nsew')
		lbl_fuel.grid(row=1, column=0, rowspan=2, columnspan=3, sticky='nsew')
		lbl_fuel_remain.grid(row=3, column=0, rowspan=2, columnspan=3, sticky='nsew')

		lbl_tire_temp_header.grid(row=6, column=10, columnspan=6, sticky='nsew')
		lbl_fl_tyre_temp.grid(row=7, column=10, rowspan=1, columnspan=3, sticky='nsew')
		lbl_fr_tyre_temp.grid(row=7, column=13, rowspan=1, columnspan=3, sticky='nsew')
		lbl_rl_tyre_temp.grid(row=8, column=10, rowspan=1, columnspan=3, sticky='nsew')
		lbl_rr_tyre_temp.grid(row=8, column=13, rowspan=1, columnspan=3, sticky='nsew')

		self.labels = [lbl_water_header, lbl_water_temp, lbl_oil_header, lbl_oil_temp,
		lbl_aero_header, lbl_aero_dmg, lbl_engine_header, lbl_engine_dmg,
		lbl_fuel_header, lbl_fuel, lbl_fuel_remain, lbl_tire_temp_header,
		lbl_fl_tyre_temp, lbl_fr_tyre_temp, lbl_rl_tyre_temp, lbl_rr_tyre_temp]

		for lbl in self.labels:
			resizeFont(lbl)

		#frame.bind('<Configure>', self.resize)

	def resize(self, event):
			pass
			#resizeFont(self.lbl_fuel_remain)

def resizeFont(lbl):
	lblHeight = root.winfo_height()
	lblFont = tkFont.Font(size = 50)
	lbl.configure(font=lblFont)
	print (lblHeight)




'''
lbl_gearNum = tk.Label(root, textvariable=num, font=("System", 70, "bold"), fg="white", bg="$

lbl_gearNum.grid(row=0, column=0)

gui_setup()
root.after(500, method)
root.mainloop()
'''