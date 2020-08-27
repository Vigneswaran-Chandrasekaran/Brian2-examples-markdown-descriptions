# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **20. ms**

**NeuronGroup(s) defined:**
- Name **neurongroup\_1**, with                population size **10**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{v}{10.ms}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is rad

	exact method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt 1">, <img src="https://render.githubusercontent.com/render/math?math=v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=0">

- Name **neurongroup**, with                population size **10**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{v}{10.ms}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is rad

	exact method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt 1">, <img src="https://render.githubusercontent.com/render/math?math=v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=0.0">


**Synapses defined:**
- 	From neurongroup to neurongroup_1

	**Dynamics:**

		<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} w">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{w}{50.ms}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=w"> is rad and event-driven as flag(s) associated

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=v">+=<img src="https://render.githubusercontent.com/render/math?math=w"> is executed


**StateMonitor(s) defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=v"> of neurongroup_1 for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">.


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=v"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=1.2"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=delay"> of synapses_pre initialized with <img src="https://render.githubusercontent.com/render/math?math=i.ms + 0.25.ms.{randn}{\left(- \right)} + ms"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=w"> of synapses initialized with <img src="https://render.githubusercontent.com/render/math?math=1."> to all members 


**Synaptic Connection(s) defined:**
- Connection from neurongroup to neurongroup_1 with condition <img src="https://render.githubusercontent.com/render/math?math=i = j">, with probabilty <img src="https://render.githubusercontent.com/render/math?math=0.75">

