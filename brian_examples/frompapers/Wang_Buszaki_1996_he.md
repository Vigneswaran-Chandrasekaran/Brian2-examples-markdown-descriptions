# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **100. ms**

**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **1**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\alpha_{m}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{1.0}{ms.{exprel}{\left(\frac{- 35.mV - v}{10.mV} \right)}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\alpha_{m}"> is Hz

	<img src="https://render.githubusercontent.com/render/math?math=\alpha_{n}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{0.1}{ms.{exprel}{\left(\frac{- 34.mV - v}{10.mV} \right)}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\alpha_{n}"> is Hz

	<img src="https://render.githubusercontent.com/render/math?math=\beta_{h}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{1.0}{ms.\left(1 + e^{- \frac{0.1.\left(28.mV + v\right)}{mV}}\right)}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\beta_{h}"> is Hz

	<img src="https://render.githubusercontent.com/render/math?math=\alpha_{h}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{0.07.e^{\frac{- 58.mV - v}{20.mV}}}{ms}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\alpha_{h}"> is Hz

	<img src="https://render.githubusercontent.com/render/math?math=m">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{\alpha_{m}}{\alpha_{m} + \beta_{m}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=m"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{Iapp - gK.n^{4}.\left(- EK + v\right) - gL.\left(- EL + v\right) - gNa.h.m^{3}.\left(- ENa + v\right)}{Cm}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is V

	<img src="https://render.githubusercontent.com/render/math?math=\beta_{m}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{4.e^{\frac{- 60.mV - v}{18.mV}}}{ms}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\beta_{m}"> is Hz

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} h">&#8592;<img src="https://render.githubusercontent.com/render/math?math=5.\alpha_{h}.\left(1 - h\right) - 5.\beta_{h}.h">, where unit of <img src="https://render.githubusercontent.com/render/math?math=h"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} n">&#8592;<img src="https://render.githubusercontent.com/render/math?math=5.\alpha_{n}.\left(1 - n\right) - 5.\beta_{n}.n">, where unit of <img src="https://render.githubusercontent.com/render/math?math=n"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\beta_{n}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{0.125.e^{\frac{- 44.mV - v}{80.mV}}}{ms}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\beta_{n}"> is Hz

	exponential_euler method is used for integration

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=gK">: <img src="https://render.githubusercontent.com/render/math?math=9. mS">, <img src="https://render.githubusercontent.com/render/math?math=gL">: <img src="https://render.githubusercontent.com/render/math?math=100. uS">, <img src="https://render.githubusercontent.com/render/math?math=EK">: <img src="https://render.githubusercontent.com/render/math?math=-90. mV">, <img src="https://render.githubusercontent.com/render/math?math=ENa">: <img src="https://render.githubusercontent.com/render/math?math=55. mV">, <img src="https://render.githubusercontent.com/render/math?math=gNa">: <img src="https://render.githubusercontent.com/render/math?math=35. mS">, <img src="https://render.githubusercontent.com/render/math?math=EL">: <img src="https://render.githubusercontent.com/render/math?math=-65. mV">, <img src="https://render.githubusercontent.com/render/math?math=Iapp">: <img src="https://render.githubusercontent.com/render/math?math=2. uA">, <img src="https://render.githubusercontent.com/render/math?math=Cm">: <img src="https://render.githubusercontent.com/render/math?math=1. uF">


**StateMonitor(s) defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=v"> of neurongroup, for member(s): 0 with time step <img src="https://render.githubusercontent.com/render/math?math=10. us">.


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=v"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=-70. mV"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=h"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=1."> to all members 

