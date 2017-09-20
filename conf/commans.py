#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:xieshengsen


import uuid


def create_uuid():
    """
    创建角色UUID
    :return:
    """
    return str(uuid.uuid1())