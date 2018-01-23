from .CakeModel import CakeModel


class Click(CakeModel):
    '''http://staging.cakemarketing.com/api/12/reports.asmx?op=Clicks'''

    def __init__(self, **kwargs):
        self.param_defaults = {
            'click_id': None,
            'visitor_id': None,
            'original_visitor_id': None,
            'tracking_id': None,
            'original_tracking_id': None,
            'request_session_id': None,
            'click_date': None,
            'udid': None,
            'source_affiliate': None, 
            'brand_advertiser': None, 
            'site_offer': None,
            'site_offer_contract': None,
            'channel': None,
            'campaign': None,
            'creative': None,
            'sub_id_1': None,
            'sub_id_2': None,
            'sub_id_3': None,
            'sub_id_4': None,
            'sub_id_5': None,
            'ip_address': None,
            'user_agent': None,
            'referrer_url': None,
            'search_term': None,
            'request_url': None,
            'redirect_url': None,
            'country': None,
            'region': None,
            'language': None,
            'isp': None,
            'device': None,
            'operating_system': None,
            'browser': None,
            'disposition': None,
            'paid_action': None,
            'paid': None,
            'received': None,
            'duplicate': None,
            'duplicate_clicks': None,
            'total_clicks': None,
        }

        for (param, default) in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))
