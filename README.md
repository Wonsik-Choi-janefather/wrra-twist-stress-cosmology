# WRRA Twist-Stress Cosmology

## Reproducibility package for the spatial-stress mass phenotype of dark matter

**Version 1.0.0 · Wonsik Choi · Independent Researcher**  
Contact: [janefather@gmail.com](mailto:janefather@gmail.com)

WRRA means **Wonsik Reality Renderer Architecture**. This repository turns the
twist-stress cosmology paper into a deterministic, inspectable calculation
chain. Its central result is a cross-scale closure: under the declared
three-dimensional isotropic matched-response condition \(C=1\), cosmological
inputs determine the galactic transition acceleration without using the
galactic comparison value in the forward calculation.

\[
a_T=CcH_0\sqrt{\frac{f_T}{8}},
\qquad
f_T=8\left(\frac{a_T}{CcH_0}\right)^2 .
\]

With \(H_0=67.4\ \mathrm{km\,s^{-1}\,Mpc^{-1}}\), \(f_T=0.265\), and
\(C=1\), the package obtains

\[
\boxed{a_T=1.191812669\times10^{-10}\ \mathrm{m\,s^{-2}}}.
\]

The external comparison value \(1.2007\times10^{-10}\ \mathrm{m\,s^{-2}}\)
is withheld until after that calculation. The relative difference is
**0.7402%**. Conversely, inserting the paper's rounded galactic value
\(1.20\times10^{-10}\ \mathrm{m\,s^{-2}}\) gives \(f_T=0.268653\).

## Why this result matters

The repository tests one economical explanatory chain rather than assembling
independent halo profiles for each scale:

1. a distributed spatial twist stress is the proposed **Actual**;
2. gravitationally inferred dark mass is its observable **Phenotype**;
3. a single matched normalization connects the cosmological stress fraction to
   the galactic low-acceleration scale;
4. the same response yields the deep-limit radial-acceleration and baryonic
   Tully–Fisher forms;
5. a one-metric, small-slip completion connects the same effective source to
   lensing;
6. an explicitly attributed Khronon/DBI scaffold checks whether the proposed
   owner can remain nearly pressureless around recombination.

The scientific contribution is therefore not a renamed MOND equation. It is
the **owner–renderer–phenotype assignment, the cross-scale matched-response
closure, and the auditable boundary between original structure, imported
mathematics, external inputs, and still-open tests**.

## Reproduced results

| Quantity | Reproduced value | Role |
|---|---:|---|
| \(H_0\) in SI units | 2.1842852410855023e-18 s^-1 | verified input conversion |
| \(cH_0\) | 6.548322413981453e-10 m s^-2 | intermediate output |
| \(a_T\) | 1.1918126691055912e-10 m s^-2 | WRRA matched-response output |
| Difference from 1.2007e-10 | 0.740179% | external comparison only |
| \(f_T\) from rounded \(a_T=1.20\times10^{-10}\) | 0.2686534181618261 | inverse check |
| DBI \(r=I_0/(2\mu^2)\) | 9.99132478599749e-6 | exact present-density normalization |
| DBI \(w\), recombination | 3.759694368198329e-5 | imported survival check |
| DBI \(c_{ad}^2\), recombination | 2.827272942096203e-9 | imported survival check |

The committed result file is results/reference_results.json. Thirteen automated
tests regenerate the values, check the source-paper table, verify structural
identities, and prove computationally that the external galaxy value is not a
forward input.

## Fixed evaluation chain

| Stage | Repository realization |
|---|---|
| **Verified input** | \(H_0\), \(f_T\), \(C=1\), exact SI conversion, and separately identified comparison data. |
| **WRRA-specific transformation** | Twist stress is assigned as the Actual; the renderer maps it to an effective mass phenotype and applies the matched-response relation. |
| **Output** | \(a_T\), inverse \(f_T\), deep-limit RAR samples, and the declared DBI background table. |
| **Falsification conditions** | The closure fails if independent scale measurements violate the relation, one \(a_T\) cannot sustain RAR and BTFR, lensing slip becomes unacceptable, cosmological or cluster calculations fail, or the committed numbers cannot be regenerated. |
| **Conclusion** | The package establishes a reproducible conditional cross-scale closure and a viable minimum early-time check. It does not substitute an unperformed SPARC fit, Boltzmann likelihood, or colliding-cluster simulation. |

## Ownership of the equations

| Layer | Status in this project |
|---|---|
| Twist stress as the Actual and dark mass as its phenotype | WRRA model assignment |
| \(a_T=CcH_0\sqrt{f_T/8}\) and the \(C=1\) cross-scale closure | WRRA conditional derivation |
| Hodge decomposition | established mathematics used to separate local and global sectors |
| AQUAL/MOND static response | established external mathematics used as the galactic renderer |
| One-metric lensing with \(\Phi\simeq\Psi\) | conditional leading-order completion |
| Relativistic Khronon/DBI action and perturbation response | imported covariant scaffold, explicitly attributed |
| Full CMB, growth, collision-cluster and topology likelihoods | open tests, not claimed as completed |

See docs/CLAIM_LEDGER.md and docs/EQUATION_MAP.md for the full audit.

## Reproduce everything

Python 3.10 or later is sufficient. There are no third-party dependencies and
no random numbers.

~~~bash
python code/reproduce_all.py --output reproduced/reproduction_results.json
python -m unittest discover -s tests -v
sha256sum -c SHA256SUMS
~~~

The first command regenerates the machine-readable calculation ledger. The
second checks all declared numerical and structural results. The third verifies
the release files byte for byte.

## Repository contents

~~~text
code/
  twist_stress_model.py       equations and unit-safe transformations
  reproduce_all.py            deterministic result generator
data/
  inputs.json                 all numerical inputs and provenance labels
docs/
  CLAIM_LEDGER.md             original/imported/open claim boundary
  EQUATION_MAP.md             paper equation-to-code map
  FALSIFICATION.md            decisive failure conditions
  REPRODUCTION_REPORT.md      readable numerical audit
  REFERENCES.md               source chain
paper/
  ..._KR_v1.0.docx            original Korean research note
results/
  reference_results.json      committed machine-readable outputs
  verification_ledger.json    result and claim audit
tests/
  test_reproduction.py        deterministic regression suite
.github/workflows/
  reproduce.yml               continuous reproduction audit
~~~

## What would strengthen the result next

The next calculations are already sharply defined:

1. fit the same \(a_T\) jointly to the full SPARC sample without per-galaxy dark
   halos;
2. implement the covariant perturbation equations in a Boltzmann solver and run
   CMB, BAO, matter-spectrum, and growth likelihoods;
3. solve non-spherical lensing and collision-cluster stress dynamics;
4. derive object-by-object junction conditions and search for global holonomy
   signatures.

These are extensions of a working calculation chain, not replacements for the
results reproduced here.

## Related WRRA records

- Related historical preprint *Minimal Computing Cosmology 2.1*: <https://doi.org/10.5281/zenodo.22660185>. This DOI is not a citation for MCC 2.3.2 or for this software package.
- WRRA Core: <https://doi.org/10.5281/zenodo.22650956>

## Citation and license

Citation metadata are in CITATION.cff. Code is released under the MIT License.
Original documentation, result data, and the source report are released under
CC BY 4.0. See LICENSES.md.
