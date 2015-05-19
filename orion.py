# -*- coding: utf-8 -*-
import requests
import logging

log = logging.getLogger(__name__)


class OrionClient(object):
    """Client interface for the orion context broker"""

    def __init__(self, host, port, service=''):
        self.url = "http://{0}:{1}".format(host, port)
        self.headers = {'content-type': "application/json",
                        'accept': "application/json"}
        if service:
            self.headers['Fiware-Service'] = service

    def build_attribute(self, instance):
        """Build a json from an instance

        Instance must have name, type and value attributes
        """
        attribute = {'name': instance.name,
                     'type': instance.type,
                     'value': instance.value}
        return attribute

    def append(self, entity_type, id, attribute):
        """Append an attribute/measure to a contextentity
        """
        update_url = self.url + "/v1/updateContext"
        if not isinstance(attribute, dict):
            attribute = self.build_attribute(attribute)
        data = {
            "contextElements": [
                {
                    "type": entity_type,
                    "isPattern": False,
                    "id": id,
                    "attributes": [attribute]
                }
            ],
            "updateAction": "APPEND"
        }
        response = requests.post(update_url, headers=self.headers, json=data)
        return response.json()
