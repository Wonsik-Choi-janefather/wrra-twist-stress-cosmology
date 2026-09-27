# Reproduction report

## Result 1: cross-scale closure

### Verified input

\[
H_0=67.4\ \mathrm{km\,s^{-1}\,Mpc^{-1}},\qquad f_T=0.265,
\qquad C=1.
\]

Using \(1\ \mathrm{Mpc}=3.0856775814913673\times10^{22}\ \mathrm m\),

\[
H_0=2.1842852410855023\times10^{-18}\ \mathrm{s^{-1}},
\]

\[
cH_0=6.548322413981453\times10^{-10}\ \mathrm{m\,s^{-2}}.
\]

### WRRA-specific transformation

The matched-response rule is

\[
a_T=CcH_0\sqrt{\frac{f_T}{8}}.
\]

### Output

\[
a_T=1.1918126691055912\times10^{-10}\ \mathrm{m\,s^{-2}}.
\]

Only after this forward calculation is the external comparison
\(1.2007\times10^{-10}\ \mathrm{m\,s^{-2}}\) read. Their relative difference is

\[
\frac{|1.1918126691055912-1.2007|}{1.2007}\times100
=0.740179\%.
\]

The inverse calculation with the paper's rounded
\(a_T=1.20\times10^{-10}\ \mathrm{m\,s^{-2}}\) gives

\[
f_T=8\left(\frac{a_T}{cH_0}\right)^2=0.2686534181618261.
\]

### Conclusion

The numerical meeting of the cosmological fraction and galactic acceleration
scale is exactly reproducible. It is a conditional cross-scale output of the
declared \(C=1\) closure, and the galaxy comparison is not used to manufacture
the forward value.

## Result 2: DBI minimum early-time check

### Verified input

\[
\Omega_{T,0}=0.265,\qquad \mu^{-1}=22.3\ \mathrm{Mpc},
\qquad \lambda_D=1.
\]

The exact present-density normalization solves

\[
r+\frac{\sqrt{1+\lambda_Dr^2}-1}{\lambda_D}
=\frac{3}{2}\Omega_{T,0}
\left(\frac{H_0\mu^{-1}}{c}\right)^2,
\qquad r\equiv\frac{I_0}{2\mu^2}.
\]

### Output

\[
r=9.99132478599749\times10^{-6},
\]

which rounds to the source report's \(9.9913\times10^{-6}\).

| State | \(q\) | \(w\) | \(c_{ad}^2\) |
|---|---:|---:|---:|
| \(a=10^{-5}\) | 1.0 at float precision | 5.00434e-11 | 5.00869e-21 |
| \(a=1/1100\) | 0.9999999971727271 | 3.759694e-5 | 2.827273e-9 |
| \(a=1\) | 9.9913248e-6 | 4.995637e-6 | 9.991225e-6 |
| \(a=10\) | 9.9913248e-9 | 4.995662e-9 | 9.9913247e-9 |

### Conclusion

The imported DBI response reproduces the report's minimum background and
sound-speed table and remains close to a pressureless component at the declared
epochs. The calculation is evidence that this covariant scaffold can carry the
WRRA interpretation through the stated minimum test. A full CMB likelihood is a
separate, explicitly open calculation.
