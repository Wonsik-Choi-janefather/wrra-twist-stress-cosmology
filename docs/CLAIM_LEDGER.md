# Claim ledger

This ledger prevents three different achievements from being collapsed into
one vague word such as “fit”: an original WRRA transformation, a reproduced
external scaffold, and an unperformed empirical test.

## A. WRRA contributions implemented here

| ID | Claim | Evidence in package | Status |
|---|---|---|---|
| W-01 | Spatial twist stress can be designated as a single Actual whose gravitational phenotype is inferred dark mass. | Architecture and equation chain in the source report; explicit owner map in this repository. | model construction |
| W-02 | The matched response \(C=1\) connects the cosmic stress fraction to the galactic transition scale through \(a_T=cH_0\sqrt{f_T/8}\). | matched_transition_acceleration; exact unit conversion; regression test. | reproduced conditional derivation |
| W-03 | \(H_0=67.4\) and \(f_T=0.265\) produce \(a_T=1.191812669\times10^{-10}\,\mathrm{m\,s^{-2}}\). | results/reference_results.json; external galaxy value withheld from forward inputs. | reproduced numerical result |
| W-04 | The same \(a_T\) gives both deep-limit RAR and BTFR forms. | deep_low_acceleration_response and btfr_velocity_fourth_m4_s4. | analytical consequence |
| W-05 | Total twist strength and chirality are separate invariants, allowing large bidirectional stress with small net handedness. | twist_invariants; unit test. | reproduced structural identity |
| W-06 | \(f_T\) fixes only the combination \(\zeta\alpha^2\), not stiffness and twist separately. | cosmic_stress_fraction; loop-size degeneracy test. | identified parameter degeneracy |
| W-07 | The theory is evaluated by a fail-closed chain of inputs, transformation, outputs, and failure conditions. | README, automated tests, and FALSIFICATION.md. | implemented methodology |

## B. Established mathematics used as tools

| ID | Component | Role | Attribution boundary |
|---|---|---|---|
| E-01 | Hodge decomposition | separates exact, co-exact, and harmonic/global sectors | mathematical tool, not claimed as a WRRA invention |
| E-02 | AQUAL/MOND low-acceleration equation | provides a transparent static renderer yielding RAR and BTFR | Bekenstein–Milgrom/Milgrom mathematics |
| E-03 | weak-field one-metric lensing equations | relates \(\Phi+\Psi\) to deflection and \(\Phi\simeq\Psi\) to mass agreement | standard relativistic weak-field result |
| E-04 | relativistic Khronon/DBI action | supplies a covariant background and perturbation scaffold | Blanchet–Skordis calculation, imported and cited |

Reproducing E-02 or E-04 inside the WRRA chain demonstrates compatibility and
computational closure. It does not relabel those external equations as original
WRRA discoveries.

## C. External inputs and comparisons

| ID | Quantity | Use |
|---|---|---|
| I-01 | \(H_0=67.4\,\mathrm{km\,s^{-1}\,Mpc^{-1}}\) | forward cosmological input |
| I-02 | \(f_T=0.265\) | forward effective-stress fraction input |
| I-03 | \(a_0=1.2007\times10^{-10}\,\mathrm{m\,s^{-2}}\) | post-calculation comparison only |
| I-04 | \(\mu^{-1}=22.3\,\mathrm{Mpc}\), \(\lambda_D=1\) | imported DBI parameter choice |

The test test_external_a0_is_not_a_forward_input changes I-03 by a factor of
three and verifies that W-03 remains exactly unchanged.

## D. Supported conclusions

1. The cross-scale number is reproducible and non-circular at the code level:
   the galaxy comparison value is absent from the forward function.
2. The result is conditional on the declared matched-response rule \(C=1\).
   That condition is part of the theory and is exposed rather than hidden in a
   fitted coefficient.
3. The same minimal owner survives the source paper's declared background DBI
   check at recombination, today, and \(a=10\).
4. The framework produces a compact research program: one normalization must
   survive galaxies, lensing, early structure, and clusters.

## E. Claims not made

- No completed full-catalogue SPARC likelihood is claimed.
- No completed Boltzmann-code CMB likelihood is claimed.
- No numerical Bullet Cluster or other colliding-cluster solution is claimed.
- No unique value of cosmic loop size is claimed without independent stiffness
  or holonomy information.
- No particle-dark-matter nonexistence theorem is claimed.
- The imported Khronon/DBI equations are not represented as an original WRRA
  field-theory derivation.
