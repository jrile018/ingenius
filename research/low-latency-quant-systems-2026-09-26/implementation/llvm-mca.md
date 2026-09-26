# LLVM Machine Code Analyzer

## Evidence

LLVM MCA is an official static analyzer for assembly based on LLVM processor scheduling models. It estimates IPC, block throughput, resource pressure, and timeline behavior and supports target triples, target CPUs, analysis regions, iteration counts, queue parameters, bottleneck analysis, and JSON output.

## Skill use

Pin the compiler, flags, target triple, `-mcpu`, assembly region, and LLVM version. Use MCA to test a specific pipeline hypothesis and inspect resource pressure or dependency chains. Ensure region markers do not alter the generated code. Corroborate the prediction with wall-clock distributions and hardware counters on the deployment processor.

## Limits

Accuracy is limited by the scheduling model. The default analysis does not fully model fetch/decode, branch prediction, cache hierarchy, or all memory hazards, and unsupported instructions may be skipped. A favorable MCA report is not evidence of end-to-end improvement.

## Source

- [Official llvm-mca command guide](https://llvm.org/docs/CommandGuide/llvm-mca.html)
