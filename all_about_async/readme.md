### parallel vs concurrency

* parallel computing means each task runs on a separate processing unit, and do them together. means 2 lines 2 cashier. not good for python as the GIL.
* concurrency means application is making progress on more than one task at same time, and it switch between these tasks instead of running them one by one or in parallel. means 2 lines one cashier. works well in python. and it is a smart way, as many tasks involve waiting (network response etc..)

### asyncio

* the core of asyncio is a even loop, even loop is the brain, it can do tasks, and decide what tasks to be done. In python, 1 thread, only 1 task is done at one time. Thus, there is no racing condition.
* coroutine func, coroutine obj, and task
    * coroutine function: anything start with `async dev` is a coroutine function. it defines the process of a coroutine. for normal function with just `def`, it returns a return value or something. but when to call (well here means putting a `(...)` behind it) a coroutine function, it returns a coroutine object. like a func return a func. all the code in the `async def` wont be executed if we simply call it!
    * well, how to execute? 
        * first, we need to enter the async mode, which is the even loop! (this is `asyncio.run(coroutines)`), it is like we are entering the async world, letting the even loop take control of the sequence of execution!
        * second we need to turn coroutine into a task. `await` is a common way, it turns a coroutine (like asyncio.sleep()) into a task!. when we do await, below things happen
            * coroutine is packaged into a task, and the even loop is told that here we have a new task!. 
            * it also tells the even loop that, the runing of later code, needs to wait for the current coroutine is finished (or awaited).
            * it will yield, tells the evenloop that no need to spend time here, do something task else!
            * at last, when event loop thinks it is its turn, it will run it, get the result and assign to a variable if need to assign.
    * thus, coroutine func is something we `async def`. coroutine obj is `coroutine_obj = async_defined_func(...)`. and it becomes a task when it is `await`ed, and let evenloop take control.
        
* example

    * code 

        ```
        async def say_after(delay, what):
            await asyncio.sleep(delay=delay)
            print(what)

        async def say():
            print("start")
            await say_after(2, what="2s")
            await say_after(1, what="1s")
            print("end")

        asyncio.run(say())
        ```
    * explanation:
        * first the asyncloop sees `say()`, it put `say()` as its first task.
        * evenloop had nothing to do, it start to execute the code inside the async func `say`.
        * it prints start
        * it sees the first `say_after` function, it runs `say_after(...)` to get a coroutine obj. and the `await` in the front of this coroutine turns it into a task, and tells the evenloop that, we have a new task! and tells evenloop that, NEED TO WAIT FOR IT, then give the control back to even loop.
        * now evenloop has 2 tasks, `say` and the first `say_after`. but `say` cannot be executed anymore cos evenloop is told to WAIT for the finish of `say_after`.
        * thus evenloop let the `say_after` run first. `say after` did something similar cos there is a `await asyncio.sleep()` inside it. so this `say_after` needs to wait for the `sleep`. `await` give the task `sleep` to control loop and also tells the control loop that `say_after` needs to wait for `sleep` to finish.
        * now we have 3 tasks in the even loop
            * after 1s, `sleep` finished
            * `print(what)` in `say_after` get executed
            * back to `say` (now the evenloop has only `say` left)
            * now it sees the second `say_after`...
        * thus the whole process took 3 seconds.
    * observation
        * eventloop cannot active take control, it must be told
            * told by `await` (parent task waits for its children)
            * told by the finish of task (child task finishes)
        * here we have 2 coroutine, one took 1s, the other took 2s, why they dont wait together? where is the async?? when the first say_after is in the evenloop, why not trigger the second? well this is the issue with `await`. as the above explanation, `await` did quite a lot things (it lets the parent wait and create the task!!!), which seemingly makes async sync.
    
    * updated code which allows async

        ```
        async def say():
            print("start")
            task1 = asyncio.create_task(say_after(2, what="2s"))
            task2 = asyncio.create_task(say_after(1, what="1s"))
            await task1
            await task2
            print("end")
        ```
    
    * explanation
        * here we used the function `create_task`. this function can do part of job `await` does.
            * create task
            * register the task into evenloop
            * BUT DO NOT TASK THE PARENT TO WAIT, DO NOT GIVE CONTROL
        * thus the control still in the hand of `say`. 
            * now the first `await` appears
            * the `await task1` tells even loop, I need the task1 to be done, and let you take control.
            * now even loop takes control, it sees 3 tasks already!
                * say
                * task1
                * task2
            * and it knows say is paused to wait for task1
            * then it runs task1
                * task1 awaits sleep, control back to evenloop
            * evenloop FINDS OUT THAT, I can RUN task2 as well!!!
            * then it runs task2
                * tasks2 finishes first, cos it only waits 1s, then it prints `1s`
            * when task2 finished, evenloop took control again, it has nothing to do but wait
            * now task1 finished. 
            * now evenloop let `say` run
            * `say` sees `await task2`. but task2 is done!!. Thus here `await`'s function is more to fetch the return value of task2 (if there is any and assign to a variable)
    
    * observation
        * if we have 10 tasks, we write 10 times `await` and `create_task`?
        * that what `asyncio.gather` is for, `gather` returns `future`.
    
    * update code with gather
        ```
        async def say_after(delay, what):
            await asyncio.sleep(delay=delay)
            print(what)
            return what


        async def say():
            r1, r2 = None, None
            print("start")
            task1 = asyncio.create_task(say_after(2, what="2s"))
            task2 = asyncio.create_task(say_after(1, what="1s"))
            r1, r2 = await asyncio.gather(task1, task2)
            print(f"end, {r1=}, {r2=}")
        
        # gives
        # start
        # 1s
        # 2s
        # end, r1='2s', r2='1s'
        ```
    
    * explanation
        * `gather` return `future`, future can be awaited as well.
        * `gather` takes a number of coroutine or task, or even future. if coroutine, it will package it into a task and register into evenloop. `await` `future` will put all the return value of tasks into a list. (thats why above code can unpack it)
        * since `gather` can help up package coroutine into task and help REGISTER THEM ALL into evenloop, so we can update the code again!
    
    * update code with gather

        ```
        async def say():
            r1, r2 = None, None
            print("start")
            r1, r2 = await asyncio.gather(
                say_after(2, what="2s"),
                say_after(1, what="1s"),
            )
            print(f"end, {r1=}, {r2=}")
        ```
    
        and generically:

        ```
        async def say():
            things_to_do = [1,2,3]
            coroutines = [say_after(x, what=f"{x}s") for x in things_to_do]
            print("start")
            r = await asyncio.gather(
                *coroutines
            )
            print(f"end, {r}")  # end, ['1s', '2s', '3s']
        ```

    * finally
        * coroutine, without become a task, cannot be executed
        * must use await to get the return values

