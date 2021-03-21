import yaml
from common.log_main import logger

def black_handle(fun):
    def run(*args,**kwargs):
        with open('../page/black_list.yaml', 'r', encoding='utf-8') as f:
            _black_list = yaml.safe_load(f)# 弹窗黑名单
        self = args[0]
        try:
            return fun(*args,**kwargs)
        except Exception as e:
            for black in _black_list:
                eles = self._driver.find_elements(*black)
                if len(eles) > 0:
                    eles[0].click()
                    return fun(*args,**kwargs)
            raise e
    return run


