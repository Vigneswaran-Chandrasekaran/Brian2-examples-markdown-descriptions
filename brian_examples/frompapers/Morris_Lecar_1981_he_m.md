# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **220. ms**

**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **17**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} n">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\lambda_{n}.\left(- n + n_{inf}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=n"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=n_{inf}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=0.5.\tanh{\left(\frac{V - V_{3}}{V_{4}} \right)} + 0.5">, where unit of <img src="https://render.githubusercontent.com/render/math?math=n_{inf}"> is rad

	Parameter <img src="https://render.githubusercontent.com/render/math?math=I">, where unit of <img src="https://render.githubusercontent.com/render/math?math=I"> is A

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} V">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{I - g_{Ca}.m_{inf}.\left(V - V_{Ca}\right) - g_{K}.n.\left(V - V_{K}\right) - g_{L}.\left(V - V_{L}\right)}{C}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=V"> is V

	<img src="https://render.githubusercontent.com/render/math?math=m_{inf}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=0.5.\tanh{\left(\frac{V - V_{1}}{V_{2}} \right)} + 0.5">, where unit of <img src="https://render.githubusercontent.com/render/math?math=m_{inf}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\lambda_{n}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\lambda^{max}_{n}.\cosh{\left(\frac{V - V_{3}}{2.V_{4}} \right)}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\lambda_{n}"> is Hz

	exponential_euler method is used for integration

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=g_{Ca}">: <img src="https://render.githubusercontent.com/render/math?math=4. mS">, <img src="https://render.githubusercontent.com/render/math?math=V_{1}">: <img src="https://render.githubusercontent.com/render/math?math=10. mV">, <img src="https://render.githubusercontent.com/render/math?math=V_{3}">: <img src="https://render.githubusercontent.com/render/math?math=-1. mV">, <img src="https://render.githubusercontent.com/render/math?math=V_{Ca}">: <img src="https://render.githubusercontent.com/render/math?math=100. mV">, <img src="https://render.githubusercontent.com/render/math?math=\lambda^{max}_{n}">: <img src="https://render.githubusercontent.com/render/math?math=66.66666667 Hz">, <img src="https://render.githubusercontent.com/render/math?math=g_{L}">: <img src="https://render.githubusercontent.com/render/math?math=2. mS">, <img src="https://render.githubusercontent.com/render/math?math=V_{2}">: <img src="https://render.githubusercontent.com/render/math?math=15. mV">, <img src="https://render.githubusercontent.com/render/math?math=V_{K}">: <img src="https://render.githubusercontent.com/render/math?math=-70. mV">, <img src="https://render.githubusercontent.com/render/math?math=V_{L}">: <img src="https://render.githubusercontent.com/render/math?math=-50. mV">, <img src="https://render.githubusercontent.com/render/math?math=C">: <img src="https://render.githubusercontent.com/render/math?math=20. uF">, <img src="https://render.githubusercontent.com/render/math?math=g_{K}">: <img src="https://render.githubusercontent.com/render/math?math=8. mS">, <img src="https://render.githubusercontent.com/render/math?math=V_{4}">: <img src="https://render.githubusercontent.com/render/math?math=14.5 mV">


**StateMonitor(s) defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=V">,<img src="https://render.githubusercontent.com/render/math?math=n"> of neurongroup for all members with time step <img src="https://render.githubusercontent.com/render/math?math=10. us">.


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=I"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=[100. 125. 150. 175. 200. 225. 250. 275. 300. 325. 350. 375. 400. 425.
 450. 475. 500.] uA"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=V"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=-50. mV"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=n"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=n_{inf}"> to all members 

