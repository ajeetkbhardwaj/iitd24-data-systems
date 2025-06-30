Aim to build a distributed word count application but we assume our multi-core system is a distributed system in itself.

We will start stateless python processes to act as distributed workers. These workers will co-ordinate with each other through [Redis](https://redis.io/). Redis behaves like the master (or driver program) in contemporary systems. 

For further simplicity, we do not create control plane/data plane separation which is crucial for performance! Workers take tasks from Redis and push word counts back to Redis.

All workers have access to a shared file system for reading and writing large inputs. This is again trivially true on our single system. In a real setup, workers would additionally use a distributed file system like HDFS or a blob store like S3.
