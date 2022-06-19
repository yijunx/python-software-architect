###


### parallel vs concurrency

* parallel computing means each task runs on a separate processing unit, and do them together. means 2 lines 2 cashier. not good for python as the GIL.
* concurrency means application is making progress on more than one task at same time, and it switch between these tasks instead of running them one by one or in parallel. means 2 lines one cashier. works well in python. and it is a smart way, as many tasks involve waiting (network response etc..)