* what does `await` really do?
    * there are some issues with above discussion
        * when you await coroutune, await did not create task
        * rather, it adds coroutine into the task!, the control did not get passed back to the control loop
    * code
        ```
        async def main():
            # just await
            # await asyncio.sleep(0.1)

            # using create task
            await asyncio.create_task(
                asyncio.sleep(0.1)
            )
        ```
    * analysis: in the above code
        * if we just await
            * one task!, but it has 2 coroutine
            * bytecode: 

                ```
                ...
                GET_AWAITABLE
                LOAD_CONST
                YIELD_FROM
                ...
                ```

            * GET_AWAITABLE
                * _PyCoro_GetAwaitableIter: this helper function returns an awaitable for 'o'. if o is coroutine obj, returns o, other wise tp_as_async
                * GET_AWAITABLE put whatever returned to the top of the stack!
            * YIELD_FROM
                * for whatever we await, it is either a coroutine obj or it is a generator. it uses _PyGen_Send (uses the send in the generator)
                * and the core control part is here also. no matter it is task, coroutine or future, when it is finished, `retval` will be null. . Anything return in async def, is same as StopIteration puts the return value in the exception. and put the value on the top of the stack. The continue (continue the next byte code, in the infinite loop of EvalFrameDefault).
                * if retval is not null, which means it is not finished yet. it will set the position of instruction back. `f->f_lasti -= SIZEOF(_Py_CODEUNIT)`.  then it saved the current status of this function. which means, the next time when you run this function, it will continue from here. finally `goto existing`. it did not finish executing the function, but it return some value, the retval, the value yielded.
                * so this is how await stop half way inside a function, return something.
            * source code of await
                * coroutine is generator!
                * Task inherets from future, future has the `__await__`, which allows you to `await xxxxxx()`. this await, when it is not done, it yields. it done, it returns.
            * now task, how does it async, and wait each other?
                * in the init of the task, there is a `self._loop.call_soon(...)`
                * this `call_soon`, remember that the minimal object even loop can control is task, there will be always one task being executed.
                * in the just await example, the top task is `main`.
                * task will "tag" other tasks, says, when you finish, wake me up!. then this task disppears from even loop. (wake me up is a callback put at other tasks this task depends on.)
                * the depending task, upon finishing will call `__schedule_callbacks`. it adds all the callbacks of him, to loop.call_soon. it did not call the callback, but ask the even loop to schedule!, this is make it "even" for all tasks and even loop also has the context of them all.
            * evenloop
                * i dont know how the magic works at evenloop yet..


        * using create task
            * two tasks!
