#!/usr/bin/env python
# -*- coding: utf-8 -*-
from aztarna.helpers import HelpersLINQ

class HelpersROS:
    """
    A helper class from ROS system state response manipulation.
    Process response is of type array = [ [a, [a1, a2] ] , [b, [b1, b2] ] ]
    """
    @staticmethod
    def process_line(array_object):
        if not array_object:
            return None

        topic_name = array_object[0]
        node_names = (HelpersLINQ.distinct(array_object[1]))

        return [topic_name, node_names]
