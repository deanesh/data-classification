import pandas as pd
class EntitySchemaMapper:
    MAPPINGS = {
        "organization": {
            "organization_id": "organization_id",
            "name": "org_name",
            "address": "org_address",
            "contact_email": "org_email",
            "contact_phone": "org_phone",
            "industry": "org_industry"
        },
        "asset": {
            "asset_id": "asset_id",
            "name": "asset_name",
            "location": "asset_location",
            "purchase_date": "asset_purchase_date",
            "owner": "asset_owner",
            "organization_id": "organization_id"
        },
        "device": {
            "device_id": "device_id",
            "ip_address": "device_ip",
            "serial_number": "device_serial",
            "manufacturer": "device_manufacturer",
            "asset_id": "asset_id",
            "device_class_id": "device_class_id"
        },
        "interface": {
            "interface_id": "interface_id",
            "name": "interface_name",
            "mac_address": "interface_mac",
            "status": "interface_status",
            "device_id": "device_id"
        },
        "device_class": {
            "device_class_id": "device_class_id",
            "name": "device_class_name",
            "description": "device_class_description"
        },
        "event": {
            "event_id": "event_id",
            "timestamp": "event_timestamp",
            "event_type": "event_type",
            "description": "event_description",
            "device_id": "device_id",
            "interface_id": "interface_id"
        }
    }

    @classmethod
    def rename_columns(cls, df: pd.DataFrame, entity: str) -> pd.DataFrame:
        return df.rename(columns=cls.MAPPINGS.get(entity, {}))
