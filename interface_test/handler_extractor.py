#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2023/11/28 12:48
# @Author: 白云苍狗
# @File: handler_extractor.py
# @Software: PyCharm

from requests import Response
import jsonpath
import jmespath
import re
from interface_test.handler_requests import handler


class ResponseExtractor:
    """
    A class to extract various elements from a Response object.
    """

    def __init__(self, response: Response):
        self.response = response
        self.response_body = self._get_response_body()

    import logging

    def _get_response_body(self):
        try:
            return self.response.json()
        except ValueError as e:
            print(f"Error parsing JSON from response: {e}")
            return {}

    def extract(self, extract_expression: str):
        """
        Extracts value from the response based on the provided expression.
        """
        if not isinstance(extract_expression, str):
            return extract_expression

        if extract_expression in ["status_code", "url", "ok", "encoding"]:
            return getattr(self.response, extract_expression)

        if extract_expression.startswith(('body', 'content', '$.')):
            return self._extract_with_jmespath_or_jsonpath(extract_expression)

        if '.+?' in extract_expression or '.*?' in extract_expression:
            return self._extract_with_regex(extract_expression)

        return extract_expression

    def _extract_with_jmespath_or_jsonpath(self, expression):
        try:
            if expression.startswith('$.'):
                return jsonpath.jsonpath(self.response_body, expression)
            return jmespath.search(expression, {"body": self.response_body})
        except Exception as e:
            raise ValueError(f'Invalid expression: {expression}') from e

    def _extract_with_regex(self, expression):
        matches = re.findall(expression, self.response.text, flags=re.S)
        if not matches:
            print(f'Invalid expression: {expression}')
            return []
        # return matches[0] if len(matches) == 1 else matches
        return matches


if __name__ == '__main__':
    _base_url = 'https://httpbin.org'
    # Example JSON-like string
    json_string = {"url": "/post", "method": "post", "data": {"name": "panpan"}, "files": {"file": "foo.png"}}
    _response = handler.handle_request(json_string, _base_url)

    extractor = ResponseExtractor(_response)
    # jsonpath_expr = '$.files.file'
    # value = extractor.extract(jsonpath_expr)

    regex_expr = r'"file":\s*"(.*?)"'
    value = extractor.extract(regex_expr)
    print(value)
