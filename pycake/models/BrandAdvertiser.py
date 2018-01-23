from .CakeModel import CakeModel


class BrandAdvertiser(CakeModel):

    def __init__(self, **kwargs):
        self.param_defaults = {
            'advertiser_id': None,
            'advertiser_name': None,
            'third_party_name': None,
            'account_managers': None,
            'account_status': None,
            'address': None,
            'website': None,
            'contacts': None,
            'tags': None,
            'credit_limits': None,
            'suppression_lists': None,
            'blacklists': None,
            'billing_cycle': None,
            'events': None,
            'voucher_codes': None,
            'storefronts': None,
            'quickbooks_id': None,
            'online_signup': None,
            'signup_ip_address': None,
            'api_key': None,
            'date_created': None,
            'date_last_accepted_terms': None,
            'notes': None
        }

        for (param, default) in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))