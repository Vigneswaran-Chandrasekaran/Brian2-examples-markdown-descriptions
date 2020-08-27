# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **1. s**

**StateMonitor(s) defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=g"> of neurongroup_1, for member(s): 0 with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">.

- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=g"> of synapses, for member(s): 0,1 with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">.


**NeuronGroup(s) defined:**
- Name **neurongroup\_1**, with                population size **1**.

	**Dynamics:**

	Parameter <img src="https://render.githubusercontent.com/render/math?math=g">, where unit of <img src="https://render.githubusercontent.com/render/math?math=g"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{g - v}{10.ms}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is rad

	exact method is used for integration

- Name **neurongroup**, with                population size **2**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{1}{10.ms}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is rad

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt 1">, <img src="https://render.githubusercontent.com/render/math?math=v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=0">


**Synapses defined:**
- 	From neurongroup to neurongroup_1

	**Dynamics:**

		Parameter <img src="https://render.githubusercontent.com/render/math?math=w">, where unit of <img src="https://render.githubusercontent.com/render/math?math=w"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} x">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- c.x">, where unit of <img src="https://render.githubusercontent.com/render/math?math=x"> is rad and clock-driven as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} g_{syn}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- a.g_{syn} + b.x.\left(1 - g_{syn}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=g_{syn}"> is rad and clock-driven as flag(s) associated

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=x">+=<img src="https://render.githubusercontent.com/render/math?math=w"> is executed

	**Summed variables: **

	Updates target group neurongroup_1 with statement: <img src="https://render.githubusercontent.com/render/math?math=g_{syn}">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=c">: <img src="https://render.githubusercontent.com/render/math?math=100. Hz">, <img src="https://render.githubusercontent.com/render/math?math=a">: <img src="https://render.githubusercontent.com/render/math?math=100. Hz">, <img src="https://render.githubusercontent.com/render/math?math=b">: <img src="https://render.githubusercontent.com/render/math?math=100. Hz">


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=w"> of synapses initialized with <img src="https://render.githubusercontent.com/render/math?math=[ 1. 10.]"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=v"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=[0.  0.5]"> to all members 


**Synaptic Connection(s) defined:**
- Connection from neurongroup to neurongroup_1

