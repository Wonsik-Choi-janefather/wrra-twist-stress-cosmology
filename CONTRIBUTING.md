# Contributing

Reproduction reports, mathematical corrections, independent data checks, and
implementations of the open tests are welcome.

Please include:

1. the exact command and Python version used;
2. the input file and output diff;
3. whether the issue concerns a WRRA-specific transformation, an imported
   scaffold, an external input, or an open empirical test; and
4. a minimal test that fails before the proposed correction and passes after it.

Changes that introduce a fitted parameter must update the cost and claim
ledgers. A successful fit with a new free parameter is useful, but it is not the
same model as the declared \(C=1\) closure.
