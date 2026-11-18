# Computational Closure of a Finite-Source Cosmological Toy Model
## From 1,015,000 Arithmetic Addresses to Spatial Geometry and Effective Quantization

**Wonsik Choi** | Independent Researcher, Republic of Korea  
**Correspondence:** janefather@gmail.com  
**Date:** 18 November 2026 | **Manuscript:** v1.0  
**Status:** Public preprint, conditional executable toy-model result; no Zenodo DOI assigned.

## Abstract
We report a reproducible finite-source cosmological toy model within Minimal Computing Cosmology 3.0 (MCC 3.0) and the Wonsik Reality Renderer Architecture (WRRA). Starting with 1,015,000 natural-number addresses, a normalized arithmetic weight and an eight-frame conditional admission rule recover the calibrated address fractions P = 0.050, D = 0.268, and R = 0.682. The return sector contains prime-address weight and non-admitted odd-composite weight. An explicitly declared spatial projection places address-resolved sector loads on a periodic 128-cell ring. A mean-subtracted D/R contrast is mapped through a periodic inverse-Laplacian receiver into a weak metric perturbation; its amplitude is fixed to 10⁻⁸ by a toy-model normalization. Proper relational distances are then mapped to a bounded effective quantization readout q_eff and complementary residual r. Twelve internal numerical checks and twelve separate audit checks pass. An independent Fourier-domain audit reports a relative Poisson residual of 1.3381 × 10⁻¹³. This establishes conditional, one-way computational closure for the specified finite toy model. It does not derive the spatial receiver, metric amplitude, homogeneous expansion, or quantum-mechanical constants from first principles; the original MCC 3.0 28-component Einstein solver is not reproduced.

**Keywords:** Minimal Computing Cosmology; Wonsik Reality Renderer Architecture; finite-source cosmology; computational closure; arithmetic address weighting; emergent spatial geometry; finite information; periodic spatial receiver; Poisson-type spatial response; effective quantization; reproducible computational physics; cosmological toy model.

## 1. Introduction
A finite cosmological model should make the passage from a finite source ledger to an interpretable output executable and auditable. MCC 3.0 proposes a finite arithmetic SOURCE and a phenotype-oriented accounting framework. The narrower question studied here is whether a complete, declared computational path can be implemented from its weighted address classes through a finite spatial receiver to a metric-sensitive representation readout. The target is a toy-model closure, not a unique derivation of the observed Universe.

The present contribution is structural: an explicit finite transformation chain, a strict separation of information-address and physical-energy accounts, a spatial receiver with a numerical residual audit, and an effective quantization decoder. Agreement with calibrated inputs is reported as model consistency and explanatory reproduction, not as an independent observational prediction.

## 2. Evaluation contract and scope
The word *closure* is restricted to a deterministic one-way computational map under stated inputs. It does not imply a closed covariant action, an autonomous evolution law, a physically derived metric amplitude, or an empirical fit to cosmological observations.

| Validated input | WRRA-specific transformation | Output | Falsification condition |
|---|---|---|---|
| 1,015,000 weighted natural-number addresses | Prime/even-composite/conditional odd-composite classification | P/D/R ledger | Wrong fractions, non-finite or negative weights |
| P/D/R address loads | 128-cell modular projection and D/R contrast | Finite spatial field | Normalization or zero-mode failure |
| Finite contrast | Declared periodic inverse-Laplacian receiver | Weak metric potential | Poisson residual, loss of metric positivity |
| Metric potential | Proper distance and bounded readout | q_eff and r | Non-finite outputs, failure of q+r=I |

## 3. Finite arithmetic SOURCE
Let N = 1,015,000 and n ∈ {2, …, N}. The normalized address weights are

**wₙ = n^(−α) / Σₘ₌₂ᴺ m^(−α), α = 1.8996877935161325.**

