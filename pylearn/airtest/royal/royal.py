# -*- encoding=utf8 -*-
__author__ = "ReoNa"

from airtest.core.api import *

from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/adbc40c",
    ])


# script content
print("start...")

while True:
    xy = wait(Template(r"tpl1584275391655.png", record_pos=(0.247, 0.172), resolution=(1920, 1200)))
    touch(xy)
    sleep(6.0)

    xy = wait(Template(r"tpl1584274727963.png", record_pos=(0.454, -0.288), resolution=(1920, 1200)))
    touch(xy)
    sleep(55.0)

    xy = wait(Template(r"tpl1584274727963.png", record_pos=(0.454, -0.288), resolution=(1920, 1200)))
    touch(xy)
    xy = wait(Template(r"tpl1584274727963.png", record_pos=(0.454, -0.288), resolution=(1920, 1200)))
    touch(xy)
    sleep(6.0)
    xy = wait(Template(r"tpl1584274859765.png", record_pos=(0.007, 0.221), resolution=(1920, 1200)))
    touch(xy)
    xy = wait(Template(r"tpl1584274892328.png", record_pos=(0.344, 0.268), resolution=(1920, 1200)))
    touch(xy)

    



# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
