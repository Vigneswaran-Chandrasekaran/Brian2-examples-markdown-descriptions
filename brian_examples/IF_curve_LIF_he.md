# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **1. s**

**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **1000**.

	**Dynamics:**

	Parameter <img src="https://render.githubusercontent.com/render/math?math=v_{0}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v_{0}"> is V

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{- v + v_{0}}{\tau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is V and unless refractory as flag(s) associated

	exact method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt 10.mV">, <img src="https://render.githubusercontent.com/render/math?math=v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=0">, with refractory <img src="https://render.githubusercontent.com/render/math?math=5. ms">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=\tau">: <img src="https://render.githubusercontent.com/render/math?math=10. ms">


**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=i">,<img src="https://render.githubusercontent.com/render/math?math=t"> of neurongroup. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=v"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=0. V"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=v_{0}"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=\frac{20.i.mV}{n - 1}"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=n">: <img src="https://render.githubusercontent.com/render/math?math=1000">



