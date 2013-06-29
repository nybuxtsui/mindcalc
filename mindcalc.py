#!/usr/bin/env python
#coding:utf-8

import random, time;

# 生成一个整数, 范围是[from_num, to_num)
def gen_number(from_num, to_num):
    r = 0
    while True:
        r = int(random.random() * to_num)
        if r >= from_num and r < to_num:
            return r

# 创建题目
def make_multiply_topic():
    a = gen_number(11, 100)
    b = gen_number(2, 10)
    return ('%d * %d' % (a, b), a * b)
def make_minus_topic():
    a = gen_number(11, 100)
    b = gen_number(11, 100)
    return ('%d - %d' % (a + b, b), a)
def make_div_topic():
    a = gen_number(11, 100)
    b = gen_number(2, 10)
    return ('%d / %d' % (a * b, b), a)
def make_plus_topic():
    a = gen_number(11, 100)
    b = gen_number(11, 100)
    return ('%d + %d' % (a, b), a + b)


# 让用户做题，返回True/False表示是否正确
def test(topic, result):
    print '%s =' % (topic),
    while True:
        try:
            i = int(raw_input().strip())
            break
        except ValueError:
            print "number:",
    if result == i:
        return True
    else:
        return False

while True:
    error = 0
    total = 0
    total_secs = 0

    while True:
        start_sec = time.time()
        n = random.random()
        if n < 0.2:
            topic, result = make_multiply_topic()
        elif n < 0.4:
            topic, result = make_plus_topic()
        elif n < 0.7:
            topic, result = make_minus_topic()
        else:
            topic, result = make_div_topic()

        while True:
            ok = test(topic, result)
            if not ok:
                print "error!"
                error += 1
            else:
                break
        end_sec = time.time()
        total_secs += int(end_sec - start_sec)
        total += 1
        print "total: %d, error: %d, time:" % (total, error),
        if total_secs <= 60:
            print total_secs
        else:
            min = total_secs / 60
            sec = total_secs % 60
            print "%d:%02d" % (min, sec)



