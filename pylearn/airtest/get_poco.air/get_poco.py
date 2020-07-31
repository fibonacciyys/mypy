# -*- encoding=utf8 -*-
__author__ = "ReoNa"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

#poco("com.miui.home:id/workspace").offspring("微博").offspring("com.miui.home:id/icon_icon").click()

poco("com.miui.home:id/workspace").offspring("微信").offspring("com.miui.home:id/icon_icon").click()

start_app('com.sina.weibo')




