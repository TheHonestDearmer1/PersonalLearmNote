 

进程池是为了简化多进程任务而生。当我们有大量的任务，其处理函数都是相同的，或者只是函数参数不同。这种情况，直接生成和任务数量相同的进程是极其消耗资源的（比如用Process和for依次生成进程）。这个时候就非常适合使用进程池Pool

```python
import multiprocessing as mp
n_proc = 5
pool = mp.Pool(n_proc)
```

以上代码生成了5个进程的池子。最多可以同时运行5个相同的函数。  
pool类有以下4种非常常用的类型。

*   apply：阻塞，任务其实是一个一个执行完的。无法实现并行效果
*   apply\_async
*   map
*   map\_async

其中map和map\_async的用法接近，apply和appy\_async的用法接近。  
带async的区别主要有：

*   返回的顺序不是按照建立任务的顺序来的，完全看哪个任务先结束谁先返回
*   有一个callback参数。可以用于记录返回值和其他回调功能，比如结合tqdm制作多进程进度条。
*   异步函数接受参数，但同步函数接受一个装载参数的迭代器。

现在有一个函数，功能是睡眠一段时间。来看一下四种函数的用法。

```python
import multiprocessing as mp

def test_func(v):
    print(v)
    sleep(10/2-v/2)  # v越大 运行时间越少
    return v

# 所需要测试的数据
data = range(10)
```

#### apply

```python
# apply
n_proc = 5
pool = mp.Pool(n_proc)
res = []
for d in data:
    pool.apply(test_func, (d,))
pool.close()
pool.join()
```

可以发现，运行的总时长等于所有任务的总时长。那这个函数的意义是？

#### apply\_async

```python
n_proc = 5
pool = mp.Pool(n_proc)
res = []
for d in data:
    tmp = pool.apply_async(test_func, (d,))
    # tmp.get() # 如果有这句，则程序会等待该进程执行完，拿到其返回值，才会进入下个for循环。相当于map的效果
    res.append(tmp)

pool.close()
pool.join()
for r in res:
	# 如果get放到tmp后面，则会实现和map一样的效果
    r.get() # 返回值需要用get()拿到。

```

从打印内容来看，一共有10个任务，pool同时处理5个任务，哪个任务结束了，该进程就执行下个任务

#### map

```python
n_proc = 5
pool = mp.Pool(n_proc)
res = pool.map(test_func, data)
pool.close()
pool.join()
print(res) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

也是同时执行5个任务。总时间在5s左右。说明是确实是并行执行以上10个任务的

#### map\_async

```python
n_proc = 5
pool = mp.Pool(n_proc)
res = pool.map_async(test_func, data)
pool.close()
pool.join()
print(res.get())
```

依然是并行运行

大家应该注意到了。map和map\_async没有用到for循环新建进程任务。因此总结出：以map为首的函数用法是，针对多次运行同一个任务（test\_func），如果只是参数不同，可以把参数做成一个迭代器。

#### callback回调函数的用法

带async的函数，支持应用回调函数。  
当进行执行完毕，我们就会调用这个回调函数。回调函数的参数有一个，为进程任务的返回值。

```python
def log(v):
    callback_res.append(v)
    # print(callback_res)

data = range(10)
callback_res = []
n_proc = 5
pool = mp.Pool(n_proc)
for d in data:
    pool.apply_async(test_func, (d,), callback=log)
pool.close()
pool.join()
print(callback_res)  # [4, 3, 2, 1, 0, 6, 8, 7, 9, 5]
```

从该示例中，我们可以看到，log函数中执行的内容是，在callback\_res中加入test\_func的返回值。同时注意到callback\_res不是按照顺序排列的，而是按照执行速度依次排列的。在头5个任务中，输入为4的任务执行最快。

#### 多进程进度条

```python
from tqdm import tqdm
pbar = tqdm(total=len(data))
pbar.set_description('Sleep')
update = lambda *args: pbar.update()

n_proc = 5
pool = mp.Pool(n_proc)
for d in data:
	pool.apply_async(test_func, (d,), callback=update)
pool.close()
pool.join()
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/2aeffdb163874c55869f7fc785c3f612.png)  
这里我们采用[tqdm](https://so.csdn.net/so/search?q=tqdm&spm=1001.2101.3001.7020)生成进度条，然后使用labmda操作符，将其转换为函数，然后作为回调对象。那么进程池每处理完一个任务，就会调用一次tqdm的update()。从而实现多进程的进度条显示。

参考
--

[Python multiprocessing.Pool的四种方法比较：: map, apply, map\_async, apply\_async](https://blog.csdn.net/txpp520/article/details/106911867?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-5.base&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-5.base)  
[Python多进程处理方法（Pool、apply\_async、map\_async）](https://blog.csdn.net/achitc/article/details/118379686?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-5.base&spm=1001.2101.3001.4242)  
[python多进程打印进度条](https://blog.csdn.net/JNingWei/article/details/105605624)  
[Multiprocessing : use tqdm to display a progress bar](https://stackoverflow.com/questions/41920124/multiprocessing-use-tqdm-to-display-a-progress-bar)

 

文章知识点与官方知识档案匹配，可进一步学习相关知识

[Python入门技能树](https://edu.csdn.net/skill/python/?utm_source=csdn_ai_skill_tree_blog)[首页](https://edu.csdn.net/skill/python/?utm_source=csdn_ai_skill_tree_blog)[概览](https://edu.csdn.net/skill/python/?utm_source=csdn_ai_skill_tree_blog)409178 人正在系统学习中

本文转自 <https://blog.csdn.net/qq_34914551/article/details/119451639>，如有侵权，请联系删除。