.. image:: https://img.shields.io/badge/license-MIT-blue.svg?style=flat
   :target: http://www.opensource.org/licenses/MIT
   :align: left

Introduction
============
**pycake** is a python package intended to make CAKE's API *seem* more RESTful. **pycake** contains two modules,  ``pycake.api`` and ``pycake.models``. ``pycake.api`` contains the ``AdminApi`` and ``AffiliateAPI`` classes designed to make calling the CAKE API a bit simpler. Due to the .NET framework, without **pycake** a user would need to include every parameter with every api call. When editing an entity, this can be annoying if you're only changing one or a few settings. Additionally, when exporting entities or reporting data, it is less than ideal to have to pass every parameter(filter) if you wish to include all results. For example, if you want to edit one setting on one offer (ADDEDIT Offer), you can use ``pycake.api.AdminAPI.edit_offer()`` and only pass the ``offer_id`` and the key-value pair for the setting you wish to change:

.. code:: python

    >>> from pycake.api import AdminAPI

    >>> ckadmin = AdminAPI('somecakedomain.com', api_key='ADhakjnOtAreALkEY')
    >>> offer_edit_response = ckadmin.edit_offer(offer_id=4, click_cookie_days=60)

New in 2.1.0
============
- added ``pycake.api.BuyerAPI`` class
- added ``pycake.api.AdminAPI.get_lead_return_reasons()`` function
- changed ``pycake.api.AdminAPI.conversion_changes()`` to ``pycake.AdminAPI.event_conversion_changes()`` and updated to underlying API v17
- updated ``pycake.api.AdminAPI.export_campaigns()`` to underlying api v8

Python
======
Only really tested in 3.4+ but *probably* works in 2.7.10+

Installation
============

.. code:: bash

    $ pip3 install pycake --upgrade
    
pycake.api Module
=================
pycake.api contains three classes:

- **AdminAPI**\(*admin_domain, api_key=None, response_format=ResponseFormat.JSON, use_https=True*)
- **AffiliateAPI**\(*admin_domain, affiliate_id, api_key, response_format=ResponseFormat.JSON, use_https=True*)
- **BuyerAPI**\(*admin_domain, response_format=ResponseFormat.JSON, use_https=True*)

**Initialize an AdminAPI object with an API key**

.. code:: python

    >>> from pycake.api import AdminAPI

    >>> ckadmin = AdminAPI('somecakedomain.com', api_key='ADhakjnOtAreALkEY')
    >>> offer_info = ckadmin.export_offers()
    >>> media_type_info = ckadmin.get_media_types()
   
**Initialize an AdminAPI object without an API key**

You can initialize an AdminAPI object without an API key and then use the ``set_api_key()`` function. This is useful when you need to utilize user-provided admin login credentials to perform API calls.

.. code:: python
    
    >>> from pycake.api import AdminAPI

    >>> ckadmin = AdminAPI('somecakedomain.com')
    >>> username = 'email@domain.com'
    >>> password = 'SomePassword123'
    >>> ckadmin.set_api_key(username=username, password=password)
    >>> print(ckadmin.api_key)
    ADhakjnOtAreALkEY
    >>> conversion_data = ckadmin.conversions(start_date='2017-5-1', end_date='2017-6-1')

*Note:* If ``username`` and ``password`` are not valid admin credentials ``AdminAPI.api_key`` is set to ``None``. Calling subsequent AdminAPI functions other than ``set_api_key()`` will raise an Exception.

**Initialize an AffiliateAPI object**

.. code:: python

    >>> from pycake.api import AffiliateAPI

    >>> ckaff = AffiliateAPI(
            admin_domain='somecakedomain.com',
            affiliate_id=123,
            api_key='ADhakjsOmeAFfaPIkEY')
    >>> campaign_report = ckaff.campaign_summary(start_date='2017-10-1', end_date='2017-11-1')
    >>> offer_feed = ckaff.offer_feed()

AdminAPI Functions
------------------

**API KEY**

- **set_api_key**\(*username, password*)

**ACCOUNTING** 

- **export_advertiser_bills**\(*billing_period_start_date, billing_period_end_date, billing_cycle='all'*)

- **export_affiliate_bills**\(*billing_period_start_date, billing_period_end_date, billing_cycle='all', paid_only='FALSE', payment_type_id='0'*)

