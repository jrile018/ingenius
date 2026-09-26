# Stanford CS349F — Fabric Architectures for AI Systems

## Scope and public material

Stanford's official catalog describes a course on fabrics for GPU/CPU clusters, cloud systems, financial trading, and other time-sensitive workloads. The public evidence is a catalog description and offering metadata; detailed lectures and assignments were not found publicly.

## What it contributes

The description emphasizes deterministic ultra-low latency at near-100% goodput and treats topology, congestion control, load balancing, job scheduling, fabric scheduling, and edge-centric versus network-centric control as a coupled design problem.

## Transfer to trading systems

The useful design rule is to evaluate tail latency and goodput together, especially near saturation and under burst contention. A component with excellent unloaded median latency may still violate the system objective when queues, load balancing, and scheduling interact. Edge and network mechanisms need an explicit coordination contract.

## Limits

The public page supports a capability taxonomy, not recipes, thresholds, or benchmark procedures. Detailed claims require independent primary sources before they become skill instructions.

## Sources

- [Official Stanford Bulletin entry](https://bulletin.stanford.edu/courses/2213481)
- [Stanford Spring course schedule](https://www.cs.stanford.edu/course-schedule-spring-quarter)
