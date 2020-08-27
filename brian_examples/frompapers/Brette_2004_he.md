# Network details
The Network consists of **3**                            simulation runs
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **5. s**

**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **2000**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{a - v + 2.\sin{\left(\frac{2.\pi.t}{\tau} \right)}}{\tau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is rad

	Parameter <img src="https://render.githubusercontent.com/render/math?math=a">, where unit of <img src="https://render.githubusercontent.com/render/math?math=a"> is rad

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt 1">, <img src="https://render.githubusercontent.com/render/math?math=v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=0">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=\tau">: <img src="https://render.githubusercontent.com/render/math?math=100. ms">


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=a"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=[2.        2.0010005 2.002001  ... 3.997999  3.9989995 4.       ]"> to all members 

### Run 2 details
Duration of simulation is **5. s**

**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **2000**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{a - v + 2.\sin{\left(\frac{2.\pi.t}{\tau} \right)}}{\tau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is rad

	Parameter <img src="https://render.githubusercontent.com/render/math?math=a">, where unit of <img src="https://render.githubusercontent.com/render/math?math=a"> is rad

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt 1">, <img src="https://render.githubusercontent.com/render/math?math=v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=0">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=\tau">: <img src="https://render.githubusercontent.com/render/math?math=100. ms">


**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=i">,<img src="https://render.githubusercontent.com/render/math?math=t"> of neurongroup. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.


### Run 3 details
Duration of simulation is **0.5 s**

**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **2000**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{a - v + 2.\sin{\left(\frac{2.\pi.t}{\tau} \right)}}{\tau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is rad

	Parameter <img src="https://render.githubusercontent.com/render/math?math=a">, where unit of <img src="https://render.githubusercontent.com/render/math?math=a"> is rad

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt 1">, <img src="https://render.githubusercontent.com/render/math?math=v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=0">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=\tau">: <img src="https://render.githubusercontent.com/render/math?math=100. ms">


**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=i">,<img src="https://render.githubusercontent.com/render/math?math=t"> of neurongroup. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.