**ADDEDIT** 

- **add_advertiser**\(*advertiser_name, third_party_name='', account_status_id='1', online_signup='FALSE', signup_ip_address='', website='', billing_cycle_id='3', account_manager_id='0', address_street='', address_street2='', address_city='', address_state='', address_zip_code='', address_country='', notes='', tags=''*)

- **add_affiliate**\(*affiliate_name, third_party_name='', account_status_id='1', inactive_reason_id='0', affiliate_tier_id='0', account_manager_id='0', hide_offers='FALSE', website='', tax_class='', ssn_tax_id='', vat_tax_required='FALSE', swift_iban='', payment_to='0', payment_fee='-1', payment_min_threshold='-1', currency_id='0', payment_setting_id='1', billing_cycle_id='3', payment_type_id='1', payment_type_info='', address_street='', address_street2='', address_city='', address_state='', address_zip_code='', address_country='', media_type_ids='', price_format_ids='', vertical_category_ids='', country_codes='', tags='', pixel_html='', postback_url='', postback_delay_ms='-1', fire_global_pixel='TRUE', date_added=datetime.now(), online_signup='FALSE', signup_ip_address='', referral_affiliate_id='0', referral_notes='', terms_and_conditions_agreed='TRUE', notes=''*)

- **add_blacklist**\(*affiliate_id, blacklist_reason_id, redirect_type, sub_id='', advertiser_id='0', offer_id='0', blacklist_date=datetime.now()*)

- **add_buyer**\(*buyer_name, account_manager_id, account_status_id='1', address_street='', address_street2='', address_city='', address_state='', address_zip_code='', address_country='', website='', billing_cycle_id='3', credit_type='unlimited', credit_limit='-1'*)

- **add_buyer_contract**\(*buyer_id, vertical_id, buyer_contract_name, account_status_id='1', offer_id='0', replace_returns='off', replacements_non_returnable='off', max_return_age_days='30', buy_upsells='off', vintage_leads='off', min_lead_age_minutes='0', max_lead_age_minutes='7200', posting_wait_seconds='0', default_confirmation_page_link='', max_post_errors='10', send_alert_only='off', rank='0', email_template_id='0', portal_template_id='0'*)

- **add_campaign**\(*affiliate_id, media_type_id, payout, offer_id='0', offer_contract_id='0', third_party_name='', account_status_id='1', display_link_type_id='1', expiration_date='', currency_id='0', paid='on', static_suppression='-1', paid_redirects='on', paid_upsells='on', review='off', auto_disposition_delay_hours='-1', redirect_offer_contract_id='0', redirect_404='off', clear_session_on_conversion='off', postback_url='', postback_delay_ms='-1', unique_key_hash_type='none', pixel_html='', test_link='', redirect_domain=''*)

- **add_campaign_creative_exception**\(*campaign_id, creative_id*)

- **add_campaign_subid_exception**\(*campaign_id, sub_id*)

- **add_contact**\(*entity_type, entity_id, role_id, contact_email_address, contact_first_name, include_in_mass_emails='on', contact_middle_name='', contact_last_name='', contact_title='', contact_department_id='-1', contact_phone_work='', contact_phone_cell='', contact_phone_fax='', contact_im_service='', contact_im_name='', contact_timezone='', contact_language_id='-1'*)

- **add_creative**\(*creative_name, offer_id, creative_type_id, third_party_name='', creative_status_id='1', width='-1', height='-1', offer_link='', allow_link_override='FALSE', notes=''*)

- **add_creative_files**\(*creative_id, creative_file_import_url, is_preview_file='FALSE', replace_all_files='FALSE'*)

