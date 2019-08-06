"""
This File contains constants for this API services
"""


class ORDER_BY:
    ASCENDING_ORDER = "asc"
    DESCENDING_ORDER = "desc"


class APIConstants:
    AVAILABLE_FILTERS = set(["date_from", "date_to", "channel", "country", "os"])
    AVAILABLE_GROUP_BY = set(["date", "channel", "country", "os"])
    AVAILABLE_ORDERS = set([ORDER_BY.ASCENDING_ORDER, ORDER_BY.DESCENDING_ORDER])
    SORT_FIELDS = set(["date", "country", "impressions", "channel", "os", "clicks", "installs", "spend", "revenue", "cpi"])
    DEFAULT_SORT_BY = "channel"