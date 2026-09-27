# Reliable quantitative data systems electives

## Capability target

Build research and trading data flows that preserve point-in-time truth, identity, reproducibility, transactional invariants, and recoverability under duplicates, reordering, concurrency, and partial failure.

## Selected sources

- [MIT 6.5840 Distributed Systems, Spring 2026](https://pdos.csail.mit.edu/6.824/): current graduate course on distributed-system abstractions and implementation, especially fault tolerance, replication, and consistency, with labs and case studies.
- [CMU 15-445/645 Database Systems, Spring 2025](https://15445.courses.cs.cmu.edu/spring2025/syllabus.html): upper-level project course on storage, indexes, concurrency control, recovery, and distributed/parallel OLTP/OLAP tradeoffs.
- [CMU Database Group course catalog](https://db.cs.cmu.edu/courses/): pathway to graduate 15-721 and research topics when DBMS implementation depth is needed.
- [Stanford CS244B Distributed Systems](https://www.scs.stanford.edu/17au-cs244b/): public historical materials on transactions, consistency, storage, failure, and distributed state.

## Synthesis and boundary

The domain-specific addition is temporal truth: event, effective, receipt, ingestion, and knowledge time; dated symbology; revisions; point-in-time universes; and reproducible lineage. Database and distributed-systems mechanisms are selected to preserve these facts, not treated as ends in themselves.

This skill owns data correctness and recovery. It does not own statistical interpretation or microsecond hot-path optimization, which remain with the finance and low-latency skills.

