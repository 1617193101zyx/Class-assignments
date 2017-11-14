Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib
>>> response = urllib2.urlopen("http://www.jsit.edu.cn")

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    response = urllib2.urlopen("http://www.jsit.edu.cn")
NameError: name 'urllib2' is not defined
>>> 
KeyboardInterrupt
>>> import urllib2
>>> response = urllib2.urlopen("http://www.jsit.edu.cn")
>>> print response.read()
 <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>欢迎光临 - 江苏信息职业技术学院</title>
<meta http-equiv="keywords" content="欢迎光临 - 江苏信息职业技术学院"/>
<meta http-equiv="description" content="欢迎光临- 江苏信息职业技术学院"/>


<script type="text/javascript" src="/r/cms/www/red/js1/jquery-1.7.1.min.js"></script>
<script type="text/javascript" src="/r/cms/www/red/js1/js.js"></script>
<script type="text/javascript" src="/r/cms/www/red/js1/jquery.jslides.js"></script>
<script type="text/JavaScript">
$(function(){
	$(".tab01 li").hover(function(e) {
		nowTab=$(this).index();
		$(this).parent().children().removeClass("selected01");
		$(this).addClass("selected01");
		$(this).parent().parent().nextAll().addClass("dpN");
		$(this).parent().parent().parent().children().eq(nowTab+1).removeClass("dpN");
	});
	
	$(".tab02 li").hover(function(e) {
		nowTab=$(this).index();
		$(this).parent().children().removeClass("selected02");
		$(this).addClass("selected02");
		$(this).parent().parent().nextAll().addClass("dpN");
		$(this).parent().parent().parent().children().eq(nowTab+1).removeClass("dpN");
	});
	});
</script>

<link href="/r/cms/www/red/css/style2015.css" rel="stylesheet" type="text/css" />

<link href="/r/cms/www/red/css/layoutnxq.css" rel="stylesheet" type="text/css"/>


</head>

<body>
<div class="topbg">
    <div class="w980 mc cb">
        <div class="fL logo"><a href="index.html"><img src="/r/cms/www/red/images/logo.jpg" /></a></div>
        <div class="fL topone"></div>
        <div class="fL toptwo">
                   </div>
    </div>
