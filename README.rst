Introduction
------------
**pycake** is a python wrapper intended to make CAKE's API seem more RESTful. For example, if you want to edit one setting on one offer, you can use the ``edit_offer()`` method and only pass the ``offer_id`` and the key-value pair for the setting you wish to change. Example: ``edit_offer(offer_id=4, click_cookie_days=60)``. In short, if settings or filters are not explicitly set when calling a method, they are automatically skipped or all results returned (depending on the method type). 

Python
------
Supports 2.x and 3.x

Use
---

**Installation**

.. code:: bash

    $ pip install pycake --upgrade
    
**Initialize a CAKEApi object with an API key**

.. code:: python

    >>> from pycake.api import CAKEApi
    >>> ckapi = CAKEApi(
            admin_domain='some.domain', api_key='sfhgjhGjhgJHg',
            secure=False, json_response=True)
    >>> advertiser_info = ckapi.get(item='Advertisers')
    >>> offer_info = ckapi.export_offers()
   
*Note:* Only ``admin_domain`` is required to initialize a CAKEApi object.

**Initialize a CAKEApi Object without an API key**

You can initialize a CAKEApi object without an API key and then use the ``set_api_key()`` method. This is useful when you need to utilize user-provided login credentials to perform API calls. 

.. code:: python
    
    >>> from pycake.api import CAKEApi
    >>> admin_domain = 'some.domain'
    >>> ckapi = CAKEApi(admin_domain=admin_domain)
    >>> username = 'email@domain.com'
    >>> password = 'SomePassword123'
    >>> ckapi.set_api_key(username=username, password=password)
    >>> print ckapi.api_key
    gjhfgGJhgjhGgfHGjhg

*Note:* If the ``username`` and ``password`` are not valid admin credentials the object's ``api_key`` attribute will be set as
``None``. Calling subsequent object methods other than ``set_api_key()``
will raise an error.

Supported Methods
-----------------

**API KEY**

- ``set_api_key()``

**ACCOUNTING** 

- ``export_advertiser_bills()``
- ``export_affiliate_bills()``

**ADDEDIT** 

- ``add_advertiser()``
- ``add_affiliate()``
- ``add_blacklist()``
- ``add_buyer()``
- ``add_buyer_contract()``
- ``add_campaign()``
- ``add_creative_files()``
- ``add_offer()``
- ``edit_advertiser()``
- ``edit_affiliate()``
- ``edit_buyer()``
- ``edit_buyer_contract()``
- ``edit_campaign()``
- ``edit_creative_files()``
- ``edit_offer()``
- ``remove_blacklist()``

**EXPORT**

- ``export_advertisers()``
- ``export_affiliates()``
- ``export_blacklists()``
- ``export_buyer_contracts()``
- ``export_buyers()``
- ``export_campaigns()``
- ``export_creatives()``
- ``export_pixel_log_requests()``
- ``export_rule_targets()``
- ``export_schedules()``

**GET**

- ``get(item)``
 
**REPORTS**
 
- ``brand_advertiser_summary()``
- ``campaign_summary()``
- ``clicks()``
- ``conversions()``
- ``creative_summary()``
- ``daily_summary_export()``
- ``leads_by_buyer()``
- ``leads_by_affiliate()``
- ``lite_clicks_advertiser_summary()``
- ``lite_clicks_affiliate_summary()``
- ``lite_clicks_campaign_summary()``
- ``lite_clicks_offer_summary()``
- ``lite_clicks_sub_id_summary()``
- ``login_export()``
- ``order_details()``
- ``site_offer_summary()``
- ``source_affiliate_summary()``
- ``sub_id_summary()``
- ``traffic_export()``

**TRACK**

- ``update_conversion()``