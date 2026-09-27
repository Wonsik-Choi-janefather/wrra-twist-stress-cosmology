# Equation-to-code map

The equation numbers refer to the Korean source report in paper/.

| Eq. | Mathematical content | Implementation | Verification level |
|---:|---|---|---|
| 1 | \(C_{min}=\min\{C(M):M\text{ survives all tests}\}\) | evaluation policy in README and ledger | methodological |
| 2 | Actual \(\xrightarrow{\mathcal R}\) Phenotype | owner map in README | architectural |
| 5 | \(A=d\phi+\delta B+h\) | documented | established decomposition; no field dataset supplied |
| 6 | \(\oint_\gamma h=\Theta_\gamma\neq0\) | documented | topology observable specified |
| 7 | \(\kappa^2=\kappa_+^2+\kappa_-^2\), \(\chi_T=(\kappa_+^2-\kappa_-^2)/(\kappa_+^2+\kappa_-^2)\) | twist_invariants | unit tested |
| 8 | \(L_\gamma=|\Theta_\gamma|cH_0^{-1}\sqrt{\zeta/(6f_T)}\) | representative_loop_size_m | unit tested; degeneracy retained |
| 9 | \(u_T=\zeta c^4\kappa^2/(16\pi G)\) | twist_energy_density_j_m3 | direct implementation |
| 10 | \(\alpha=c\kappa/H_0\), \(f_T=\zeta\alpha^2/6\) | cosmic_stress_fraction | unit tested |
| 11 | \(\rho_T^{eff}=-(4\pi G)^{-1}\nabla\cdot[(1-\mu)\mathbf g]\) | documented | requires a supplied spatial field for numerical evaluation |
| 12 | static effective energy \(E[\phi]\) | documented | imported AQUAL scaffold |
| 13 | \(\nabla\cdot[\mu(|\mathbf g|/a_T)\mathbf g]=-4\pi G\rho_b\) | documented | imported AQUAL scaffold |
| 14 | \(g=\sqrt{a_Tg_b}\), \(v_f^4=GM_ba_T\) | two functions in twist_stress_model.py | implemented and sampled |
| 15 | \(\lambda_\perp=\mu>0\), \(\lambda_\parallel=\mu+x\mu'>0\) | elliptic_stability_eigenvalues | unit tested |
| 16 | \(a_T=CcH_0\sqrt{f_T/8}\) and inverse | forward and inverse functions | exact numerical reproduction |
| 17–19 | weak-field metric, deflection, and \(\Phi\simeq\Psi\) lensing/dynamical-mass agreement | documented | conditional leading-order result; no lens catalogue supplied |
| 20–21 | covariant Khronon action and normalized foliation variables | documented | imported scaffold |
| 22 | DBI \(K(Q)\) | documented in reproduction report | imported scaffold |
| 23 | \(q(a)=[\lambda_D+(a^3/r)^2]^{-1/2}\) | dbi_state | exact reproduction |
| 24 | \(w(a)\) and \(c_{ad}^2(a)\) | dbi_state using the stable \(Z=r/a^3\) form | source table reproduced |
| 25 | \(k\)-dependent \(c_s^2\), zero anisotropic viscosity | dbi_sound_speed_squared_from_ratio; zero viscosity in ledger | equation implemented with an explicit consistent-unit ratio; no Boltzmann run claimed |
| 26 | \(\delta\mathbf g(x)/\delta B_{boundary}(y)\neq0\) | falsification proposal | no signal amplitude claimed |
| 27 | acceptance requires survival of galaxy, lensing, CMB, and structure tests | FALSIFICATION.md | program-level acceptance rule |

## Numerical-stability note

For Eq. 24 the code evaluates the algebraically equivalent form

\[
Z=\frac{r}{a^3},\qquad
w=\frac{Z}{1+\lambda_DZ^2+(1+Z)\sqrt{1+\lambda_DZ^2}},
\]

\[
c_{ad}^2=\frac{Z}{(1+\lambda_DZ^2)
\left(\sqrt{1+\lambda_DZ^2}+Z\right)}.
\]

This avoids subtracting nearly equal floating-point numbers when \(q\to1\) in
the early universe.
