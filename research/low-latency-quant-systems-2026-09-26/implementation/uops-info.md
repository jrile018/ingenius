# uops.info

## Evidence

uops.info publishes automatically measured instruction latency, reciprocal throughput, execution-port use, and operand-pair dependencies for many Intel and AMD generations. Its interactive tables, generated instruction pages, and machine-readable XML distinguish exact encodings and explicit or implicit operands. The associated ASPLOS 2019 work documents the measurement approach.

## Skill use

Use uops.info only after a hot instruction sequence and target microarchitecture are known. Query the exact form, operands, encoding, and CPU. Keep latency, throughput, dependency chains, and port pressure separate. Use the result to form a hypothesis about generated assembly, then test the application workload and counters. Never copy a number from one CPU generation to another.

## Limits

These are isolated instruction measurements, not predictions of cache misses, branches, OS interference, queues, or end-to-end trading latency. No explicit dataset license was identified for the XML, so the skill should link or query rather than vendor the dataset without permission.

## Sources

- [Project](https://uops.info/)
- [Background](https://uops.info/background.html)
- [Machine-readable XML](https://uops.info/xml.html)
- [Paper page](https://uops.info/paper.html)
