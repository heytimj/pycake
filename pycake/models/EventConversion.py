from .CakeModel import CakeModel


class EventConversion(CakeModel):

	def __init__(self, **kwargs):
		self.param_defaults = {
			'event_conversion_id': None,
			'visitor_id': None,
			'original_visitor_id': None,
			'user_id': None,
			'tracking_id': None,
			'original_tracking_id': None,
			'request_session_id': None,
			'click_request_session_id': None,
			'click_id': None,
			'event_conversion_date': None,
			'last_updated': None,
			'click_date': None,
			'source_date': None,
			'udid': None,
			'event_info': None,
			'source_affiliate': None,
			'brand_advertiser': None,
			'site_offer': None,
			'site_offer_contract': None,
			'channel': None,
			'campaign': None,
			'creative': None,
			'voucher_code': None,
			'sub_id_1': None,
			'sub_id_2': None,
			'sub_id_3': None,
			'sub_id_4': None,
			'sub_id_5': None,
			'event_conversion_ip_address': None,
			'click_ip_address': None,
			'event_conversion_referrer_url': None,
			'click_referrer_url': None,
			'event_conversion_user_agent': None,
			'click_user_agent': None,
			'source_type': None,
			'price_format': None,
			'paid': None,
			'paid_unbilled': None,
			'received': None,
			'received_unbilled': None,
			'site_offer_credit_percentage': None,
			'site_offer_payment_percentage': None,
			'program_credit_percentage': None,
			'pixel_dropped': None,
			'suppressed': None,
			'returned': None,
			'test': None,
			'transaction_id': None,
			'current_disposition': None,
			'order_total': None,
			'storefront': None,
			'payout_rule': None,
			'event_conversion_score': None,
			'country': None,
			'region': None,
			'language': None,
			'isp': None,
			'device': None,
			'operating_system': None,
			'browser': None,
			'search_term': None,
			'keyword': None,
			'note': None
		}

		for (param, default) in self.param_defaults.items():
			setattr(self, param, kwargs.get(param, default))



