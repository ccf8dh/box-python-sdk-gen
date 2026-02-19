from enum import Enum

from box_sdk_gen.internal.base_object import BaseObject

from box_sdk_gen.box.errors import BoxSDKError


class IntegrationMappingPartnerItemOneDriveCreateRequestTypeField(str, Enum):
    FOLDER = 'folder'
    DRIVE = 'drive'


class IntegrationMappingPartnerItemOneDriveCreateRequest(BaseObject):
    _discriminator = 'type', {'folder', 'drive'}

    def __init__(
        self,
        type: IntegrationMappingPartnerItemOneDriveCreateRequestTypeField,
        id: str,
        tenant_id: str,
        **kwargs
    ):
        """
        :param type: Type of the mapped item referenced in `id`
        :type type: IntegrationMappingPartnerItemOneDriveCreateRequestTypeField
        :param id: ID of the mapped item (of type referenced in `type`)
        :type id: str
        :param tenant_id: ID of the tenant that is registered with Microsoft OneDrive.
        :type tenant_id: str
        """
        super().__init__(**kwargs)
        self.type = type
        self.id = id
        self.tenant_id = tenant_id
