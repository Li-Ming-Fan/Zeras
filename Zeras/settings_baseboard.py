# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 21:12:23 2018

@author: limingfan
"""

import os
import time
import json

import logging


class SettingsBaseboard(object):
    """
    """
    def __init__(self):
        """
        """
        self.str_datetime = time.strftime("%Y_%m_%d_%H_%M_%S")
        self.except_list = ["str_datetime", "except_list" ]

    #
    def create_logger(self, log_path):
        """
        """
        logger = logging.getLogger(log_path)  # use log_path as log_name
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(log_path, encoding='utf-8') 
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        # self.logger.info('test')
        self.logger = logger
        self.log_path = log_path
        # return logger
        #

    def create_or_reset_log_file(self, log_path=None):
        if log_path is None:
            log_path = self.log_path        
        with open(log_path, 'w', encoding='utf-8'):
            print("log file renewed")
    
    def close_logger(self, logger=None):
        if logger is None:
            logger = self.logger
        for item in logger.handlers:
            item.close()
            print("logger handler item closed")
    
    def print_and_log(self, str_info):
        print(str_info)
        self.logger.info(str_info)
    #
    
    #
    def display(self):
        """
        """        
        print()
        for name, value in vars(self).items():
            if not isinstance(value, (int, float, str, bool, list, dict, tuple)):
                continue
            print(str(name) + ': ' + str(value))
        print()
    #
    def __str__(self):
        """
        """
        info_dict = self.trans_info_to_dict()
        return json.dumps(info_dict)
    #
    def assign_info_from_namedspace(self, named_data, except_list=[]):
        """
        """
        for key in named_data.__dict__.keys():
            if key in except_list:
                continue
            else:
                self.__dict__[key] = named_data.__dict__[key]
        #    
    #
    def trans_info_to_dict(self, except_list=[]):
        """
        """
        info_dict = {}
        for name, value in vars(self).items():
            if not isinstance(value, (int, float, str, bool, list, dict, tuple)):
                continue
            elif name in except_list:
                continue
            else:
                info_dict[str(name)] = value
        #    
        return info_dict
    
    def assign_info_from_dict(self, info_dict, except_list=[]):
        """
        """
        for key in info_dict:
            value = info_dict[key]
            if key in except_list:
                continue
            else:
                setattr(self, key, value)
        #

    def save_to_json_file(self, file_path, except_list=[]):
        """
        """
        info_dict = self.trans_info_to_dict(except_list)
        #
        with open(file_path, "w", encoding="utf-8") as fp:
            json.dump(info_dict, fp, ensure_ascii=False, indent=4)
        #       
    
    def load_from_json_file(self, file_path, except_list=[]):
        """
        """
        if file_path is None:
            print("model settings file: %s NOT found, using default settings"
                  % file_path)
            return
        #
        with open(file_path, "r", encoding="utf-8") as fp:
            info_dict = json.load(fp)
        #
        self.assign_info_from_dict(info_dict, except_list)
        #
    #
        
        
    
        
if __name__ == '__main__':
    
    sett = SettingsBaseboard()
    
    #print(dir(sett))
    #l = [i for i in dir(sett) if inspect.isbuiltin(getattr(sett, i))]
    #l = [i for i in dir(sett) if inspect.isfunction(getattr(sett, i))]
    #l = [i for i in dir(sett) if not callable(getattr(sett, i))]
    
    print(sett.__dict__.keys())
    print()
    
    info_dict = sett.trans_info_to_dict([])
    print(info_dict)
    print()
    
    #
    info_dict["model_name"] = "transformer"
    sett.assign_info_from_dict(info_dict, [])
    
    #
    info_dict = sett.trans_info_to_dict([])
    print(info_dict)
    print()
    #
    
    file_path = "./settings_template.json"
    sett.save_to_json_file(file_path, sett.except_list)    
    sett.load_from_json_file(file_path, [])
    
    #
    info_dict = sett.trans_info_to_dict([])
    print(info_dict)
    print()
    #

    #
    sett.create_logger("log.txt")
    sett.close_logger()
    #