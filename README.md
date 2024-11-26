# iitd24-data-systems

Day 1: Distributed data processing
Holy grail: transparently scale, and tolerate faults/stragglers;
Difficulties in transparent locality, scalability, fault tolerance, and straggler mitigation;
Introduction to checkpointing and replication;
Introduction to distributed data processing with MapReduce;
Main ideas: functional programming model; separate control and data plane; locality optimizations, re-execute lost/backup tasks, deterministic/idempotent tasks.
Lab: Write a fault tolerant computation from scratch
Day 2: Dataflow systems for batch processing
Keynote address: TBA
Spark’s Resilient distributed dataset (RDD) abstraction: write-once for consistent replication, coarse-grained transformations to reduce lineage, lineage-based re-execution of lost/backup tasks;
Abstractions beyond MapReduce, lazy execution, stage planning, narrow and wide-dependencies, query optimizations.
Lab: Hands-on exercises with Spark.
Day 3: Dataflow systems for stream processing
Semantics of stream processing: unbounded streams, event time vs processing time, hopping/sliding/session windows, watermarks;
Streaming query optimizations and continuous operator model of Flink for low-latency;
Fault tolerance: problems due to state in continuous operators, pull state out of operators by discretizing streams, consistent checkpoints in Flink using Chandy-Lamport algorithm.
Lab: Hands-on exercises with Flink.
Day 4: Cyclic dataflow systems
Iterative data processing: solving graph problems with iterative data processing, driver-based iterations vs native iterations with cyclic dataflows, changes for creating consistent checkpoints.
Introduction to ML workflows: error handling and correction as a first class citizen, Reactive dataflow with deletes, edits, and appends.
Backward and forward lineage for backward tracing and delete propagation, stage planning with incremental/non-incremental, monotonic/non-monotonic operators
Lab: Hands-on exercises with Popper.
Day 5: Cross-platform data processing
Introduction to Wayang: a platform for cross-framework data processing, allowing optimizations across Spark, Flink, and Relational Databases.
Sessions about data systems research at IITD, guiding participants interested in pursuing higher studies, and research success stories.
Lab: Hands-on exercises with Wayang.
