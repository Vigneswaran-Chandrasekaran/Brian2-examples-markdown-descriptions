# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **0.5 s**

**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=t">,<img src="https://render.githubusercontent.com/render/math?math=i"> of neurongroup_1. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.

- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=t">,<img src="https://render.githubusercontent.com/render/math?math=i"> of neurongroup. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.


**Synapses defined:**
- 	From neurongroup to neurongroup_1

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=y">+=<img src="https://render.githubusercontent.com/render/math?math=wex"> is executed

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=wex">: <img src="https://render.githubusercontent.com/render/math?math=7">

- 	From neurongroup to neurongroup_1

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=y">+=<img src="https://render.githubusercontent.com/render/math?math=winh"> is executed, with synaptic delay of <img src="https://render.githubusercontent.com/render/math?math=0.7 ms">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=winh">: <img src="https://render.githubusercontent.com/render/math?math=-2">


**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **8**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=1.4142135623731.\sigma.\xi.\left(\frac{1}{\tau_{legs}}\right)^{0.5} + \frac{- v + {rates}{\left(- d + t \right)} + 1}{\tau_{legs}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is rad

	Parameter <img src="https://render.githubusercontent.com/render/math?math=d">, where unit of <img src="https://render.githubusercontent.com/render/math?math=d"> is s

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt 1">, <img src="https://render.githubusercontent.com/render/math?math=v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=0">, with refractory <img src="https://render.githubusercontent.com/render/math?math=1. ms">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=rates"> of type timedarray with dimentsion <img src="https://render.githubusercontent.com/render/math?math=1"> and dt as <img src="https://render.githubusercontent.com/render/math?math=0.0001 s">, <img src="https://render.githubusercontent.com/render/math?math=\tau_{legs}">: <img src="https://render.githubusercontent.com/render/math?math=1. ms">, <img src="https://render.githubusercontent.com/render/math?math=\sigma">: <img src="https://render.githubusercontent.com/render/math?math=0.01">

- Name **neurongroup\_1**, with                population size **8**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} y">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{y}{taus}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=y"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} x">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{- x + y}{taus}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=x"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{- v + x}{\tau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is rad

	exact method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt 1">, <img src="https://render.githubusercontent.com/render/math?math=v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=0">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=taus">: <img src="https://render.githubusercontent.com/render/math?math=1.001 ms">, <img src="https://render.githubusercontent.com/render/math?math=\tau">: <img src="https://render.githubusercontent.com/render/math?math=1. ms">


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=d"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=[761.24928236 383.27731807  73.67991782  13.8150398  238.75071764
 616.72268193 926.32008218 986.1849602 ] us"> to all members 


**Synaptic Connection(s) defined:**
- Connection from neurongroup to neurongroup_1. Connection for all members in source group to target group with generator syntax i

- Connection from neurongroup to neurongroup_1 with condition <img src="https://render.githubusercontent.com/render/math?math=\left|{- \frac{N_{post}}{2} + \left(\left(- i + j\right)\bmod{N_{post}}\right)}\right| \leq 1">. Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=N_{post}">: <img src="https://render.githubusercontent.com/render/math?math=8">



