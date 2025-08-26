import numpy as np
import matplotlib.pyplot as plt

# Varibles
A = 8
n_p = 0.8

CL_max_clean = 1.5
CD0_clean = 0.028
e_clean = 0.81

CL_max_to = 1.8
CL_max_l = 2.2
rho_sea_level = 0.002387 # slugs/cu. ft
rho_5000 = 0.00204834 # slugs/cu. ft

######## Takeoff

s_to = 2500 # ft

a = 0.0149
b = 8.134
c = -s_to

top_23_1 = (-b + np.sqrt(b**2 - 4*a*c)) / 2 / a
top_23_2 = (-b - np.sqrt(b**2 - 4*a*c)) / 2 / a
top_23 = top_23_1

######## Landing

s_land = 3000 # ft

v_sl = (s_land/0.5136)**0.5 # in knots
v_sl = v_sl * 1.68781 # in ft/s

######## Climb - AEO

cgr = 0.083
sigma = 1
CL_climb = CL_max_to - 0.2
CD0 = CD0_clean + 0.015
e = e_clean - 0.05

CD_climb = CD0 + CL_climb**2/np.pi/A/e

L_by_D = CL_climb / CD_climb

cgrp_aeo = ( cgr + L_by_D**(-1) ) / CL_climb**0.5

######## Climb - OEI

cgr = 0.015
CL_climb = CL_max_clean - 0.2
CD0 = CD0_clean
e = e_clean

CD_climb = CD0 + CL_climb**2/np.pi/A/e

L_by_D = CL_climb / CD_climb

cgrp_oei = ( cgr + L_by_D**(-1) ) / CL_climb**0.5

###### Climb blanked landing

cgr = 0.03
CL_climb = CL_max_l - 0.2
CD0 = CD0_clean + 0.065 + 0.020
e = e_clean - 0.1

CD_climb = CD0 + CL_climb**2/np.pi/A/e

L_by_D = CL_climb / CD_climb

cgrp_bl = ( cgr + L_by_D**(-1) ) / CL_climb**0.5

######## Plotting

fs = 14
num_pts = 15
wing_loading = np.linspace(5, 50, num_pts) # lb/ft^2
power_loading = np.linspace(5, 30, num_pts) # lb/hp

X, Y = np.meshgrid(wing_loading, power_loading)

takeoff_data = X * Y / CL_max_to - top_23 # takeoff

landing_data = X * 2 / rho_sea_level / CL_max_l - v_sl**2 # landing

cgr_aeo_data = Y * X**0.5 - 18.97 * n_p / cgrp_aeo # climb aeo

cgr_oei_data = Y * X**0.5 - 18.97 * n_p * rho_5000 / rho_sea_level / cgrp_oei # climb oei

cgr_bl_data = Y * X**0.5 - 18.97 * n_p / cgrp_bl # climb bl

cruise_speed_data = Y * 3.856 - X # cruise speed

fig, ax = plt.subplots(figsize=(8,6))

cs = ax.contour(wing_loading, power_loading, takeoff_data, colors="k", levels=[0])#, levels=[-1e-2,1e-2], label="Take-off")

ax.clabel(cs, fmt="Takeoff", fontsize=fs-2)

cs = ax.contour(wing_loading, power_loading, landing_data, colors="r", levels=[0])#, levels=[-1e-2,1e-2], label="Take-off")

ax.clabel(cs, fmt="Landing", fontsize=fs-2)

cs = ax.contour(wing_loading, power_loading, cgr_aeo_data, colors="g", levels=[0])#, levels=[-1e-2,1e-2], label="Take-off")

ax.clabel(cs, fmt="Climb AEO", fontsize=fs-2)

cs = ax.contour(wing_loading, power_loading, cgr_oei_data, colors="b", levels=[0])#, levels=[-1e-2,1e-2], label="Take-off")

ax.clabel(cs, fmt="Climb OEI", fontsize=fs-2)

cs = ax.contour(wing_loading, power_loading, cgr_bl_data, colors="c", levels=[0])#, levels=[-1e-2,1e-2], label="Take-off")

ax.clabel(cs, fmt="Climb BL", fontsize=fs-2)

cs = ax.contour(wing_loading, power_loading, cruise_speed_data, colors="c", levels=[0])#, levels=[-1e-2,1e-2], label="Take-off")

ax.clabel(cs, fmt="Cruise Speed", fontsize=fs-2)

ax.set_xlabel("Wing Loading ($W/S$) [lbs/$ft^2$]")

ax.set_ylabel("Power Loading ($W/P$) [lbs/hp]")

ax.legend(fontsize=fs)

plt.tight_layout()

plt.show()
