OBSERVATIONS FORMAT IN DYNASTVO
===============================
Author: J.Desmars
Date: 2020.06.24
===============================

EXAMPLE
===============================
First line of file (one first line per object)
      345        0        0      345      237     FIT  2445634.548257130 2458287.842620741 100004

Optical Data (1 line per observation)
O A 1983 10 27.047630 338.823750000000 -57.261472222222 809   0.000   0.000  0.150E+01  0.150E+01 1   99.99   1   79  -0.032   0.089    0.06         100004
O A 1983 11  1.415220 333.427500000000 -57.313333333333 500   0.000   0.000  0.212E+01  0.212E+01 0   17.00   2   58 -23.647  -9.447   12.01 1  0.45 100004
O A 1983 11  1.486790 333.372500000000 -57.308333333333 500   0.000   0.000  0.212E+01  0.212E+01 0   99.99   2   58  14.270   1.066    6.75         100004
O A 1984  5  3.211150 199.374166666667  17.248750000000 801   0.000   0.000  0.150E+01  0.150E+01 1 A 99.99   1   78   1.018   1.100    1.00         100004
............
Space Data (always 2 lines per measurement)
S s 2020  5 27.278480 170.173833333333 -20.965277777778 C51   0.000   0.000  0.100E+01  0.100E+01 1 L 17.00            0.144  -0.171    0.22 1  0.78 99935
s s 2020  5 27.278480 space              -6257.190400    -847.030300   -2683.112600 C51 99935
............
Radar Data (1 line per measurement)
V r 2005  1 29.000000     557835.37894            c 251 251   0.000          0.136E+01            1  -0.217                             0.16 99942
R r 2005  1 29.000000   28784349.07929            c 251 251   0.000          0.600E+00            1   0.059                             0.10 99942


MEANING OF COLUMNS
===============================
FIRST LINE
-------------------
      345        0        0      345      237     FIT  2445634.548257130 2458287.842620741 100004
-------------------
 1. number of optical observations
 2. number of ranging measurements (distance with radar)
 3. number of doppler measurements (velocity with radar)
 4. total number of accepted measurements in the fitting process
 5. FIT
 6. julian date of the first observation (used in the fitting process)
 7. julian date of the last observation (used in the fitting process)
 8. Designation or MPC number of the object

-------------------
OPTICAL/SPACE DATA (space data have one additional line, see format below)
-------------------
O A 1984  5  3.211150 199.374166666667  17.248750000000 801   0.000   0.000  0.150E+01  0.150E+01 1 A 99.99   1   78   1.018   1.100    1.00         100004
-------------------
 1.  (a1): Type of observation (O: optical, S:Space)
	 (x)
 2.  (a1): Type of measurements (see Table 17, DynAstVO report)
     (x)
 3.  (i4): Year of the observation
     (x)
 4.  (i2): Month of the observation
     (x)
 5.  (f9.6): Decimal day of the observation (in UTC)
     (x)
 6.  (f16.12): right ascension of the object in decimal degrees (in J2000 reference frame)
     (x)
 7.  (f16.12): declination of the object in decimal degrees (in J2000 reference frame)
     (x)
 8.  (a3): IAU observatory code (see https://minorplanetcenter.net//iau/lists/ObsCodes.html)
     (x)
 9.  (f7.3): bias correction in right ascension (in arcsec) in the sense new observation = RA - bias / cos (delta)
     (x)
10.  (f7.3): bias correction in declination (in arcsec) in the sense new observation = DE - bias 
     (x)
11.  (e10.3): estimated precision of the observation in right ascension (in arcsec) used in the fitting process: weight = 1/(estimated precision)^2
     (x)
12.  (e10.3): estimated precision of the observation in declination (in arcsec) used in the fitting process: weight = 1/(estimated precision)^2
     (x)
13.  (i1): flag of acceptance of the observation in the fitting process (1: accepted, 0: rejected)
     (x)
14.  (a1): code of the stellar catalogue used for the reduction (see https://minorplanetcenter.net//iau/info/CatalogueCodes.html)
     (x)
15.  (f7.2): apparent magnitude of the object (measured from the observation)
     (x)
16.  (i3): number of observation performed during the same night in the same observatory
     (x)
17.  (i3): random number linked to the night of observation related to col16
     (x)
18.  (f7.3): residual (O-C) in right ascension : Delta alpha = (alpha_obs - alpha_computed)x cos(delta)
     (x)
19.  (f7.3): residual (O-C) in declination : Delta delta = (delta_obs - delta_computed)
     (x)
20.  (f7.2): xhi square of the observations xhi=sqrt((col18/col11)^2+(col19/col12)^ 2)
     (x)
21.  (i1): flag of acceptance for magnitude parameter fitting (1: accepted, 0: rejected)
     (x)
22.  (f5.2): residual of magnitude (observed magnitude - computed magnitude)
     (x)
23.  (a) Designation or number of the object



-------------------
SPACE DATA (additional line)
-------------------
s s 2020  5 27.278480 space              -6257.190400    -847.030300   -2683.112600 C51 99935
-------------------
 1.  (a1): s
	 (x)
 2.  (a1): s
     (x)
 3.  (i4): Year of the observation
     (x)
 4.  (i2): Month of the observation
     (x)
 5.  (f9.6): Decimal day of the observation (in UTC)
     (x)
 6.  (f16.12): 'space'
     (x)
 7.  (f14.6): x-component of the geocentric position of the spacecraft at the time of observation (in km)
     (x)
 8.  (f14.6): y-component of the geocentric position of the spacecraft at the time of observation (in km)
     (x)
 9.  (f14.6): z-component of the geocentric position of the spacecraft at the time of observation (in km)
     (x)
10.  (a3): IAU observatory code (see https://minorplanetcenter.net//iau/lists/ObsCodes.html)
     (x)
11.  (a) Designation or number of the object


-------------------
RADAR DATA 
-------------------
V r 2005  1 29.000000     557835.37894            c 251 251   0.000          0.136E+01            1  -0.217                             0.16 99942
R r 2005  1 29.000000   28784349.07929            c 251 251   0.000          0.600E+00            1   0.059                             0.10 99942
-------------------
 1.  (a1): Type of observation (R: ranging, V: doppler)
	 (x)
 2.  (a1): Type of measurements (radar)
     (x)
 3.  (i4): Year of the observation
     (x)
 4.  (i2): Month of the observation
     (x)
 5.  (f9.6): Decimal day of the observation (in UTC)
     (x)
 6.  (f16.5): Measurement of the distance in km (ranging case) or radial velocity in km/d (doppler case)
     (12x)
 7.  (a1): c
     (x)
 8.  (a3): IAU observatory code transmitting (see https://minorplanetcenter.net//iau/lists/ObsCodes.html)
     (x)
 9.  (a3): IAU observatory code receiving (see https://minorplanetcenter.net//iau/lists/ObsCodes.html)
     (x)
10.  (f7.3): bias correction (normally 0.000)
     (10x)
11.  (e10.3): estimated precision of the observation (in km for ranging or km/d for doppler)
     (12x)
12.  (i1): flag of acceptance of the observation in the fitting process (1: accepted, 0: rejected)
     (x)
13.  (f7.3): residual (O-C) in right ascension : Delta alpha = (alpha_obs - alpha_computed)x cos(delta)
     (29x)
14.  (f7.2): xhi square of the observations xhi=sqrt((col13/col11)^2)
     (x)
15.  (a) Designation or number of the object
===============================