</div>
<div class="navbg">
	<div id="b" class="mc">
    <div class="topnav">
        <ul class="menu">
            <li class="no_sub"><a href="http://www.jsit.edu.cn" class="tablink nosub">本站首页&nbsp;&nbsp;&nbsp;|</a></li>
            <li><a   href="#" target="_blank" class="tablink">苏信概况&nbsp;&nbsp;&nbsp;|</a>
            	<ul style="width:82px;">
                   <li class="nofl"><a href="/xxjj.jhtml">学院简介</a></li>
                    <li class="nofl"><a href="/xyld.jhtml">学院领导</a></li>
                    <li class="nofl"><a href="/fzgh.jhtml">发展规划</a></li>
                    <li class="nofl"><a href="/mtbd/index.jhtml">媒体苏信</a></li>
                    <li class="nofl"><a href="/xyfg.jhtml">校园风光</a></li>
                    <li class="nofl"><a href="/xyxw/index.jhtml">苏信新闻</a></li>
                    <li class="nofl"><a href="/yb/index.jhtml">苏信院报</a></li>
                    <li class="nofl"><a href="/tzgg.jhtml">通知公告</a></li>
                    <li class="nofl"><a href="/xysbxt.jhtml">校园识别系统</a></li>

                </ul>
            </li>
            <li>
            	<a href="#" class="tablink">专业与课程&nbsp;&nbsp;&nbsp;&nbsp;|</a>
                <ul style="width:700px;">
		<li style="clear:both;">
                    	<div><a href="http://dxxy.jsit.edu.cn/" target="_blank"><span style="font-size:15px; color:#ffba00; font-weight:700; margin-right:15px;">电子信息工程学院</span></a></div>
                        <div class="navone cb"><a style=" margin-right:15px;" href="/dzxxgcjs.jhtml">电子信息工程技术</a><a style=" margin-right:15px;" href="/yydzjs.jhtml">应用电子技术</a><a style=" margin-right:15px;" href="/wdzjs.jhtml">微电子技术</a><a style=" margin-right:15px;" href="/gfyyjs.jhtml">光伏应用技术</a><a href="/ydtxjs.jhtml">移动通信技术</a></div>
                    </li>
                    <li style="clear:both;">
                    	<div><a href="http://jdxy.jsit.edu.cn/" target="_blank"><span style="font-size:15px;color:#ffba00; font-weight:700; margin-right:15px;">机电工程学院</span></a></div>
                        <div class="navone cb"><a style=" margin-right:15px;" href="/jxzzyzdh.jhtml">机械制造与自动化</a><a style=" margin-right:15px;" href="/skjs.jhtml">数控技术</a><a style=" margin-right:15px;" href="/mjsjyzz.jhtml">模具设计与制造</a><a style=" margin-right:15px;" href="/sksbyyywh.jhtml">数控设备应用与维护</a><a style=" margin-right:15px;" href="/jdythjs.jhtml">机电一体化技术</a><a style=" margin-right:15px;"  href="/dqzdhjs.jhtml">电气自动化技术</a><a style=" margin-right:15px;"  href="/sbyy.jhtml">自动化生产设备应用</a><a style=" margin-right:15px;"  href="/gyjqr.jhtml">工业机器人技术</a> </div>

                    </li>
                    
                    <li style="clear:both;">
                    	<div><a href="http://auto.jsit.edu.cn/s/auto" target="_blank"><span style="font-size:15px;color:#ffba00; font-weight:700; margin-right:15px;">汽车工程学院</span></a></div>
                        <div class="navone cb"><a style=" margin-right:15px;" href="/qcjx.jhtml">汽车检测与维修技术</a><a style=" margin-right:15px;" href="/qcdz.jhtml">新能源汽车技术</a><a href="/qcyxfw.jhtml">汽车技术服务与营销</a></div>

                    </li>

                    <li style="clear:both;">
                    	<div><a href="http://iot.jsit.edu.cn/" target="_blank"><span style="font-size:15px;color:#ffba00; font-weight:700; margin-right:15px;">物联网工程学院</span></a></div>
                        <div class="navone cb"><a style=" margin-right:15px;" href="/wlwyyjs.jhtml">物联网应用技术</a><a style=" margin-right:15px;" href="/wlwyyjs1.jhtml">物联网应用技术（3+2）</a><a style=" margin-right:15px;" href="/rjjs.jhtml">软件技术</a> <a style=" margin-right:15px;" href="/rjjsydhl.jhtml">软件技术（联想移动互联）</a> <a style=" margin-right:15px;" href="/jsjwljs.jhtml">计算机网络技术</a><a style=" margin-right:15px;" href="/jsjwllx.jhtml">计算机网络技术（联想云计算）</a><a style=" margin-right:15px;" href="/xxaqgl.jhtml">信息安全与管理</a><a href="/jsjyyjs.jhtml">计算机应用技术</a><a style=" margin-right:15px;" href="/ydhljszy.jhtml">&nbsp;&nbsp;&nbsp;移动互联应用技术</a></div>
                    </li> 
                    <li style="clear:both;">
                    	<div><a href="http://art.jsit.edu.cn/" target="_blank"><span style="font-size:15px;color:#ffba00; font-weight:700; margin-right:15px;">艺术设计学院</span></a></div>
                        <div class="navone cb"><a style=" margin-right:15px;" href="/hjyssj.jhtml">环境艺术设计</a><a style=" margin-right:15px;" href="/gysj.jhtml">工业设计</a><a style=" margin-right:15px;" href="/dmsjyjs.jhtml">动漫设计与制作</a><a style=" margin-right:15px;" href="/fzsj.jhtml">服装设计</a><a style=" margin-right:15px;" href="/zhyszy.jhtml">装潢艺术设计</a><a href="/ggsjyzz.jhtml">广告设计与制作</a></div>
                    </li> 
                    <li style="clear:both;">
                    	<div><a href="http://sxy.jsit.edu.cn/" target="_blank"><span style="font-size:15px;color:#ffba00; font-weight:700; margin-right:15px;">商学院</span></a></div>
                        <div class="navone cb"><a style=" margin-right:15px;" href="/jryzq.jhtml">证券与期货专业</a><a style=" margin-right:15px;" href="/cwgl.jhtml">财务管理</a><a style=" margin-right:15px;" href="/hjysj.jhtml">会计专业</a><a style=" margin-right:15px;" href="/gjmysw.jhtml">国际贸易实务</a><a style=" margin-right:15px;" href="/scyx.jhtml">酒店管理专业</a><a style=" margin-right:15px;" href="/dzsw.jhtml">电子商务</a><a style=" margin-right:15px;" href="/swgl.jhtml">商务管理</a><a style=" margin-right:15px;" href="/wlgl.jhtml">物流管理</a><a style=" margin-right:15px;" href="/lygl.jhtml">旅游管理</a><a style=" margin-right:15px;" href="/rlzygl.jhtml">人力资源管理</a></div>
                    </li> 

                    <li style="clear:both;">
                    	<div><a href="http://jgxy.jsit.edu.cn/" target="_blank"><span style="font-size:15px;color:#ffba00; font-weight:700; margin-right:15px;">建筑工程学院</span></a></div>
                        <div class="navone cb"><a style=" margin-right:15px;" href="/jsgcgl.jhtml">建设工程管理</a><a style=" margin-right:15px;" href="/jsgcjl.jhtml">建设工程监理</a><a style=" margin-right:15px;" href="/gczj.jhtml">工程造价</a><a style=" margin-right:15px;" href="/jzgcjs.jhtml">建筑工程技术</a></div>
                    </li> 

                </ul>
            </li>
            <li>
            	<a href="#"  target="_blank" class="tablink">教学科研&nbsp;&nbsp;&nbsp;&nbsp;|</a>
                <ul style="width:86px;">
                    <li class="nofl"><a href="http://jwc.jsit.edu.cn/"  target="_blank">教学管理</a></li>
                    <li class="nofl"><a href="/zyjs.jhtml">专业建设</a></li>
                    <li class="nofl"><a href="/kygl.jhtml">科研管理</a></li>
                    <li class="nofl"><a href="http://jdyjs.jsit.edu.cn/"  target="_blank">机电研究所</a></li>
                </ul>
            </li>
            <li>
            	<a href="#">合作交流&nbsp;&nbsp;&nbsp;&nbsp;|</a>
                <ul style="width:86px;">
                   <li class="nofl"><a href="xqhz.jhtml">校企合作</a></li>
		             <li class="nofl"><a href="/gjhz.jhtml">国际合作</a></li>
		             <li class="nofl"><a href="/gnhz.jhtml">国内合作</a></li>
		            <li class="nofl"><a href="/xjhz.jhtml">校际合作</a></li>
                    <li class="nofl"><a href="/szjl.jhtml">师资交流</a></li>
                    <li class="nofl"><a href="/xsjl.jhtml">学生交流</a></li>
                    <li class="nofl"><a href="/kzjs.jhtml">客座教授</a></li>
                </ul>
                
            </li>
            <li>
            	<a href="#" class="tablink">校内站点&nbsp;&nbsp;&nbsp;&nbsp;|</a>
                <ul style="width:86px;">
                      
                      <li class="nofl"><a href="http://dyb.jsit.edu.cn/"  target="_blank">办公室</a></li>
		            <li class="nofl"><a href="http://jw.jsit.edu.cn"  target="_blank">纪委办</a></li>
		            <li class="nofl"><a href="http://rsc.jsit.edu.cn/"  target="_blank">人事处</a></li>
		            <li class="nofl"><a href="/more.jhtml">更多</a></li>
                </ul>
            </li>
             <li>
            	<a href="#" class="tablink">招生就业&nbsp;&nbsp;&nbsp;&nbsp;|</a>
                <ul style="width:86px;">
                      <li class="nofl"><a href="http://zsxx.jsit.edu.cn/"  target="_blank">招生信息网</a></li>
		      <li class="nofl"><a href="http://jsit.91job.gov.cn/"  target="_blank">就业服务网</a></li>
		</ul>
            </li>
           
            <li>
            	<a href="http://lib.jsit.edu.cn/twxx/"  target="_blank" class="tablink">公共服务&nbsp;&nbsp;&nbsp;&nbsp;|</a>
                <ul style="width:110px;">
                    <li class="nofl"><a href="http://lib.jsit.edu.cn/"  target="_blank" >图书馆</a></li>
                    <li class="nofl"><a href="/dhcx/index.jhtml">电话号码查询</a></li>
                    <li class="nofl"><a href="/skb/1454.jhtml">班车时刻表</a></li>
                    <li class="nofl"><a href="/fwzx/981.jhtml">后勤服务中心</a></li>
                    <li class="nofl"><a href="http://xsfw.jsit.edu.cn/"  target="_blank">苏信学子服务网</a></li>
                </ul>
            </li>
            <li class="no_sub"><a href="/rczp/index.jhtml" class="tablink nosub">人才招聘&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|</a></li>
            <li class="no_sub"><a href="http://xyw.jsit.edu.cn/"  target="_blank" class="tablink nosub">校友网</a></li>
                    </ul>
    </div>
