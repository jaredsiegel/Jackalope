"""Functions for interacting with Slack's APIs."""
from flask import current_app
import requests


def send_notification(url, message):
    """Send a formatted Slack message to a channel's inbound webhook.
    
    :param str url: The URL for a Slack channel's inbound webhook.
    :param dict message: A formatted Slack message generated by
        :func:`jackalope.routes.jamfpro.webhooks._message`.
    """
    headers = {'Content-Type': 'application/json'}

    resp = requests.post(url, headers=headers, json=message)

    current_app.logger.debug(
        'Slack notification response code: {}'.format(resp.status_code))
    current_app.logger.debug(
        'Slack notification response message: {}'.format(resp.text))
