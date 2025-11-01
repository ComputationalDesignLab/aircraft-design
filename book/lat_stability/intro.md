# Lateral stability

This section performs lateral stability analysis for the example airplane. This includes estimation of static stability derivatives and performing trim analysis for one-engine out condition. Refer to lecture notes and Section 16.4 in Raymer for further details. At the conceptual design phase, it is difficult to perform lateral analysis since it requires 6-DOF analysis, and hence, is limited to static stability derivative estimation, along with one engine-out and cross-wind landing/takeoff analysis (if possible).

Following topics are covered:

1. Static roll and yaw stability derivatives
2. One engine-out analysis

Before proceeding to above topics, it is important to define the size of the rudder. Note that the aileron size was defined in [HL devices section](../hl_devices/intro.md). The rudder chord ratio ($c_e/c$) is set to 40% based on the historical data in Table 8.3b in Roskam Part 2. For the analysis, it assumed that the rudder extends along the entire span. The rudder and aileron size can be later updated, if dictated by the stability and trim requirement. Note that aileron and rudder are essentially a plain flap, so the lift/force change can be computed using a similar analysis demonstrated for HL devices section.