- **add_offer**\(*advertiser_id, vertical_id, offer_name, offer_status_id, offer_type_id, last_touch, price_format_id, payout, received, offer_link, third_party_name='', hidden='off', currency_id='0', ssl='on', click_cookie_days='30', impression_cookie_days='30', auto_disposition_type='none', auto_disposition_delay_hours='-1', redirect_offer_contract_id='0', redirect_404='off', redirect_domain='', conversions_from_whitelist_only='off', track_search_terms_from_non_supported_search_engines='off', enable_view_thru_conversions='off', click_trumps_impression='off', disable_click_deduplication='off', session_regeneration_seconds='-1', session_regeneration_type_id='0', enable_transaction_id_deduplication='off', cookie_domain='', postbacks_only='off', pixel_html='', postback_url='', postback_url_ms_delay='-1', fire_global_pixel='on', fire_pixel_on_non_paid_conversions='off', static_suppression='-1', conversion_cap_behavior='0', conversion_behavior_on_redirect='0', expiration_date='', offer_contract_name='', offer_contract_hidden='off', received_percentage='off', thankyou_link='', preview_link='', thumbnail_file_import_url='', offer_description='', restrictions='', advertiser_extended_terms='', testing_instructions='', tags_modification_type='do_not_change', tags='', allow_affiliates_to_create_creatives='off', unsubscribe_link='', from_lines='', subject_lines='', allowed_media_type_modification_type='do_not_change', allowed_media_type_ids=''*)

- **edit_advertiser**\(*advertiser_id, advertiser_name='', third_party_name='', account_status_id='0', website='', billing_cycle_id='0', account_manager_id='0', address_street='', address_street2='', address_city='', address_state='', address_zip_code='', address_country='', notes='', tags=''*)

- **edit_affiliate**\(*affiliate_id, affiliate_name='', third_party_name='', account_status_id='0', inactive_reason_id='0', affiliate_tier_id='0', account_manager_id='0', hide_offers='', website='', tax_class='', ssn_tax_id='', vat_tax_required='', swift_iban='', payment_to='', payment_fee='-1', payment_min_threshold='-1', currency_id='0', payment_setting_id='0', billing_cycle_id='0', payment_type_id='0', payment_type_info='', address_street='', address_street2='', address_city='', address_state='', address_zip_code='', address_country='', media_type_ids='', price_format_ids='', vertical_category_ids='', country_codes='', tags='', pixel_html='', postback_url='', postback_delay_ms='-1', fire_global_pixel='', referral_affiliate_id='0', referral_notes='', notes=''*)

- **edit_buyer**\(*buyer_id, buyer_name='', account_status_id='0', account_manager_id='0', address_street='', address_street2='', address_city='', address_state='', address_zip_code='', address_country='', website='', billing_cycle_id='0', credit_type='no_change', credit_limit='-1'*)

- **edit_buyer_contract**\(*buyer_contract_id, buyer_contract_name='', account_status_id='0', offer_id='0', replace_returns='no_change', replacements_non_returnable='no_change', max_return_age_days='-1', buy_upsells='no_change', vintage_leads='no_change', min_lead_age_minutes='-1', max_lead_age_minutes='-1', posting_wait_seconds='-1', default_confirmation_page_link='', max_post_errors='-1', send_alert_only='no_change', rank='-1', email_template_id='0', portal_template_id='0'*)

- **edit_campaign**\(*campaign_id, offer_contract_id='0', media_type_id='0', third_party_name='', account_status_id='0', display_link_type_id='0', expiration_date='', use_offer_contract_payout='no_change', payout='', paid='no_change', static_suppression='-1', paid_redirects='no_change', paid_upsells='no_change', review='no_change', auto_disposition_delay_hours='-1', redirect_offer_contract_id='0', redirect_404='no_change', clear_session_on_conversion='no_change', postback_url='', postback_delay_ms='-1', unique_key_hash_type='', pixel_html='', test_link='', redirect_domain=''*)

- **edit_caps**\(*cap_type_id, cap_interval_id, cap_amount, send_alert_only, offer_id='0', offer_contract_id='0', campaign_id='0', cap_start=''*)

- **edit_creative**\(*creative_id, allow_link_override, creative_name='', third_party_name='', creative_type_id='0', creative_status_id='0', width='-1', height='-1', offer_link='', notes=''*)

