from typing import Optional

from typing import List

from box_sdk_gen.internal.base_object import BaseObject

from box_sdk_gen.schemas.integration_mapping_onedrive import IntegrationMappingOneDrive

from box_sdk_gen.box.errors import BoxSDKError


class IntegrationMappingsOneDrive(BaseObject):
    def __init__(
        self, *, entries: Optional[List[IntegrationMappingOneDrive]] = None, **kwargs
    ):
        """
        :param entries: A list of integration mappings, defaults to None
        :type entries: Optional[List[IntegrationMappingOneDrive]], optional
        """
        super().__init__(**kwargs)
        self.entries = entries
