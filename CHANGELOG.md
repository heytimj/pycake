# pycake Changelog

### v1.7.0
- September 25, 2016
- Added `CAKEApi.country_summary()` and `CAKEApi.lite_clicks_country_summary()`
- Added CHANGELOG.md
- Updated README.rst

### v1.6.1
- August 23, 2017
- Bug Fixes:
    - `CAKEApi.export_campaigns()` now requires at least one of the following arguments: `affiliate_id`, `offer_id`, `campaign_id`. This matches requirements in the underlying API.

### v1.6.0
- August 22, 2017
- Added `CAKEApi.affiliate_offer_feed()`

### v1.5.0
- August 22, 2017
- Added `CAKEApi.conversion_changes()`

### v1.4.0
- August 18, 2017
- Added `CAKEApi.export_offers()`

### v1.3.0
- July 27, 2017
- Updated version of underlying API call for `CAKEApi.conversions()`

### v1.2.1
- July 26, 2017
- Bug Fixes:
    - Resolved error caused by passing date/datetime objects as `start_date` and `end_date` arguments

### v1.2.0
- July 26, 2017
- Renamed `CAKEApi.daily_summary_export()` to `CAKEApi.daily_summary()`
- Added `CAKEApi.lite_clicks_daily_summary()`

### v1.1.0
- July 24, 2017
- Updated version of underlying API call for `CAKEApi.conversions()` and `CAKEApi.clicks()`

### v1.0.0
- July 14, 2017
- Initial release