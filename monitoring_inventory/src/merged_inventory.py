import sys

import pandas as pd
import os
from Mapping_Entities.EntitySchemaMapper import EntitySchemaMapper

BASE_PATH = r"../data"

# Read CSVs
org_df = pd.read_csv(os.path.join(BASE_PATH, "Organization", "organization.csv"))
assets_df = pd.read_csv(os.path.join(BASE_PATH, "Asset", "assets.csv"))
dev_class_df = pd.read_csv(os.path.join(BASE_PATH, "Device_Class", "device_class.csv"))
device_df = pd.read_csv(os.path.join(BASE_PATH, "Device", "devices.csv"))
interface_df = pd.read_csv(os.path.join(BASE_PATH, "Interface", "interfaces.csv"))
events_df = pd.read_csv(os.path.join(BASE_PATH, "Event", "events.csv"))

# Apply entity-based column renaming
org_df = EntitySchemaMapper.rename_columns(org_df, "organization")
assets_df = EntitySchemaMapper.rename_columns(assets_df, "asset")
dev_class_df = EntitySchemaMapper.rename_columns(dev_class_df, "device_class")
device_df = EntitySchemaMapper.rename_columns(device_df, "device")
interface_df = EntitySchemaMapper.rename_columns(interface_df, "interface")
events_df = EntitySchemaMapper.rename_columns(events_df, "event")


# Merge
assets_merged = assets_df.merge(org_df, on="organization_id")
device_merged = device_df.merge(assets_merged, on="asset_id") \
                         .merge(dev_class_df, on="device_class_id")
interface_merged = interface_df.merge(device_merged, on="device_id")
events_merged = events_df.merge(interface_merged, on="interface_id")
events_merged = events_merged.rename(columns={
    "device_id_x": "device_id",
    "device_id_y": "device_id_device",  # if needed
    # similarly for others if you want
})

# For example, drop device_id_device if not needed
events_merged = events_merged.drop(columns=["device_id_device"])

# Inspect final column names
print("Final merged columns:\n", events_merged.columns.tolist())

# Cleaned final selection (use only columns you are sure exist)
final_df = events_merged[[
    "event_id",
    "event_timestamp",
    "device_id",          # no device_id_x, use this instead
    "interface_id",
    "event_type",
    "event_description",
    "interface_name",
    "interface_mac",
    "interface_status",
    "asset_id",
    "device_class_id",
    "device_ip",
    "device_serial",
    "device_manufacturer",
    "asset_name",
    "organization_id",
    "asset_location",
    "asset_purchase_date",
    "asset_owner",
    "org_name",
    "org_industry",
    "org_address",
    "org_email",
    "org_phone",
    "device_class_name",
    "device_class_description"
]]



# Save
os.makedirs("../data/monitoring_inventory", exist_ok=True)
final_df.to_csv("../data/monitoring_inventory/merged_output.csv", index=False)

print("\n✅ Merged data saved to monitoring_inventory/merged_output.csv")
