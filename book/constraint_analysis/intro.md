# Constraint Analysis

For any airplane, the wing loading ($W/S$) and power loading ($W/P$) (or thrust loading ($T/W$) in case of jet airplanes) are important parameters that determine its performance. This section demonstrates constraint analysis method for estimating $W/S$ and $W/P$. Note that $W/P$ is used in this section instead of $T/W$ since the example aircraft is propeller driven. The constraint analysis method involves identifying feasible region in the $W/S$ and $W/P$ design space under various performance constraints, and then selecting appropriate values for wing and power loading in the feasible region. Refer to the lecture notes for more details. In this section, constraint analysis is demonstrated using the example aircraft. Following performance requirements are used within constraint analysis:

- Takeoff distance
- Landing distance
- Climb gradient
- Cruise speed

The takeoff distance, landing distance and cruise speed are mentioned in the [example aircraft specifications](example_aircraft.md), while the climb gradient is included to satisfy 14 CFR Part 23 requirements. If desired or required by RFP, other requirements such as service ceiling and turn rates can also be included, refer to lecture notes or any of the aircraft design books for more details. 

> **_NOTE_:** There is no stall speed requirement according to the latest 14 CFR Part 23, one has to only determine the value of stall speed. Additionally, there is no rate of climb requirement.

Before computing feasible region for any of the performance constraints, additional data is required which can be obtained from historical data for similar aircraft. Following table outlines this data:

Parameter | Value | Source
--------- | :---: | :---:
Aspect ratio, $A$ | 8 | From initial sizing section
Propeller efficiency, $\eta_P$ | 0.8 | Raymer and Roskam
Maximum lift coeff. with no flaps, $C_{L_{max}}$ | 1.5 | Roskam Part 1, Table 3.1
Maximum lift coeff. with takeoff flaps, $C_{L_{max_{TO}}}$ | 1.8 | Roskam Part 1, Table 3.1
Maximum lift coeff. with landing flaps, $C_{L_{max_{L}}}$ | 2.2 | Roskam Part 1, Table 3.1
Oswald efficiency factor with no flaps, $e$ | 0.81 | From initial sizing section
Zero-lift drag coeff., $C_{D_0}$ | 0.028 | From initial sizing section
