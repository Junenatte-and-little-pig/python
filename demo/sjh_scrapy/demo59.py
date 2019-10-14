# -*- encoding: utf-8 -*-
from lxml import etree

baidu_src = '''
<html>
    <head text="hello">
        <meta http-equiv="content-type" content="text/html;charset=utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=Edge">
        <meta content="always" name="referrer">
        <meta name="theme-color" content="#2932e1">
        <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
        <link rel="search" type="application/opensearchdescription+xml" href="/content-search.xml" title="百度搜索">
        <link rel="icon" sizes="any" mask="" href="//www.baidu.com/img/baidu_85beaf5496f291521eb75ba38eacbd87.svg">
        <link rel="dns-prefetch" href="//s1.bdstatic.com">
        <link rel="dns-prefetch" href="//t1.baidu.com">
        <link rel="dns-prefetch" href="//t2.baidu.com">
        <link rel="dns-prefetch" href="//t3.baidu.com">
        <link rel="dns-prefetch" href="//t10.baidu.com">
        <link rel="dns-prefetch" href="//t11.baidu.com">
        <link rel="dns-prefetch" href="//t12.baidu.com">
        <link rel="dns-prefetch" href="//b1.bdstatic.com">
        <title>百度一下，你就知道</title>
    </head>
    <body link="#0000cc">hello
        <div id="wrapper" style="display: block;">
            <div class="s_tab" id="s_tab">
                <div class="s_tab_inner">
                    <b>网页</b>
                    <a href="//www.baidu.com/s?rtt=1&amp;bsst=1&amp;cl=2&amp;tn=news&amp;word=" wdfield="word" onmousedown="return c({'fm':'tab','tab':'news'})" sync="true">资讯</a>
                    <a href="http://tieba.baidu.com/f?kw=&amp;fr=wwwt" wdfield="kw" onmousedown="return c({'fm':'tab','tab':'tieba'})">贴吧</a>
                    <a href="http://zhidao.baidu.com/q?ct=17&amp;pn=0&amp;tn=ikaslist&amp;rn=10&amp;word=&amp;fr=wwwt" wdfield="word" onmousedown="return c({'fm':'tab','tab':'zhidao'})">知道</a>
                    <a href="http://music.taihe.com/search?fr=ps&amp;ie=utf-8&amp;key=" wdfield="key" onmousedown="return c({'fm':'tab','tab':'music'})">音乐</a>
                    <a href="http://image.baidu.com/search/index?tn=baiduimage&amp;ps=1&amp;ct=201326592&amp;lm=-1&amp;cl=2&amp;nc=1&amp;ie=utf-8&amp;word=" wdfield="word" onmousedown="return c({'fm':'tab','tab':'pic'})">图片</a>
                    <a href="http://v.baidu.com/v?ct=301989888&amp;rn=20&amp;pn=0&amp;db=0&amp;s=25&amp;ie=utf-8&amp;word=" wdfield="word" onmousedown="return c({'fm':'tab','tab':'video'})">视频</a>
                    <a href="http://map.baidu.com/m?word=&amp;fr=ps01000" wdfield="word" onmousedown="return c({'fm':'tab','tab':'map'})">地图</a>
                    <a href="http://wenku.baidu.com/search?word=&amp;lm=0&amp;od=0&amp;ie=utf-8" wdfield="word" onmousedown="return c({'fm':'tab','tab':'wenku'})">文库</a>
                    <a href="//www.baidu.com/more/" onmousedown="return c({'fm':'tab','tab':'more'})">更多»</a>
                </div>
            </div>
            <div class="qrcodeCon">
                <div id="qrcode">
                    <div class="qrcode-item qrcode-item-1">
                        <div class="qrcode-img"></div>
                        <div class="qrcode-text">
                            <p class="title">下载百度APP</p>
                            <p class="sub-title">有事搜一搜&nbsp;&nbsp;没事看一看</p>
                        </div>
                    </div>
                </div>
            </div>
            <div id="ftCon">
                <div class="ftCon-Wrapper">
                    <div id="ftConw">
                        <p id="lh">
                            <a id="setf" href="//www.baidu.com/cache/sethelp/help.html" onmousedown="return ns_c({'fm':'behs','tab':'favorites','pos':0})" target="_blank">把百度设为主页</a><a onmousedown="return ns_c({'fm':'behs','tab':'tj_about'})" href="http://home.baidu.com">关于百度</a><a onmousedown="return ns_c({'fm':'behs','tab':'tj_about_en'})" href="http://ir.baidu.com">About&nbsp;&nbsp;Baidu</a><a onmousedown="return ns_c({'fm':'behs','tab':'tj_tuiguang'})" href="http://e.baidu.com/?refer=888">百度推广</a></p><p id="cp">©2019&nbsp;Baidu&nbsp;<a href="http://www.baidu.com/duty/" onmousedown="return ns_c({'fm':'behs','tab':'tj_duty'})">使用百度前必读</a>&nbsp;<a href="http://jianyi.baidu.com/" class="cp-feedback" onmousedown="return ns_c({'fm':'behs','tab':'tj_homefb'})">意见反馈</a>
                            &nbsp;京ICP证030173号&nbsp;
                            <i class="c-icon-icrlogo"></i>
                            &nbsp;
                            <a id="jgwab" target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11000002000001">京公网安备11000002000001号</a>
                            &nbsp;
                            <i class="c-icon-jgwablogo"></i>
                        </p>
                    </div>
                </div>
            </div>
            <div id="wrapper_wrapper">
            </div>
        </div>
        <div class="c-tips-container" id="c-tips-container"></div>
    </body>
</html>
'''
html = etree.HTML(baidu_src)  # == html.xpath('.')[0]
# print(etree.tostring(html).decode('utf-8'))
'''
位置路径表达式

位置路径可以是绝对的，也可以是相对的。
绝对路径起始于正斜杠( / )，而相对路径不会这样。在两种情况中，位置路径均包括一个或多个步，每个步均被斜杠分割：
绝对位置路径：
    /step/step/...
相对位置路径：
    step/step/...

每个步均根据当前节点集之中的节点来进行计算。
步（step）包括：
    轴（axis）
        定义所选节点与当前节点之间的树关系
    节点测试（node-test）
        识别某个轴内部的节点
    零个或者更多谓语（predicate）
        更深入地提炼所选的节点集

步的语法：
    轴名称::节点测试[谓语]
'''