- **edit_offer**\(*offer_id, offer_name='', vertical_id='0', third_party_name='', hidden='no_change', offer_status_id='0', ssl='no_change', click_cookie_days='-1', impression_cookie_days='-1', auto_disposition_type='no_change', auto_disposition_delay_hours='-1', redirect_offer_contract_id='0', redirect_404='no_change', redirect_domain='', conversions_from_whitelist_only='no_change', track_search_terms_from_non_supported_search_engines='no_change', enable_view_thru_conversions='no_change', click_trumps_impression='no_change', disable_click_deduplication='no_change', last_touch='no_change', session_regeneration_seconds='-1', session_regeneration_type_id='0', enable_transaction_id_deduplication='no_change', cookie_domain='', postbacks_only='no_change', pixel_html='', postback_url='', postback_url_ms_delay='-1', fire_global_pixel='no_change', fire_pixel_on_non_paid_conversions='no_change', static_suppression='-1', conversion_cap_behavior='-1', conversion_behavior_on_redirect='-1', expiration_date='', offer_contract_name='', offer_contract_hidden='no_change', payout='', received='', received_percentage='no_change', offer_link='', thankyou_link='', preview_link='', thumbnail_file_import_url='', offer_description='', restrictions='', advertiser_extended_terms='', testing_instructions='', tags_modification_type='do_not_change', tags='', allow_affiliates_to_create_creatives='no_change', unsubscribe_link='', from_lines='', subject_lines='', allowed_media_type_modification_type='do_not_change', allowed_media_type_ids=''*)

- **remove_blacklist**\(*blacklist_id*)

- **remove_campaign_creative_exception**\(*campaign_id, creative_id*)

- **remove_campaign_subid_exception**\(*campaign_id, sub_id*)

**EXPORT**

- **export_advertisers**\(*advertiser_id='0', advertiser_name='', account_manager_id='0', tag_id='0', start_at_row='0', row_limit='0', sort_field='advertiser_id', sort_descending='FALSE'*) 

- **export_affiliates**\(*affiliate_id='0', affiliate_name='', account_manager_id='0', tag_id='0', start_at_row='0', row_limit='0', sort_field='affiliate_id', sort_descending='FALSE'*) 

- **export_blacklists**\(*affiliate_id='0', sub_id='', advertiser_id='0', offer_id='0'*)

- **export_buyer_contracts**\(*buyer_contract_id='0', buyer_id='0', vertical_id='0', buyer_contract_status_id='0'*)

- **export_buyers**\(*buyer_id='0', account_status_id='0'*)

- **export_campaigns**\(*campaign_id='0', offer_id='0', affiliate_id='0', account_status_id='0', media_type_id='0', start_at_row='0', row_limit='0', sort_field='campaign_id', sort_descending='FALSE'*)

- **export_creatives**\(*offer_id, creative_id='0', creative_name='', creative_type_id='0', creative_status_id='0', start_at_row='0', row_limit='0', sort_field='creative_id', sort_descending='FALSE'*)

- **export_offers**\(*offer_id='0', offer_name='', advertiser_id='0', vertical_id='0', offer_type_id='0', media_type_id='0', offer_status_id='0', tag_id='0', start_at_row='0', row_limit='0', sort_field='offer_id', sort_descending='FALSE'*)

- **export_pixel_log_requests**\(*start_date, end_date, advertiser_id='0', offer_id='0', converted_only='FALSE', start_at_row='0', row_limit='0', sort_descending='FALSE'*)

- **export_rule_targets**\(*rule_id*)

- **export_schedules**\(*start_date, end_date, buyer_id='0', status_id='0', vertical_id='0', priority_only='FALSE', active_only='FALSE'*)

**GET**

- **get_account_statuses**\()

- **get_advertisers**\()

- **get_affiliate_tags**\()

- **get_affiliate_tiers**\()

- **get_billing_cycles**\()

- **get_blacklist_reasons**\()

- **get_cap_intervals**\()

- **get_cap_types**\()

- **get_conversion_dispositions**\()

- **get_countries**\()

- **get_currencies**\()

- **get_custom_queue_statuses**\()

- **get_departments**\()

- **get_email_templates**\(*email_type='both'*)

- **get_exchange_rates**\(*start_date, end_date*)

- **get_filter_types**\(*filter_type_id='0', filter_type_name='', vertical_id='0'*)

- **get_api_key**\(*username, password*)

- **get_inactive_reasons**\()

- **get_languages**\()

- **get_lead_info**\(*lead_id, vertical_id='0'*)

- **get_lead_return_reasons**\()

- **get_lead_tier_groups**\(*lead_tier_group_id='0'*)

- **get_link_display_types**\()

- **get_media_types**\()

- **get_offer_statuses**\()

- **get_offer_types**\()

- **get_payment_settings**\()

- **get_payment_types**\()

- **get_price_formats**\()

- **get_response_dispositions**\()

- **get_roles**\()

- **get_schedule_types**\()

- **get_session_regeneration_types**\()