</div>
</div><div class="mainbg w1000 mc">
    <div class="w1000 mc">
        <div id="full-screen-slider">
            <ul id="slides">
                <li style="background:url('/r/cms/www/red/images/kv011.jpg') no-repeat center top"></li>
                <li style="background:url('/r/cms/www/red/images/kv02.jpg') no-repeat center top"></li>
                <li style="background:url('/r/cms/www/red/images/kv03.jpg') no-repeat center top"></li>
                <li style="background:url('/r/cms/www/red/images/kv04.jpg') no-repeat center top"></li>
                <li style="background:url('/r/cms/www/red/images/kv05.jpg') no-repeat center top"></li>
                <li style="background:url('/r/cms/www/red/images/kv06.jpg') no-repeat center top"></li>
                <li style="background:url('/r/cms/www/red/images/kv07.jpg') no-repeat center top"></li>
            </ul>
        </div>
    </div>
    <div class="main w1000 mc">
        <div class="w980 mc cb">
            <div class="mainleft fL">
                <div class="mainleftnews">
                    <div class="cb">
                        <ul class="cb tab01 fL">
                            <li class="indexjx fL selected01">苏信要闻&nbsp;/&nbsp;</li>
                            <li class="indexjx fL">通知公告&nbsp;/&nbsp;</li>
                            <li class="indexjx fL">媒体苏信</li>
                        </ul>
                    </div>
                    <div class="mainsxyw">
                    	<div class="more"><a href="/xyxw/index.jhtml"><img src="/r/cms/www/red/images/in02.jpg" /></a></div>
                        <ul class="mainsxywlist">
					 <ul  class="topnews">
										   <li><a href="/xyxw/20170928/5678.html" title="中国共产党江苏信息职业技术学院第二次代表大会胜利闭幕" target="_blank"><span style="">中国共产党江苏信息职业技术学院第二次代表大会胜利闭幕</span></a><em>2017-09-28</em></li>
										   <li><a href="/xyxw/20171113/5828.html" title="我院荣获“中国产学研合作促进奖”和“2017年度中国校企合作好案例”" target="_blank"><span style="">我院荣获“中国产学研合作促进奖”和“2017年度中国校企合作好案例”</span></a><em>2017-11-13</em></li>
										   <li><a href="/xyxw/20171110/5823.html" title="我院2017校园文化艺术节隆重开幕" target="_blank"><span style="">我院2017校园文化艺术节隆重开幕</span></a><em>2017-11-10</em></li>
										   <li><a href="/xyxw/20171110/5822.html" title="我院杰出校友王旭东等回母校与老师座谈" target="_blank"><span style="">我院杰出校友王旭东等回母校与老师座谈</span></a><em>2017-11-10</em></li>
										   <li><a href="/xyxw/20171109/5819.html" title="学院召开财务处廉情分析会" target="_blank"><span style="">学院召开财务处廉情分析会</span></a><em>2017-11-09</em></li>
										   <li><a href="/xyxw/20171109/5818.html" title="我院开展11.9消防宣传月系列活动" target="_blank"><span style="">我院开展11.9消防宣传月系列活动</span></a><em>2017-11-09</em></li>
										   <li><a href="/xyxw/20171109/5817.html" title="离退休党支部专题学习十九大精神" target="_blank"><span style="">离退休党支部专题学习十九大精神</span></a><em>2017-11-09</em></li>
										   <li><a href="/xyxw/20171109/5816.html" title="我院举办中国职业教育微电子产教联盟2017年年会暨全国高职电子信息类专业教学标准内审会" target="_blank"><span style="">我院举办中国职业教育微电子产教联盟2017年年会暨全国高职电子信息类</span></a><em>2017-11-09</em></li>
										   <li><a href="/xyxw/20171108/5815.html" title="我院学生在江苏省大学生机器人大赛中获一等奖" target="_blank"><span style="">我院学生在江苏省大学生机器人大赛中获一等奖</span></a><em>2017-11-08</em></li>
										   <li><a href="/xyxw/20171108/5814.html" title="我院学生获“行云新能杯”纯电动汽车技术服务大赛二等奖" target="_blank"><span style="">我院学生获“行云新能杯”纯电动汽车技术服务大赛二等奖</span></a><em>2017-11-08</em></li>
										</ul >

                        </ul>
                    </div>
                    <div class="dpN">
                    	<div class="more"><a href="/tzgg/index.jhtml"><img src="/r/cms/www/red/images/in02.jpg" /></a></div>
                        <ul class="mainsxywlist">
					 <ul  class="topnews">
										   <li><a href="/tzgg/20170928/5680.html" title="关于2017年部分节假日安排的通知" target="_blank"><span style="">关于2017年部分节假日安排的通知</span></a><em>2017-09-28</em></li>
										   <li><a href="/tzgg/20161015/4854.html" title="苏信校友基金" target="_blank"><span style="">苏信校友基金</span></a><em>2016-10-15</em></li>
										   <li><a href="/tzgg/20171113/5827.html" title="精智模具研究院工具询价采购项目通知书" target="_blank"><span style="">精智模具研究院工具询价采购项目通知书</span></a><em>2017-11-13</em></li>
										   <li><a href="/tzgg/20171113/5826.html" title="精智模具研究院电气设备询价采购项目通知书" target="_blank"><span style="">精智模具研究院电气设备询价采购项目通知书</span></a><em>2017-11-13</em></li>
										   <li><a href="/tzgg/20171110/5821.html" title="直膨组合式空气处理机组采购项目预中标结果公示" target="_blank"><span style="">直膨组合式空气处理机组采购项目预中标结果公示</span></a><em>2017-11-10</em></li>
										   <li><a href="/tzgg/20171110/5820.html" title="空压机设备采购及安装工程预中标结果公示" target="_blank"><span style="">空压机设备采购及安装工程预中标结果公示</span></a><em>2017-11-10</em></li>
										   <li><a href="/tzgg/20171108/5813.html" title="台式计算机内存采购及安装项目招标公告" target="_blank"><span style="">台式计算机内存采购及安装项目招标公告</span></a><em>2017-11-08</em></li>
										   <li><a href="/tzgg/20171108/5812.html" title="艺术设计学院整体实训基地木工类工具采购项目招标公告（第二次）" target="_blank"><span style="">艺术设计学院整体实训基地木工类工具采购项目招标公告（第二次）</span></a><em>2017-11-08</em></li>
										   <li><a href="/tzgg/20171108/5811.html" title="艺术设计学院整体实训基地金属类工具采购项目招标公告（第二次）" target="_blank"><span style="">艺术设计学院整体实训基地金属类工具采购项目招标公告（第二次）</span></a><em>2017-11-08</em></li>
										   <li><a href="/tzgg/20171106/5809.html" title="建工学院实训室家具采购招标公告" target="_blank"><span style="">建工学院实训室家具采购招标公告</span></a><em>2017-11-06</em></li>
										</ul >

                        </ul>
                    </div>
                    <div class="dpN">
                    	<div class="more"><a href="/mtbd/index.jhtml"><img src="/r/cms/www/red/images/in02.jpg" /></a></div>
                        <ul class="mainsxywlist">
					 <ul  class="topnews">
										   <li><a href="/mtbd/20171113/5824.html" title="无锡日报：部分无锡高校学生奋战“双11”" target="_blank"><span style="">无锡日报：部分无锡高校学生奋战“双11”</span></a><em>2017-11-13</em></li>
										   <li><a href="/mtbd/20171107/5810.html" title="江苏教育视频新闻：江苏信息职业技术学院深入开展党的十九大精神专题学习活动" target="_blank"><span style="">江苏教育视频新闻：江苏信息职业技术学院深入开展党的十九大精神专题</span></a><em>2017-11-07</em></li>
										   <li><a href="/mtbd/20171102/5804.html" title="无锡日报：江苏信息职业技术学院培育七大校企合作专业群" target="_blank"><span style="">无锡日报：江苏信息职业技术学院培育七大校企合作专业群</span></a><em>2017-11-02</em></li>
										   <li><a href="/mtbd/20171018/5734.html" title="无锡商报：江苏信息职院迎来“一带一路”国家留学生" target="_blank"><span style="">无锡商报：江苏信息职院迎来“一带一路”国家留学生</span></a><em>2017-10-18</em></li>
										   <li><a href="/mtbd/20171013/5712.html" title="中国江苏网：江苏信息职院携手“一带一路”国家 培育优质人才" target="_blank"><span style="">中国江苏网：江苏信息职院携手“一带一路”国家 培育优质人才</span></a><em>2017-10-13</em></li>
										   <li><a href="/mtbd/20171013/5711.html" title="扬子晚报：无锡大中专院校创业能力大赛开幕" target="_blank"><span style="">扬子晚报：无锡大中专院校创业能力大赛开幕</span></a><em>2017-10-13</em></li>
										   <li><a href="/mtbd/20170928/5679.html" title="网易新闻：江苏信息职院第二次党代会开幕 聚焦高水平高职名校发展" target="_blank"><span style="">网易新闻：江苏信息职院第二次党代会开幕 聚焦高水平高职名校发展</span></a><em>2017-09-28</em></li>
										   <li><a href="/mtbd/20170918/5639.html" title="江苏教育网：江苏信息学院：知名企业助力迎新生 校企融合展示新成果" target="_blank"><span style="">江苏教育网：江苏信息学院：知名企业助力迎新生 校企融合展示新成果</span></a><em>2017-09-18</em></li>
										   <li><a href="/mtbd/20170914/5628.html" title="扬子晚报：学院迎新生搞出新花样 3辆保时捷开进校园" target="_blank"><span style="">扬子晚报：学院迎新生搞出新花样 3辆保时捷开进校园</span></a><em>2017-09-14</em></li>
										   <li><a href="/mtbd/20170906/5600.html" title="无锡商报：江苏信息职院获2017年金砖国家技能创新大赛冠军" target="_blank"><span style="">无锡商报：江苏信息职院获2017年金砖国家技能创新大赛冠军</span></a><em>2017-09-06</em></li>
										</ul >

                        </ul>
                    </div>
                </div>
             
               

 <div class="indexline1"></div>
                <div class="cb">
                	<div class="indexjx fL">院部</div>
                	<ul class="cb fL indexxjlist">
                    	<li class="fL"><a href="http://dxxy.jsit.edu.cn/" target="_blank">电子信息工程学院</a></li>
                        <li class="fL"><a href="http://jdxy.jsit.edu.cn/"  target="_blank">机电工程学院</a></li>
                        <li class="fL"><a href="http://auto.jsit.edu.cn/"  target="_blank">汽车工程学院</a></li>
                        <li class="fL"><a href="http://iot.jsit.edu.cn/"  target="_blank">物联网工程学院</a></li>
                        <li class="fL"><a href="http://art.jsit.edu.cn/"  target="_blank">艺术设计学院</a></li>
                        <li class="fL"><a href="http://sxy.jsit.edu.cn/"  target="_blank">商学院</a></li> 
                        <li class="fL"><a href="http://jgxy.jsit.edu.cn/"  target="_blank">建筑工程学院</a></li>                                             
                        <li class="fL"><a href="http://jxjy.jsit.edu.cn"  target="_blank">继续教育学院</a></li>
                        <li class="fL"><a href="http://jckb.jsit.edu.cn"  target="_blank">基础课部</a></li>
                        <li class="fL"><a href="http://192.168.16.13/"  target="_blank">体育部</a></li>
                    </ul>
                </div>
                <div class="mt10 cb">
                	<div class="indexjx fL">友情链接</div>
                	<ul class="cb indexxjlist fL">
                         <li class="fL"><a href="http://www.moe.edu.cn/" target="_blank">教育部</a>&nbsp;&nbsp;</li>

                        <li class="fL"><a href="http://www.ec.js.edu.cn/" target="_blank">江苏教育</a>&nbsp;&nbsp;</li>
                    	<li class="fL"><a href="http://www.jseea.cn/" target="_blank">江苏省教育考试院</a>&nbsp;&nbsp;</li>
                        <li class="fL"><a href="http://www.wxjy.com.cn/Index.html" target="_blank">无锡教育网</a>&nbsp;&nbsp;</li>
                         <li class="fL"><a href="https://vpn.jsit.edu.cn/welcome.php" target="_blank">江苏信息VPN网关</a>&nbsp;&nbsp;</li>

                    
                       
                    </ul>
                </div>
 
            </div>
            <div class="mainright fR">
                <div class="cb">
                    <ul class="cb tab02 fL">
                        <li class="fL selected02">校内平台</li>
                        <li class="fL">校内专题</li>
                    </ul>
                </div>
                <div class="mt5">
                	<ul class="cb xnptlist"> 
                       <li class="fL" style="margin-right:1px;"><a href="http://my.jsit.edu.cn/" target="_blank"><img src="/r/cms/www/red/images/xn02.jpg" /></a></li>
                        <li class="fL"><a href="http://mail.jsit.edu.cn" target="_blank"><img src="/r/cms/www/red/images/xn01.jpg" /></a></li>
                        <li class="fL" style="margin-right:1px;"><a href="http://58.214.11.21/Netoffice/" target="_blank"><img src="/r/cms/www/red/images/xn03.jpg" /></a></li>
                        <li class="fL"><a href="http://jwxt.jsit.edu.cn/" target="_blank"><img src="/r/cms/www/red/images/xn07.jpg" /></a></li>
                        <li class="fL" style="margin-right:1px;"><a href="http://cbgz.jsit.edu.cn/WFManager/login.jsp" target="_blank"><img src="/r/cms/www/red/images/xn05.jpg" /></a></li>
                        <li class="fL"><a href="http://cbgz.jsit.edu.cn/payment" target="_blank"><img src="/r/cms/www/red/images/xn06.jpg" /></a></li>
                        <li class="fL" style="margin-right:1px;"><a href="http://192.168.16.45:8080/xgxt/" target="_blank"><img src="/r/cms/www/red/images/xn04.jpg" /></a></li>
                        <li class="fL"><a href="http://cas.jsit.edu.cn/cas/login/" target="_blank"><img src="/r/cms/www/red/images/xn14.jpg"/></a></li>
                        <li class="fL" style="margin-right:1px;"><a href="http://www.jsit.edu.cn/" target="_blank"><img src="/r/cms/www/red/images/xn09.jpg" /></a></li>
                        <li class="fL"><a href="http://221.6.107.237:8090/wljxpt/index.html" target="_blank"><img src="/r/cms/www/red/images/xn10.jpg" /></a></li>
                        <!--li class="fL"><a href="http://192.168.16.12:8090/wljxpt/index.html" target="_blank"><img src="/r/cms/www/red/images/xn10.jpg" /></a></li-->
                        <li class="fL" style="margin-right:1px;"><a href="http://lib.jsit.edu.cn/" target="_blank"><img src="/r/cms/www/red/images/xn11.jpg" /></a></li>
                        <li class="fL"><a href="http://192.168.15.91/" target="_blank"><img src="/r/cms/www/red/images/xn12.jpg"/></a></li>
                        <li class="fL" style="margin-right:1px;"><a href="http://jshs.eamn.net/" target="_blank"><img src="/r/cms/www/red/images/xn13.jpg" /></a></li>                        
                        <li class="fL"><a href="http://gzc.jsit.edu.cn/" target="_blank"><img src="/r/cms/www/red/images/xn08.jpg" /></a></li>
                </ul>
                </div>
                <div class="dpN mt5">
                	<li class="fL"><a href="http://www.jsit.edu.cn/xxgk/" target="_blank"><img src="/r/cms/www/red/images/zt02.jpg" /></a></li>
                       <li class="fL" style="margin-right:1px;"><a href="http://lxyz.jsit.edu.cn/" target="_blank"><img src="/r/cms/www/red/images/zt011.jpg" /></a></li>
                    
                    <li class="fL" style="margin-right:1px;"><a href="http://gxpx1.ceat.edu.cn/" target="_blank"><img src="/r/cms/www/red/images/zt03.jpg" /></a></li>
                    <li class="fL"><a href="http://58.214.11.22:8022/default.htm" target="_blank"><img src="/r/cms/www/red/images/zt04.jpg" /></a></li>

                    <li class="fL" style="margin-right:1px;"><a href="http://grwz.jsit.edu.cn:8080/grwz/" target="_blank"><img src="/r/cms/www/red/images/zt05.jpg" /></a></li>
                 </div>
            </div>
        </div>
    </div>
   