'''
轴名称 	结果
ancestor 	选取当前节点的所有先辈（父、祖父等）。
ancestor-or-self 	选取当前节点的所有先辈（父、祖父等）以及当前节点本身。
attribute 	选取当前节点的所有属性。
child 	选取当前节点的所有子元素。
descendant 	选取当前节点的所有后代元素（子、孙等）。
descendant-or-self 	选取当前节点的所有后代元素（子、孙等）以及当前节点本身。
following 	选取文档中当前节点的结束标签之后的所有节点。
namespace 	选取当前节点的所有命名空间节点。
parent 	选取当前节点的父节点。
preceding 	选取文档中当前节点的开始标签之前的所有节点。
preceding-sibling 	选取当前节点之前的所有同级节点。
self 	选取当前节点。
'''

'''
表达式 	描述
nodename 	选取此节点的所有子节点
/ 	从当前节点选取直接子节点
// 	从当前节点选取子孙节点
. 	选取当前节点
.. 	选取当前节点的父节点
@ 	选取属性
* 	通配符，选择所有元素节点与元素名
@* 	选取所有属性
'''

'''
n   指定位置元素 从1开始
last()  最后一个元素
position()  元素位置
text()  内容文本
[@attrib] 	选取具有给定属性的所有元素
[@attrib='value'] 	选取给定属性具有给定值的所有元素
[tag] 	选取所有具有指定元素的直接子节点
[tag='text'] 	选取所有具有指定元素并且文本内容是text节点
'''

