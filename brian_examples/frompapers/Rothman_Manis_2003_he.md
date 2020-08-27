# Network details
The Network consists of **2**                            simulation runs
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **50. ms**

**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **1**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=ztau">&#8592;<img src="https://render.githubusercontent.com/render/math?math=ms.\left(50 + \frac{1000.0}{20.0855369231877.e^{0.05.vu} + 0.000553084370147834.e^{- 0.125.vu}}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ztau"> is s

	<img src="https://render.githubusercontent.com/render/math?math=pinf">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{1.0}{1 + 0.0216373707194931.e^{- 0.166666666666667.vu}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=pinf"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=minf">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{1.0}{1 + 0.00438936184277844.e^{- 0.142857142857143.vu}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=minf"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=ileak">&#8592;<img src="https://render.githubusercontent.com/render/math?math=gl.\left(El - v\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ileak"> is A

	<img src="https://render.githubusercontent.com/render/math?math=rtau">&#8592;<img src="https://render.githubusercontent.com/render/math?math=ms.\left(25.0 + \frac{100000.0}{35173.9187073107.e^{0.0833333333333333.vu} + 0.233984374461857.e^{- 0.0714285714285714.vu}}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=rtau"> is s

	<img src="https://render.githubusercontent.com/render/math?math=ihcno">&#8592;<img src="https://render.githubusercontent.com/render/math?math=gbarno.\left(Eh - v\right).\left(frac.h_{1} + h_{2}.\left(1 - frac\right)\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ihcno"> is A

	<img src="https://render.githubusercontent.com/render/math?math=hinfno">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{1.0}{12438.7443981114.e^{0.142857142857143.vu} + 1}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=hinfno"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} c">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{q_{10}.\left(- c + cinf\right)}{ctau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=c"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=ainf">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{1.0}{\left(1 + 0.00570354899800741.e^{- 0.166666666666667.vu}\right)^{0.25}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ainf"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=alp_{1}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=e^{\frac{289.44.vu + 14472.0}{8.315.temp + 2271.3254}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=alp_{1}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=ih">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\bar{gh}.r.\left(Eh - v\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ih"> is A

	<img src="https://render.githubusercontent.com/render/math?math=\tau_{1}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{125.0.bet_{1}.ms}{qt.\left(alp_{1} + 1\right)}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\tau_{1}"> is s

	<img src="https://render.githubusercontent.com/render/math?math=htau">&#8592;<img src="https://render.githubusercontent.com/render/math?math=ms.\left(0.6 + \frac{100.0}{1636.72996021326.e^{0.0909090909090909.vu} + 0.907179532894125.e^{- 0.04.vu}}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=htau"> is s

	<img src="https://render.githubusercontent.com/render/math?math=binf">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{0.0089662682574368}{\left(e^{0.142857142857143.vu} + 8.03939664643187.10^{-5}\right)^{0.5}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=binf"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=ntau">&#8592;<img src="https://render.githubusercontent.com/render/math?math=ms.\left(0.7 + \frac{100.0}{134.007433567738.e^{0.0416666666666667.vu} + 1.54624094027712.e^{- 0.0434782608695652.vu}}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ntau"> is s

	<img src="https://render.githubusercontent.com/render/math?math=ina">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\bar{gna}.h.m^{3}.\left(ENa - v\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ina"> is A

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} h_{2}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{- h_{2} + hinfno}{\tau_{2}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=h_{2}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\tau_{2}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{344.827586206897.bet_{2}.ms}{qt.\left(alp_{2} + 1\right)}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\tau_{2}"> is s

	<img src="https://render.githubusercontent.com/render/math?math=ctau">&#8592;<img src="https://render.githubusercontent.com/render/math?math=ms.\left(10 + \frac{90.0}{1 + 0.0206022921249195.e^{- 0.0588235294117647.vu}}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ctau"> is s

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} p">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{q_{10}.\left(- p + pinf\right)}{ptau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=p"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=cinf">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{0.0089662682574368}{\left(e^{0.142857142857143.vu} + 8.03939664643187.10^{-5}\right)^{0.5}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=cinf"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=zinf">&#8592;<img src="https://render.githubusercontent.com/render/math?math=zss + \frac{1.0 - zss}{1211.96707449258.e^{0.1.vu} + 1}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=zinf"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=ptau">&#8592;<img src="https://render.githubusercontent.com/render/math?math=ms.\left(5 + \frac{100.0}{26.0832764813204.e^{0.03125.vu} + 0.326987016149301.e^{- 0.0454545454545455.vu}}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ptau"> is s

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} h_{1}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{- h_{1} + hinfno}{\tau_{1}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=h_{1}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=atau">&#8592;<img src="https://render.githubusercontent.com/render/math?math=ms.\left(0.1 + \frac{100.0}{508.580969450158.e^{0.0714285714285714.vu} + 2.38046496009307.e^{- 0.0416666666666667.vu}}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=atau"> is s

	<img src="https://render.githubusercontent.com/render/math?math=wtau">&#8592;<img src="https://render.githubusercontent.com/render/math?math=ms.\left(1.5 + \frac{100.0}{132158.79476884.e^{0.166666666666667.vu} + 4.21755420985163.e^{- 0.0222222222222222.vu}}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=wtau"> is s

	<img src="https://render.githubusercontent.com/render/math?math=ninf">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\left(1 + 0.0497870683678639.e^{- 0.2.vu}\right)^{-0.5}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ninf"> is rad

	Parameter <img src="https://render.githubusercontent.com/render/math?math=I">, where unit of <img src="https://render.githubusercontent.com/render/math?math=I"> is A

	<img src="https://render.githubusercontent.com/render/math?math=winf">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{1.0}{\left(1 + 0.000335462627902512.e^{- 0.166666666666667.vu}\right)^{0.25}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=winf"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=bet_{2}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=e^{\frac{173.664.vu + 14587.776}{8.315.temp + 2271.3254}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=bet_{2}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} r">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{q_{10}.\left(- r + rinf\right)}{rtau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=r"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=btau">&#8592;<img src="https://render.githubusercontent.com/render/math?math=ms.\left(1 + \frac{1000.0}{129.189400929953.e^{0.037037037037037.vu} + 2.38046496009307.e^{- 0.0416666666666667.vu}}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=btau"> is s

	<img src="https://render.githubusercontent.com/render/math?math=mtau">&#8592;<img src="https://render.githubusercontent.com/render/math?math=ms.\left(0.04 + \frac{10.0}{140.158124472631.e^{0.0555555555555556.vu} + 3.26584631841885.e^{- 0.04.vu}}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=mtau"> is s

	<img src="https://render.githubusercontent.com/render/math?math=hinf">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{1.0}{50682.3667554257.e^{0.166666666666667.vu} + 1}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=hinf"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=rinf">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{1.0}{51903.5702194154.e^{0.142857142857143.vu} + 1}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=rinf"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=iklt">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\bar{gklt}.w^{4}.z.\left(EK - v\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=iklt"> is A

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} h">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{q_{10}.\left(- h + hinf\right)}{htau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=h"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=vu">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{v}{mV}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=vu"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=ikht">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\bar{gkht}.\left(EK - v\right).\left(n^{2}.nf + p.\left(1 - nf\right)\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ikht"> is A

	<img src="https://render.githubusercontent.com/render/math?math=ika">&#8592;<img src="https://render.githubusercontent.com/render/math?math=a^{4}.b.c.\bar{gka}.\left(EK - v\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ika"> is A

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} z">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{q_{10}.\left(- z + zinf\right)}{ztau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=z"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} m">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{q_{10}.\left(- m + minf\right)}{mtau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=m"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=bet_{1}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=e^{\frac{86.832.vu + 4341.6}{8.315.temp + 2271.3254}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=bet_{1}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} n">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{q_{10}.\left(- n + ninf\right)}{ntau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=n"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} b">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{q_{10}.\left(- b + binf\right)}{btau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=b"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{I + ih + ihcno + ika + ikht + iklt + ileak + ina}{C}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is V

	<img src="https://render.githubusercontent.com/render/math?math=alp_{2}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=e^{\frac{289.44.vu + 24312.96}{8.315.temp + 2271.3254}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=alp_{2}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} w">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{q_{10}.\left(- w + winf\right)}{wtau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=w"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} a">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{q_{10}.\left(- a + ainf\right)}{atau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=a"> is rad

	exponential_euler method is used for integration

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=C">: <img src="https://render.githubusercontent.com/render/math?math=12. pF">, <img src="https://render.githubusercontent.com/render/math?math=\bar{gklt}">: <img src="https://render.githubusercontent.com/render/math?math=0. S">, <img src="https://render.githubusercontent.com/render/math?math=zss">: <img src="https://render.githubusercontent.com/render/math?math=0.5">, <img src="https://render.githubusercontent.com/render/math?math=temp">: <img src="https://render.githubusercontent.com/render/math?math=22.0">, <img src="https://render.githubusercontent.com/render/math?math=El">: <img src="https://render.githubusercontent.com/render/math?math=-65. mV">, <img src="https://render.githubusercontent.com/render/math?math=EK">: <img src="https://render.githubusercontent.com/render/math?math=-70. mV">, <img src="https://render.githubusercontent.com/render/math?math=\bar{gh}">: <img src="https://render.githubusercontent.com/render/math?math=0.5 nS">, <img src="https://render.githubusercontent.com/render/math?math=gbarno">: <img src="https://render.githubusercontent.com/render/math?math=0. S">, <img src="https://render.githubusercontent.com/render/math?math=\bar{gka}">: <img src="https://render.githubusercontent.com/render/math?math=0. S">, <img src="https://render.githubusercontent.com/render/math?math=gl">: <img src="https://render.githubusercontent.com/render/math?math=2. nS">, <img src="https://render.githubusercontent.com/render/math?math=\bar{gna}">: <img src="https://render.githubusercontent.com/render/math?math=1. uS">, <img src="https://render.githubusercontent.com/render/math?math=ENa">: <img src="https://render.githubusercontent.com/render/math?math=50. mV">, <img src="https://render.githubusercontent.com/render/math?math=nf">: <img src="https://render.githubusercontent.com/render/math?math=0.85">, <img src="https://render.githubusercontent.com/render/math?math=q_{10}">: <img src="https://render.githubusercontent.com/render/math?math=1.0">, <img src="https://render.githubusercontent.com/render/math?math=frac">: <img src="https://render.githubusercontent.com/render/math?math=0.0">, <img src="https://render.githubusercontent.com/render/math?math=\bar{gkht}">: <img src="https://render.githubusercontent.com/render/math?math=150. nS">, <img src="https://render.githubusercontent.com/render/math?math=qt">: <img src="https://render.githubusercontent.com/render/math?math=0.191190467371012">, <img src="https://render.githubusercontent.com/render/math?math=Eh">: <img src="https://render.githubusercontent.com/render/math?math=-43. mV">


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=v"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=-65. mV"> to all members 

### Run 2 details
Duration of simulation is **100. ms**

**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **1**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=ztau">&#8592;<img src="https://render.githubusercontent.com/render/math?math=ms.\left(50 + \frac{1000.0}{20.0855369231877.e^{0.05.vu} + 0.000553084370147834.e^{- 0.125.vu}}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ztau"> is s

	<img src="https://render.githubusercontent.com/render/math?math=pinf">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{1.0}{1 + 0.0216373707194931.e^{- 0.166666666666667.vu}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=pinf"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=minf">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{1.0}{1 + 0.00438936184277844.e^{- 0.142857142857143.vu}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=minf"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=ileak">&#8592;<img src="https://render.githubusercontent.com/render/math?math=gl.\left(El - v\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ileak"> is A

	<img src="https://render.githubusercontent.com/render/math?math=rtau">&#8592;<img src="https://render.githubusercontent.com/render/math?math=ms.\left(25.0 + \frac{100000.0}{35173.9187073107.e^{0.0833333333333333.vu} + 0.233984374461857.e^{- 0.0714285714285714.vu}}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=rtau"> is s

	<img src="https://render.githubusercontent.com/render/math?math=ihcno">&#8592;<img src="https://render.githubusercontent.com/render/math?math=gbarno.\left(Eh - v\right).\left(frac.h_{1} + h_{2}.\left(1 - frac\right)\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ihcno"> is A

	<img src="https://render.githubusercontent.com/render/math?math=hinfno">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{1.0}{12438.7443981114.e^{0.142857142857143.vu} + 1}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=hinfno"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} c">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{q_{10}.\left(- c + cinf\right)}{ctau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=c"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=ainf">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{1.0}{\left(1 + 0.00570354899800741.e^{- 0.166666666666667.vu}\right)^{0.25}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ainf"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=alp_{1}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=e^{\frac{289.44.vu + 14472.0}{8.315.temp + 2271.3254}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=alp_{1}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=ih">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\bar{gh}.r.\left(Eh - v\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ih"> is A

	<img src="https://render.githubusercontent.com/render/math?math=\tau_{1}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{125.0.bet_{1}.ms}{qt.\left(alp_{1} + 1\right)}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\tau_{1}"> is s

	<img src="https://render.githubusercontent.com/render/math?math=htau">&#8592;<img src="https://render.githubusercontent.com/render/math?math=ms.\left(0.6 + \frac{100.0}{1636.72996021326.e^{0.0909090909090909.vu} + 0.907179532894125.e^{- 0.04.vu}}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=htau"> is s

	<img src="https://render.githubusercontent.com/render/math?math=binf">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{0.0089662682574368}{\left(e^{0.142857142857143.vu} + 8.03939664643187.10^{-5}\right)^{0.5}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=binf"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=ntau">&#8592;<img src="https://render.githubusercontent.com/render/math?math=ms.\left(0.7 + \frac{100.0}{134.007433567738.e^{0.0416666666666667.vu} + 1.54624094027712.e^{- 0.0434782608695652.vu}}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ntau"> is s

	<img src="https://render.githubusercontent.com/render/math?math=ina">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\bar{gna}.h.m^{3}.\left(ENa - v\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ina"> is A

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} h_{2}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{- h_{2} + hinfno}{\tau_{2}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=h_{2}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\tau_{2}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{344.827586206897.bet_{2}.ms}{qt.\left(alp_{2} + 1\right)}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\tau_{2}"> is s

	<img src="https://render.githubusercontent.com/render/math?math=ctau">&#8592;<img src="https://render.githubusercontent.com/render/math?math=ms.\left(10 + \frac{90.0}{1 + 0.0206022921249195.e^{- 0.0588235294117647.vu}}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ctau"> is s

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} p">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{q_{10}.\left(- p + pinf\right)}{ptau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=p"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=cinf">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{0.0089662682574368}{\left(e^{0.142857142857143.vu} + 8.03939664643187.10^{-5}\right)^{0.5}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=cinf"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=zinf">&#8592;<img src="https://render.githubusercontent.com/render/math?math=zss + \frac{1.0 - zss}{1211.96707449258.e^{0.1.vu} + 1}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=zinf"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=ptau">&#8592;<img src="https://render.githubusercontent.com/render/math?math=ms.\left(5 + \frac{100.0}{26.0832764813204.e^{0.03125.vu} + 0.326987016149301.e^{- 0.0454545454545455.vu}}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ptau"> is s

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} h_{1}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{- h_{1} + hinfno}{\tau_{1}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=h_{1}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=atau">&#8592;<img src="https://render.githubusercontent.com/render/math?math=ms.\left(0.1 + \frac{100.0}{508.580969450158.e^{0.0714285714285714.vu} + 2.38046496009307.e^{- 0.0416666666666667.vu}}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=atau"> is s

	<img src="https://render.githubusercontent.com/render/math?math=wtau">&#8592;<img src="https://render.githubusercontent.com/render/math?math=ms.\left(1.5 + \frac{100.0}{132158.79476884.e^{0.166666666666667.vu} + 4.21755420985163.e^{- 0.0222222222222222.vu}}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=wtau"> is s

	<img src="https://render.githubusercontent.com/render/math?math=ninf">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\left(1 + 0.0497870683678639.e^{- 0.2.vu}\right)^{-0.5}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ninf"> is rad

	Parameter <img src="https://render.githubusercontent.com/render/math?math=I">, where unit of <img src="https://render.githubusercontent.com/render/math?math=I"> is A

	<img src="https://render.githubusercontent.com/render/math?math=winf">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{1.0}{\left(1 + 0.000335462627902512.e^{- 0.166666666666667.vu}\right)^{0.25}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=winf"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=bet_{2}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=e^{\frac{173.664.vu + 14587.776}{8.315.temp + 2271.3254}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=bet_{2}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} r">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{q_{10}.\left(- r + rinf\right)}{rtau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=r"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=btau">&#8592;<img src="https://render.githubusercontent.com/render/math?math=ms.\left(1 + \frac{1000.0}{129.189400929953.e^{0.037037037037037.vu} + 2.38046496009307.e^{- 0.0416666666666667.vu}}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=btau"> is s

	<img src="https://render.githubusercontent.com/render/math?math=mtau">&#8592;<img src="https://render.githubusercontent.com/render/math?math=ms.\left(0.04 + \frac{10.0}{140.158124472631.e^{0.0555555555555556.vu} + 3.26584631841885.e^{- 0.04.vu}}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=mtau"> is s

	<img src="https://render.githubusercontent.com/render/math?math=hinf">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{1.0}{50682.3667554257.e^{0.166666666666667.vu} + 1}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=hinf"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=rinf">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{1.0}{51903.5702194154.e^{0.142857142857143.vu} + 1}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=rinf"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=iklt">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\bar{gklt}.w^{4}.z.\left(EK - v\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=iklt"> is A

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} h">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{q_{10}.\left(- h + hinf\right)}{htau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=h"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=vu">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{v}{mV}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=vu"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=ikht">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\bar{gkht}.\left(EK - v\right).\left(n^{2}.nf + p.\left(1 - nf\right)\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ikht"> is A

	<img src="https://render.githubusercontent.com/render/math?math=ika">&#8592;<img src="https://render.githubusercontent.com/render/math?math=a^{4}.b.c.\bar{gka}.\left(EK - v\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ika"> is A

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} z">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{q_{10}.\left(- z + zinf\right)}{ztau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=z"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} m">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{q_{10}.\left(- m + minf\right)}{mtau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=m"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=bet_{1}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=e^{\frac{86.832.vu + 4341.6}{8.315.temp + 2271.3254}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=bet_{1}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} n">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{q_{10}.\left(- n + ninf\right)}{ntau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=n"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} b">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{q_{10}.\left(- b + binf\right)}{btau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=b"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{I + ih + ihcno + ika + ikht + iklt + ileak + ina}{C}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is V

	<img src="https://render.githubusercontent.com/render/math?math=alp_{2}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=e^{\frac{289.44.vu + 24312.96}{8.315.temp + 2271.3254}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=alp_{2}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} w">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{q_{10}.\left(- w + winf\right)}{wtau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=w"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} a">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{q_{10}.\left(- a + ainf\right)}{atau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=a"> is rad

	exponential_euler method is used for integration

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=C">: <img src="https://render.githubusercontent.com/render/math?math=12. pF">, <img src="https://render.githubusercontent.com/render/math?math=\bar{gklt}">: <img src="https://render.githubusercontent.com/render/math?math=0. S">, <img src="https://render.githubusercontent.com/render/math?math=zss">: <img src="https://render.githubusercontent.com/render/math?math=0.5">, <img src="https://render.githubusercontent.com/render/math?math=temp">: <img src="https://render.githubusercontent.com/render/math?math=22.0">, <img src="https://render.githubusercontent.com/render/math?math=El">: <img src="https://render.githubusercontent.com/render/math?math=-65. mV">, <img src="https://render.githubusercontent.com/render/math?math=EK">: <img src="https://render.githubusercontent.com/render/math?math=-70. mV">, <img src="https://render.githubusercontent.com/render/math?math=\bar{gh}">: <img src="https://render.githubusercontent.com/render/math?math=0.5 nS">, <img src="https://render.githubusercontent.com/render/math?math=gbarno">: <img src="https://render.githubusercontent.com/render/math?math=0. S">, <img src="https://render.githubusercontent.com/render/math?math=\bar{gka}">: <img src="https://render.githubusercontent.com/render/math?math=0. S">, <img src="https://render.githubusercontent.com/render/math?math=gl">: <img src="https://render.githubusercontent.com/render/math?math=2. nS">, <img src="https://render.githubusercontent.com/render/math?math=\bar{gna}">: <img src="https://render.githubusercontent.com/render/math?math=1. uS">, <img src="https://render.githubusercontent.com/render/math?math=ENa">: <img src="https://render.githubusercontent.com/render/math?math=50. mV">, <img src="https://render.githubusercontent.com/render/math?math=nf">: <img src="https://render.githubusercontent.com/render/math?math=0.85">, <img src="https://render.githubusercontent.com/render/math?math=q_{10}">: <img src="https://render.githubusercontent.com/render/math?math=1.0">, <img src="https://render.githubusercontent.com/render/math?math=frac">: <img src="https://render.githubusercontent.com/render/math?math=0.0">, <img src="https://render.githubusercontent.com/render/math?math=\bar{gkht}">: <img src="https://render.githubusercontent.com/render/math?math=150. nS">, <img src="https://render.githubusercontent.com/render/math?math=qt">: <img src="https://render.githubusercontent.com/render/math?math=0.191190467371012">, <img src="https://render.githubusercontent.com/render/math?math=Eh">: <img src="https://render.githubusercontent.com/render/math?math=-43. mV">


**StateMonitor(s) defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=v"> of neurongroup, for member(s): 0 with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">.


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=I"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=250. pA"> to all members 

