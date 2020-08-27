# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **2. s**

**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=v">,<img src="https://render.githubusercontent.com/render/math?math=i">,<img src="https://render.githubusercontent.com/render/math?math=t"> of neurongroup. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.


**Synapses defined:**
- 	From poissongroup to neurongroup

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=v">+=<img src="https://render.githubusercontent.com/render/math?math=3.mV"> is executed


**PoissonGroup(s) defined:**
- 	Name **poissongroup**, with                population size **1** and rate as <img src="https://render.githubusercontent.com/render/math?math=0.5 kHz">.


**StateMonitor(s) defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=v"> of neurongroup for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">.

- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=vt"> of neurongroup for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">.


**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **1**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} vt">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{10.mV - vt}{15.ms}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=vt"> is V

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{v}{10.ms}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is V

	exact method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt vt">, , <img src="https://render.githubusercontent.com/render/math?math=v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=0">, <img src="https://render.githubusercontent.com/render/math?math=vt">+=<img src="https://render.githubusercontent.com/render/math?math=3.mV">, 


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=vt"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=10. mV"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=rates"> of poissongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=0.5 kHz"> to all members 


**Synaptic Connection(s) defined:**
- Connection from poissongroup to neurongroup

