# DPDK poll-mode networking

## Evidence

DPDK's official programmer guide describes user-space poll-mode drivers that access receive and transmit descriptors directly, avoiding normal interrupt-driven packet handling. It documents run-to-completion and pipeline models, logical-core and queue relationships, packet buffers, memory pools, offload, and queue ownership. Sample applications demonstrate forwarding, callbacks, packet latency, and PTP-related behavior.

## Skill use

DPDK is an architecture option after the kernel path has been measured, not a default recommendation. The skill should define queue ownership, core placement, NUMA and memory-pool layout, batch size, burst behavior, timestamp boundaries, and failure/recovery handling. It should compare run-to-completion and pipeline designs under the same workload and include CPU reservation and operability costs.

## Limits

Poll-mode design can consume cores and complicate deployment. Queue APIs have concurrency assumptions; for example, a receive queue is not generally polled concurrently by multiple logical cores. Sample applications are teaching references, not production exchange gateways. Verify the documentation version against the installed DPDK release.

## Sources

- [Current Poll Mode Driver guide](https://doc.dpdk.org/guides/prog_guide/ethdev/ethdev.html)
- [Programmer's Guide](https://doc.dpdk.org/guides-23.11/prog_guide/index.html)
- [Sample applications introduction](https://doc.dpdk.org/guides-19.02/sample_app_ug/intro.html)
