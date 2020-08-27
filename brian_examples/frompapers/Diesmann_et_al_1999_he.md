# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **100. ms**

**SpikeGeneratorGroup(s) defined:**
- 	Name **spikegeneratorgroup**, with population size **85**, has neuron(s) 58, 16, 14, 61, 77, 51, 7, 79, 42, 46, 68, 57, 43, 41, 75, 72, 6, 12, 56, 65, 50, 25, 30, 34, 21, 18, 82, 19, 24, 62, 44, 64, 8, 66, 0, 69, 10, 38, 49, 26, 63, 60, 67, 45, 52, 29, 1, 39, 59, 17, 53, 83, 13, 78, 3, 28, 31, 9, 35, 15, 55, 71, 84, 37, 27, 2, 32, 48, 74, 80, 76, 11, 5, 23, 47, 4, 40, 81, 73, 36, 54, 70, 33, 22, 20 that spike at times 0.0463189140221769, 0.04760103208703523, 0.04766127870962344, 0.047723745161654056, 0.04790027813057957, 0.048274578589704846, 0.04827537373952091, 0.04841330410010276, 0.04851107564408642, 0.04851278306595233, 0.04851856419679028, 0.04860882936655099, 0.048777667932099714, 0.04889592684869927, 0.048919930087023895, 0.048996690039308476, 0.04901869971452755, 0.04904240810624238, 0.04911162333594607, 0.049131784412178844, 0.049167989484927066, 0.049179216802216326, 0.0491896799200464, 0.04928440158338413, 0.04929122014214978, 0.04942925241284756, 0.04951611754653849, 0.04952458921298168, 0.04960222681008206, 0.04971965104702711, 0.04972071680563151, 0.04972810340742011, 0.04973171668298158, 0.04975766333707932, 0.04979928861547412, 0.04980501230891524, 0.049884558378991535, 0.04990079763904542, 0.04991153539008396, 0.04992485918540195, 0.04996336430230828, 0.04997119740606994, 0.049995594094917585, 0.05000053176104535, 0.05003578901922995, 0.05010241807914731, 0.050209172846963, 0.0502163702015185, 0.050227904022255826, 0.05024944320282294, 0.050267508186098736, 0.050305222630459064, 0.05031810368546299, 0.05037671226240601, 0.05038679815366007, 0.05043906023698257, 0.05045058814583314, 0.0504610523767973, 0.050522466032321994, 0.05055690605802627, 0.05062702331806357, 0.0506427144013253, 0.05073273201041854, 0.0507392908520627, 0.05077948143379298, 0.05081147381441873, 0.05083922612467842, 0.05085060146899949, 0.050889281669697715, 0.05090487105594371, 0.05091311186355523, 0.051071602872699705, 0.05109457693924062, 0.05115231172162019, 0.05115435137105042, 0.051174518738306356, 0.05126214498808206, 0.05129103325700334, 0.05130906322552547, 0.05132180528237951, 0.05143387311097897, 0.051477237825861985, 0.05175201290074565, 0.051777836259891526, 0.05185814034097157, with period 0. s.


**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=t">,<img src="https://render.githubusercontent.com/render/math?math=i"> of spikegeneratorgroup. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.

- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=t">,<img src="https://render.githubusercontent.com/render/math?math=i"> of neurongroup. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.


**Synapses defined:**
- 	From spikegeneratorgroup to neurongroup_subgroup

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=y">+=<img src="https://render.githubusercontent.com/render/math?math=weight"> is executed

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=weight">: <img src="https://render.githubusercontent.com/render/math?math=4.86 mV">

- 	From neurongroup to neurongroup

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=y">+=<img src="https://render.githubusercontent.com/render/math?math=weight"> is executed

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=weight">: <img src="https://render.githubusercontent.com/render/math?math=4.86 mV">


**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **1000**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} V">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{1.0.\left(- V + Vr + x\right)}{taum}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=V"> is V

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} y">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{39.24.mV.\xi}{ms^{0.5}} + \frac{25.27.mV}{ms} - \frac{1.0.y}{taupsp}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=y"> is V

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} x">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{1.0.\left(- x + y\right)}{taupsp}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=x"> is V

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=V \gt Vt">, <img src="https://render.githubusercontent.com/render/math?math=V">&#8592;<img src="https://render.githubusercontent.com/render/math?math=Vr">, with refractory <img src="https://render.githubusercontent.com/render/math?math=1. ms">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=taupsp">: <img src="https://render.githubusercontent.com/render/math?math=0.325 ms">, <img src="https://render.githubusercontent.com/render/math?math=Vt">: <img src="https://render.githubusercontent.com/render/math?math=-55. mV">, <img src="https://render.githubusercontent.com/render/math?math=taum">: <img src="https://render.githubusercontent.com/render/math?math=10. ms">, <img src="https://render.githubusercontent.com/render/math?math=Vr">: <img src="https://render.githubusercontent.com/render/math?math=-70. mV">


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=V"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=Vr + \left(- Vr + Vt\right).{rand}{\left(- \right)}"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=Vr">: <img src="https://render.githubusercontent.com/render/math?math=-70. mV">, <img src="https://render.githubusercontent.com/render/math?math=Vt">: <img src="https://render.githubusercontent.com/render/math?math=-55. mV">




**Synaptic Connection(s) defined:**
- Connection from neurongroup to neurongroup. Connection for all members in source group to target group with generator syntax k for k in range((int(i/group_size)+1)*group_size, (int(i/group_size)+2)*group_size) if i<N_pre-group_size

- Connection from spikegeneratorgroup to neurongroup_subgroup