<div style="margin:0 auto;">
 <div class="w1000 mc bottom">
        <div class="w980 mc cb">
            <div class="fL bottomnr">
            	Copyright ©江苏信息职业技术学院   2017, All Rights Reserved    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="mailto:xiht@jsit.edu.cn"><font color="#ffffff">书记信箱</font></a> &nbsp;&nbsp;&nbsp; <a href="mailto:weip@jsit.edu.cn"><font color="#ffffff">院长信箱</font></a> <br />  
 
                江苏省无锡市惠山区钱藕路1号    邮编：214153  联系电话：0510-85804253  &nbsp;&nbsp;0510-85811518（招生咨询专线）   <br /> 
                推荐使用IE7.0以上浏览器，1024*768分辨率访问本网站   <a href="http://www.miitbeian.gov.cn" target="_blank" style="color:#ffffff;"> 苏ICP备11036003号-1 </a>&nbsp;&nbsp;  <bR />
            </div>
            <div class="fR bottomwb"> <img src="/r/cms/www/red/images/sxqn.jpg" /> </div>
           
            <div class="fR bottomwb"><img src="/r/cms/www/red/images/2wm.jpg" /> </div>
             <div class="fR bottomwb"> <img src="/r/cms/www/red/images/xywx.jpg" /> </div>
        </div>
    </div></div>