Prime addresses contribute to R. Even composite addresses contribute to D. Odd composite addresses are conditionally admitted to P over eight frame updates, with non-admitted weight assigned to R. The implementation uses h = 1.4476744689338703, γ = (14.134725141734695, 21.022039638771556, 25.01085758014569, 30.424876125859512), and frame offsets 0.1 × frame.

| Address sector | Reproduced fraction |
|---|---:|
| Phenotype P | 0.050 |
| Resident non-phenotype D | 0.268 |
| Return R | 0.682 |
| R from prime addresses | 0.674227036122008 |
| R from non-admitted odd composites | 0.00777296387799199 |

The address fractions (0.050, 0.268, 0.682) must not be confused with the separately calibrated SI energy fractions (0.0493, 0.265, 0.6857). They are different ledgers and are not interchanged in the code.

## 4. Finite spatial receiver
The spatial ring has M = 128 cells indexed j = 0, …, 127. Each address n is placed in cell j = n mod M. The three sector loads Pⱼ, Dⱼ, Rⱼ are sums of address weights assigned to each cell. This placement is a chosen toy mapping, not a theorem about physical spatial localization.

The normalized non-phenotype contrast is

**sⱼ = ½[Dⱼ/ΣₖDₖ + Rⱼ/ΣₖRₖ] − meanⱼ{½[Dⱼ/ΣₖDₖ + Rⱼ/ΣₖRₖ]}.**

The receiver uses a periodic spectral inverse Laplacian with zero Fourier mode set to zero. For nonzero wavenumber k, φ̂ₖ is proportional to ŝₖ/k². The resulting real-space potential is scaled so maxⱼ|φⱼ| = 10⁻⁸. The receiver equation takes the form ∇²φ = C s, where C is fixed by the declared normalization rather than derived from SOURCE dynamics.

This one-dimensional periodic Poisson-type toy receiver is not the original seven-mode/twenty-eight-component GR calculation described in MCC 3.0 chapter 116.

## 5. Spatial distance and effective quantization
For a weak-field spatial slice, the proper ring length is

**R(a) = (a/M) Σⱼ √(1 − 2φⱼ), a > 0.**

The bounded readout is

**q_eff(a) = I · 49R(a)/[1 + 49R(a)], r(a) = I − q_eff(a), I = 5.**

The factor 49 follows from the declared present-epoch toy calibration q_eff = 4.9 when R = 1. q_eff is an effective representation measure, not a quantum of action, a Planck-scale cell size, or a directly observed quantum constant. The residual r is not the cosmological return sector R and is not additional cosmic energy.

The background comparison inherits the calibrated flat dust-plus-vacuum FLRW expression E(a)² = (0.0493 + 0.265)/a³ + 0.6857. This is imported background physics, not a SOURCE-derived expansion law. The local potential is static in comoving coordinates and no q-to-stress feedback is implemented.

## 6. Numerical results
At a = 1, the local metric ranges from −5.7202542728128274 × 10⁻⁹ to +1.0 × 10⁻⁸. The corresponding cellwise effective readout ranges from 4.89999999902 to 4.900000000560585. The periodic Poisson-type equation has a maximum-relative numerical residual of 3.7980988376540695 × 10⁻¹⁴ and an independent Fourier-domain L2 residual of 1.338085121214686 × 10⁻¹³.

| Scale factor a | Homogeneous q_eff | Residual r |
|---:|---:|---:|
| 0.02 | 2.474747474747475 | 2.525252525252525 |
| 0.1 | 4.1525423728813555 | 0.8474576271186445 |
| 0.6119598068 | 4.838636962722839 | 0.16136303727716061 |
| 1 | 4.9 | 0.1 |
| 2 | 4.94949494949495 | 0.050505050505050164 |

## 7. Verification, repeatability, and limitations
The archived implementation reports 12/12 internal tests passed and 12/12 separate audit tests passed. The audit checks the address ledger, positivity and normalization, finite weak metric, Fourier residual, readout bounds, and deterministic execution. Two separate-process runs were reported to produce byte-identical JSON. Numerical audit files and reproducibility scripts are indexed below.

