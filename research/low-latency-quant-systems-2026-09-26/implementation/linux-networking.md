# Linux networking, queue placement, and timestamping

## Evidence

The Linux kernel documents receive/transmit queue scaling, IRQ affinity, RSS/RPS/RFS/XPS, NAPI busy polling, per-socket and epoll controls, and software/hardware timestamping. The timestamping interface exposes multiple boundaries, including userspace-to-scheduler, scheduler-to-driver, completion, and hardware timestamps.

## Skill use

A networking experiment must define exactly where time starts and ends. Queue count, IRQ affinity, CPU placement, NUMA locality, interrupt moderation, busy-poll settings, socket options, and NIC configuration belong in the benchmark record. Queue-to-core changes can improve one load point and hurt another, so test burst load and tail latency rather than repeat a universal queue-count rule. Busy polling trades CPU and power for latency and must be treated as an explicit operational cost.

## Limits

Kernel documentation describes mechanisms and suggested configurations, not a guarantee for every NIC, driver, topology, kernel, or workload. Current documentation should be rechecked at use time because interfaces evolve.

## Sources

- [Scaling in the Linux networking stack](https://www.kernel.org/doc/html/next/networking/scaling.html)
- [NAPI and busy polling](https://docs.kernel.org/networking/napi.html)
- [Network timestamping](https://docs.kernel.org/networking/timestamping.html)
