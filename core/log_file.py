#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:xieshengsen

import os
import sys
import logging

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import settings


def student_log(info_str):
    """
    学生操作日志
    :param info_str:
    :return:
    """
    logger = logging.getLogger("用户操作日志")
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler(settings.STUDENT_LOG, encoding='utf-8')
    fh.setLevel(logging.DEBUG)

    fh_format = logging.Formatter('%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    fh.setFormatter(fh_format)

    logger.addHandler(fh)
    logger.warning(info_str)
    return


def admin_log(info_str):
    """
    管理员操作日志
    :param info_str:
    :return:
    """
    logger = logging.getLogger("用户操作日志")
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler(settings.ADMIN_LOG, encoding='utf-8')
    fh.setLevel(logging.DEBUG)

    fh_format = logging.Formatter('%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    fh.setFormatter(fh_format)

    logger.addHandler(fh)
    logger.warning(info_str)
    return


def teacher_log(info_str):
    """
    讲师操作日志
    :param info_str:
    :return:
    """
    logger = logging.getLogger("用户操作日志")
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler(settings.TEACHER_LOG, encoding='utf-8')
    fh.setLevel(logging.DEBUG)

    fh_format = logging.Formatter('%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    fh.setFormatter(fh_format)

    logger.addHandler(fh)
    logger.warning(info_str)
    return