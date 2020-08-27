# Network details
The Network consists of **3**                            simulation runs
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **20. ms**

**StateMonitor(s) defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=vm"> of neurongroup, for member(s): 0 with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">.


**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=i">,<img src="https://render.githubusercontent.com/render/math?math=t"> of neurongroup. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.


**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **1**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} w">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{a.\left(- EL + vm\right) - w}{tauw}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=w"> is A

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} vm">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{DeltaT.gL.e^{\frac{- VT + vm}{DeltaT}} + I + gL.\left(EL - vm\right) - w}{C}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=vm"> is V

	Parameter <img src="https://render.githubusercontent.com/render/math?math=I">, where unit of <img src="https://render.githubusercontent.com/render/math?math=I"> is A

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=vm \gt Vcut">, <img src="https://render.githubusercontent.com/render/math?math=vm">&#8592;<img src="https://render.githubusercontent.com/render/math?math=Vr">, <img src="https://render.githubusercontent.com/render/math?math=w">+=<img src="https://render.githubusercontent.com/render/math?math=b">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=VT">: <img src="https://render.githubusercontent.com/render/math?math=-50.4 mV">, <img src="https://render.githubusercontent.com/render/math?math=b">: <img src="https://render.githubusercontent.com/render/math?math=80.5 pA">, <img src="https://render.githubusercontent.com/render/math?math=a">: <img src="https://render.githubusercontent.com/render/math?math=4. nS">, <img src="https://render.githubusercontent.com/render/math?math=C">: <img src="https://render.githubusercontent.com/render/math?math=281. pF">, <img src="https://render.githubusercontent.com/render/math?math=DeltaT">: <img src="https://render.githubusercontent.com/render/math?math=2. mV">, <img src="https://render.githubusercontent.com/render/math?math=tauw">: <img src="https://render.githubusercontent.com/render/math?math=144. ms">, <img src="https://render.githubusercontent.com/render/math?math=Vr">: <img src="https://render.githubusercontent.com/render/math?math=-70.6 mV">, <img src="https://render.githubusercontent.com/render/math?math=EL">: <img src="https://render.githubusercontent.com/render/math?math=-70.6 mV">, <img src="https://render.githubusercontent.com/render/math?math=gL">: <img src="https://render.githubusercontent.com/render/math?math=30. nS">, <img src="https://render.githubusercontent.com/render/math?math=Vcut">: <img src="https://render.githubusercontent.com/render/math?math=-40.4 mV">


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=vm"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=-70.6 mV"> to all members 

### Run 2 details
Duration of simulation is **100. ms**

**StateMonitor(s) defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=vm"> of neurongroup, for member(s): 0 with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">.


**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=i">,<img src="https://render.githubusercontent.com/render/math?math=t"> of neurongroup. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.


**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **1**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} w">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{a.\left(- EL + vm\right) - w}{tauw}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=w"> is A

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} vm">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{DeltaT.gL.e^{\frac{- VT + vm}{DeltaT}} + I + gL.\left(EL - vm\right) - w}{C}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=vm"> is V

	Parameter <img src="https://render.githubusercontent.com/render/math?math=I">, where unit of <img src="https://render.githubusercontent.com/render/math?math=I"> is A

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=vm \gt Vcut">, <img src="https://render.githubusercontent.com/render/math?math=vm">&#8592;<img src="https://render.githubusercontent.com/render/math?math=Vr">, <img src="https://render.githubusercontent.com/render/math?math=w">+=<img src="https://render.githubusercontent.com/render/math?math=b">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=VT">: <img src="https://render.githubusercontent.com/render/math?math=-50.4 mV">, <img src="https://render.githubusercontent.com/render/math?math=b">: <img src="https://render.githubusercontent.com/render/math?math=80.5 pA">, <img src="https://render.githubusercontent.com/render/math?math=a">: <img src="https://render.githubusercontent.com/render/math?math=4. nS">, <img src="https://render.githubusercontent.com/render/math?math=C">: <img src="https://render.githubusercontent.com/render/math?math=281. pF">, <img src="https://render.githubusercontent.com/render/math?math=DeltaT">: <img src="https://render.githubusercontent.com/render/math?math=2. mV">, <img src="https://render.githubusercontent.com/render/math?math=tauw">: <img src="https://render.githubusercontent.com/render/math?math=144. ms">, <img src="https://render.githubusercontent.com/render/math?math=Vr">: <img src="https://render.githubusercontent.com/render/math?math=-70.6 mV">, <img src="https://render.githubusercontent.com/render/math?math=EL">: <img src="https://render.githubusercontent.com/render/math?math=-70.6 mV">, <img src="https://render.githubusercontent.com/render/math?math=gL">: <img src="https://render.githubusercontent.com/render/math?math=30. nS">, <img src="https://render.githubusercontent.com/render/math?math=Vcut">: <img src="https://render.githubusercontent.com/render/math?math=-40.4 mV">


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=I"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=1. nA"> to all members 

### Run 3 details
Duration of simulation is **20. ms**

**StateMonitor(s) defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=vm"> of neurongroup, for member(s): 0 with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">.


**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=i">,<img src="https://render.githubusercontent.com/render/math?math=t"> of neurongroup. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.


**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **1**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} w">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{a.\left(- EL + vm\right) - w}{tauw}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=w"> is A

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} vm">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{DeltaT.gL.e^{\frac{- VT + vm}{DeltaT}} + I + gL.\left(EL - vm\right) - w}{C}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=vm"> is V

	Parameter <img src="https://render.githubusercontent.com/render/math?math=I">, where unit of <img src="https://render.githubusercontent.com/render/math?math=I"> is A

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=vm \gt Vcut">, <img src="https://render.githubusercontent.com/render/math?math=vm">&#8592;<img src="https://render.githubusercontent.com/render/math?math=Vr">, <img src="https://render.githubusercontent.com/render/math?math=w">+=<img src="https://render.githubusercontent.com/render/math?math=b">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=VT">: <img src="https://render.githubusercontent.com/render/math?math=-50.4 mV">, <img src="https://render.githubusercontent.com/render/math?math=b">: <img src="https://render.githubusercontent.com/render/math?math=80.5 pA">, <img src="https://render.githubusercontent.com/render/math?math=a">: <img src="https://render.githubusercontent.com/render/math?math=4. nS">, <img src="https://render.githubusercontent.com/render/math?math=C">: <img src="https://render.githubusercontent.com/render/math?math=281. pF">, <img src="https://render.githubusercontent.com/render/math?math=DeltaT">: <img src="https://render.githubusercontent.com/render/math?math=2. mV">, <img src="https://render.githubusercontent.com/render/math?math=tauw">: <img src="https://render.githubusercontent.com/render/math?math=144. ms">, <img src="https://render.githubusercontent.com/render/math?math=Vr">: <img src="https://render.githubusercontent.com/render/math?math=-70.6 mV">, <img src="https://render.githubusercontent.com/render/math?math=EL">: <img src="https://render.githubusercontent.com/render/math?math=-70.6 mV">, <img src="https://render.githubusercontent.com/render/math?math=gL">: <img src="https://render.githubusercontent.com/render/math?math=30. nS">, <img src="https://render.githubusercontent.com/render/math?math=Vcut">: <img src="https://render.githubusercontent.com/render/math?math=-40.4 mV">


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=I"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=0. A"> to all members 

