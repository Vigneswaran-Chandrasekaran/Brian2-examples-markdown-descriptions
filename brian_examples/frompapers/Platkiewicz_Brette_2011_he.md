# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **1. s**

**StateMonitor(s) defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=v"> of neurongroup for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">.

- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=\theta"> of neurongroup, for member(s): 0 with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">.


**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **200**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} \theta">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{a.{clip}{\left(- Vi + v,0,\infty.mV \right)} - \theta + vT}{tauh}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\theta"> is V

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{EL + I.\sigma + \mu - v}{\tau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is V

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} I">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{I}{tauI} + 1.4142135623731.\xi.\left(\frac{1}{tauI}\right)^{0.5}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=I"> is rad

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt \theta">, <img src="https://render.githubusercontent.com/render/math?math=v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=EL">, with refractory <img src="https://render.githubusercontent.com/render/math?math=5. ms">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=Vi">: <img src="https://render.githubusercontent.com/render/math?math=-63. mV">, <img src="https://render.githubusercontent.com/render/math?math=\tau">: <img src="https://render.githubusercontent.com/render/math?math=5. ms">, <img src="https://render.githubusercontent.com/render/math?math=\mu">: <img src="https://render.githubusercontent.com/render/math?math=15. mV">, <img src="https://render.githubusercontent.com/render/math?math=EL">: <img src="https://render.githubusercontent.com/render/math?math=-70. mV">, <img src="https://render.githubusercontent.com/render/math?math=vT">: <img src="https://render.githubusercontent.com/render/math?math=-55. mV">, <img src="https://render.githubusercontent.com/render/math?math=a">: <img src="https://render.githubusercontent.com/render/math?math=0.833333333333333">, <img src="https://render.githubusercontent.com/render/math?math=tauI">: <img src="https://render.githubusercontent.com/render/math?math=5. ms">, <img src="https://render.githubusercontent.com/render/math?math=\sigma">: <img src="https://render.githubusercontent.com/render/math?math=8.48528137 mV">, <img src="https://render.githubusercontent.com/render/math?math=tauh">: <img src="https://render.githubusercontent.com/render/math?math=5. ms">


**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=i">,<img src="https://render.githubusercontent.com/render/math?math=t"> of neurongroup. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=v"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=-70. mV"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=\theta"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=-55. mV"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=I"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=0."> to all members 