- **get_shared_rules**\()

- **get_tracking_domains**\(*domain_type='all'*)

- **get_verticals**\(*vertical_category_id='0'*)

- **get_vertical_categories**\()

**REPORTS**

- **brand_advertiser_summary**\(*start_date, end_date, brand_advertiser_id='0', brand_advertiser_manager_id='0', brand_advertiser_tag_id='0', event_id='0', event_type='all'*)
- **campaign_summary**\(*start_date, end_date, campaign_id='0', source_affiliate_id='0', subid_id='', site_offer_id='0', source_affiliate_tag_id='0', site_offer_tag_id='0', source_affiliate_manager_id='0', brand_advertiser_manager_id='0', event_id='0', event_type='all'*)
- **clicks**\(*start_date, end_date, affiliate_id='0', advertiser_id='0', offer_id='0', campaign_id='0', creative_id='0', price_format_id='0', include_duplicates='FALSE', include_tests='FALSE', start_at_row='0', row_limit='0'*)
- **conversion_changes**\(*changes_since, include_new_conversions='FALSE', affiliate_id='0', advertiser_id='0', offer_id='0', campaign_id='0', creative_id='0', include_tests='FALSE', start_at_row='0', row_limit='0', sort_field='conversion_id', sort_descending='FALSE'*)

- **country_summary**\(*start_date, end_date, affiliate_id='0', affiliate_tag_id='0', advertiser_id='0', offer_id='0', campaign_id='0', event_id='0', revenue_filter='conversions_and_events'*)

- **creative_summary**\(*start_date, end_date, site_offer_id='0', campaign_id='0', event_id='0', event_type='all'*)

- **daily_summary**\(*start_date, end_date, source_affiliate_id='0', brand_advertiser_id='0', site_offer_id='0', vertical_id='0', campaign_id='0', creative_id='0', account_manager_id='0', include_tests='FALSE'*)

- **events_conversions**\(*start_date, end_date, event_type='all', event_id='0', source_affiliate_id='0', brand_advertiser_id='0', channel_id='0', site_offer_id='0', site_offer_contract_id='0', source_affiliate_tag_id='0', brand_advertiser_tag_id='0', site_offer_tag_id='0', campaign_id='0', creative_id='0', price_format_id='0', source_type='all', payment_percentage_filter='both', disposition_type='all', disposition_id='0', source_affiliate_billing_status='all', brand_advertiser_billing_status='all', test_filter='non_tests', start_at_row='0', row_limit='0', sort_field='event_conversion_date', sort_descending='FALSE'*)

- **leads_by_affiliate**\(*start_date, end_date, vertical_id='0', source_affiliate_id='0', site_offer_id='0', source_affiliate_manager_id='0', upsell='upsells_and_non_upsells', lead_tier_id='0', start_at_row='0', row_limit='0'*)

- **leads_by_buyer**\(*start_date, end_date, vertical_id='0', buyer_id='0', buyer_contract_id='0', status_id='0', sub_status_id='0', start_at_row='0', row_limit='0', sort_field='transaction_date', sort_descending='FALSE'*)
    
- **lite_clicks_advertiser_summary**\(*start_date, end_date, advertiser_id='0', advertiser_manager_id='0', advertiser_tag_id='0', event_id='0', revenue_filter='conversions_and_events'*)

- **lite_clicks_affiliate_summary**\(*start_date, end_date, affiliate_id='0', affiliate_manager_id='0', affiliate_tag_id='0', offer_tag_id='0', event_id='0', revenue_filter='conversions_and_events'*)

- **lite_clicks_campaign_summary**\(*start_date, end_date, affiliate_id='0', subaffiliate_id='', affiliate_tag_id='0', offer_id='0', offer_tag_id='0', campaign_id='0', event_id='0', revenue_filter='conversions_and_events'*)

- **lite_clicks_country_summary**\(*start_date, end_date, affiliate_id='0', affiliate_tag_id='0', advertiser_id='0', offer_id='0', campaign_id='0', event_id='0', revenue_filter='conversions_and_events'*)

- **lite_clicks_daily_summary**\(*start_date, end_date, affiliate_id='0', advertiser_id='0', offer_id='0', vertical_id='0', campaign_id='0', creative_id='0', account_manager_id='0', include_tests='FALSE'*)

