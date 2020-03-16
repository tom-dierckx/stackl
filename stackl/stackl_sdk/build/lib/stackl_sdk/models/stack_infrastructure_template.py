# coding: utf-8

"""
    FastAPI

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class StackInfrastructureTemplate(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'description': 'str',
        'infrastructure_targets': 'list[InfrastructureTarget]',
        'infrastructure_capabilities': 'dict(str, object)',
        'type': 'str',
        'category': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'infrastructure_targets': 'infrastructure_targets',
        'infrastructure_capabilities': 'infrastructure_capabilities',
        'type': 'type',
        'category': 'category'
    }

    def __init__(self, name=None, description='', infrastructure_targets=None, infrastructure_capabilities=None, type='stack_infrastructure_template', category='configs'):  # noqa: E501
        """StackInfrastructureTemplate - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._infrastructure_targets = None
        self._infrastructure_capabilities = None
        self._type = None
        self._category = None
        self.discriminator = None
        self.name = name
        if description is not None:
            self.description = description
        self.infrastructure_targets = infrastructure_targets
        if infrastructure_capabilities is not None:
            self.infrastructure_capabilities = infrastructure_capabilities
        if type is not None:
            self.type = type
        if category is not None:
            self.category = category

    @property
    def name(self):
        """Gets the name of this StackInfrastructureTemplate.  # noqa: E501


        :return: The name of this StackInfrastructureTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StackInfrastructureTemplate.


        :param name: The name of this StackInfrastructureTemplate.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this StackInfrastructureTemplate.  # noqa: E501


        :return: The description of this StackInfrastructureTemplate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StackInfrastructureTemplate.


        :param description: The description of this StackInfrastructureTemplate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def infrastructure_targets(self):
        """Gets the infrastructure_targets of this StackInfrastructureTemplate.  # noqa: E501


        :return: The infrastructure_targets of this StackInfrastructureTemplate.  # noqa: E501
        :rtype: list[InfrastructureTarget]
        """
        return self._infrastructure_targets

    @infrastructure_targets.setter
    def infrastructure_targets(self, infrastructure_targets):
        """Sets the infrastructure_targets of this StackInfrastructureTemplate.


        :param infrastructure_targets: The infrastructure_targets of this StackInfrastructureTemplate.  # noqa: E501
        :type: list[InfrastructureTarget]
        """
        if infrastructure_targets is None:
            raise ValueError("Invalid value for `infrastructure_targets`, must not be `None`")  # noqa: E501

        self._infrastructure_targets = infrastructure_targets

    @property
    def infrastructure_capabilities(self):
        """Gets the infrastructure_capabilities of this StackInfrastructureTemplate.  # noqa: E501


        :return: The infrastructure_capabilities of this StackInfrastructureTemplate.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._infrastructure_capabilities

    @infrastructure_capabilities.setter
    def infrastructure_capabilities(self, infrastructure_capabilities):
        """Sets the infrastructure_capabilities of this StackInfrastructureTemplate.


        :param infrastructure_capabilities: The infrastructure_capabilities of this StackInfrastructureTemplate.  # noqa: E501
        :type: dict(str, object)
        """

        self._infrastructure_capabilities = infrastructure_capabilities

    @property
    def type(self):
        """Gets the type of this StackInfrastructureTemplate.  # noqa: E501


        :return: The type of this StackInfrastructureTemplate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StackInfrastructureTemplate.


        :param type: The type of this StackInfrastructureTemplate.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def category(self):
        """Gets the category of this StackInfrastructureTemplate.  # noqa: E501


        :return: The category of this StackInfrastructureTemplate.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this StackInfrastructureTemplate.


        :param category: The category of this StackInfrastructureTemplate.  # noqa: E501
        :type: str
        """

        self._category = category

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(StackInfrastructureTemplate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StackInfrastructureTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other