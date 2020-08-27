# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **8. s**

**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=i">,<img src="https://render.githubusercontent.com/render/math?math=t"> of neurongroup_subgroup. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.

- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=i">,<img src="https://render.githubusercontent.com/render/math?math=t"> of neurongroup_subgroup_1. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.

- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=i">,<img src="https://render.githubusercontent.com/render/math?math=t"> of neurongroup_1. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=10. ms"> when event **spike** is triggered.


**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **4000**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{I_{ex}.{stimulus}{\left(t \right)} + g_{e}.\left(E_{e} - v\right) + g_{i}.\left(E_{i} - v\right) + g_{l}.\left(E_{l} - v\right)}{C_{m}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is V and unless refractory as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} g_{e}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{g_{e}}{\tau_{e}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=g_{e}"> is S

	Parameter <img src="https://render.githubusercontent.com/render/math?math=y">, where unit of <img src="https://render.githubusercontent.com/render/math?math=y"> is m and constant as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} g_{i}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{g_{i}}{\tau_{i}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=g_{i}"> is S

	Parameter <img src="https://render.githubusercontent.com/render/math?math=x">, where unit of <img src="https://render.githubusercontent.com/render/math?math=x"> is m and constant as flag(s) associated

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt V_{th}">, <img src="https://render.githubusercontent.com/render/math?math=v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=V_{r}">, with refractory <img src="https://render.githubusercontent.com/render/math?math=\tau_{r}">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=I_{ex}">: <img src="https://render.githubusercontent.com/render/math?math=100. pA">, <img src="https://render.githubusercontent.com/render/math?math=g_{l}">: <img src="https://render.githubusercontent.com/render/math?math=9.99 nS">, <img src="https://render.githubusercontent.com/render/math?math=V_{r}">: <img src="https://render.githubusercontent.com/render/math?math=-60. mV">, <img src="https://render.githubusercontent.com/render/math?math=E_{l}">: <img src="https://render.githubusercontent.com/render/math?math=-60. mV">, <img src="https://render.githubusercontent.com/render/math?math=V_{th}">: <img src="https://render.githubusercontent.com/render/math?math=-50. mV">, <img src="https://render.githubusercontent.com/render/math?math=E_{e}">: <img src="https://render.githubusercontent.com/render/math?math=0. V">, <img src="https://render.githubusercontent.com/render/math?math=C_{m}">: <img src="https://render.githubusercontent.com/render/math?math=198. pF">, <img src="https://render.githubusercontent.com/render/math?math=\tau_{e}">: <img src="https://render.githubusercontent.com/render/math?math=5. ms">, <img src="https://render.githubusercontent.com/render/math?math=E_{i}">: <img src="https://render.githubusercontent.com/render/math?math=-80. mV">, <img src="https://render.githubusercontent.com/render/math?math=stimulus"> of type timedarray with dimentsion <img src="https://render.githubusercontent.com/render/math?math=1"> and dt as <img src="https://render.githubusercontent.com/render/math?math=2. s">, <img src="https://render.githubusercontent.com/render/math?math=\tau_{i}">: <img src="https://render.githubusercontent.com/render/math?math=10. ms">

- Name **neurongroup\_1**, with                population size **3200**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} h">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{- h + h_{inf}}{\tau_{h}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=h"> is rad

	Parameter <img src="https://render.githubusercontent.com/render/math?math=y">, where unit of <img src="https://render.githubusercontent.com/render/math?math=y"> is m and constant as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} C">&#8592;<img src="https://render.githubusercontent.com/render/math?math=J_{l} - J_{p} + J_{r}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=C"> is mM

	<img src="https://render.githubusercontent.com/render/math?math=h_{inf}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{Q_{2}}{C + Q_{2}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=h_{inf}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=J_{p}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{C^{2}.O_{P}}{C^{2} + K_{P}^{2}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=J_{p}"> is mM/s

	Parameter <img src="https://render.githubusercontent.com/render/math?math=x">, where unit of <img src="https://render.githubusercontent.com/render/math?math=x"> is m and constant as flag(s) associated

	Parameter <img src="https://render.githubusercontent.com/render/math?math=Y_{S}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=Y_{S}"> is mM

	Parameter <img src="https://render.githubusercontent.com/render/math?math=J_{coupling}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=J_{coupling}"> is mM/s

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} I">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- J_{3K} - J_{5P} + J_{\beta} + J_{coupling} + J_{\delta}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=I"> is mM

	<img src="https://render.githubusercontent.com/render/math?math=J_{\beta}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\Gamma_{A}.O_{\beta}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=J_{\beta}"> is mM/s

	<img src="https://render.githubusercontent.com/render/math?math=m_{inf}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{C.I}{\left(C + d_{5}\right).\left(I + d_{1}\right)}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=m_{inf}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} G_{A}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- G_{A}.\Omega_{e}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=G_{A}"> is mM

	<img src="https://render.githubusercontent.com/render/math?math=J_{\delta}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{C^{2}.O_{\delta}}{\left(C^{2} + K_{\delta}^{2}\right).\left(\frac{I}{\kappa_{\delta}} + 1\right)}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=J_{\delta}"> is mM/s

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} \Gamma_{A}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=O_{N}.Y_{S}.\left(1 - {clip}{\left(\Gamma_{A},0,1 \right)}\right) - \Omega_{N}.\left(\frac{C.\zeta}{C + K_{KC}} + 1\right).{clip}{\left(\Gamma_{A},0,1 \right)}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\Gamma_{A}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=Q_{2}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{d_{2}.\left(I + d_{1}\right)}{I + d_{3}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=Q_{2}"> is mM

	<img src="https://render.githubusercontent.com/render/math?math=J_{l}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\Omega_{L}.\left(- C.\left(\rho_{A} + 1\right) + C_{T}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=J_{l}"> is mM/s

	<img src="https://render.githubusercontent.com/render/math?math=J_{r}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\Omega_{C}.h^{3}.m_{inf}^{3}.\left(- C.\left(\rho_{A} + 1\right) + C_{T}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=J_{r}"> is mM/s

	<img src="https://render.githubusercontent.com/render/math?math=J_{3K}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{C^{4}.I.O_{3K}}{\left(C^{4} + K_{D}^{4}\right).\left(I + K_{3K}\right)}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=J_{3K}"> is mM/s

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} x_{A}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\Omega_{A}.\left(1 - x_{A}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=x_{A}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=J_{5P}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=I.\Omega_{5P}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=J_{5P}"> is mM/s

	<img src="https://render.githubusercontent.com/render/math?math=\tau_{h}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{1}{O_{2}.\left(C + Q_{2}\right)}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\tau_{h}"> is s

	rk4 method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=C \gt C_{\Theta}">, , <img src="https://render.githubusercontent.com/render/math?math=G_{A}">+=<img src="https://render.githubusercontent.com/render/math?math=G_{T}.U_{A}.\rho_{e}.x_{A}">, <img src="https://render.githubusercontent.com/render/math?math=x_{A}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=U_{A}.x_{A}">, , with refractory <img src="https://render.githubusercontent.com/render/math?math=C \gt C_{\Theta}">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=\Omega_{e}">: <img src="https://render.githubusercontent.com/render/math?math=60. Hz">, <img src="https://render.githubusercontent.com/render/math?math=\zeta">: <img src="https://render.githubusercontent.com/render/math?math=10">, <img src="https://render.githubusercontent.com/render/math?math=\Omega_{5P}">: <img src="https://render.githubusercontent.com/render/math?math=50. mHz">, <img src="https://render.githubusercontent.com/render/math?math=\rho_{e}">: <img src="https://render.githubusercontent.com/render/math?math=0.00065">, <img src="https://render.githubusercontent.com/render/math?math=d_{3}">: <img src="https://render.githubusercontent.com/render/math?math=0.9434 uM">, <img src="https://render.githubusercontent.com/render/math?math=K_{P}">: <img src="https://render.githubusercontent.com/render/math?math=50. nM">, <img src="https://render.githubusercontent.com/render/math?math=K_{\delta}">: <img src="https://render.githubusercontent.com/render/math?math=100. nM">, <img src="https://render.githubusercontent.com/render/math?math=\rho_{A}">: <img src="https://render.githubusercontent.com/render/math?math=0.18">, <img src="https://render.githubusercontent.com/render/math?math=O_{\beta}">: <img src="https://render.githubusercontent.com/render/math?math=0.0005 mM/s">, <img src="https://render.githubusercontent.com/render/math?math=d_{5}">: <img src="https://render.githubusercontent.com/render/math?math=80. nM">, <img src="https://render.githubusercontent.com/render/math?math=\Omega_{C}">: <img src="https://render.githubusercontent.com/render/math?math=6. Hz">, <img src="https://render.githubusercontent.com/render/math?math=\Omega_{N}">: <img src="https://render.githubusercontent.com/render/math?math=0.5 Hz">, <img src="https://render.githubusercontent.com/render/math?math=O_{P}">: <img src="https://render.githubusercontent.com/render/math?math=0.0009 mM/s">, <img src="https://render.githubusercontent.com/render/math?math=\Omega_{A}">: <img src="https://render.githubusercontent.com/render/math?math=0.6 Hz">, <img src="https://render.githubusercontent.com/render/math?math=O_{\delta}">: <img src="https://render.githubusercontent.com/render/math?math=0.0012 mM/s">, <img src="https://render.githubusercontent.com/render/math?math=d_{1}">: <img src="https://render.githubusercontent.com/render/math?math=130. nM">, <img src="https://render.githubusercontent.com/render/math?math=C_{T}">: <img src="https://render.githubusercontent.com/render/math?math=2. uM">, <img src="https://render.githubusercontent.com/render/math?math=K_{KC}">: <img src="https://render.githubusercontent.com/render/math?math=0.5 uM">, <img src="https://render.githubusercontent.com/render/math?math=O_{N}">: <img src="https://render.githubusercontent.com/render/math?math=300. m^3 s^-1 mol^-1">, <img src="https://render.githubusercontent.com/render/math?math=\Omega_{L}">: <img src="https://render.githubusercontent.com/render/math?math=100. mHz">, <img src="https://render.githubusercontent.com/render/math?math=d_{2}">: <img src="https://render.githubusercontent.com/render/math?math=1.05 uM">, <img src="https://render.githubusercontent.com/render/math?math=U_{A}">: <img src="https://render.githubusercontent.com/render/math?math=0.6">, <img src="https://render.githubusercontent.com/render/math?math=\kappa_{\delta}">: <img src="https://render.githubusercontent.com/render/math?math=1.5 uM">, <img src="https://render.githubusercontent.com/render/math?math=O_{2}">: <img src="https://render.githubusercontent.com/render/math?math=200. m^3 s^-1 mol^-1">, <img src="https://render.githubusercontent.com/render/math?math=K_{3K}">: <img src="https://render.githubusercontent.com/render/math?math=1. uM">, <img src="https://render.githubusercontent.com/render/math?math=K_{D}">: <img src="https://render.githubusercontent.com/render/math?math=0.7 uM">, <img src="https://render.githubusercontent.com/render/math?math=C_{\Theta}">: <img src="https://render.githubusercontent.com/render/math?math=0.5 uM">, <img src="https://render.githubusercontent.com/render/math?math=G_{T}">: <img src="https://render.githubusercontent.com/render/math?math=200. mM">, <img src="https://render.githubusercontent.com/render/math?math=O_{3K}">: <img src="https://render.githubusercontent.com/render/math?math=0.0045 mM/s">


**Synapses defined:**
- 	From neurongroup_1 to neurongroup_1

	**Dynamics:**

		<img src="https://render.githubusercontent.com/render/math?math=\delta_{I}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=I_{post} - I_{pre}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\delta_{I}"> is mM

	**Summed variables: **

	Updates target group neurongroup_1 with statement: <img src="https://render.githubusercontent.com/render/math?math=\frac{F.\left(- \tanh{\left(\frac{- I_{\Theta} + \left|{\delta_{I}}\right|}{\omega_{I}} \right)} - 1\right).{sign}{\left(\delta_{I} \right)}}{2}">

- 	From neurongroup_subgroup_1 to neurongroup

	**Dynamics:**

		<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} \Gamma_{S}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=G_{A}.O_{G}.\left(1 - \Gamma_{S}\right) - \Gamma_{S}.\Omega_{G}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\Gamma_{S}"> is rad and clock-driven as flag(s) associated

	Parameter <img src="https://render.githubusercontent.com/render/math?math=U_{0}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=U_{0}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} Y_{S}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \Omega_{c}.Y_{S}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=Y_{S}"> is mM and clock-driven as flag(s) associated

	Parameter <img src="https://render.githubusercontent.com/render/math?math=astrocyte_{index}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=astrocyte_{index}"> is rad and constant as flag(s) associated

	Parameter <img src="https://render.githubusercontent.com/render/math?math=G_{A}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=G_{A}"> is mM

	Parameter <img src="https://render.githubusercontent.com/render/math?math=r_{S}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=r_{S}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} u_{S}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \Omega_{f}.u_{S}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=u_{S}"> is rad and event-driven as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} x_{S}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\Omega_{d}.\left(1 - x_{S}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=x_{S}"> is rad and event-driven as flag(s) associated

	exact method is used for integration

	**Pathways:**

	On **pre** of event spike statement(s): , <img src="https://render.githubusercontent.com/render/math?math=U_{0}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\Gamma_{S}.\alpha + U^{star}_{0}.\left(1 - \Gamma_{S}\right)">, <img src="https://render.githubusercontent.com/render/math?math=u_{S}">+=<img src="https://render.githubusercontent.com/render/math?math=U_{0}.\left(1 - u_{S}\right)">, <img src="https://render.githubusercontent.com/render/math?math=r_{S}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=u_{S}.x_{S}">, <img src="https://render.githubusercontent.com/render/math?math=x_{S}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=r_{S}">, <img src="https://render.githubusercontent.com/render/math?math=Y_{S}">+=<img src="https://render.githubusercontent.com/render/math?math=Y_{T}.r_{S}.\rho_{c}">, <img src="https://render.githubusercontent.com/render/math?math=g_{i post}">+=<img src="https://render.githubusercontent.com/render/math?math=r_{S}.w_{i}"> is executed

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=\alpha">: <img src="https://render.githubusercontent.com/render/math?math=0.0">, <img src="https://render.githubusercontent.com/render/math?math=O_{G}">: <img src="https://render.githubusercontent.com/render/math?math=1500. m^3 s^-1 mol^-1">, <img src="https://render.githubusercontent.com/render/math?math=\Omega_{f}">: <img src="https://render.githubusercontent.com/render/math?math=3.33 Hz">, <img src="https://render.githubusercontent.com/render/math?math=\Omega_{c}">: <img src="https://render.githubusercontent.com/render/math?math=40. Hz">, <img src="https://render.githubusercontent.com/render/math?math=\Omega_{G}">: <img src="https://render.githubusercontent.com/render/math?math=8.33333333 mHz">, <img src="https://render.githubusercontent.com/render/math?math=Y_{T}">: <img src="https://render.githubusercontent.com/render/math?math=0.5 M">, <img src="https://render.githubusercontent.com/render/math?math=U^{star}_{0}">: <img src="https://render.githubusercontent.com/render/math?math=0.6">, <img src="https://render.githubusercontent.com/render/math?math=\rho_{c}">: <img src="https://render.githubusercontent.com/render/math?math=0.005">, <img src="https://render.githubusercontent.com/render/math?math=w_{i}">: <img src="https://render.githubusercontent.com/render/math?math=1. nS">, <img src="https://render.githubusercontent.com/render/math?math=\Omega_{d}">: <img src="https://render.githubusercontent.com/render/math?math=2. Hz">

- 	From neurongroup_1 to synapses

	**Summed variables: **

	Updates target group synapses with statement: <img src="https://render.githubusercontent.com/render/math?math=G_{A pre}">

- 	From neurongroup_subgroup to neurongroup

	**Dynamics:**

		<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} \Gamma_{S}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=G_{A}.O_{G}.\left(1 - \Gamma_{S}\right) - \Gamma_{S}.\Omega_{G}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\Gamma_{S}"> is rad and clock-driven as flag(s) associated

	Parameter <img src="https://render.githubusercontent.com/render/math?math=U_{0}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=U_{0}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} Y_{S}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \Omega_{c}.Y_{S}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=Y_{S}"> is mM and clock-driven as flag(s) associated

	Parameter <img src="https://render.githubusercontent.com/render/math?math=astrocyte_{index}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=astrocyte_{index}"> is rad and constant as flag(s) associated

	Parameter <img src="https://render.githubusercontent.com/render/math?math=G_{A}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=G_{A}"> is mM

	Parameter <img src="https://render.githubusercontent.com/render/math?math=r_{S}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=r_{S}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} u_{S}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \Omega_{f}.u_{S}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=u_{S}"> is rad and event-driven as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} x_{S}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\Omega_{d}.\left(1 - x_{S}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=x_{S}"> is rad and event-driven as flag(s) associated

	exact method is used for integration

	**Pathways:**

	On **pre** of event spike statement(s): , <img src="https://render.githubusercontent.com/render/math?math=U_{0}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\Gamma_{S}.\alpha + U^{star}_{0}.\left(1 - \Gamma_{S}\right)">, <img src="https://render.githubusercontent.com/render/math?math=u_{S}">+=<img src="https://render.githubusercontent.com/render/math?math=U_{0}.\left(1 - u_{S}\right)">, <img src="https://render.githubusercontent.com/render/math?math=r_{S}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=u_{S}.x_{S}">, <img src="https://render.githubusercontent.com/render/math?math=x_{S}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=r_{S}">, <img src="https://render.githubusercontent.com/render/math?math=Y_{S}">+=<img src="https://render.githubusercontent.com/render/math?math=Y_{T}.r_{S}.\rho_{c}">, <img src="https://render.githubusercontent.com/render/math?math=g_{e post}">+=<img src="https://render.githubusercontent.com/render/math?math=r_{S}.w_{e}"> is executed

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=\alpha">: <img src="https://render.githubusercontent.com/render/math?math=0.0">, <img src="https://render.githubusercontent.com/render/math?math=w_{e}">: <img src="https://render.githubusercontent.com/render/math?math=50. pS">, <img src="https://render.githubusercontent.com/render/math?math=O_{G}">: <img src="https://render.githubusercontent.com/render/math?math=1500. m^3 s^-1 mol^-1">, <img src="https://render.githubusercontent.com/render/math?math=\Omega_{f}">: <img src="https://render.githubusercontent.com/render/math?math=3.33 Hz">, <img src="https://render.githubusercontent.com/render/math?math=\Omega_{c}">: <img src="https://render.githubusercontent.com/render/math?math=40. Hz">, <img src="https://render.githubusercontent.com/render/math?math=\Omega_{G}">: <img src="https://render.githubusercontent.com/render/math?math=8.33333333 mHz">, <img src="https://render.githubusercontent.com/render/math?math=Y_{T}">: <img src="https://render.githubusercontent.com/render/math?math=0.5 M">, <img src="https://render.githubusercontent.com/render/math?math=U^{star}_{0}">: <img src="https://render.githubusercontent.com/render/math?math=0.6">, <img src="https://render.githubusercontent.com/render/math?math=\rho_{c}">: <img src="https://render.githubusercontent.com/render/math?math=0.005">, <img src="https://render.githubusercontent.com/render/math?math=\Omega_{d}">: <img src="https://render.githubusercontent.com/render/math?math=2. Hz">

- 	From synapses to neurongroup_1

	**Summed variables: **

	Updates target group neurongroup_1 with statement: <img src="https://render.githubusercontent.com/render/math?math=\frac{Y_{S pre}}{N_{incoming}}">


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=x"> of neurongroup_subgroup initialized with <img src="https://render.githubusercontent.com/render/math?math=- 0.5.N_{rows}.grid_{dist} + grid_{dist}.\left\lfloor{\frac{i}{N_{rows}}}\right\rfloor"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=grid_{dist}">: <img src="https://render.githubusercontent.com/render/math?math=65.78947368 um">, <img src="https://render.githubusercontent.com/render/math?math=N_{rows}">: <img src="https://render.githubusercontent.com/render/math?math=56">



- Variable <img src="https://render.githubusercontent.com/render/math?math=y"> of neurongroup_subgroup initialized with <img src="https://render.githubusercontent.com/render/math?math=- 0.5.N_{cols}.grid_{dist} + \left(grid_{dist}.\left(i\bmod{N_{rows}}\right)\right)"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=N_{cols}">: <img src="https://render.githubusercontent.com/render/math?math=57">, <img src="https://render.githubusercontent.com/render/math?math=grid_{dist}">: <img src="https://render.githubusercontent.com/render/math?math=65.78947368 um">, <img src="https://render.githubusercontent.com/render/math?math=N_{rows}">: <img src="https://render.githubusercontent.com/render/math?math=56">



- Variable <img src="https://render.githubusercontent.com/render/math?math=v"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=E_{l} + \left(- E_{l} + V_{th}\right).{rand}{\left(- \right)}"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=E_{l}">: <img src="https://render.githubusercontent.com/render/math?math=-60. mV">, <img src="https://render.githubusercontent.com/render/math?math=V_{th}">: <img src="https://render.githubusercontent.com/render/math?math=-50. mV">



- Variable <img src="https://render.githubusercontent.com/render/math?math=g_{e}"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=w_{e}.{rand}{\left(- \right)}"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=w_{e}">: <img src="https://render.githubusercontent.com/render/math?math=50. pS">



- Variable <img src="https://render.githubusercontent.com/render/math?math=g_{i}"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=w_{i}.{rand}{\left(- \right)}"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=w_{i}">: <img src="https://render.githubusercontent.com/render/math?math=1. nS">



- Variable <img src="https://render.githubusercontent.com/render/math?math=x_{S}"> of synapses initialized with <img src="https://render.githubusercontent.com/render/math?math=1."> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=x_{S}"> of synapses_1 initialized with <img src="https://render.githubusercontent.com/render/math?math=1."> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=astrocyte_{index}"> of synapses initialized with <img src="https://render.githubusercontent.com/render/math?math=N_{cols a}.{int_{}}{\left(\frac{y_{post}}{grid_{dist}} \right)} + {int_{}}{\left(\frac{x_{post}}{grid_{dist}} \right)}"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=N_{cols a}">: <img src="https://render.githubusercontent.com/render/math?math=57.1428571428571">, <img src="https://render.githubusercontent.com/render/math?math=grid_{dist}">: <img src="https://render.githubusercontent.com/render/math?math=66.96428571 um">



- Variable <img src="https://render.githubusercontent.com/render/math?math=x"> of neurongroup_1 initialized with <img src="https://render.githubusercontent.com/render/math?math=- 0.5.N_{rows a}.grid_{dist} + grid_{dist}.\left\lfloor{\frac{i}{N_{rows a}}}\right\rfloor"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=N_{rows a}">: <img src="https://render.githubusercontent.com/render/math?math=56">, <img src="https://render.githubusercontent.com/render/math?math=grid_{dist}">: <img src="https://render.githubusercontent.com/render/math?math=66.96428571 um">



- Variable <img src="https://render.githubusercontent.com/render/math?math=y"> of neurongroup_1 initialized with <img src="https://render.githubusercontent.com/render/math?math=- 0.5.N_{cols a}.grid_{dist} + \left(grid_{dist}.\left(i\bmod{N_{rows a}}\right)\right)"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=N_{rows a}">: <img src="https://render.githubusercontent.com/render/math?math=56">, <img src="https://render.githubusercontent.com/render/math?math=N_{cols a}">: <img src="https://render.githubusercontent.com/render/math?math=57.1428571428571">, <img src="https://render.githubusercontent.com/render/math?math=grid_{dist}">: <img src="https://render.githubusercontent.com/render/math?math=66.96428571 um">



- Variable <img src="https://render.githubusercontent.com/render/math?math=C"> of neurongroup_1 initialized with <img src="https://render.githubusercontent.com/render/math?math=10. nM"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=h"> of neurongroup_1 initialized with <img src="https://render.githubusercontent.com/render/math?math=0.9"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=I"> of neurongroup_1 initialized with <img src="https://render.githubusercontent.com/render/math?math=10. nM"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=x_{A}"> of neurongroup_1 initialized with <img src="https://render.githubusercontent.com/render/math?math=1."> to all members 


**Synaptic Connection(s) defined:**
- Connection from neurongroup_subgroup to neurongroup, with probabilty <img src="https://render.githubusercontent.com/render/math?math=0.05">

- Connection from neurongroup_subgroup_1 to neurongroup, with probabilty <img src="https://render.githubusercontent.com/render/math?math=0.2">

- Connection from neurongroup_1 to synapses with condition <img src="https://render.githubusercontent.com/render/math?math=i = astrocyte_{index post}">

- Connection from synapses to neurongroup_1 with condition <img src="https://render.githubusercontent.com/render/math?math=astrocyte_{index pre} = j">

- Connection from neurongroup_1 to neurongroup_1 with condition <img src="https://render.githubusercontent.com/render/math?math=\sqrt{\left(\left(- x_{post} + x_{pre}\right)^{2} + \left(- y_{post} + y_{pre}\right)^{2} \right)} \lt 75.um \wedge i \neq j">

