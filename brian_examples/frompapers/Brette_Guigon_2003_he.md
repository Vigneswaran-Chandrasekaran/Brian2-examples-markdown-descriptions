# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **1. s**

**StateMonitor(s) defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=B"> of neurongroup_1, for member(s): 0 with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">.


**NeuronGroup(s) defined:**
- Name **neurongroup\_1**, with                population size **500**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=1.4142135623731.\sigma.\xi.\left(\frac{1}{\tau}\right)^{0.5} + \frac{I.v + 1}{\tau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is rad

	Parameter <img src="https://render.githubusercontent.com/render/math?math=x">, where unit of <img src="https://render.githubusercontent.com/render/math?math=x"> is rad and linked as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=I">&#8592;<img src="https://render.githubusercontent.com/render/math?math=3.B.p + 0.5">, where unit of <img src="https://render.githubusercontent.com/render/math?math=I"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=B">&#8592;<img src="https://render.githubusercontent.com/render/math?math=-1 + \frac{2.0}{1 + e^{- 2.x}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=B"> is rad and shared as flag(s) associated

	Parameter <img src="https://render.githubusercontent.com/render/math?math=p">, where unit of <img src="https://render.githubusercontent.com/render/math?math=p"> is rad

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt 1">, <img src="https://render.githubusercontent.com/render/math?math=v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=0">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=\sigma">: <img src="https://render.githubusercontent.com/render/math?math=0.02">, <img src="https://render.githubusercontent.com/render/math?math=\tau">: <img src="https://render.githubusercontent.com/render/math?math=33. ms">

- Name **neurongroup**, with                population size **1**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} x">&#8592;<img src="https://render.githubusercontent.com/render/math?math=1.4142135623731.\xi.\left(\frac{1}{taux}\right)^{0.5} - \frac{x}{taux}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=x"> is rad

	euler method is used for integration

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=taux">: <img src="https://render.githubusercontent.com/render/math?math=20. ms">


**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=i">,<img src="https://render.githubusercontent.com/render/math?math=t"> of neurongroup_1. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=p"> of neurongroup_1 initialized with <img src="https://render.githubusercontent.com/render/math?math=\frac{1.0.i}{N}"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=N">: <img src="https://render.githubusercontent.com/render/math?math=500">



- Variable <img src="https://render.githubusercontent.com/render/math?math=v"> of neurongroup_1 initialized with <img src="https://render.githubusercontent.com/render/math?math={rand}{\left(- \right)}"> to all members 

