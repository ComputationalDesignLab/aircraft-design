# Code setup

This section describes the code used for computing the MTOW for a given wing loading, power loading, and aspect ratio. The code is divided into three modules. The first module defines a dataclass which contains all the parameter values for the airplane. The second and third modules defines a set of functions for computing fuel and empty weight fractions, respectively. These modules are described in following sub-sections:

1. Parameters
2. Fuel estimation
3. Empty weight estimation

Refer to the above sections for more details about the modules.

<!-- > __NOTE__: If jupyter notebooks are going to be used, then jdc and nbimporter is required. Use ``pip install jdc`` and ``pip install nbimporter``. -->

<!-- As described in previous section, the iterative process starts with a guess value for MTOW. Then, fuel fractio and empty weight fraction are computed. This is then used to compute MOTW, which is compared with the guess value. This process continues untill 

This structure is followed for every pair of $W/S$ and $W/P$ -->