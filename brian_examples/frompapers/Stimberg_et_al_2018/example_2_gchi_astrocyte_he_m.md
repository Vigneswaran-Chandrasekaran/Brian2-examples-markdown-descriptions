# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **30. s**

**NeuronGroup(s) defined:**
- Name **neurongroup\_1**, with                population size **1**.

	**Dynamics:**

- Name **neurongroup**, with                population size **1**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} x">&#8592;<img src="https://render.githubusercontent.com/render/math?math=f_{0}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=x"> is rad

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=x \gt 1">, <img src="https://render.githubusercontent.com/render/math?math=x">&#8592;<img src="https://render.githubusercontent.com/render/math?math=0">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=f_{0}">: <img src="https://render.githubusercontent.com/render/math?math=0.5 Hz">

- Name **neurongroup\_2**, with                population size **2**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} I">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- J_{3K} - J_{5P} + J_{\beta} + J_{\delta} + J_{ex}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=I"> is mM

	<img src="https://render.githubusercontent.com/render/math?math=J_{3K}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{C^{4}.I.O_{3K}}{\left(C^{4} + K_{D}^{4}\right).\left(I + K_{3K}\right)}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=J_{3K}"> is mM/s

	Parameter <img src="https://render.githubusercontent.com/render/math?math=I_{bias}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=I_{bias}"> is mM and constant as flag(s) associated

	Parameter <img src="https://render.githubusercontent.com/render/math?math=noise">, where unit of <img src="https://render.githubusercontent.com/render/math?math=noise"> is rad and constant as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} h">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{\left(- h_{clipped} + h_{inf}\right).\left(noise.\tau_{h}^{0.5}.\xi + 1\right)}{\tau_{h}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=h"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=J_{p}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{C^{2}.O_{P}}{C^{2} + K_{P}^{2}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=J_{p}"> is mM/s

	<img src="https://render.githubusercontent.com/render/math?math=J_{ex}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{F_{ex}.\left(\tanh{\left(\frac{- I_{\Theta} + \left|{\delta_{I bias}}\right|}{\omega_{I}} \right)} + 1\right).{sign}{\left(\delta_{I bias} \right)}}{2}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=J_{ex}"> is mM/s

	<img src="https://render.githubusercontent.com/render/math?math=Q_{2}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{d_{2}.\left(I + d_{1}\right)}{I + d_{3}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=Q_{2}"> is mM

	<img src="https://render.githubusercontent.com/render/math?math=J_{\delta}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{C^{2}.O_{\delta}}{\left(C^{2} + K_{\delta}^{2}\right).\left(\frac{I}{\kappa_{\delta}} + 1\right)}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=J_{\delta}"> is mM/s

	<img src="https://render.githubusercontent.com/render/math?math=\tau_{h}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{1}{O_{2}.\left(C + Q_{2}\right)}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\tau_{h}"> is s

	<img src="https://render.githubusercontent.com/render/math?math=h_{inf}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{Q_{2}}{C + Q_{2}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=h_{inf}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=J_{\beta}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\Gamma_{A}.O_{\beta}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=J_{\beta}"> is mM/s

	<img src="https://render.githubusercontent.com/render/math?math=h_{clipped}">&#8592;<img src="https://render.githubusercontent.com/render/math?math={clip}{\left(h,0,1 \right)}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=h_{clipped}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\delta_{I bias}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=I - I_{bias}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\delta_{I bias}"> is mM

	<img src="https://render.githubusercontent.com/render/math?math=J_{r}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\Omega_{C}.h_{clipped}^{3}.m_{inf}^{3}.\left(- C.\left(\rho_{A} + 1\right) + C_{T}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=J_{r}"> is mM/s

	Parameter <img src="https://render.githubusercontent.com/render/math?math=Y_{S}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=Y_{S}"> is mM

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} C">&#8592;<img src="https://render.githubusercontent.com/render/math?math=J_{l} - J_{p} + J_{r}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=C"> is mM

	<img src="https://render.githubusercontent.com/render/math?math=J_{l}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\Omega_{L}.\left(- C.\left(\rho_{A} + 1\right) + C_{T}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=J_{l}"> is mM/s

	<img src="https://render.githubusercontent.com/render/math?math=J_{5P}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=I.\Omega_{5P}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=J_{5P}"> is mM/s

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} \Gamma_{A}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \Gamma_{A}.\Omega_{N}.\left(\frac{C.\zeta}{C + K_{KC}} + 1\right) + O_{N}.Y_{S}.\left(1 - \Gamma_{A}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\Gamma_{A}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=m_{inf}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{C.I}{\left(C + d_{5}\right).\left(I + d_{1}\right)}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=m_{inf}"> is rad

	milstein method is used for integration

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=\Omega_{L}">: <img src="https://render.githubusercontent.com/render/math?math=100. mHz">, <img src="https://render.githubusercontent.com/render/math?math=F_{ex}">: <img src="https://render.githubusercontent.com/render/math?math=9.e-05 mM/s">, <img src="https://render.githubusercontent.com/render/math?math=K_{P}">: <img src="https://render.githubusercontent.com/render/math?math=100. nM">, <img src="https://render.githubusercontent.com/render/math?math=O_{\beta}">: <img src="https://render.githubusercontent.com/render/math?math=0.005 mM/s">, <img src="https://render.githubusercontent.com/render/math?math=\Omega_{C}">: <img src="https://render.githubusercontent.com/render/math?math=6. Hz">, <img src="https://render.githubusercontent.com/render/math?math=K_{KC}">: <img src="https://render.githubusercontent.com/render/math?math=0.5 uM">, <img src="https://render.githubusercontent.com/render/math?math=d_{3}">: <img src="https://render.githubusercontent.com/render/math?math=0.9434 uM">, <img src="https://render.githubusercontent.com/render/math?math=d_{1}">: <img src="https://render.githubusercontent.com/render/math?math=130. nM">, <img src="https://render.githubusercontent.com/render/math?math=\zeta">: <img src="https://render.githubusercontent.com/render/math?math=10">, <img src="https://render.githubusercontent.com/render/math?math=\kappa_{\delta}">: <img src="https://render.githubusercontent.com/render/math?math=1.5 uM">, <img src="https://render.githubusercontent.com/render/math?math=\rho_{A}">: <img src="https://render.githubusercontent.com/render/math?math=0.18">, <img src="https://render.githubusercontent.com/render/math?math=O_{2}">: <img src="https://render.githubusercontent.com/render/math?math=200. m^3 s^-1 mol^-1">, <img src="https://render.githubusercontent.com/render/math?math=C_{T}">: <img src="https://render.githubusercontent.com/render/math?math=2. uM">, <img src="https://render.githubusercontent.com/render/math?math=I_{\Theta}">: <img src="https://render.githubusercontent.com/render/math?math=300. nM">, <img src="https://render.githubusercontent.com/render/math?math=O_{P}">: <img src="https://render.githubusercontent.com/render/math?math=0.0009 mM/s">, <img src="https://render.githubusercontent.com/render/math?math=\Omega_{5P}">: <img src="https://render.githubusercontent.com/render/math?math=100. mHz">, <img src="https://render.githubusercontent.com/render/math?math=\Omega_{N}">: <img src="https://render.githubusercontent.com/render/math?math=0.5 Hz">, <img src="https://render.githubusercontent.com/render/math?math=O_{N}">: <img src="https://render.githubusercontent.com/render/math?math=300. m^3 s^-1 mol^-1">, <img src="https://render.githubusercontent.com/render/math?math=d_{5}">: <img src="https://render.githubusercontent.com/render/math?math=80. nM">, <img src="https://render.githubusercontent.com/render/math?math=K_{3K}">: <img src="https://render.githubusercontent.com/render/math?math=1. uM">, <img src="https://render.githubusercontent.com/render/math?math=K_{\delta}">: <img src="https://render.githubusercontent.com/render/math?math=300. nM">, <img src="https://render.githubusercontent.com/render/math?math=O_{3K}">: <img src="https://render.githubusercontent.com/render/math?math=0.0045 mM/s">, <img src="https://render.githubusercontent.com/render/math?math=K_{D}">: <img src="https://render.githubusercontent.com/render/math?math=0.5 uM">, <img src="https://render.githubusercontent.com/render/math?math=O_{\delta}">: <img src="https://render.githubusercontent.com/render/math?math=0.0002 mM/s">, <img src="https://render.githubusercontent.com/render/math?math=d_{2}">: <img src="https://render.githubusercontent.com/render/math?math=1.05 uM">, <img src="https://render.githubusercontent.com/render/math?math=\omega_{I}">: <img src="https://render.githubusercontent.com/render/math?math=50. nM">


**StateMonitor(s) defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=\Gamma_{A}">,<img src="https://render.githubusercontent.com/render/math?math=C">,<img src="https://render.githubusercontent.com/render/math?math=h">,<img src="https://render.githubusercontent.com/render/math?math=I"> of neurongroup_2 for all members with time step <img src="https://render.githubusercontent.com/render/math?math=1. ms">.


**Synapses defined:**
- 	From neurongroup to neurongroup_1

	**Dynamics:**

		<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} Y_{S}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \Omega_{c}.Y_{S}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=Y_{S}"> is mM and clock-driven as flag(s) associated

	exact method is used for integration

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=Y_{S}">+=<img src="https://render.githubusercontent.com/render/math?math=Y_{T}.\rho_{c}"> is executed

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=\rho_{c}">: <img src="https://render.githubusercontent.com/render/math?math=0.001">, <img src="https://render.githubusercontent.com/render/math?math=Y_{T}">: <img src="https://render.githubusercontent.com/render/math?math=0.5 M">, <img src="https://render.githubusercontent.com/render/math?math=\Omega_{c}">: <img src="https://render.githubusercontent.com/render/math?math=40. Hz">

- 	From synapses to neurongroup_2

	**Summed variables: **

	Updates target group neurongroup_2 with statement: <img src="https://render.githubusercontent.com/render/math?math=Y_{S pre}">


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=h"> of neurongroup_2 initialized with <img src="https://render.githubusercontent.com/render/math?math=0.9"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=noise"> of neurongroup_2 initialized with <img src="https://render.githubusercontent.com/render/math?math=[0. 1.]"> to all members 


**Synaptic Connection(s) defined:**
- Connection from neurongroup to neurongroup_1

- Connection from synapses to neurongroup_2

