import tkinter as tk
import tkinter.font as tkFont

bg_color = 'black'
border_color = 'white'
txt_color = 'white'
header_color = 'yellow'


root = tk.Tk()

main_font = tkFont.Font(family='Helvetica', size=12, weight='bold')
small_font = tkFont.Font(family='Helvetica', size=int(main_font['size']*2), weight='bold')

gear_num = tk.StringVar()

fl_tire_temp = tk.IntVar()
fr_tire_temp = tk.IntVar()
rl_tire_temp = tk.IntVar()
rr_tire_temp = tk.IntVar()

aero_dmg = tk.IntVar()
engine_dmg = tk.IntVar()
water_temp = tk.IntVar()
oil_temp = tk.IntVar()

fuel = tk.StringVar()
fuel_laps_remain = tk.StringVar()

def update_variables(gData):
	gear_num.set(gData.gear)

	fl_tire_temp.set(gData.FL_tire_temp_c())
	fr_tire_temp.set(gData.FR_tire_temp_c())
	rl_tire_temp.set(gData.RL_tire_temp_c())
	rr_tire_temp.set(gData.RR_tire_temp_c())

	water_temp.set(gData.waterTemp)
	oil_temp.set(gData.oilTemp)

	aero_dmg.set(gData.aero_damage)
	engine_dmg.set(gData.engine_damage)

	fuel.set('{:.2f}'.format(gData.curr_fuel()))

def quit(event):
	root.quit()
	root.destroy()
	#import sys
	#sys.exit()

def get_window_dimensions():
	return root.winfo_screenwidth(), root.winfo_screenheight()

def root_setup(root):
	root.bind('<Escape>', quit)
	
	#Making background a grid of 1x1 (Space just for a frame)
	tk.Grid.rowconfigure(root, 0, weight=1)
	tk.Grid.columnconfigure(root, 0, weight=1)

	# Make it cover the entire screen (http://effbot.org/zone/tkinter-toplevel-fullscree$
	w, h = get_window_dimensions()
	root.overrideredirect(1)
	root.geometry('%dx%d+0+0' % (w, h))

	#root.focus_set() # <-- move focus to this widget

