from box_sdk_gen.internal.base_object import BaseObject

from box_sdk_gen.schemas.integration_mapping_partner_item_onedrive_create_request import (
    IntegrationMappingPartnerItemOneDriveCreateRequest,
)

from box_sdk_gen.schemas.folder_reference import FolderReference

from box_sdk_gen.box.errors import BoxSDKError


class IntegrationMappingOneDriveCreateRequest(BaseObject):
    def __init__(
        self,
        partner_item: IntegrationMappingPartnerItemOneDriveCreateRequest,
        box_item: FolderReference,
        **kwargs
    ):
        """
        :param partner_item: Mapped item object for OneDrive
        :type partner_item: IntegrationMappingPartnerItemOneDriveCreateRequest
        :param box_item: The Box folder to which the OneDrive object should be mapped.
        :type box_item: FolderReference
        """
        super().__init__(**kwargs)
        self.partner_item = partner_item
        self.box_item = box_item
