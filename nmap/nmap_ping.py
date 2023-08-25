#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""**************************************************************************
*  Copyright @ 颐希科技 2023. All rights reserved.                            *
*                                                                            *
*                                                                            *
*                                                                            *
*  @file     nmap_ping.py                                                    *
*  @brief                                                                    *
*                                                                            *
*  @author   陈钢强                                                           *
*  @version  1.0.0.1(版本号)                                                  *
*  @date     2023/8/25 22:55                                                 *
*                                                                            *
*----------------------------------------------------------------------------*
*  Change History :                                                          *
*  <Date>     | <Version> | <Author>       | <Description>                   *
*----------------------------------------------------------------------------*
*  2023/8/25   | 1.0.0.1   | 陈钢强           | Create file                   *
*----------------------------------------------------------------------------*
*                                                                            *
***************************************************************************"""

import sys
import nmap


def nmap_ping_scan(network_prefix):
    # 创建端口扫描对象
    nm = nmap.PortScanner()
    # 调用扫描方法，参数指定扫描主机hosts，扫描参数arguments
    ping_scan_raw_result = nm.scan(hosts=network_prefix, arguments='-v -n -sn')
    host_list = []
    # 遍历扫描主机
    for result in ping_scan_raw_result['scan'].values():
        if result['status']['state'] == 'up':
            host_list.append(result['addresses']['ipv4'])
    return host_list


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: ' + sys.argv[0] + ' <network_prefix>')
        sys.exit(1)
    network_prefix = sys.argv[1]
    host_list = nmap_ping_scan(network_prefix)
    for host in host_list:
        print(host)
