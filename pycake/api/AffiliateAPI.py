import requests as _requests
import json as _json
from collections import OrderedDict as _OrderedDict
from datetime import datetime as _datetime
from .function_validation import _must_have_one, _if_one_then_all
from .ResponseFormat import ResponseFormat


class AffiliateAPI(object):
    
    def __init__(
            self, admin_domain, affiliate_id, api_key,
            response_format=ResponseFormat.JSON, use_https=True):
        
        self.admin_domain = admin_domain
        self.affiliate_id = affiliate_id
        self.api_key = api_key
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

    #---------------------------------ACCOUNT---------------------------------#

    def change_account_info(
            self, contact_id, contact_type_id='0', first_name='', last_name='',
            email_address='', title='', phone_work='', phone_cell='',
            phone_fax='', im_service='', im_name='', tax_class='',
            ssn_tax_id='', payment_to='', website='', address_street_1='',
            address_street_2='', address_city='', address_state='',
            address_country='', address_zip_code='', **kwargs):

        api_url = ('{}://{}/affiliates/api/2/account.asmx/ChangeAccountInfo'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['contact_id'] = contact_id
        parameters['contact_type_id'] = contact_type_id
        parameters['first_name'] = first_name
        parameters['last_name'] = last_name
        parameters['email_address'] = email_address
        parameters['title'] = title
        parameters['phone_work'] = phone_work
        parameters['phone_cell'] = phone_cell
        parameters['phone_fax'] = phone_fax
        parameters['im_service'] = im_service
        parameters['im_name'] = im_name
        parameters['tax_class'] = tax_class
        parameters['ssn_tax_id'] = ssn_tax_id
        parameters['payment_to'] = payment_to
        parameters['website'] = website
        parameters['address_street_1'] = address_street_1
        parameters['address_street_2'] = address_street_2
        parameters['address_city'] = address_city
        parameters['address_state'] = address_state
        parameters['address_country'] = address_country
        parameters['address_zip_code'] = address_zip_code

        return self._make_api_call(url=api_url, params=parameters)


    def change_language(
            self, contact_id, new_language_id, **kwargs):

        api_url = ('{}://{}/affiliates/api/2/account.asmx/ChangeLanguage'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['contact_id'] = contact_id
        parameters['new_language_id'] = new_language_id

        return self._make_api_call(url=api_url, params=parameters)


    def change_media_types(
            self, contact_id, new_media_type_ids, **kwargs):

        api_url = ('{}://{}/affiliates/api/2/account.asmx/ChangeMediaTypes'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['contact_id'] = contact_id
        parameters['new_media_type_ids'] = new_media_type_ids

        return self._make_api_call(url=api_url, params=parameters)


    def change_price_formats(
            self, contact_id, new_price_format_ids, **kwargs):

        api_url = ('{}://{}/affiliates/api/2/account.asmx/ChangePriceFormats'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['contact_id'] = contact_id
        parameters['new_price_format_ids'] = new_price_format_ids

        return self._make_api_call(url=api_url, params=parameters)


    def change_vertical_categories(
            self, contact_id, new_vertical_category_ids, **kwargs):

        api_url = ('{}://{}/affiliates/api/2/account.asmx/ChangeVertical'
            'Categories'.format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['contact_id'] = contact_id
        parameters['new_vertical_category_ids'] = new_vertical_category_ids

        return self._make_api_call(url=api_url, params=parameters)


    def get_account_info(self, contact_id, **kwargs):

        api_url = ('{}://{}/affiliates/api/2/account.asmx/GetAccountInfo'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['contact_id'] = contact_id

        return self._make_api_call(url=api_url, params=parameters)


    def get_account_manager(self, **kwargs):

        api_url = ('{}://{}/affiliates/api/2/account.asmx/GetAccountManager'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id

        return self._make_api_call(url=api_url, params=parameters)


    def get_contact_types(self, **kwargs):

        api_url = ('{}://{}/affiliates/api/2/account.asmx/GetContactTypes'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id

        return self._make_api_call(url=api_url, params=parameters)


    def get_countries(self, **kwargs):

        api_url = ('{}://{}/affiliates/api/2/account.asmx/GetCountries'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id

        return self._make_api_call(url=api_url, params=parameters)


    def get_languages(self, **kwargs):

        api_url = ('{}://{}/affiliates/api/2/account.asmx/GetLanguages'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id

        return self._make_api_call(url=api_url, params=parameters)


    def get_media_types(self, **kwargs):

        api_url = ('{}://{}/affiliates/api/2/account.asmx/GetMediaTypes'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id

        return self._make_api_call(url=api_url, params=parameters)


    def get_payment_to_types(self, **kwargs):

        api_url = ('{}://{}/affiliates/api/2/account.asmx/GetPaymentToTypes'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id

        return self._make_api_call(url=api_url, params=parameters)


    def get_price_formats(self, **kwargs):

        api_url = ('{}://{}/affiliates/api/2/account.asmx/GetPriceFormats'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id

        return self._make_api_call(url=api_url, params=parameters)


    def get_tax_classes(self, **kwargs):

        api_url = ('{}://{}/affiliates/api/2/account.asmx/GetTaxClasses'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id

        return self._make_api_call(url=api_url, params=parameters)


    def get_us_states(self, **kwargs):

        api_url = ('{}://{}/affiliates/api/2/account.asmx/GetUSStates'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id

        return self._make_api_call(url=api_url, params=parameters)


    def reset_password(self, contact_id, **kwargs):

        api_url = ('{}://{}/affiliates/api/2/account.asmx/ResetPassword'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['contact_id'] = contact_id

        return self._make_api_call(url=api_url, params=parameters)

    #---------------------------------OFFERS----------------------------------#

    def add_link_creative(
            self, campaign_id, creative_name, offer_link, description='',
            **kwargs):

        api_url = ('{}://{}/affiliates/api/2/offers.asmx/AddLinkCreative'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['campaign_id'] = campaign_id
        parameters['creative_name'] = creative_name
        parameters['offer_link'] = offer_link
        parameters['description'] = description

        return self._make_api_call(url=api_url, params=parameters)


    def apply_for_offer(
            self, offer_contract_id, media_type_id, agreed_to_terms, notes='',
            agreed_from_ip_address='', **kwargs):

        api_url = '{}://{}/affiliates/api/3/offers.asmx/ApplyForOffer'.format(
            self.protocol, self.admin_domain) 

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['offer_contract_id'] = offer_contract_id
        parameters['media_type_id'] = media_type_id
        parameters['notes'] = notes
        parameters['agreed_to_terms'] = agreed_to_terms
        parameters['agreed_from_ip_address'] = agreed_from_ip_address

        return self._make_api_call(url=api_url, params=parameters)


    def creative_feed(self, updates_since, export_feed_id, **kwargs):

        api_url = '{}://{}/affiliates/api/2/offers.asmx/CreativeFeed'.format(
            self.protocol, self.admin_domain) 

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['export_feed_id'] = export_feed_id
        parameters['updates_since'] = updates_since

        return self._make_api_call(url=api_url, params=parameters)


    def get_campaign(self, campaign_id, **kwargs):

        api_url = '{}://{}/affiliates/api/2/offers.asmx/GetCampaign'.format(
            self.protocol, self.admin_domain) 

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['campaign_id'] = campaign_id

        return self._make_api_call(url=api_url, params=parameters)


    def get_creative_code(self, campaign_id, creative_id, **kwargs):

        api_url = ('{}://{}/affiliates/api/2/offers.asmx/GetCreativeCode'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['campaign_id'] = campaign_id
        parameters['creative_id'] = creative_id

        return self._make_api_call(url=api_url, params=parameters)


    def get_creative_feeds(self, **kwargs):

        api_url = ('{}://{}/affiliates/api/2/offers.asmx/GetCreativeFeeds'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id

        return self._make_api_call(url=api_url, params=parameters)


    def get_creative_types(self, **kwargs):

        api_url = ('{}://{}/affiliates/api/2/offers.asmx/GetCreativeTypes'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id

        return self._make_api_call(url=api_url, params=parameters)


    def get_featured_offer(self, **kwargs):

        api_url = ('{}://{}/affiliates/api/2/offers.asmx/GetFeaturedOffer'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id

        return self._make_api_call(url=api_url, params=parameters)


    def get_media_type_categories(self, **kwargs):

        api_url = ('{}://{}/affiliates/api/2/offers.asmx/GetMediaTypeCategories'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id

        return self._make_api_call(url=api_url, params=parameters)


    def get_offer_statuses(self, **kwargs):

        api_url = ('{}://{}/affiliates/api/2/offers.asmx/GetOfferStatuses'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id

        return self._make_api_call(url=api_url, params=parameters)


    def get_pixel_tokens(self, **kwargs):

        api_url = ('{}://{}/affiliates/api/2/offers.asmx/GetPixelTokens'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id

        return self._make_api_call(url=api_url, params=parameters)


    def get_product_feeds(self, **kwargs):

        api_url = ('{}://{}/affiliates/api/2/offers.asmx/GetProductFeeds'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id

        return self._make_api_call(url=api_url, params=parameters)


    def get_sub_affiliates(self, start_at_row='0', row_limit='0', **kwargs):

        api_url = ('{}://{}/affiliates/api/2/offers.asmx/GetSubAffiliates'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['start_at_row'] = start_at_row
        parameters['row_limit'] = row_limit

        return self._make_api_call(url=api_url, params=parameters)


    def get_suppression_list(self, offer_id, **kwargs):

        api_url = ('{}://{}/affiliates/api/2/offers.asmx/GetSuppressionList'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['offer_id'] = offer_id

        return self._make_api_call(url=api_url, params=parameters)


    def get_tags(self, **kwargs):

        api_url = '{}://{}/affiliates/api/2/offers.asmx/GetTags'.format(
            self.protocol, self.admin_domain)

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id

        return self._make_api_call(url=api_url, params=parameters)


    def get_vertical_categories(self, **kwargs):

        api_url = ('{}://{}/affiliates/api/2/offers.asmx/GetVerticalCategories'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id

        return self._make_api_call(url=api_url, params=parameters)  


    def get_verticals(self, **kwargs):

        api_url = ('{}://{}/affiliates/api/2/offers.asmx/GetVerticals'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id

        return self._make_api_call(url=api_url, params=parameters)   


    def offer_feed(
            self, campaign_name='', media_type_category_id='0',
            vertical_category_id='0', country_code='', vertical_id='0',
            offer_status_id='0', tag_id='0', start_at_row='0', row_limit='0',
            **kwargs):
        
        api_url = '{}://{}/affiliates/api/5/offers.asmx/OfferFeed'.format(
            self.protocol, self.admin_domain) 
        
        parameters = _OrderedDict()
        parameters['affiliate_id'] = self.affiliate_id
        parameters['api_key'] = self.api_key
        parameters['campaign_name'] = campaign_name
        parameters['media_type_category_id'] = media_type_category_id
        parameters['vertical_category_id'] = vertical_category_id
        parameters['country_code'] = country_code
        parameters['vertical_id'] = vertical_id
        parameters['offer_status_id'] = offer_status_id
        parameters['tag_id'] = tag_id
        parameters['start_at_row'] = start_at_row
        parameters['row_limit'] = row_limit
        
        return self._make_api_call(url=api_url, params=parameters)


    def send_creative_pack(
        self, campaign_id, creative_id='0', contact_id='0', **kwargs):

        api_url = ('{}://{}/affiliates/api/2/offers.asmx/SendCreativePack'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['campaign_id'] = campaign_id
        parameters['creative_id'] = creative_id
        parameters['contact_id'] = contact_id

        return self._make_api_call(url=api_url, params=parameters)


    def set_pixel(self, campaign_id, pixel_html, **kwargs):

        api_url = '{}://{}/affiliates/api/2/offers.asmx/SetPixel'.format(
            self.protocol, self.admin_domain)

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['campaign_id'] = campaign_id
        parameters['pixel_html'] = pixel_html

        return self._make_api_call(url=api_url, params=parameters)


    def set_postback_url(self, campaign_id, postback_url, **kwargs):

        api_url = '{}://{}/affiliates/api/2/offers.asmx/SetPostbackURL'.format(
            self.protocol, self.admin_domain)

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['campaign_id'] = campaign_id
        parameters['postback_url'] = postback_url

        return self._make_api_call(url=api_url, params=parameters)


    def set_test_link(self, campaign_id, test_link, **kwargs):

        api_url = '{}://{}/affiliates/api/2/offers.asmx/SetTestLink'.format(
            self.protocol, self.admin_domain)

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['campaign_id'] = campaign_id
        parameters['test_link'] = test_link

        return self._make_api_call(url=api_url, params=parameters)

    #---------------------------------REPORTS---------------------------------#

    def bills(self, start_at_row='0', row_limit='0', **kwargs):
        api_url = '{}://{}/affiliates/api/3/reports.asmx/Bills'.format(
            self.protocol, self.admin_domain)

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['start_at_row'] = start_at_row
        parameters['row_limit'] = row_limit

        return self._make_api_call(url=api_url, params=parameters)


    def campaign_summary(
            self, start_date, end_date, sub_affiliate='', event_type='all',
            start_at_row='0', row_limit='0', sort_field='site_offer_id',
            sort_descending='FALSE', **kwargs):

        api_url = ('{}://{}/affiliates/api/6/reports.asmx/CampaignSummary'
            .format(self.protocol, self.admin_domain))
        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['start_date'] = str(start_date)
        parameters['end_date'] = str(end_date)
        parameters['sub_affiliate'] = sub_affiliate
        parameters['event_type'] = event_type
        parameters['start_at_row'] = start_at_row
        parameters['row_limit'] = row_limit
        parameters['sort_field'] = sort_field
        parameters['sort_descending'] = sort_descending

        return self._make_api_call(url=api_url, params=parameters)


    def clicks(
            self, start_date, end_date, offer_id='0', campaign_id='0', 
            include_duplicates='FALSE', start_at_row='0', row_limit='0',
            **kwargs):
        
        api_url = '{}://{}/affiliates/api/10/reports.asmx/Clicks'.format(
            self.protocol, self.admin_domain)
        
        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['start_date'] = str(start_date)
        parameters['end_date'] = str(end_date)
        parameters['offer_id'] = offer_id
        parameters['campaign_id'] = campaign_id
        parameters['include_duplicates'] = include_duplicates
        parameters['start_at_row'] = start_at_row
        parameters['row_limit'] = row_limit
        
        return self._make_api_call(url=api_url, params=parameters)


    def daily_summary(self, start_date, end_date, site_offer_id='0', **kwargs):

        api_url = ('{}://{}/affiliates/api/3/reports.asmx/DailySummary'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['start_date'] = str(start_date)
        parameters['end_date'] = str(end_date)
        parameters['site_offer_id'] = site_offer_id

        return self._make_api_call(url=api_url, params=parameters)


    def events_conversions(
            self, start_date, end_date, currency_id, site_offer_id='0',
            disposition_type='', event_type='all', exclude_bot_traffic='FALSE',
            start_at_row='0', row_limit='0', **kwargs):
        
        api_url = ('{}://{}/affiliates/api/9/reports.asmx/EventConversions'
            .format(self.protocol, self.admin_domain))
        
        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['start_date'] = str(start_date)
        parameters['end_date'] = str(end_date)
        parameters['site_offer_id'] = site_offer_id
        parameters['currency_id'] = currency_id
        parameters['disposition_type'] = disposition_type
        parameters['event_type'] = event_type
        parameters['exclude_bot_traffic'] = exclude_bot_traffic
        parameters['start_at_row'] = start_at_row
        parameters['row_limit'] = row_limit
        
        return self._make_api_call(url=api_url, params=parameters)


    def hourly_summary(self, start_date, end_date, site_offer_id='0', **kwargs):

        api_url = ('{}://{}/affiliates/api/3/reports.asmx/HourlySummary'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['start_date'] = str(start_date)
        parameters['end_date'] = str(end_date)
        parameters['site_offer_id'] = site_offer_id

        return self._make_api_call(url=api_url, params=parameters)


    def network_news(self, row_limit='0', **kwargs):

        api_url = ('{}://{}/affiliates/api/2/reports.asmx/NetworkNews'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['row_limit'] = row_limit


    def offer_compliance(self, start_at_row='0', row_limit='0', **kwargs):
        api_url = ('{}://{}/affiliates/api/3/reports.asmx/OfferCompliance'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['start_at_row'] = start_at_row
        parameters['row_limit'] = row_limit

        return self._make_api_call(url=api_url, params=parameters)


    def order_detail_changes(
            self, changes_since, include_new_conversions='FALSE',
            start_at_row='0', row_limit='0', sort_field='conversion_id',
            sort_descending='FALSE', **kwargs):

        api_url = ('{}://{}/affiliates/api/2/reports.asmx/OrderDetailChanges'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['changes_since'] = str(changes_since)
        parameters['include_new_conversions'] = include_new_conversions
        parameters['start_at_row'] = start_at_row
        parameters['row_limit'] = row_limit
        parameters['sort_field'] = sort_field
        parameters['sort_descending'] = sort_descending

        return self._make_api_call(url=api_url, params=parameters)


    @_must_have_one(['conversion_id', 'order_id'])
    def order_details(
            self, start_date, end_date, conversion_id='0', order_id='',
            start_at_row='0', row_limit='0', sort_field='conversion_id',
            sort_descending='FALSE', **kwargs):

        api_url = ('{}://{}/affiliates/api/2/reports.asmx/OrderDetails'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['start_date'] = str(start_date)
        parameters['end_date'] = str(end_date)
        parameters['conversion_id'] = conversion_id
        parameters['order_id'] = order_id
        parameters['start_at_row'] = start_at_row
        parameters['row_limit'] = row_limit
        parameters['sort_field'] = sort_field
        parameters['sort_descending'] = sort_descending

        return self._make_api_call(url=api_url, params=parameters)


    def performance_summary(self, date, **kwargs):

        api_url = ('{}://{}/affiliates/api/2/reports.asmx/PerformanceSummary'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['date'] = str(date)

        return self._make_api_call(url=api_url, params=parameters)


    def referral(
            self, start_date, end_date, over_minimum, start_at_row='0',
            row_limit='0', sort_field='affiliate_id', sort_descending='FALSE',
            **kwargs):

        api_url = '{}://{}/affiliates/api/2/reports.asmx/Referral'.format(
            self.protocol, self.admin_domain)

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['start_date'] = str(start_date)
        parameters['end_date'] = str(end_date)
        parameters['over_minimum'] = over_minimum
        parameters['start_at_row'] = start_at_row
        parameters['row_limit'] = row_limit
        parameters['sort_field'] = sort_field
        parameters['sort_descending'] = sort_descending

        return self._make_api_call(url=api_url, params=parameters)


    def sub_affiliate_summary(
            self, start_date, end_date, site_offer_id='0', start_at_row='0',
            row_limit='0', **kwargs):

        api_url = ('{}://{}/affiliates/api/4/reports.asmx/SubAffiliateSummary'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['start_date'] = str(start_date)
        parameters['end_date'] = str(end_date)
        parameters['site_offer_id'] = site_offer_id
        parameters['start_at_row'] = start_at_row
        parameters['row_limit'] = row_limit

        return self._make_api_call(url=api_url, params=parameters)


    def top_offer_summary(
            self, start_date, end_date, vertical_id='0', start_at_row='0',
            row_limit='0', **kwargs):

        api_url = ('{}://{}/affiliates/api/3/reports.asmx/TopOfferSummary'
            .format(self.protocol, self.admin_domain))

        parameters = _OrderedDict()
        parameters['api_key'] = self.api_key
        parameters['affiliate_id'] = self.affiliate_id
        parameters['start_date'] = str(start_date)
        parameters['end_date'] = str(end_date)
        parameters['vertical_id'] = vertical_id
        parameters['start_at_row'] = start_at_row
        parameters['row_limit'] = row_limit

        return self._make_api_call(url=api_url, params=parameters)








