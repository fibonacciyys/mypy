# -*- encoding=utf8 -*-
__author__ = "ReoNa"
import sys
import airtest.core.api as at
try:
    device_1 = at.connect_device("Android://127.0.0.1:5037/" + str(sys.argv[1]) + ":5555")
except:
    device_1 = at.connect_device("Android://127.0.0.1:5037/2eb1ddac")
import time
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(device_1,use_airtest_input=True, screenshot_each_action=False)

at.auto_setup(__file__)

class Sina_super(object):
    
    def __init__(self):
        self.is_finished = 0
        self.yiyi = 0  #若已领积分改 1 否则为0
        self.sign_index = []
        self.idol_get = '苏杉杉'
        
    def wait_poco(self,string,mode=1,duriation=10):
        '''
        mode:0,'text'
        '''
        b_time = time.time()
        will_continue = 1
        while will_continue:
            try:
                if mode:
                    if not poco(string):
                        raise Exception('not find')
                else:
                    if not poco(text=string):
                        raise Exception('not find')
                print('find: ',string)
                return True
            except:
                pass
            dur_time = time.time() - b_time
            if dur_time > duriation:
                will_continue = 0
                raise Exception('err')
    
    def is_exist_sign(self):
        for i in range(1,6,1):
            if poco("android:id/content").offspring(
                "com.sina.weibo:id/fl_activity_bottom_tabs_container").offspring(
                "com.sina.weibo:id/viewpager").offspring(
                "com.sina.weibo:id/content").child(
                "android.widget.RelativeLayout")[i].offspring(
                "android.widget.Button").get_text() == '签到':
                self.sign_index.append(i)
        return not self.sign_index == []
    
    def sign(self,i):
        item = poco("android:id/content").offspring(
            "com.sina.weibo:id/fl_activity_bottom_tabs_container").offspring(
            "com.sina.weibo:id/viewpager").offspring(
            "com.sina.weibo:id/content").child(
            "android.widget.RelativeLayout")[i].offspring(
            "android.widget.Button")
        item.click()

    
    def points_yiyi(self):
        self.wait_poco('已关注')
        try:
            if not poco("android:id/content").child(
                "android.widget.RelativeLayout").offspring(
                "com.sina.weibo:id/lvCard").offspring(
                self.idol_get + "  ").exists():
                raise Exception('not find')
            poco("com.sina.weibo:id/right_lottie_btn").click()
            self.wait_poco("赠送",0)
            poco("com.sina.weibo:id/webview_container").child(
                "android.webkit.WebView").child(
                "android.webkit.WebView").offspring(
                "card_div").child(
                "android.view.View")[3].click()
            self.wait_poco("每日任务",0)
            poco("com.sina.weibo:id/webview_container").child(
                "android.webkit.WebView").child(
                "android.webkit.WebView").offspring(
                "app").child(
                "android.view.View").child(
                "android.view.View")[1].child(
                "android.widget.ListView")[0].child(
                "android.view.View")[2].click()
            print('get points')
            self.yiyi = 1
            self.follow = 0
            while not self.follow:
                at.keyevent('4')
                time.sleep(0.5)
                if poco('已关注'):
                    self.follow = 1
                else:
                    print('continue back')
        except:
            print('Not find yiyi')
        
    def to_super(self):
        #poco("com.miui.home:id/workspace").offspring("微博").offspring("com.miui.home:id/icon_icon").click()
        print(at.shell("am start -n com.sina.weibo/.MainTabActivity"))
        at.sleep(3)
        self.wait_poco("我")
        poco("我").click()
        self.wait_poco("com.sina.weibo:id/cabFollow")
        poco("com.sina.weibo:id/cabFollow").click()
        self.wait_poco("超话",0)
        poco(text="超话").click()
        at.sleep(1.5)
        self.wait_poco("com.sina.weibo:id/numbertext")
        poco("com.sina.weibo:id/numbertext").click()
        self.wait_poco("com.sina.weibo:id/hroizontalscoll")

    def all_sign(self):
        self.to_super()
        while not self.is_finished:
            if self.is_exist_sign():
#                try:
#                    at.wait(at.Template(
#                        r"tpl1567161786393.png", record_pos=(-0.238, 0.827), resolution=(1080, 1920)))
#                except:
#                    continue
#                time.sleep(0.3)
                for i in self.sign_index:
                    while poco("com.sina.weibo:id/hroizontalscoll").exists():
                        self.sign(i)
                        time.sleep(0.3)
                    at.sleep(1.0)
                    at.keyevent('4') 
                    at.sleep(1.0)
                    if poco('已关注').exists():
                        at.keyevent('4')
                    self.wait_poco("com.sina.weibo:id/hroizontalscoll")
                self.sign_index = []
                print('swipe')
                at.swipe((540,1586),(540,352))
            elif poco(text="+ 更多感兴趣的超话").exists():
                print('finish!')
                self.is_finished = 1
            else:
                print('swipe')
                at.swipe((540,1686),(540,322))
        if not self.yiyi:
            at.keyevent('4')
            self.wait_poco("com.sina.weibo:id/numbertext")
            poco("com.sina.weibo:id/numbertext").click()
            self.wait_poco("com.sina.weibo:id/hroizontalscoll")
            poco(text=self.idol_get).click()
            self.points_yiyi()
            
    def unit_points(self):
        self.to_super()
        poco(text="王奕").click()
        self.points_yiyi()

if __name__ == '__main__':
    sign_sc = Sina_super()
    sign_sc.all_sign()
#    sign_sc.unit_points()


