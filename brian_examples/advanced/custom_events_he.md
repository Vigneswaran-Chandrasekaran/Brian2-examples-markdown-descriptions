# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **0.5 s**

**Synapses defined:**
- 	From neurongroup to neurongroup_1

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=x">+=<img src="https://render.githubusercontent.com/render/math?math=1"> is executed

	On **pre** of event gspike statement(s): <img src="https://render.githubusercontent.com/render/math?math=y">+=<img src="https://render.githubusercontent.com/render/math?math=1"> is executed

- 	From poissongroup to neurongroup

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=g">+=<img src="https://render.githubusercontent.com/render/math?math=0.5"> is executed


**PoissonGroup(s) defined:**
- 	Name **poissongroup**, with                population size **1** and rate as <img src="https://render.githubusercontent.com/render/math?math=250. Hz">.


**NeuronGroup(s) defined:**
- Name **neurongroup\_1**, with                population size **1**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} x">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{x}{10.ms}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=x"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} y">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{y}{10.ms}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=y"> is rad

- Name **neurongroup**, with                population size **1**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} g">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{g}{10.ms}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=g"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{g - v}{50.ms}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is rad

	Parameter <img src="https://render.githubusercontent.com/render/math?math=allow_{gspike}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=allow_{gspike}"> is rad

	**Events:**

	Event **gspike**, after <img src="https://render.githubusercontent.com/render/math?math=allow_{gspike} \wedge g \gt 1">, <img src="https://render.githubusercontent.com/render/math?math=allow_{gspike}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\text{False}">

	Event **end\_gspike**, after <img src="https://render.githubusercontent.com/render/math?math=\neg allow_{gspike} \wedge g \lt 1">, <img src="https://render.githubusercontent.com/render/math?math=allow_{gspike}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\text{True}">

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt 1">, <img src="https://render.githubusercontent.com/render/math?math=v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=0">, <img src="https://render.githubusercontent.com/render/math?math=g">&#8592;<img src="https://render.githubusercontent.com/render/math?math=0">, <img src="https://render.githubusercontent.com/render/math?math=allow_{gspike}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\text{True}">, 


**StateMonitor(s) defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=x">,<img src="https://render.githubusercontent.com/render/math?math=y"> of neurongroup_1 for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">.

- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=v">,<img src="https://render.githubusercontent.com/render/math?math=g"> of neurongroup for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">.


**EventMonitor(s) defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=g">,<img src="https://render.githubusercontent.com/render/math?math=t">,<img src="https://render.githubusercontent.com/render/math?math=i"> of neurongroup. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **gspike** is triggered.


**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=v">,<img src="https://render.githubusercontent.com/render/math?math=t">,<img src="https://render.githubusercontent.com/render/math?math=i"> of neurongroup. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=rates"> of poissongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=250. Hz"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=allow_{gspike}"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=1."> to all members 


**Synaptic Connection(s) defined:**
- Connection from poissongroup to neurongroup

- Connection from neurongroup to neurongroup_1

