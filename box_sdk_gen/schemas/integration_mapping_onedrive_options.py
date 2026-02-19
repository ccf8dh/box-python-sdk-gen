from typing import Optional

from box_sdk_gen.internal.base_object import BaseObject

from box_sdk_gen.box.errors import BoxSDKError


class IntegrationMappingOneDriveOptions(BaseObject):
    def __init__(
        self, *, is_access_management_disabled: Optional[bool] = None, **kwargs
    ):
        """
        :param is_access_management_disabled: Indicates whether or not user
        access to the underlying box item
        should be automatically managed.
        Access is managed through creating collaborations or shared links., defaults to None
        :type is_access_management_disabled: Optional[bool], optional
        """
        super().__init__(**kwargs)
        self.is_access_management_disabled = is_access_management_disabled
