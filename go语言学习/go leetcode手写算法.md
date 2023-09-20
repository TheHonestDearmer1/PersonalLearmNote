## 冒泡排序

冒泡排序：从序列的一端开始往另一端冒泡，依次比较相邻的两个数的大小。

设数组长度为N。

1．每轮比较相邻的前后两个数据，如果前面数据大于或者小于后面的数据，就将二个数据交换。

2．这样每轮对数组的第0个数据到N-1个数据进行一次遍历后，最大或者最小的一个数据就到数组第N-1个位置。

3. 第一轮比较到下标为N-1的数据（最后一个），以后每次比较都-1。

```go
   for i := 0;i<len(nums1)-1;i++ {
         for j := i+1;j<len(nums1);j++ {
          if nums1[i] >=nums1[j] {
             temp = nums1[i]
             nums1[i] = nums1[j] 
             nums1[j] = temp
          }
     }
   }
```



## 双指针

在处理数组和链表相关问题时，双指针技巧是经常用到的，双指针技巧主要分为两类：**左右指针**和**快慢指针**。

所谓**左右指针**，就是两个指针相向而行或者相背而行；而所谓**快慢指针**，就是两个指针同向而行，一快一慢。

对于单链表来说，大部分技巧都属于快慢指针，前文 [单链表的六大解题套路](https://labuladong.github.io/algo/di-ling-zh-bfe1b/shuang-zhi-0f7cc/) 都涵盖了，比如链表环判断，倒数第 `K` 个链表节点等问题，它们都是通过一个 `fast` 快指针和一个 `slow` 慢指针配合完成任务。

在数组中并没有真正意义上的指针，但我们可以把索引当做数组中的指针，这样也可以在数组中施展双指针技巧，**本文主要讲数组相关的双指针算法**。

**个人思路卡点**：快指针曾经是经过慢指针经过的位置了，已经检查过了慢指针的位置



### 快慢指针

**定义一个慢，一个快指针，指针前后比较，适合用于在不开辟新数组的情况下修改数据**

**数组问题中比较常见的快慢指针技巧，是让你原地修改数组**。

[26. 删除有序数组中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/)

**思路：**

**这道题的逻辑是两个指针指到非相同元素前指向的都是非相同元素**

```go
func removeDuplicates(nums []int) int {
  slow,fast := 0,0
  for fast <len(nums){
      if nums[slow] != nums[fast] {
          slow++
          nums[slow] = nums[fast]
      }
      fast++
  }
  return slow+1 //引索+1
}
```



**思路：**

**这道题的逻辑是找到非val元素之前，找到的是val元素，所以slow代表的是val元素，用非val元素替代val元素**

[27. 移除元素](https://leetcode.cn/problems/remove-element/)

```go
func removeElement(nums []int, val int) int {
   slow,fast := 0, 0
   for fast<len(nums) {
       if nums[fast] != val { //逻辑是找到非val元素之前，找到的是val元素，所以slow代表的是val元素
       //slow的数值是fast走过的
          nums[slow] = nums[fast] //快指针覆盖慢指针
          slow++
       }
       fast++
   }
   return slow 
}
```

