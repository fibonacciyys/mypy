# -*- coding: utf-8 -*-
import datetime

dtstr=str(input('请输入日期(20180213):'))
dt=datetime.datetime.strptime(dtstr,'%Y%m%d')
head_datestr=dtstr[:4]+'0101'
hdt=datetime.datetime.strptime(head_datestr,'%Y%m%d')
midd_day=int((dt-hdt).days)+1
print(midd_day)