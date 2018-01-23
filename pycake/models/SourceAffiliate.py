from .CakeModel import CakeModel


class SourceAffiliate(CakeModel):

	def __init__(self, **kwargs):
		self.param_defaults = {
			'affiliate_id': None,
			'affiliate_name': None,
			'third_party_name': None,
			'tier': None,
			'account_managers': None,
			'account_status': None,
			'inactive_reason': None,
			'address': None,
			'website': None,
			'payment_type': None,
			'contacts': None,
			'tags': None,
			'traffic_types': None,
			'minimum_payment_threshold': None,
			'auto_payment_fee': None,
			'payment_to': None,
			'tax_class': None,
			'ssn_tax_id': None,
			'pay_vat': None,
			'swift_iban': None,
			'referrals_enabled': None,
			'referred_by_affiliate': None,
			'referral_info': None,
			'billing_cycle': None,
			'currency_settings': None,
			'quickbooks_id': None,
			'online_signup': None,
			'signup_ip_address': None,
			'pay_for_conversions': None,
			'review': None,
			'review_new_subaffiliates': None,
			'suppression': None,
			'suppression_cap': None,
			'pixel_info': None,
			'fire_global_pixel': None,
			'blacklists': None,
			'redirect_domain_override': None,
			'auto_approve_campaigns': None,
			'auto_approve_pixels': None,
			'hide_offers': None,
			'api_key': None,
			'date_created': None,
			'date_last_accepted_terms': None,
			'notes': None
		}
		for (param, default) in self.param_defaults.items():
			setattr(self, param, kwargs.get(param, default))