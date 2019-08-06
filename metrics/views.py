
from django.core.exceptions import SuspiciousOperation
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Metric
from .serializers import MetricSerializer
from .constants import APIConstants, ORDER_BY


class ListMetrics(APIView):
    """
    List all metrics
    possible request args:
    1. Filter:
        * date_from, date_to - YYYY-MM-DD Format
        * channel - eg: channel=adcolony,apple_search_ads
        * country - eg: country=US,DE
        * os - eg:os=android, ios
    2. Group by: Multiple fields
        * date,channel, country,os
    3. sort_by: Single Field
        * date, country, impressions, channel, os,
          clicks, installs, spend, revenue, cpi - eg: sort_by=date
    4. sort_order : desc/asc
        * desc for descending order
        * asc for ascending order
    """
    def get(self, request, format=None):
        """
        This function returns API Response for GET call to
        /performance_metrics API call
        """
        filters, group_by, sort_by = self.__get_filters_groupby_sortby(
            request.query_params)
        metrics = Metric().get(filters, group_by, sort_by)
        response = MetricSerializer().adapt_list(metrics)
        return Response(response)

    def __get_filters_groupby_sortby(self, params):
        """
        This function formats filters, group_by and
        sort_by fields to be used in DAL Layer
        (data abstraction layer) from request arguments
        """
        filters = {}
        args = params.copy()
        group_by = []
        sort_by = []
        sort_order = ''
        if 'group_by' in args:
            group_by_values = args["group_by"].split(",")
            for each in group_by_values:
                if each not in APIConstants.AVAILABLE_GROUP_BY:
                    raise SuspiciousOperation("Invalid group_by:{}".format(each))
                group_by.append(each)
            args.pop('group_by')
        if 'sort_order' in args:
            if args['sort_order'] not in APIConstants.AVAILABLE_ORDERS:
                raise SuspiciousOperation("Invalid sort_order:{}".format(each))
            else:
                sort_order = '' if params['sort_order'] == ORDER_BY.ASCENDING_ORDER else '-'
            args.pop('sort_order')
        if 'sort_by' in args:
            if args['sort_by'] not in APIConstants.SORT_FIELDS:
                raise SuspiciousOperation("Invalid sort_by:{}".format(each))
            sort_by.append("{}{}".format(sort_order, args.pop('sort_by')[0]))
        else:
            sort_by.append(APIConstants.DEFAULT_SORT_BY)
        if args:
            for each, value in args.items():
                if each not in APIConstants.AVAILABLE_FILTERS:
                    raise SuspiciousOperation("Invalid argument:{}".format(each))
                if each == "date_from":
                    filters["date__gte"] = value
                elif each == "date_to":
                    filters["date__lte"] = value
                else:
                    filter_list = args[each].split(",")
                    filters["{}__in".format(each)] = filter_list
        return filters, group_by, sort_by
