# University of Chicago FINM 32700 — Low Latency Trading Systems

## Scope and public material

The current course description covers advanced data structures, STL/Boost, parallel programming, inter-process communication, linear algebra, simulation/modeling, and C++ trading-strategy projects. The historical 2019–20 catalog, under the older title *Advanced Computing for Finance*, says students build a trading system, implement an algorithm, connect to an exchange or broker, and address performance. A separate 2012 UChicago course, CSPP 51025 *Practicum in Trading Systems Development*, supplies a complementary exchange workload: order receipt, matching, book management, market-data broadcast, trade notification, shared memory, threads, queues, sockets, multicast, and TCP/UDP tradeoffs. No lineage or equivalence between CSPP 51025 and FINM 32700 is assumed.

## What it contributes

FINM 32700 supplies the domain skeleton missing from generic performance courses. The target is not an isolated kernel but a trading algorithm connected through simulator or exchange workflows, concurrent state, IPC, protocols, and recovery behavior.

## Transfer to trading systems

The skill should measure feed-to-state, state-to-decision, and decision-to-wire paths under representative message rates. It should verify order-state transitions, sequence handling, reconnect/recovery, and IPC ordering alongside throughput and latency. Architecture changes should be assessed at the system boundary, not accepted because one function benchmark improves.

## Limits

The current page is a concise description and links a Box syllabus whose contents were not inspectable in this review. The 2019–20 catalog and separate 2012 syllabus are historical and must not be presented as the current course. Public accessibility does not establish an open redistribution license; this corpus links and paraphrases. None of the public sources prescribes a modern benchmark threshold.

## Sources

- [Current FINM 32700 page](https://finmath.uchicago.edu/curriculum/degree-concentrations/financial-computing/finm-32700/)
- [Current linked Box syllabus](https://uchicago.app.box.com/s/6npwocd9tmffsbgddwgaujn9xto2gkbb)
- [2019–20 Graduate Catalog](https://cpb-us-w2.wpmucdn.com/voices.uchicago.edu/dist/7/1014/files/2020/02/Graduate-Divisions-Catalog-2019-20.pdf)
- [Separate 2012 CSPP 51025 syllabus](https://klasses.cs.uchicago.edu/archive/2012/spring/51025-1/syllabus.html)
