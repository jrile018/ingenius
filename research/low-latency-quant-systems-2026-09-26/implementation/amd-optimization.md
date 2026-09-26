# AMD architecture and optimization documentation

## Evidence

AMD publishes generation-specific optimization guides, AMD64 architecture manuals, AOCC target-selection documentation, processor programming references, and uProf material. Current guides cover cache behavior, alignment, prefetch, branches, register reuse, dependencies, load/store behavior, allocation, and SIMD for specific Zen generations.

## Skill use

Select guidance by exact processor generation and pin the compiler and `-march` target. Validate on the deployment CPU. When one artifact must run across machines, use runtime feature selection or separately built variants and test the fallback path.

## Limits

Generation-specific advice is not portable, and unsupported ISA instructions can make a binary fail rather than merely slow down. The manuals are reference documents, not an open course corpus.

## Sources

- [AMD developer documentation](https://www.amd.com/en/developer/browse-by-resource-type/documentation.html)
- [Zen 5 Software Optimization Guide](https://docs.amd.com/v/u/en-US/58455_1.00)
- [AOCC target selection](https://docs.amd.com/r/en-US/57222-AOCC-user-guide/Target-Selection)
