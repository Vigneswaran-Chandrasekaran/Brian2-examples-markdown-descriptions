# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **0.5 s**

**NeuronGroup(s) defined:**
- Name **neurongroup\_1**, with                population size **25**.

	**Dynamics:**

	Parameter <img src="https://render.githubusercontent.com/render/math?math=I">, where unit of <img src="https://render.githubusercontent.com/render/math?math=I"> is rad and linked as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} x">&#8592;<img src="https://render.githubusercontent.com/render/math?math=1.4142135623731.\sigma.\xi.\left(\frac{1}{\tau}\right)^{0.5} + \frac{0.5.I - x + 0.9}{\tau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=x"> is rad

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=x \gt 1">, <img src="https://render.githubusercontent.com/render/math?math=x">&#8592;<img src="https://render.githubusercontent.com/render/math?math=0">, with refractory <img src="https://render.githubusercontent.com/render/math?math=5. ms">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=\sigma">: <img src="https://render.githubusercontent.com/render/math?math=0.015">, <img src="https://render.githubusercontent.com/render/math?math=\tau">: <img src="https://render.githubusercontent.com/render/math?math=10. ms">

- Name **neurongroup**, with                population size **1**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} x">&#8592;<img src="https://render.githubusercontent.com/render/math?math=1.4142135623731.\xi.\left(\frac{1}{\tau_{input}}\right)^{0.5} - \frac{x}{\tau_{input}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=x"> is rad

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=\tau_{input}">: <img src="https://render.githubusercontent.com/render/math?math=5. ms">


**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=i">,<img src="https://render.githubusercontent.com/render/math?math=t"> of neurongroup_1. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=x"> of neurongroup_1 initialized with <img src="https://render.githubusercontent.com/render/math?math={rand}{\left(- \right)}"> to all members 

