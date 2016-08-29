# coding: utf-8

from django.db import connections
import requests
import sqlparse


class ExplainResult(object):

    def __init__(self, sql, explain):
        self.sql = sql
        self.explain = explain

    def pretty_print(self):
        sql = sqlparse.format(self.sql, reindent=True, keyword_case='upper')
        print(sql)
        print(self.explain)

    def get_depesz_url(self):
        payload = {"title": "default", "plan": self.explain}
        url = "https://explain.depesz.com"
        response = requests.post(url=url, data=payload)
        response.raise_for_status()
        return url + response.headers.get("Location")


def explain(query, analyze=True):
    connection = connections[query.db]
    with connection.cursor() as c:
        sql, params = query.query.sql_with_params()
        tmpl = "EXPLAIN {sql}"
        if analyze:
            tmpl = "EXPLAIN ANALYZE {sql}"
        c.execute(tmpl.format(sql=sql), params)
        explain_data = "\n".join([i[0] for i in c.fetchall()])
        return ExplainResult(sql=str(query.query), explain=explain_data)