- **lite_clicks_offer_summary**\(*start_date, end_date, advertiser_id='0', advertiser_manager_id='0', offer_id='0', offer_tag_id='0', affiliate_tag_id='0', event_id='0', revenue_filter='conversions_and_events'*)

- **lite_clicks_sub_id_summary**\(*start_date, end_date, source_affiliate_id, site_offer_id='0', campaign_id='0', sub_id='NULL', event_id='0', revenue_filter='conversions_and_events'*)

- **login_export**\(*start_date, end_date, role_id='0'*)

- **order_details**\(*start_date, end_date, affiliate_id='0', conversion_id='0', order_id='', start_at_row='0', row_limit='0', sort_field='order_id', sort_descending='FALSE'*)

- **site_offer_summary**\(*start_date, end_date, brand_advertiser_id='0', brand_advertiser_manager_id='0', site_offer_id='0', site_offer_tag_id='0', source_affiliate_tag_id='0', event_id='0', event_type='all'*)

- **source_affiliate_summary**\(*start_date, end_date, source_affiliate_id='0', source_affiliate_manager_id='0', source_affiliate_tag_id='0', site_offer_tag_id='0', event_id='0', event_type='all'*)

- **sub_id_summary**\(*start_date, end_date, source_affiliate_id, site_offer_id='0', event_id='0', revenue_filter='conversions_and_events'*)

- **traffic_export**\(*start_date, end_date*)

**SIGNUP**

- **signup_advertiser**\(*company_name, address_street, address_city, address_state, address_zip_code, address_country, first_name, last_name, email_address, contact_phone_work, address_street2='', website='', notes='', contact_title='', contact_phone_cell='', contact_phone_fax='', contact_im_name='', contact_im_service=0, ip_address=''*)

- **signup_affiliate**\(*affiliate_name, account_status_id, payment_setting_id, tax_class, ssn_tax_id, address_street, address_city, address_state, address_zip_code, address_country, contact_first_name, contact_last_name, contact_email_address, contact_phone_work, contact_timezone, terms_and_conditions_agreed, affiliate_tier_id='0', hide_offers='FALSE', website='', vat_tax_required='FALSE', swift_iban='', payment_to='0', payment_fee='-1', payment_min_threshold='-1', currency_id='0', billing_cycle_id='3', payment_type_id='1', payment_type_info='', address_street2='', contact_middle_name='', contact_title='', contact_phone_cell='', contact_phone_fax='', contact_im_service='', contact_im_name='', contact_language_id='0', media_type_ids='', price_format_ids='', vertical_category_ids='', country_codes='', tag_ids='', date_added=datetime.now(), signup_ip_address='', referral_affiliate_id='0', referral_notes='', notes=''*)

**TRACK**

- **update_conversion**\(*offer_id, conversion_id='0', request_session_id='0', transaction_id='', payout='', add_to_existing_payout='TRUE', received='', received_option='no_change', disposition_type='no_change', disposition_id='0', update_revshare_payout='FALSE', effective_date_option='conversion_date', custom_date='', note_to_append='', disallow_on_billing_status='ignore'*)

**SPECIAL**

- **get_advertiser_ids**\()

- **get_affiliate_ids**\()

- **get_offer_ids**\(*advertiser_id='0'*)

AffiliateAPI Functions
----------------------

**ACCOUNT**

- **change_account_info**\(*contact_id, contact_type_id='0', first_name='', last_name='', email_address='', title='', phone_work='', phone_cell='', phone_fax='', im_service='', im_name='', tax_class='', ssn_tax_id='', payment_to='', website='', address_street_1='', address_street_2='', address_city='', address_state='', address_country='', address_zip_code=''*)

- **change_language**\(*contact_id, new_language_id*)

- **change_media_types**\(*contact_id, new_media_type_ids*)

- **change_price_formats**\(*contact_id, new_price_format_ids*)

- **change_vertical_categories**\(*contact_id, new_vertical_category_ids*)

- **get_account_info**\(*contact_id*)

- **get_account_manager**\()

- **get_contact_types**\()

- **get_countries**\()

- **get_languages**\()

- **get_media_types**\()

- **get_payment_to_types**\()

- **get_price_formats**\()

- **get_tax_classes**\()

- **get_us_states**\()

- **reset_password**\(*contact_id*)

**OFFERS**

