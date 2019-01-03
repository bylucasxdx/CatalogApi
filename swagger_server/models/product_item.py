# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ProductItem(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, name: str=None):  # noqa: E501
        """ProductItem - a model defined in Swagger

        :param id: The id of this ProductItem.  # noqa: E501
        :type id: str
        :param name: The name of this ProductItem.  # noqa: E501
        :type name: str
        """
        self.swagger_types = {
            'id': str,
            'name': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name'
        }

        self._id = id
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'ProductItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ProductItem of this ProductItem.  # noqa: E501
        :rtype: ProductItem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this ProductItem.


        :return: The id of this ProductItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this ProductItem.


        :param id: The id of this ProductItem.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this ProductItem.


        :return: The name of this ProductItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ProductItem.


        :param name: The name of this ProductItem.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name