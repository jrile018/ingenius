# Intel architecture and optimization documentation

## Evidence

Intel's optimization manuals cover front-end behavior, out-of-order execution, ports, branches, caches and memory, prefetching, address translation, store forwarding, memory disambiguation, SIMD, threading, AVX/AVX-512, and AMX. Intel also publishes latency/throughput data and performance-monitoring event references.

## Skill use

Pin the exact processor family or stepping and manual revision. Use vendor guidance to explain a candidate transformation, inspect emitted instructions, and measure on the target machine. Keep target-specific flags or binaries isolated and provide runtime dispatch when deployment spans heterogeneous CPUs.

## Limits

Processor behavior and errata change. Guidance for one generation is not universal, and document prose is not generally open content. Link and paraphrase rather than copying manuals into the skill.

## Sources

- [Intel manuals landing page](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html)
- [Optimization Reference Manual](https://www.intel.com/content/www/us/en/developer/articles/technical/intel64-and-ia32-architectures-optimization.html)
