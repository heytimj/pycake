import requests as _requests
import json as _json
from collections import OrderedDict as _OrderedDict
from .function_validation import _if_one_then_all
from .ResponseFormat import ResponseFormat


class BuyerAPI(object):

    def __init__(
            self, admin_domain,
            response_format=ResponseFormat.JSON, use_https=True):

        self.admin_domain = admin_domain
        self.response_format = response_format
        self.protocol = 'https' if use_https else 'http'


    def _make_api_call(self, url, params):
        if self.response_format.upper() == 'JSON':
            request = _requests.post(url, json=params, stream=True)
            raw_response = request.text
            try:
                json_response = _json.loads(raw_response)
                json_data = json_response['d']
                return json_data
            except:
                request = _requests.post(url, data=params, stream=True)
                raw_response = request.text
                return raw_response   
        else:
            request = _requests.post(url, data=params, stream=True)
            response = request.text
            return response


    def get_return_reasons(self):
        api_url = '{}://{}/buyers/api/1/leads.asmx/GetReturnReasons'.format(
            self.protocol, self.admin_domain)

        parameters = {}

        return self._make_api_call(url=api_url, params=parameters)


    def return_lead(self, lead_id, return_reason_id, buyer_contract_id='0'):
        api_url = '{}://{}/buyers/api/1/leads.asmx/Return'.format(
            self.protocol, self.admin_domain) 

        parameters = _OrderedDict()
        parameters['lead_id'] = lead_id
        parameters['return_reason_id'] = return_reason_id
        parameters['buyer_contract_id'] = buyer_contract_id

        return self._make_api_call(url=api_url, params=parameters)


    @_if_one_then_all(['amount', 'add_to_existing'])
    @_if_one_then_all(['status', 'sub_status'])
    def update_lead(
            self, lead_id, buyer_contract_id='0', status='', sub_status='',
            amount='0', add_to_existing='TRUE', field_name='',
            field_value='', return_reason_id='0'):
        
        api_url = '{}://{}/buyers/api/1/leads.asmx/UpdateLead'.format(
            self.protocol, self.admin_domain)

        parameters = _OrderedDict()
        parameters['lead_id'] = lead_id
        parameters['buyer_contract_id'] = buyer_contract_id
        parameters['status'] = status
        parameters['sub_status'] = sub_status
        parameters['amount'] = amount
        parameters['add_to_existing'] = add_to_existing
        parameters['field_name'] = field_name
        parameters['field_value'] = field_value
        parameters['return_reason_id'] = return_reason_id

        return self._make_api_call(url=api_url, params=parameters)













