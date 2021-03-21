from base_page_web import BasePage
from query_prescription_page import QueryPrescriptionPage


class AddPrescriptionPage(BasePage):
    '''处方中心'''
    def add_prescription_success(self,patient_name,age,phone,birthday,detail_address,medicinal_name,medicinal_num):
        '''处方创建'''
        self._params['patient_name'] = patient_name#输入患者姓名
        self._params['age'] = age#年龄
        self._params['phone'] = phone#手机号
        self._params['birthday'] = birthday#生日
        self._params['detail_address'] = detail_address#详细地址
        self._params['medicinal_name'] = medicinal_name#药材名称
        self._params['medicinal_num'] = medicinal_num#药材数量
        self.steps('./yml_casedatas/add_prescription_page.yml','add_prescription_success')
        return QueryPrescriptionPage(self._driver)

if __name__ == '__main__':
    pass