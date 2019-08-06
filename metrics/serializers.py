
from .models import Metric


class MetricSerializer():
    """
        Customized MetricSerializer for Metric Data Model
    """
    sum_fields = set(['impressions__sum', 'clicks__sum',
                      'installs__sum', 'spend__sum', 'revenue__sum'])

    def adapt(self, metric):
        if isinstance(metric, Metric):
            return {
                "date": metric.date,
                "channel": metric.channel,
                "country": metric.country,
                "os": metric.os,
                "impressions": metric.impressions,
                "clicks": metric.clicks,
                "installs": metric.installs,
                "spend": metric.spend,
                "revenue": metric.revenue,
                "cpi": metric.cpi
            }
        else:
            result = {}
            for key, value in metric.items():
                if key not in self.sum_fields:
                    result[key] = value
                else:
                    result[key.replace("__sum", "")] = value
            return result

    def adapt_list(self, metrics):
        return [self.adapt(metric) for metric in metrics]
