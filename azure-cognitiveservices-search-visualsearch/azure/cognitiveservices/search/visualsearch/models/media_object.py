# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .creative_work import CreativeWork


class MediaObject(CreativeWork):
    """Defines a media object.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: ImageObject

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar read_link: The URL that returns this resource. To use the URL,
     append query parameters as appropriate and include the
     Ocp-Apim-Subscription-Key header.
    :vartype read_link: str
    :ivar web_search_url: The URL to Bing's search result for this item.
    :vartype web_search_url: str
    :ivar name: The name of the thing represented by this object.
    :vartype name: str
    :ivar url: The URL to get more information about the thing represented by
     this object.
    :vartype url: str
    :ivar image: An image of the item.
    :vartype image:
     ~azure.cognitiveservices.search.visualsearch.models.ImageObject
    :ivar description: A short description of the item.
    :vartype description: str
    :ivar alternate_name: An alias for the item.
    :vartype alternate_name: str
    :ivar bing_id: An ID that uniquely identifies this item.
    :vartype bing_id: str
    :ivar thumbnail_url: The URL to a thumbnail of the item.
    :vartype thumbnail_url: str
    :ivar provider: The source of the creative work.
    :vartype provider:
     list[~azure.cognitiveservices.search.visualsearch.models.Thing]
    :ivar date_published: The date on which the CreativeWork was published.
    :vartype date_published: str
    :ivar text: Text content of this creative work.
    :vartype text: str
    :ivar content_url: Original URL to retrieve the source (file) for the
     media object (e.g., the source URL for the image).
    :vartype content_url: str
    :ivar host_page_url: URL of the page that hosts the media object.
    :vartype host_page_url: str
    :ivar content_size: Size of the media object content. Use format "value
     unit" (e.g., "1024 B").
    :vartype content_size: str
    :ivar encoding_format: Encoding format (e.g., png, gif, jpeg, etc).
    :vartype encoding_format: str
    :ivar host_page_display_url: Display URL of the page that hosts the media
     object.
    :vartype host_page_display_url: str
    :ivar width: The width of the media object, in pixels.
    :vartype width: int
    :ivar height: The height of the media object, in pixels.
    :vartype height: int
    """

    _validation = {
        '_type': {'required': True},
        'id': {'readonly': True},
        'read_link': {'readonly': True},
        'web_search_url': {'readonly': True},
        'name': {'readonly': True},
        'url': {'readonly': True},
        'image': {'readonly': True},
        'description': {'readonly': True},
        'alternate_name': {'readonly': True},
        'bing_id': {'readonly': True},
        'thumbnail_url': {'readonly': True},
        'provider': {'readonly': True},
        'date_published': {'readonly': True},
        'text': {'readonly': True},
        'content_url': {'readonly': True},
        'host_page_url': {'readonly': True},
        'content_size': {'readonly': True},
        'encoding_format': {'readonly': True},
        'host_page_display_url': {'readonly': True},
        'width': {'readonly': True},
        'height': {'readonly': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'read_link': {'key': 'readLink', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'image': {'key': 'image', 'type': 'ImageObject'},
        'description': {'key': 'description', 'type': 'str'},
        'alternate_name': {'key': 'alternateName', 'type': 'str'},
        'bing_id': {'key': 'bingId', 'type': 'str'},
        'thumbnail_url': {'key': 'thumbnailUrl', 'type': 'str'},
        'provider': {'key': 'provider', 'type': '[Thing]'},
        'date_published': {'key': 'datePublished', 'type': 'str'},
        'text': {'key': 'text', 'type': 'str'},
        'content_url': {'key': 'contentUrl', 'type': 'str'},
        'host_page_url': {'key': 'hostPageUrl', 'type': 'str'},
        'content_size': {'key': 'contentSize', 'type': 'str'},
        'encoding_format': {'key': 'encodingFormat', 'type': 'str'},
        'host_page_display_url': {'key': 'hostPageDisplayUrl', 'type': 'str'},
        'width': {'key': 'width', 'type': 'int'},
        'height': {'key': 'height', 'type': 'int'},
    }

    _subtype_map = {
        '_type': {'ImageObject': 'ImageObject'}
    }

    def __init__(self, **kwargs):
        super(MediaObject, self).__init__(**kwargs)
        self.content_url = None
        self.host_page_url = None
        self.content_size = None
        self.encoding_format = None
        self.host_page_display_url = None
        self.width = None
        self.height = None
        self._type = 'MediaObject'
