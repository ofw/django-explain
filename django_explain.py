# coding: utf-8

from django.db import connections
from termcolor import colored


class ExplainResult(object):

    def __init__(self, query, explain):
        self.query = query
        self.explain = explain

    def pretty_print(self):
        print(colored("QUERY", "green"))
        print(self.query)
        print()
        print(colored("RESULT", "green"))
        print(self.explain)


def explain(query, analyze=True):
    connection = connections[query.db]
    with connection.cursor() as c:
        sql, params = query.query.sql_with_params()
        tmpl = "EXPLAIN {sql}"
        if analyze:
            tmpl = "EXPLAIN ANALYZE {sql}"
        c.execute(tmpl.format(sql=sql), params)
        explain_data = "\n".join([i[0] for i in c.fetchall()])
        return ExplainResult(query=str(query.query), explain=explain_data)
