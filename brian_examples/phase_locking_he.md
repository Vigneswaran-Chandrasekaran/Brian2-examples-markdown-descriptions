# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **1. s**

**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **100**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{a.\sin{\left(2.\pi.freq.t \right)} + b - v}{\tau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is rad

	Parameter <img src="https://render.githubusercontent.com/render/math?math=a">, where unit of <img src="https://render.githubusercontent.com/render/math?math=a"> is rad

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt 1">, <img src="https://render.githubusercontent.com/render/math?math=v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=0">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=freq">: <img src="https://render.githubusercontent.com/render/math?math=10. Hz">, <img src="https://render.githubusercontent.com/render/math?math=\tau">: <img src="https://render.githubusercontent.com/render/math?math=20. ms">, <img src="https://render.githubusercontent.com/render/math?math=b">: <img src="https://render.githubusercontent.com/render/math?math=1.2">


**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=i">,<img src="https://render.githubusercontent.com/render/math?math=t"> of neurongroup. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.


**StateMonitor(s) defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=v"> of neurongroup, for member(s): 50 with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">.


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=v"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math={rand}{\left(- \right)}"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=a"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=\frac{0.7.i}{n} + 0.05"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=n">: <img src="https://render.githubusercontent.com/render/math?math=100">