The strongest unresolved limitation is dynamical: the mapping from finite SOURCE load to metric normalization is not derived from an energy-momentum constitutive law. The inverse-Laplacian receiver is a chosen local rule; its time evolution, backreaction, perturbative Einstein constraints, nonlinear GR stability, and empirical quantum interpretation are outside this study.

## 8. Falsification and claim grading
For the declared numerical model, failure occurs if (i) P+D+R departs from unity beyond floating-point tolerance, (ii) sector weights become negative or non-finite, (iii) 1−2φ is nonpositive, (iv) the periodic Poisson residual exceeds the declared threshold, (v) q_eff falls outside (0,I) or q_eff+r differs from I, or (vi) deterministic reruns disagree. The source code contains the operational assertions.

**EXACT:** finite arithmetic ledger under declared calibration, numerical inverse-Laplacian solution, bounded readout conservation, deterministic tests. **WORKING:** conditional one-way SOURCE-to-readout toy chain. **OPEN:** self-generated metric amplitude, original 28-mode GR solver, autonomous evolution and backreaction, complete cosmological and quantum-observational closure.

## 9. Discussion
The model demonstrates how finite arithmetic information may be organized into a common carrier and transformed into spatial and representation phenotypes using a completely specified computational path. Its originality lies in the structure and connection of the finite SOURCE, spatial receiver, and phenotype readout—not in claiming that the calibrated fractions or imported FLRW relations are newly discovered constants.

A next step would replace the chosen receiver with the original MCC 3.0 SOURCE-derived perturbative metric or introduce a finite autonomous evolution and constitutive relation, with conservation and stability checks. Those tasks are future research rather than prerequisites for reporting the present conditional toy result.

## 10. Conclusion
We have implemented and audited a conditional one-way computational closure from 1,015,000 weighted arithmetic addresses to finite spatial loads, a weak periodic metric, relational distance, and an effective quantization readout. Under explicitly declared arithmetic and receiver assumptions, the path is deterministic and numerically consistent. The 12 internal and 12 independent checks, together with the Fourier residual audit, establish the computational status of this specific finite toy construction.

The result does not establish a complete autonomous relativistic cosmology or derive physical quantum mechanics. The P/D/R address ledger, SI energy fractions, and quantization residual remain distinct accounting types. The principal result is a reproducible finite transformation chain with clear assumptions and falsification conditions.

## Data and code availability
- [Repository](https://github.com/Wonsik-Choi-janefather/wrra-twist-stress-cosmology)
- [MCC toy v0.8 evidence index](https://github.com/Wonsik-Choi-janefather/wrra-twist-stress-cosmology/tree/main/evidence/mcc3-toy-v0.8)
- Reproduction: `mcc3_local_toy_v08.py` and `independent_audit.py`
- Machine-readable summary: `reference_results.json`
- GitHub Actions workflow: `.github/workflows/mcc3-toy-audit.yml`
- No Zenodo DOI has yet been assigned to this manuscript.

## References and provenance
1. Choi, W. *Minimal Computing Cosmology 3.0*, Korean full-book edition v0.28-r14 (2026), especially chapters 88–92, 105, and 116.
2. Choi, W. *WRRA Twist-Stress Cosmology*, reproducible research repository (2026). https://github.com/Wonsik-Choi-janefather/wrra-twist-stress-cosmology
3. Choi, W. *MCC 3.0 finite-source local-space effective-quantization toy evidence*, v0.8 (2026). https://github.com/Wonsik-Choi-janefather/wrra-twist-stress-cosmology/tree/main/evidence/mcc3-toy-v0.8
4. Standard FLRW and Newtonian-gauge weak-field relations are used as external mathematical scaffolding; no original derivation within this toy receiver is claimed.
