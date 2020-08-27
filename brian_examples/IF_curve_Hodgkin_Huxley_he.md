# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **2. s**

**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **100**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{I - g_{kd}.n^{4}.\left(- EK + v\right) - g_{na}.h.m^{3}.\left(- ENa + v\right) + gl.\left(El - v\right)}{Cm}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is V

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} n">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{0.5.n.e^{\frac{0.025.\left(VT + 10.0.mV - v\right)}{mV}}}{ms} + \frac{0.16.\left(1.0 - n\right)}{ms.{exprel}{\left(\frac{VT + 15.0.mV - v}{5.mV} \right)}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=n"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} m">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{1.4.m}{ms.{exprel}{\left(\frac{- VT - 40.0.mV + v}{5.mV} \right)}} + \frac{1.28.\left(1 - m\right)}{ms.{exprel}{\left(\frac{VT + 13.0.mV - v}{4.mV} \right)}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=m"> is rad

	Parameter <img src="https://render.githubusercontent.com/render/math?math=I">, where unit of <img src="https://render.githubusercontent.com/render/math?math=I"> is A

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} h">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{4.0.h}{ms.\left(e^{\frac{0.2.\left(VT + 40.0.mV - v\right)}{mV}} + 1\right)} + \frac{0.128.\left(1.0 - h\right).e^{\frac{0.0555555555555556.\left(VT + 17.0.mV - v\right)}{mV}}}{ms}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=h"> is rad

	exponential_euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt - 40.mV">, with refractory <img src="https://render.githubusercontent.com/render/math?math=v \gt - 40.mV">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=gl">: <img src="https://render.githubusercontent.com/render/math?math=10. nS">, <img src="https://render.githubusercontent.com/render/math?math=VT">: <img src="https://render.githubusercontent.com/render/math?math=-63. mV">, <img src="https://render.githubusercontent.com/render/math?math=ENa">: <img src="https://render.githubusercontent.com/render/math?math=50. mV">, <img src="https://render.githubusercontent.com/render/math?math=El">: <img src="https://render.githubusercontent.com/render/math?math=-65. mV">, <img src="https://render.githubusercontent.com/render/math?math=g_{na}">: <img src="https://render.githubusercontent.com/render/math?math=20. uS">, <img src="https://render.githubusercontent.com/render/math?math=Cm">: <img src="https://render.githubusercontent.com/render/math?math=200. pF">, <img src="https://render.githubusercontent.com/render/math?math=g_{kd}">: <img src="https://render.githubusercontent.com/render/math?math=6. uS">, <img src="https://render.githubusercontent.com/render/math?math=EK">: <img src="https://render.githubusercontent.com/render/math?math=-90. mV">


**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=t">,<img src="https://render.githubusercontent.com/render/math?math=i"> of neurongroup. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=v"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=-65. mV"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=I"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=\frac{0.7.i.nA}{num_{neurons}}"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=num_{neurons}">: <img src="https://render.githubusercontent.com/render/math?math=100">



