# Falsification and acceptance conditions

The model is strongest when its economy is made costly: the same owner and
normalization must survive several domains. A success in one domain cannot be
used to erase a failure in another.

## 1. Cross-scale matched response

For \(C=1\), independently measured \(H_0\), effective stress fraction \(f_T\),
and galactic transition scale \(a_T\) must satisfy

\[
a_T=cH_0\sqrt{f_T/8}.
\]

If their joint uncertainty regions do not overlap, the \(C=1\) closure is
rejected. Introducing an unconstrained fitted \(C\) would be a more expensive
successor model and must be recorded as such.

## 2. Galaxy dynamics

One shared response scale must maintain both the radial acceleration relation
and baryonic Tully–Fisher relation across morphology, surface brightness,
environment, and distance uncertainty. Systematic, irreducible galaxy-by-galaxy
variation beyond declared nuisance parameters falsifies the minimal closure.

## 3. Lensing

The proposed effective source must explain dynamical and lensing observables
with the same stress distribution. A required large gravitational slip or a
persistent lensing/dynamical mass mismatch falsifies the one-metric,
small-slip completion used by the model.

## 4. Early universe and structure

The covariant completion must retain sufficiently small pressure, sound speed,
and unstable modes while fitting CMB anisotropies, BAO, matter power, and growth
data. The DBI table in this repository is a minimum survival calculation, not a
substitute for this joint likelihood.

## 5. Colliding clusters

A time-dependent, non-spherical stress field must reproduce the observed
separation among gas, galaxies, and lensing centers. A static spherical formula
cannot count as passing this test.

## 6. Topology and nonlocal response

Any claimed nonzero holonomy or boundary response must produce a quantitative
observable. Repeated-pattern searches, matched-circle searches, or environmental
RAR residuals can reject specific realizations. A unique cosmic loop size must
not be reported until stiffness or holonomy is independently fixed.

## 7. Computational reproducibility

The release itself fails if:

- undeclared numerical inputs are required;
- the external galaxy comparison changes the forward \(a_T\) calculation;
- regenerated results disagree with results/reference_results.json;
- the DBI rows fail their declared tolerances; or
- file hashes do not match SHA256SUMS.
