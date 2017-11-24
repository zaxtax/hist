# Hist: command-line histograms

An example usage might look like

````bash
% python3 -c "import numpy; {print(i) for i in numpy.random.normal(0,1,1000)}" | python3 hist.py
-3.35
-3.10
-2.85 =
-2.60 ==
-2.35 ==
-2.10 =========
-1.85 =========
-1.60 ==================
-1.35 =================
-1.10 ========================
-0.85 =================================
-0.60 ========================================
-0.35 =============================================
-0.10 =================================================
 0.14 =================================================
 0.39 ==========================================
 0.64 ========================
 0.89 ==========================
 1.14 ==================
 1.39 =================
 1.64 =========
 1.89 =====
 2.14 ===
 2.39
 2.64
 2.89
````

Supports discrete distributions as well

````bash
% python3 -c "import numpy; {print(i) for i in numpy.random.poisson(5,1000)}" | python3 hist.py -d
 0 =
 1 ===========
 2 =====================
 3 =========================================
 4 =================================================
 5 ===========================================
 6 ========================================
 7 ==========================
 8 ===================
 9 ===========
 10 ===
 11 ==
````