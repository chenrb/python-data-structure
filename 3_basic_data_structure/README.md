# 目标  
1、理解抽象数据类型的栈，队列，deque 和列表。  
2、能够使用 Python 列表实现 ADT 堆栈，队列和 deque。  
3、了解基本线性数据结构实现的性能。  
4、了解前缀，中缀和后缀表达式格式。  
5、使用栈来实现后缀表达式。  
6、使用栈将表达式从中缀转换为后缀。  
7、使用队列进行基本时序仿真。  
8、能够识别问题中栈，队列和 deques 数据结构的适当使用。  
9、能够使用节点和引用将抽象数据类型列表实现为链表。  
10、能够比较我们的链表实现与 Python 的列表实现的性能。  
  
>线性数据结构  
（栈，队列，deques，列表）是一类数据的容器，它们数据项之间的顺序由添加或删除的顺序决定。一旦一个数据项被添加，它相对于前后元素一直保持该位置不变。诸如此类的数据结构被称为线性数据结构。
  
>栈（有时称为“后进先出栈”）是一个项的有序集合，其中添加移除新项总发生在同一端。这一端通常称为“顶部”。与顶部对应的端称为“底部”。例如：托盘碟子，书本。  
例子：简单的括号匹配例子  
例子：十进制转换成其他进制例子  
例子：中缀前缀和后缀表达式*(有待理解)  

>队列（先进先出）是项的有序结合，其中添加新项的一端称为队尾，移除项的一端称为队首。当一个元素从队尾进入队列时，一直向队首移动，直到它成为下一个需要移除的元素为止。  
例子：烫手山芋  
例子：打印机*(有待理解)  

>Deque:deque（也称为双端队列）是与队列类似的项的有序集合。它有两个端部，首部和尾部，并且项在集合中保持不变。deque 不同的地方是添加和删除项是非限制性的。可以在前面或后面添加新项。同样，可以从任一端移除现有项。在某种意义上，这种混合线性结构提供了单个数据结构中的栈和队列的所有能力。
粒子：回文数

# 总结 
- 线性数据结构以有序的方式保存它们的数据。  
- 栈是维持 LIFO，后进先出，排序的简单数据结构。  
- 栈的基本操作是 push ， pop 和 isEmpty 。  
- 队列是维护 FIFO（先进先出）排序的简单数据结构。  
- 队列的基本操作是 enqueue ， dequeue 和 isEmpty 。  
- 前缀，中缀和后缀都是写表达式的方法。  
- 栈对于设计计算解析表达式算法非常有用。  
- 栈可以提供反转特性。  
- 队列可以帮助构建定时仿真。  
- 模拟使用随机数生成器来创建真实情况，并帮助我们回答“假设”类型的问题。  
- Deques 是允许类似栈和队列的混合行为的数据结构。  
- deque 的基本操作是 addFront ， addRear ， removeFront ， removeRear 和 isEmpty 。  
- 列表是项的集合，其中每个项目保存相对位置。  
- 链表实现保持逻辑顺序，而不需要物理存储要求。  
- 修改链表头是一种特殊情况。  