- **add_link_creative**\(*campaign_id, creative_name, offer_link, description=''*)

- **apply_for_offer**\(*offer_contract_id, media_type_id, agreed_to_terms, notes='', agreed_from_ip_address=''*)

- **creative_feed**\(*updates_since, export_feed_id*)

- **get_campaign**\(*campaign_id*)

- **get_creative_code**\(*campaign_id, creative_id*)

- **get_creative_feeds**\()

- **get_creative_types**\()

- **get_featured_offer**\()

- **get_media_type_categories**\()

- **get_offer_statuses**\()

- **get_pixel_tokens**\()

- **get_product_feeds**\()

- **get_sub_affiliates**\(*start_at_row='0', row_limit='0'*)

- **get_suppression_list**\(*offer_id*)

- **get_tags**\()

- **get_vertical_categories**\()

- **get_verticals**\()

- **offer_feed**\(*campaign_name='', media_type_category_id='0', vertical_category_id='0', country_code='', vertical_id='0', offer_status_id='0', tag_id='0', start_at_row='0', row_limit='0'*)

- **send_creative_pack**\(*campaign_id, creative_id='0', contact_id='0'*)

- **set_pixel**\(*campaign_id, pixel_html*)

- **set_postback_url**\(*campaign_id, postback_url*)

- **set_test_link**\(*campaign_id, test_link*)

**REPORTS**

- **bills**\(*start_at_row='0', row_limit='0'*)

- **campaign_summary**\(*start_date, end_date, sub_affiliate='', event_type='all', start_at_row='0', row_limit='0', sort_field='site_offer_id', sort_descending='FALSE'*)

- **clicks**\(*start_date, end_date, offer_id='0', campaign_id='0', include_duplicates='FALSE', start_at_row='0', row_limit='0'*)

- **daily_summary**\(*start_date, end_date, site_offer_id='0'*)

- **events_conversions**\(*start_date, end_date, currency_id, site_offer_id='0', disposition_type='', event_type='all', exclude_bot_traffic='FALSE', start_at_row='0', row_limit='0'*)

- **hourly_summary**\(*start_date, end_date, site_offer_id='0'*)

- **network_news**\(*row_limit='0'*)

- **offer_compliance**\(*start_at_row='0', row_limit='0'*)

- **order_detail_changes**\(*changes_since, include_new_conversions='FALSE', start_at_row='0', row_limit='0', sort_field='conversion_id', sort_descending='FALSE'*)

- **order_details**\(*start_date, end_date, conversion_id='0', order_id='', start_at_row='0', row_limit='0', sort_field='conversion_id', sort_descending='FALSE'*)

- **performance_summary**\(*date*)

- **referral**\(*start_date, end_date, over_minimum, start_at_row='0', row_limit='0', sort_field='affiliate_id', sort_descending='FALSE'*)

- **sub_affiliate_summary**\(*start_date, end_date, site_offer_id='0', start_at_row='0', row_limit='0'*)

- **top_offer_summary**\(*start_date, end_date, vertical_id='0', start_at_row='0', row_limit='0'*)

BuyerAPI Functions
------------------
- **get_return_reasons**\()
- **return_lead**\(*lead_id, return_reason_id, buyer_contract_id='0'*)
- **update_lead**\(*lead_id, buyer_contract_id='0', status='', sub_status='', amount='0', add_to_existing='TRUE', field_name='', field_value='', return_reason_id='0'*)


pycake.models Module
====================
pycake.models includes the following models:

- BrandAdvertiser
    - Initiate with a brand/advertiser record returned via ``pycake.api.AdminAPI.export_advertisers()``

- Campaign
    - Initiate with a campaign record returned via ``pycake.api.AdminAPI.export_campaigns()``

- Click
    - Initiate with a click record returned via ``pycake.api.AdminAPI.clicks()``

- EventConversion
    - Initiate with an event_conversion record returned via ``pycake.api.AdminAPI.events_conversions()``

- SiteOffer
    - Initiate with a site/offer record returned via ``pycake.api.AdminAPI.export_offers()``

- SourceAffiliate
    - Initiate with a source/affiliate record returned via ``pycake.api.AdminAPI.export_affiliates()``

Found a bug or not seeing a function you need? `Let me know!`_
                                                .. _Let me know!: https://github.com/heytimj/pycake/issues