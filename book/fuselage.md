# Fuselage Sizing

Fuselage sizing consists of determining the fuselage length, diameter, cross-sectional shape, aft upsweep angle, and cabin layout details such as seat width, seat pitch, aisle height, aisle width, etc. If desired, structural layout of the fuselage can also be defined. At this stage of the design, these quantities can be determined by looking at what other manufacturers have done. Refer to Chapter 2 in Roskam Part 2, Chapter 3 in Roskam Part 3, and Chapter 8 in Nicolai & Carichner for more details about fuselage sizing and historical data.

Fuselage produces most amount of drag on an airplane and its shape should be determined to reduce its drag as much as possible. The fuselage fineness ratio is defined as the ratio of the fuselage length ($l_f$) to its diamter ($l_d$), which governs the fuselage friction drag. The profile drag for a fuselage is governed by the aft body fineness ratio which is defined as the ratio of the fuselage tail cone length ($l_{fc}$) to the fuselage diameter. The fuselage upsweep angle ($\theta_{fc}$) can also effect the profile drag. Refer to Section 3.1 Roskam Part 3 for a detailed discussion on the affects of various parameters on the fuselage drag. The value of these parameters can be determined so that fuselage's drag decreases. Table 4.1 in Roskam Part 2 provides historical guidelines for determining these parameters.

Fuselage width depends on the cabin arrangement. The example airplane will consists of two abreast seating - two cockpit seats and four cabin seats. Since the cabin does not have to be pressurized, the fuselage cross-section consists of two semi-circles which are connected by two small flat sections (rounded rectanlges with larger corner radius). The cabin height is set to 5.5 ft and the cabin width is 5 ft. With the recommended fuselage structural depth of 1.5 in, the final fuselage width and height are 5.25 ft and 6.5 ft, respectively. The seat dimensions are determined using the guidelines provides in Table 3.1 in Roskam Part 3.

Following table outlines the value of various fusealge variables for the example airplane:

<div style="width:70%; margin: auto;">

Parameter | Value | Source
------ | :-----: | :----:
Fuselage fineness ratio | 6 | Table 4.1 Roskam Part 2
Aft body fineness ratio | 2.7 | Table 4.1 Roskam Part 2
Upsweep angle | $10^{\circ}$ | Table 4.1 Roskam Part 2
Structural depth of fuselage | 1.5 in | Section 4.1 Roskam Part 2
Fuselage height | 6.5 ft | Historical data
Fuselage width | 5.25 ft | Historical data
Fuselage length | 39 ft | Calculated
Fuselage cone length | 16.2 ft | Calculated
Seat pitch | 3 ft | Historical data
Seat height | 3.5 ft | Historical data
Seat width | 1.75 ft | Historical data
</div>

Below image shows cabin layout in a simple OpenVSP model:

<div style="width:80%; margin: auto;">

![logos](images/fuselage.png)
</div>

> __*NOTE:*__ It is recommended to create simple OpenVSP model as shown above to check if the seat and cabin are of appropriately size. The cabin size will dictate the fuselage width, which in turn will govern the fuselage length.

This concludes the fuselage sizing for initial design. But it can be further refined by including more details about fuselage structural design, refer to Chapter 3 in Roskam Part 3.
