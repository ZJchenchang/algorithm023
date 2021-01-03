学习笔记
第一周学习心得：
一.具体方向和方法论上：
1.五毒神掌其实本质是一种项目制学习。就问遇到了一个问题，我们围绕这个问题具体展开解决方案。这是一种很高效的学习方法，符合成年人的实际经验。这个方法可以迁移到其他学习领域，比如我现在要看一个英语文档，最好的办法就是直接读，虽然我英语水平不好，但就是直接读，遇到具体的从句单词再去考量它在这段文本中的意思，而不是每次都从背单词开始。再比如，现在要期末考试，如何进行系统性复习？把书从头看到尾吗？不是，是直接拿一张卷子来，开始做。你会遇到很多压根都没听过的问题，以这个问题为出发点，反向查找对应知识点，然后同时看答案，理解答案的思路和对应知识点。你脑中的知识地图就开始点亮了。
2.覃超老师是一个很有耐心的人，谢谢他的善意。群里很多小伙伴也是，感谢他们，我是一个外行人，从零开始学编程，语法都不熟悉的同时上手算法，个中滋味确实独特，但我相信有这群人在，坚持下去，主动积极，我能抵达自己要的远方。合抱之木生于毫末，九层高台始于垒土。

二.积累的编程心智模式：
1.多看那些可以形成套路的代码块：比如最多可盛水容器中，双指针夹逼的方法。比如要是涉及求一个周期性判断，可以考虑%取余数。星座，生肖，星期都可以用，
2.阅读好代码是写好代码的前提，如同阅读是写作最好的准备。阅读的同时，至少掌握一个算法问题的2种以上方法，并总结归纳出这些代码的各自优缺点，还有。比如如下总结“盛水最多的容器”，当然更多的是不足，我要加油，付出不亚于任何人的努力。人生的唯一捷径就是早点意识到“人生没有捷径”
def maxArea(self, height: List[int]) -> int:
        # # 第一种暴力解法：暴力法会导致测试用例太多而超出时间限制。
        # area = 0
        # for i in range(len(height)-1):
        #     for j in range(i+1, len(height)):
        #         areanew = min(height[i], height[j]) * (j - i) # 盛水矩形的高度以较低的一边为基准
        #         area = max(area, areanew)
        # return area

        # 第二种-模式识别：双指针法夹逼
        # left, right = 0 ,len(height)-1
        # areaMax = 0
        # while left < right:
        #     areaMax = max(areaMax, min(height[left], height[right]) * (right - left))
        #     if height[left] <= height[right]:
        #         left += 1
        #     else:
        #         right -= 1
        # return areaMax

        # 看了国际友人代码，尝试再优化，不使用max和min函数，因为if语句后已经比较过大小，直接使用height[left] or height[right]
        left, right = 0 ,len(height)-1
        areaMax = 0
        while left < right:
            if height[left] <= height[right]:
                area = height[left] * (right - left)
                left += 1
            else:
                area = height[right] * (right - left)
                right -= 1
            if areaMax <= area:
                areaMax = area
        return areaMax