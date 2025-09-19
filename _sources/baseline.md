# Initial Design Summary

Based on the results from initial weight estimation and constraint analysis, following table outlines some of the major important quantities for the example airplane:

<div style="width:90%; margin: auto;">

Parameter | Value | Source
--------- | :---: | :---:
Aspect ratio | 8 | Initial weight estimation (assumed)
Maximum takeoff weight | 5354 lbs | Initial weight estimation
Empty weight | 3094 lbs | Initial weight estimation
Fuel weight | 1060 lbs | Initial weight estimation
Takeoff Wing loading | 40 lbs/$\text{ft}^2$ | Constraint analysis
Takeoff Power loading | 9.25 lbs/hp | Constraint analysis
Wing surface area | 134 $\text{ft}^2$ | Calculated from W/S
Takeoff power | 595 hp | Calculated from W/P
Wing span | 33 ft | Calculated from $S$ and $A$
Maximum lift coeff. with no flaps, $C_{L_{max}}$ | 1.5 | Constraint analysis (assumed)
Maximum lift coeff. with takeoff flaps, $C_{L_{max_{TO}}}$ | 1.8 | Constraint analysis (assumed)
Maximum lift coeff. with landing flaps, $C_{L_{max_{L}}}$ | 2.2 | Constraint analysis (assumed)

</div>

> **_NOTE_**: The above estimates are based on the initial sizing process. These estimates can be further improved using carpet plots or by running numerical optimization.