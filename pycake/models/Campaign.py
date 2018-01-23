from .CakeModel import CakeModel


class Campaign(CakeModel):

	def __init__(self, **kwargs):
		self.param_defaults = {
			'campaign_id': None,
			'third_party_name': None,
			'campaign_type': None,
			'affiliate': None,
			'offer': None,
			'offer_contract': None,
			'original': None,
			'non_original': None,
			'exceptions': None,
			'account_status': None,
			'currency': None,
			'media_type': None,
			'display_link_type': None,
			'event_overrides': None,
			'deal_flow': None,
			'payouts': None,
			'paid': None,
			'paid_redirects': None,
			'disable_prepop_appending': None,
			'suppression_amount': None,
			'cookie_domain': None,
			'redirect_domain': None,
			'click_cap': None,
			'conversion_cap': None,
			'pixel_info': None,
			'upsell_info': None,
			'submission_options': None,
			'voucher_codes': None,
			'test_link': None,
			'redirect_offer': None,
			'redirect_404': None,
			'date_created': None,
			'expiration_date': None,
			'notes': None
		}
		for (param, default) in self.param_defaults.items():
			setattr(self, param, kwargs.get(param, default))