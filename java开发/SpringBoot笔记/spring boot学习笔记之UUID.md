 

#### 1.[UUID](https://so.csdn.net/so/search?q=UUID&spm=1001.2101.3001.7020) 简介

百度百科：

UUID 是 通用唯一识别码（Universally [Unique](https://so.csdn.net/so/search?q=Unique&spm=1001.2101.3001.7020) Identifier）的缩写，是一种软件建构的标准，亦为[开放软件基金会](https://baike.baidu.com/item/%E5%BC%80%E6%94%BE%E8%BD%AF%E4%BB%B6%E5%9F%BA%E9%87%91%E4%BC%9A/1223731)组织在[分布式计算](https://baike.baidu.com/item/%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%A1%E7%AE%97/85448)环境领域的一部分。其目的，是让[分布式系统](https://so.csdn.net/so/search?q=%E5%88%86%E5%B8%83%E5%BC%8F%E7%B3%BB%E7%BB%9F&spm=1001.2101.3001.7020)中的所有元素，都能有唯一的辨识信息，而不需要通过中央控制端来做辨识信息的指定。如此一来，每个人都可以创建不与其它人冲突的UUID。在这样的情况下，就不需考虑数据库创建时的名称重复问题。目前最广泛应用的UUID，是[微软公司](https://baike.baidu.com/item/%E5%BE%AE%E8%BD%AF%E5%85%AC%E5%8F%B8/732128)的[全局唯一标识符](https://baike.baidu.com/item/%E5%85%A8%E5%B1%80%E5%94%AF%E4%B8%80%E6%A0%87%E8%AF%86%E7%AC%A6/3352267)（[GUID](https://baike.baidu.com/item/GUID/3352285)），而其他重要的应用，则有Linux ext2/ext3文件系统、LUKS加密分区、GNOME、KDE、Mac OS X等等。另外我们也可以在e2fsprogs包中的UUID库找到实现。

参考博文：[https://www.cnblogs.com/java-class/p/4727698.html](https://www.cnblogs.com/java-class/p/4727698.html)

#### 2.UUID 组成

   UUID保证对在同一时空中的所有机器都是唯一的。通常平台会提供生成的API。

   按照开放软件基金会(OSF)制定的标准计算，用到了以太网卡地址、纳秒级时间、芯片ID码和许多可能的数字。

UUID由以下几部分的组合：

（1）当前日期和时间，UUID的第一个部分与时间有关，如果你在生成一个UUID之后，过几秒又生成一个UUID，则第一个部分不同，其余相同。

（2）时钟序列。

（3）全局唯一的IEEE机器识别号，如果有网卡，从网卡MAC地址获得，没有网卡以其他方式获得。

   UUID的唯一缺陷在于生成的结果串会比较长。关于UUID这个标准使用最普遍的是微软的GUID(Globals Unique Identifiers)。

   标准的UUID格式为：xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx (8-4-4-4-12)。

#### 3.项目实战

    UUID 来作为数据库数据表主键是非常不错的选择，保证每次生成的UUID 是唯一的。  
a.生成 UUID：

```java
public static void main(String[] args) {
        for(int i=0;i<10;i++){
            String uuid = UUID.randomUUID().toString().replaceAll("-", "");
            System.out.println(uuid);
        }
    }
```

b.生成指定数目的 UUID：

```java
/**
     * 获得指定数目的UUID 
     * @param number int 需要获得的UUID数量 
     * @return String[] UUID数组 
     */
    public static String[] getUUID(int number){
        if(number < 1){
            return null;
        }
        String[] retArray = new String[number];
        for(int i=0;i<number;i++){
            retArray[i] = getUUID();
        }
        return retArray;
    }
 
    /**
     * 获得一个UUID 
     * @return String UUID 
     */
    public static String getUUID(){
        String uuid = UUID.randomUUID().toString();
        //去掉“-”符号 
        return uuid.replaceAll("-", "");
    }
```

文章知识点与官方知识档案匹配，可进一步学习相关知识

[Java技能树](https://edu.csdn.net/skill/java/?utm_source=csdn_ai_skill_tree_blog)[首页](https://edu.csdn.net/skill/java/?utm_source=csdn_ai_skill_tree_blog)[概览](https://edu.csdn.net/skill/java/?utm_source=csdn_ai_skill_tree_blog)136489 人正在系统学习中

本文转自 <https://blog.csdn.net/vaingloryss/article/details/89408422>，如有侵权，请联系删除。