class screenPCars:
	def __init__(self, master):
		frame = tk.Frame(master, borderwidth=1, bg=bg_color, highlightbackground=border_color, highlightthickness=1, relief=tk.SOLID, bd=0) #width=master.width, height=master.height,
		frame.grid(row=0, column=0, sticky='nsew')
		
		self.relief = tk.GROOVE
		self.font = main_font
		
		#Configuring the grid in the frame
		configure_grid(frame, 9, 16)

		fuel_frame = self.make_fuel_frame(frame)
		fuel_frame.grid(row=0, column=0, rowspan=5, columnspan=3, sticky='nsew')
		
		water_t_frame = self.make_water_temperature_frame(frame)
		water_t_frame.grid(row=0, column=13, rowspan=3, columnspan=3, sticky='nsew')
		oil_t_frame = self.make_oil_temperature_frame(frame)
		oil_t_frame.grid(row=3, column=13, rowspan=3, columnspan=3, sticky='nsew')

		engine_dmg_frame = self.make_engine_damage_frame(frame)
		engine_dmg_frame.grid(row=5, column=0, rowspan=2, columnspan=3, sticky='nsew')
		aero_dmg_frame = self.make_aero_damage_frame(frame)
		aero_dmg_frame.grid(row=7, column=0, rowspan=2, columnspan=3, sticky='nsew')

		tire_temps_frame = self.make_tire_temperature_frame(frame)
		tire_temps_frame.grid(row=6, column=10, rowspan=3, columnspan=6, sticky='nsew')

		gear_frame = self.make_gear_frame(frame)
		gear_frame.grid(row=0, column=8, rowspan=6, columnspan=2, sticky='nsew')

		#frame.bind('<Configure>', self.resize)

		resizeFont()

	def make_tire_temperature_frame(self, master):
		frame = tk.Frame(master, borderwidth=1, bg=bg_color, highlightbackground=border_color, highlightthickness=1, relief=tk.SOLID, bd=0)
		configure_grid(frame, 3, 6)

		lbl_tire_temp_header = tk.Label(frame, text='Tire temps', font=self.font, bg=bg_color, fg=header_color, borderwidth=2)
		lbl_fl_tyre_temp = tk.Label(frame, textvariable=fl_tire_temp, font=self.font, bg=bg_color, fg=txt_color, borderwidth=1, relief=self.relief)
		lbl_fr_tyre_temp = tk.Label(frame, textvariable=fr_tire_temp, font=self.font, bg=bg_color, fg=txt_color, borderwidth=1, relief=self.relief)
		lbl_rl_tyre_temp = tk.Label(frame, textvariable=rl_tire_temp, font=self.font, bg=bg_color, fg=txt_color, borderwidth=1, relief=self.relief)
		lbl_rr_tyre_temp = tk.Label(frame, textvariable=rr_tire_temp, font=self.font, bg=bg_color, fg=txt_color, borderwidth=1, relief=self.relief)

		lbl_tire_temp_header.grid(row=0, column=0, columnspan=6, sticky='nsew')
		lbl_fl_tyre_temp.grid(row=1, column=0, rowspan=1, columnspan=3, sticky='nsew')
		lbl_fr_tyre_temp.grid(row=1, column=3, rowspan=1, columnspan=3, sticky='nsew')
		lbl_rl_tyre_temp.grid(row=2, column=0, rowspan=1, columnspan=3, sticky='nsew')
		lbl_rr_tyre_temp.grid(row=2, column=3, rowspan=1, columnspan=3, sticky='nsew')

		return frame

	def make_fuel_frame(self, master):
		frame = tk.Frame(master, borderwidth=1, bg=bg_color, highlightbackground=border_color, highlightthickness=1, relief=tk.SOLID, bd=0)
		configure_grid(frame, 5, 3)

		lbl_fuel_header = tk.Label(frame, text='Fuel', font=self.font, bg=bg_color, fg=header_color, borderwidth=2)
		lbl_fuel = tk.Label(frame, textvariable=fuel, font=self.font, bg=bg_color, fg=txt_color, borderwidth=1, relief=self.relief)
		lbl_fuel_remain_header = tk.Label(frame, text='Laps left', font=self.font, bg=bg_color, fg=header_color, borderwidth=2)
		lbl_fuel_remain = tk.Label(frame, textvariable=fuel_laps_remain, font=self.font, bg=bg_color, fg=txt_color, borderwidth=1, relief=self.relief)

		lbl_fuel_header.grid(row=0, column=0, columnspan=3, sticky='nsew')
		lbl_fuel.grid(row=1, column=0, rowspan=2, columnspan=3, sticky='nsew')
		lbl_fuel_remain.grid(row=3, column=0, rowspan=2, columnspan=3, sticky='nsew')

		return frame


	def make_aero_damage_frame(self, master):
		frame = tk.Frame(master, borderwidth=1, bg=bg_color, highlightbackground=border_color, highlightthickness=1, relief=tk.SOLID, bd=0)
		configure_grid(frame, 2, 3)

		lbl_aero_header = tk.Label(frame, text='Aero Dmg', font=self.font, bg=bg_color, fg=header_color, borderwidth=2)
		lbl_aero_dmg = tk.Label(frame, textvariable=aero_dmg, font=self.font, bg=bg_color, fg=txt_color, borderwidth=1, relief=self.relief)

		lbl_aero_header.grid(row=0, column=0, columnspan=3, sticky='nsew')
		lbl_aero_dmg.grid(row=1, column=0, columnspan=3, sticky='nsew')

		return frame


	def make_engine_damage_frame(self, master):
		frame = tk.Frame(master, borderwidth=1, bg=bg_color, highlightbackground=border_color, highlightthickness=1, relief=tk.SOLID, bd=0)
		configure_grid(frame, 2, 3)

		lbl_engine_header = tk.Label(frame, text='Eng Dmg', font=self.font, bg=bg_color, fg=header_color, borderwidth=2)
		lbl_engine_dmg = tk.Label(frame, textvariable=engine_dmg, font=self.font, bg=bg_color, fg=txt_color, borderwidth=1, relief=self.relief)

		lbl_engine_header.grid(row=0, column=0, columnspan=3, sticky='nsew')
		lbl_engine_dmg.grid(row=1, column=0, columnspan=3, sticky='nsew')

		return frame


	def make_water_temperature_frame(self, master):
		frame = tk.Frame(master, borderwidth=1, bg=bg_color, highlightbackground=border_color, highlightthickness=1, relief=tk.SOLID, bd=0)
		configure_grid(frame, 3, 3)

		lbl_water_header = tk.Label(frame, text='Water T', font=self.font, bg=bg_color, fg=header_color, borderwidth=2)
		lbl_water_temp = tk.Label(frame, textvariable=water_temp, font=self.font, bg=bg_color, fg=txt_color, borderwidth=1, relief=self.relief)

		lbl_water_header.grid(row=0, column=0, columnspan=3, sticky='nsew')
		lbl_water_temp.grid(row=1, column=0, rowspan=2, columnspan=3, sticky='nsew')

		return frame


	def make_oil_temperature_frame(self, master):
		frame = tk.Frame(master, borderwidth=1, bg=bg_color, highlightbackground=border_color, highlightthickness=1, relief=tk.SOLID, bd=0)
		configure_grid(frame, 3, 3)

		lbl_oil_header = tk.Label(frame, text='Oil T', font=self.font, bg=bg_color, fg=header_color, borderwidth=2)
		lbl_oil_temp = tk.Label(frame, textvariable=oil_temp, font=self.font, bg=bg_color, fg=txt_color, borderwidth=1, relief=self.relief)

		lbl_oil_header.grid(row=0, column=0, columnspan=3, sticky='nsew')
		lbl_oil_temp.grid(row=1, column=0, rowspan=2, columnspan=3, sticky='nsew')

		return frame


	def make_gear_frame(self, master):
		frame = tk.Frame(master, borderwidth=1, bg=bg_color, highlightbackground=border_color, highlightthickness=1, relief=tk.SOLID, bd=0)
		configure_grid(frame, 6, 1)

		lbl_gear_header = tk.Label(frame, text='Gear', font=self.font, bg=bg_color, fg=header_color, borderwidth=2)
		lbl_gear_num = tk.Label(frame, textvariable=gear_num, font=self.font, bg=bg_color, fg=txt_color, borderwidth=1, relief=self.relief)

		lbl_gear_header.grid(row=0, column=0, sticky='nsew')
		lbl_gear_num.grid(row=1, column=0, rowspan=5, sticky='nsew')

		return frame


	def resize(self, event):
			pass
			#resizeFont(self.lbl_fuel_remain)

def resizeFont():
	winW, winH = get_window_dimensions()

	main_font.configure(size=40)

	'''
	lblFont = tkFont.Font(family='Helvetica', size=50, weight='bold')
	lbl.configure(font=lblFont)
	print (lblHeight)
	'''

def configure_grid(frame, rows, columns):
	for row_index in range(rows):
		tk.Grid.rowconfigure(frame, row_index, weight=1)
		for col_index in range(columns):
			tk.Grid.columnconfigure(frame, col_index, weight=1)