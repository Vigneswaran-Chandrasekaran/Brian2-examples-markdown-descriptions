# Network details
The Network consists of **2**                            simulation runs
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **3. s**

**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **200**.

	**Dynamics:**

	Parameter <img src="https://render.githubusercontent.com/render/math?math=Vr">, where unit of <img src="https://render.githubusercontent.com/render/math?math=Vr"> is V

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} vm">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{DeltaT.gL.e^{\frac{- VT + vm}{DeltaT}} + I + gL.\left(EL - vm\right) - w}{C}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=vm"> is V

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} w">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{a.\left(- EL + vm\right) - w}{tauw}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=w"> is A

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=vm \gt Vcut">, <img src="https://render.githubusercontent.com/render/math?math=vm">&#8592;<img src="https://render.githubusercontent.com/render/math?math=Vr">, <img src="https://render.githubusercontent.com/render/math?math=w">+=<img src="https://render.githubusercontent.com/render/math?math=b">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=I">: <img src="https://render.githubusercontent.com/render/math?math=0.8 nA">, <img src="https://render.githubusercontent.com/render/math?math=tauw">: <img src="https://render.githubusercontent.com/render/math?math=40. ms">, <img src="https://render.githubusercontent.com/render/math?math=a">: <img src="https://render.githubusercontent.com/render/math?math=4. nS">, <img src="https://render.githubusercontent.com/render/math?math=VT">: <img src="https://render.githubusercontent.com/render/math?math=-50.4 mV">, <img src="https://render.githubusercontent.com/render/math?math=Vcut">: <img src="https://render.githubusercontent.com/render/math?math=-40.4 mV">, <img src="https://render.githubusercontent.com/render/math?math=EL">: <img src="https://render.githubusercontent.com/render/math?math=-70.6 mV">, <img src="https://render.githubusercontent.com/render/math?math=DeltaT">: <img src="https://render.githubusercontent.com/render/math?math=2. mV">, <img src="https://render.githubusercontent.com/render/math?math=gL">: <img src="https://render.githubusercontent.com/render/math?math=30. nS">, <img src="https://render.githubusercontent.com/render/math?math=b">: <img src="https://render.githubusercontent.com/render/math?math=80. pA">, <img src="https://render.githubusercontent.com/render/math?math=C">: <img src="https://render.githubusercontent.com/render/math?math=281. pF">


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=vm"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=-70.6 mV"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=w"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=[282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4
 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4
 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4
 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4
 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4
 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4
 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4
 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4
 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4
 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4
 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4
 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4
 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4
 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4
 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4
 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4
 282.4 282.4 282.4 282.4 282.4 282.4 282.4 282.4] pA"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=Vr"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=[-48.3        -48.29698492 -48.29396985 -48.29095477 -48.2879397
 -48.28492462 -48.28190955 -48.27889447 -48.2758794  -48.27286432
 -48.26984925 -48.26683417 -48.2638191  -48.26080402 -48.25778894
 -48.25477387 -48.25175879 -48.24874372 -48.24572864 -48.24271357
 -48.23969849 -48.23668342 -48.23366834 -48.23065327 -48.22763819
 -48.22462312 -48.22160804 -48.21859296 -48.21557789 -48.21256281
 -48.20954774 -48.20653266 -48.20351759 -48.20050251 -48.19748744
 -48.19447236 -48.19145729 -48.18844221 -48.18542714 -48.18241206
 -48.17939698 -48.17638191 -48.17336683 -48.17035176 -48.16733668
 -48.16432161 -48.16130653 -48.15829146 -48.15527638 -48.15226131
 -48.14924623 -48.14623116 -48.14321608 -48.14020101 -48.13718593
 -48.13417085 -48.13115578 -48.1281407  -48.12512563 -48.12211055
 -48.11909548 -48.1160804  -48.11306533 -48.11005025 -48.10703518
 -48.1040201  -48.10100503 -48.09798995 -48.09497487 -48.0919598
 -48.08894472 -48.08592965 -48.08291457 -48.0798995  -48.07688442
 -48.07386935 -48.07085427 -48.0678392  -48.06482412 -48.06180905
 -48.05879397 -48.05577889 -48.05276382 -48.04974874 -48.04673367
 -48.04371859 -48.04070352 -48.03768844 -48.03467337 -48.03165829
 -48.02864322 -48.02562814 -48.02261307 -48.01959799 -48.01658291
 -48.01356784 -48.01055276 -48.00753769 -48.00452261 -48.00150754
 -47.99849246 -47.99547739 -47.99246231 -47.98944724 -47.98643216
 -47.98341709 -47.98040201 -47.97738693 -47.97437186 -47.97135678
 -47.96834171 -47.96532663 -47.96231156 -47.95929648 -47.95628141
 -47.95326633 -47.95025126 -47.94723618 -47.94422111 -47.94120603
 -47.93819095 -47.93517588 -47.9321608  -47.92914573 -47.92613065
 -47.92311558 -47.9201005  -47.91708543 -47.91407035 -47.91105528
 -47.9080402  -47.90502513 -47.90201005 -47.89899497 -47.8959799
 -47.89296482 -47.88994975 -47.88693467 -47.8839196  -47.88090452
 -47.87788945 -47.87487437 -47.8718593  -47.86884422 -47.86582915
 -47.86281407 -47.85979899 -47.85678392 -47.85376884 -47.85075377
 -47.84773869 -47.84472362 -47.84170854 -47.83869347 -47.83567839
 -47.83266332 -47.82964824 -47.82663317 -47.82361809 -47.82060302
 -47.81758794 -47.81457286 -47.81155779 -47.80854271 -47.80552764
 -47.80251256 -47.79949749 -47.79648241 -47.79346734 -47.79045226
 -47.78743719 -47.78442211 -47.78140704 -47.77839196 -47.77537688
 -47.77236181 -47.76934673 -47.76633166 -47.76331658 -47.76030151
 -47.75728643 -47.75427136 -47.75125628 -47.74824121 -47.74522613
 -47.74221106 -47.73919598 -47.7361809  -47.73316583 -47.73015075
 -47.72713568 -47.7241206  -47.72110553 -47.71809045 -47.71507538
 -47.7120603  -47.70904523 -47.70603015 -47.70301508 -47.7       ] mV"> to all members 