<script language="JavaScript" type="text/javascript">
suspendcode="<DIV id=lovexin1 style='POSITION:absolute;left:0px;TOP:200px; '><a href='http://ddh.jsit.edu.cn/' target='_blank'><img src='/r/cms/www/red/images/ddh.png' width='232' height='79' border='0'></a></DIV>"
document.write(suspendcode);

suspendcode="<DIV id=lovexin2 style='POSITION:absolute;right:100px;TOP:200px; '><a href='http://www.jsit.edu.cn/fzxl.jhtml' target='_blank'><img src='/r/cms/www/red/images/xysjd.png' width='232' height='79' border='0'></a></DIV>"
document.write(suspendcode);

//suspendcode="<DIV id=lovexin3 style='POSITION:absolute;left:0px;TOP:300px; '><a href='http://ddh.jsit.edu.cn/' target='_blank'><img src='/r/cms/www/red/images/ddh.jpg' width='232' height='79' border='0'></a></DIV>"
//document.write(suspendcode);

//flash&cedil;&ntilde;&Ecirc;&frac12;&micro;÷&Oacute;&Atilde;·&frac12;·¨
//<EMBED src='flash.swf' quality=high  WIDTH=100 HEIGHT=300 TYPE='application/x-shockwave-flash' id=ad wmode=opaque></EMBED>
//suspendcode="<DIV id=lovexin2 style='POSITION:absolute;right:100px;TOP:200px; '><a href='http://www.jsit.edu.cn/tzgg/5188.jhtml' target='_blank'><img src='/r/cms/www/red/images/jyj20170315.png' width='305' height='60' border='0'></a></DIV>"
//document.write(suspendcode);

//suspendcode="<DIV id=lovexin2 style='POSITION:absolute;right:100px;TOP:200px; '><a href='http://www.jsit.edu.cn/tzgg/5304.jhtml' target='_blank'><img src='/r/cms/www/red/images/zyjyhdz20170512.jpg' width='144' height='46' border='0'></a></DIV>"
//document.write(suspendcode);

//suspendcode="<DIV id=lovexin2 style='POSITION:absolute;right:100px;TOP:200px; '><a href='http://rsc.jsit.edu.cn/' target='_blank'><img src='/r/cms/www/red/images/zpgg20170703.jpg' width='232' height='79' border='0'></a></DIV>"
//document.write(suspendcode);

lastScrollY=0;
function heartBeat(){
diffY=document.body.scrollTop;
percent=.3*(diffY-lastScrollY);
if(percent>0)percent=Math.ceil(percent);
else percent=Math.floor(percent);
document.all.lovexin1.style.pixelTop+=percent;
//document.all.lovexin2.style.pixelTop+=percent;
lastScrollY=lastScrollY+percent;
}
function hide()  
{   
lovexin1.style.visibility="hidden"; 
lovexin2.style.visibility="hidden";
}
window.setInterval("heartBeat()",1);
</script>




</body>



</html>
>>> 
