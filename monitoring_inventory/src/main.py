'''
monitoring_inventory/
└── data/
    ├── Organization/
    │   └── Organization.csv
    ├── Assets/
    │   └── Assets.csv
    ├── Device_Class/
    │   └── Device_Class.csv
    ├── Device/
    │   └── Device.csv
    ├── Interface/
    │   └── Interface.csv
    └── Events/
        └── Events.csv

'''
# main.py
from Organization.generate_organization import generate_organization
from Device_Class.generate_device_class import generate_device_class
from Asset.generate_asset import generate_assets
from Device.generate_device import generate_devices
from Interface.generate_interface import generate_interfaces
from Event.generate_event import generate_events

def main():
    orgs = generate_organization(num=100)
    dev_classes = generate_device_class(num=50)
    assets = generate_assets(orgs, num=200)
    devices = generate_devices(assets, dev_classes, num=10000)
    interfaces = generate_interfaces(devices, interfaces_per_device=10)
    generate_events(devices, interfaces, num=100000)

if __name__ == "__main__":
    main()