### Run 2 details
Duration of simulation is **1. s**

**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=i">,<img src="https://render.githubusercontent.com/render/math?math=t"> of neurongroup. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=10. us"> when event **spike** is triggered.


**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **200**.

	**Dynamics:**

	Parameter <img src="https://render.githubusercontent.com/render/math?math=Vr">, where unit of <img src="https://render.githubusercontent.com/render/math?math=Vr"> is V

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} vm">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{DeltaT.gL.e^{\frac{- VT + vm}{DeltaT}} + I + gL.\left(EL - vm\right) - w}{C}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=vm"> is V

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} w">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{a.\left(- EL + vm\right) - w}{tauw}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=w"> is A

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=vm \gt Vcut">, <img src="https://render.githubusercontent.com/render/math?math=vm">&#8592;<img src="https://render.githubusercontent.com/render/math?math=Vr">, <img src="https://render.githubusercontent.com/render/math?math=w">+=<img src="https://render.githubusercontent.com/render/math?math=b">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=I">: <img src="https://render.githubusercontent.com/render/math?math=0.8 nA">, <img src="https://render.githubusercontent.com/render/math?math=tauw">: <img src="https://render.githubusercontent.com/render/math?math=40. ms">, <img src="https://render.githubusercontent.com/render/math?math=a">: <img src="https://render.githubusercontent.com/render/math?math=4. nS">, <img src="https://render.githubusercontent.com/render/math?math=VT">: <img src="https://render.githubusercontent.com/render/math?math=-50.4 mV">, <img src="https://render.githubusercontent.com/render/math?math=Vcut">: <img src="https://render.githubusercontent.com/render/math?math=-40.4 mV">, <img src="https://render.githubusercontent.com/render/math?math=EL">: <img src="https://render.githubusercontent.com/render/math?math=-70.6 mV">, <img src="https://render.githubusercontent.com/render/math?math=DeltaT">: <img src="https://render.githubusercontent.com/render/math?math=2. mV">, <img src="https://render.githubusercontent.com/render/math?math=gL">: <img src="https://render.githubusercontent.com/render/math?math=30. nS">, <img src="https://render.githubusercontent.com/render/math?math=b">: <img src="https://render.githubusercontent.com/render/math?math=80. pA">, <img src="https://render.githubusercontent.com/render/math?math=C">: <img src="https://render.githubusercontent.com/render/math?math=281. pF">


**StateMonitor(s) defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=w"> of neurongroup for all members with time step <img src="https://render.githubusercontent.com/render/math?math=10. us">.


