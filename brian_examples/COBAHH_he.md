# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **1. s**

**Synapses defined:**
- 	From neurongroup_subgroup_1 to neurongroup

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=gi">+=<img src="https://render.githubusercontent.com/render/math?math=wi"> is executed

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=wi">: <img src="https://render.githubusercontent.com/render/math?math=67. nS">

- 	From neurongroup_subgroup to neurongroup

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=ge">+=<img src="https://render.githubusercontent.com/render/math?math=we"> is executed

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=we">: <img src="https://render.githubusercontent.com/render/math?math=6. nS">


**StateMonitor(s) defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=v"> of neurongroup, for member(s): 1,10,100 with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">.


**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **4000**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\alpha_{n}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{0.16}{ms.{exprel}{\left(\frac{VT + 15.mV - v}{5.mV} \right)}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\alpha_{n}"> is Hz

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} m">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\alpha_{m}.\left(1 - m\right) - \beta_{m}.m">, where unit of <img src="https://render.githubusercontent.com/render/math?math=m"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} gi">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{1.0.gi}{taui}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=gi"> is S

	<img src="https://render.githubusercontent.com/render/math?math=\beta_{m}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{1.4}{ms.{exprel}{\left(\frac{- VT - 40.mV + v}{5.mV} \right)}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\beta_{m}"> is Hz

	<img src="https://render.githubusercontent.com/render/math?math=\alpha_{m}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{1.28}{ms.{exprel}{\left(\frac{VT + 13.mV - v}{4.mV} \right)}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\alpha_{m}"> is Hz

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} ge">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{1.0.ge}{taue}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ge"> is S

	<img src="https://render.githubusercontent.com/render/math?math=\alpha_{h}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{0.128.e^{\frac{VT + 17.mV - v}{18.mV}}}{ms}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\alpha_{h}"> is Hz

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} h">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\alpha_{h}.\left(1 - h\right) - \beta_{h}.h">, where unit of <img src="https://render.githubusercontent.com/render/math?math=h"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} n">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\alpha_{n}.\left(1 - n\right) - \beta_{n}.n">, where unit of <img src="https://render.githubusercontent.com/render/math?math=n"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{- g_{kd}.n^{4}.\left(- EK + v\right) - g_{na}.h.m^{3}.\left(- ENa + v\right) + ge.\left(Ee - v\right) + gi.\left(Ei - v\right) + gl.\left(El - v\right)}{Cm}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is V

	<img src="https://render.githubusercontent.com/render/math?math=\beta_{h}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{4.0}{ms.\left(e^{\frac{VT + 40.mV - v}{5.mV}} + 1\right)}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\beta_{h}"> is Hz

	<img src="https://render.githubusercontent.com/render/math?math=\beta_{n}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{0.5.e^{\frac{VT + 10.mV - v}{40.mV}}}{ms}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\beta_{n}"> is Hz

	exponential_euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt - 20.mV">, with refractory <img src="https://render.githubusercontent.com/render/math?math=3. ms">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=El">: <img src="https://render.githubusercontent.com/render/math?math=-60. mV">, <img src="https://render.githubusercontent.com/render/math?math=Ei">: <img src="https://render.githubusercontent.com/render/math?math=-80. mV">, <img src="https://render.githubusercontent.com/render/math?math=VT">: <img src="https://render.githubusercontent.com/render/math?math=-63. mV">, <img src="https://render.githubusercontent.com/render/math?math=Ee">: <img src="https://render.githubusercontent.com/render/math?math=0. V">, <img src="https://render.githubusercontent.com/render/math?math=taui">: <img src="https://render.githubusercontent.com/render/math?math=10. ms">, <img src="https://render.githubusercontent.com/render/math?math=taue">: <img src="https://render.githubusercontent.com/render/math?math=5. ms">, <img src="https://render.githubusercontent.com/render/math?math=EK">: <img src="https://render.githubusercontent.com/render/math?math=-90. mV">, <img src="https://render.githubusercontent.com/render/math?math=g_{na}">: <img src="https://render.githubusercontent.com/render/math?math=20. uS">, <img src="https://render.githubusercontent.com/render/math?math=gl">: <img src="https://render.githubusercontent.com/render/math?math=10. nS">, <img src="https://render.githubusercontent.com/render/math?math=ENa">: <img src="https://render.githubusercontent.com/render/math?math=50. mV">, <img src="https://render.githubusercontent.com/render/math?math=g_{kd}">: <img src="https://render.githubusercontent.com/render/math?math=6. uS">, <img src="https://render.githubusercontent.com/render/math?math=Cm">: <img src="https://render.githubusercontent.com/render/math?math=200. pF">


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=v"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=El + mV.\left(5.{randn}{\left(- \right)} - 5\right)"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=El">: <img src="https://render.githubusercontent.com/render/math?math=-60. mV">



- Variable <img src="https://render.githubusercontent.com/render/math?math=ge"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=nS.\left(15.0.{randn}{\left(- \right)} + 40.0\right)"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=gi"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=nS.\left(120.0.{randn}{\left(- \right)} + 200.0\right)"> to all members 


**Synaptic Connection(s) defined:**
- Connection from neurongroup_subgroup to neurongroup, with probabilty <img src="https://render.githubusercontent.com/render/math?math=0.02">

- Connection from neurongroup_subgroup_1 to neurongroup, with probabilty <img src="https://render.githubusercontent.com/render/math?math=0.02">