print(html.xpath(
    '*'))  # [<Element head at 0x1a99a417788>, <Element body at 0x1a99a417848>]
print(html.xpath('head'))  # [<Element head at 0x1a99a417788>]
print(html.xpath('/*'))  # [<Element html at 0x1a99a385708>]
print(html.xpath('/html'))  # [<Element html at 0x1a99a385708>]
print(html.xpath(
    '/html/*'))  # [<Element head at 0x1a99a417848>, <Element body at 0x1a99a417688>]
print(html.xpath(
    '//meta'))  # [<Element meta at 0x1f806177748>, <Element meta at 0x1f806177fc8>, <Element meta at 0x1f806177648>, <Element meta at 0x1f8061777c8>]
print(html.xpath('/html/head//*'))
print(html.xpath('.'))  # [<Element html at 0x232262b5648>]
print(html.xpath(
    './*'))  # [<Element head at 0x211f9d07488>, <Element body at 0x211f9d07708>]
print(html.xpath('head')[0].xpath('..'))  # [<Element html at 0x221e4904908>]
print(html.xpath('/html/head/meta')[0].xpath(
    '@*'))  # ['content-type', 'text/html;charset=utf-8']
print(html.xpath(
    '//*/@content'))  # ['text/html;charset=utf-8', 'IE=Edge', 'always', '#2932e1']
print(html.xpath('//*/@content="text/html;charset=utf-8"'))  # True
print(html.xpath(
    '//*/meta[@content="text/html;charset=utf-8"]'))  # [<Element meta at 0x252193176c8>]
print(html.xpath(
    '//*/meta[@content="text/html;charset=utf-8"]/..'))  # [<Element head at 0x1f6d7368848>]
print(html.xpath(
    '//*/meta[@content="text/html;charset=utf-8"]/../@*'))  # ['hello']
print(html.xpath(
    '/html/body/div/div/div/a'))  # [<Element a at 0x296e27c9508>, <Element a at 0x296e27c98c8>, <Element a at 0x296e27c9a08>, <Element a at 0x296e27cc548>, <Element a at 0x296e27cc588>, <Element a at 0x296e27cc5c8>, <Element a at 0x296e27cc288>, <Element a at 0x296e27cc308>, <Element a at 0x296e27cc608>]
print(
    html.xpath('/html/body/div/div/div/a[1]'))  # [<Element a at 0x1d467949988>]
print(html.xpath(
    '/html/body/div/div/div/a[last()]'))  # [<Element a at 0x1d467949948>]
print(html.xpath(
    '/html/body/div/div/div/a[position()<3]'))  # [<Element a at 0x1d467949988>, <Element a at 0x1d467949808>]
print(html.xpath('/html/body/div/div/div/node()'))  # 包括子节点及内容文本
print(html.xpath('/html/body/div/div/div/a="贴吧"'))  # True
print(
    html.xpath('/html/body/div/div/div[a]'))  # [<Element div at 0x144316a7948>]
print(html.xpath(
    '/html/body/div/div/div[a="贴吧"]'))  # [<Element div at 0x19ccb3377c8>]
print(html.xpath(
    '/html/body/div/div/div/a[text()="贴吧"]'))  # [<Element a at 0x17261169a08>]
print(html.xpath(
    '/html/body/div/div/div/a/text()'))  # ['资讯', '贴吧', '知道', '音乐', '图片', '视频', '地图', '文库', '更多»']
print(html.xpath('body'))  # [<Element body at 0x14cdbbb7588>]
print(html.xpath('body')[0])  # <Element body at 0x19485df7548>
print(html.xpath('body')[0].tag)  # body
print(html.xpath('body')[0].attrib)  # {'link': '#0000cc'}
print(html.xpath('body')[0].get('link'))  # #0000cc
print(html.xpath('body')[0].text)  # hello
