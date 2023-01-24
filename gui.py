import simplepyble
import binascii
import asyncio


async def content():
    i = 0
    for contents in service_characteristic_pair:
        try:
            print(f"{i}:")
            r_content = peripheral.read(contents[0], contents[1])

            print(f"Original contents: {r_content}")
            print(f"Binary/Ascii contents: {binascii.b2a_hex(r_content, b' ', -2)}")
            if contents[2]:
                print(peripheral.descriptor_read(contents[0], contents[1], contents[2]))
            print("\n")
        except:
            print("Error")
            print('\n')
        i += 1
async def notify_me(pair):
    service_uuid, characteristic_uuid = pair[3]
    await peripheral.notify(service_uuid, characteristic_uuid, lambda data: print(f"Notification: {data}"))

if __name__ == "__main__":
    adapters = simplepyble.Adapter.get_adapters()

    if len(adapters) == 0:
        print("No adapters found")

    # Query the user to pick an adapter
    print("Please select an adapter:")
    for i, adapter in enumerate(adapters):
        print(f"{i}: {adapter.identifier()} [{adapter.address()}]")

    #choice = int(input("Enter choice: "))
    adapter = adapters[0]

    print(f"Selected adapter: {adapter.identifier()} [{adapter.address()}]")

    adapter.set_callback_on_scan_start(lambda: print("Scan started."))
    adapter.set_callback_on_scan_stop(lambda: print("Scan complete."))
    adapter.set_callback_on_scan_found(lambda peripheral: print(f"Found {peripheral.identifier()} [{peripheral.address()}]"))

    # Scan for 5 seconds
    adapter.scan_for(5000)
    peripherals = adapter.scan_get_results()

    # Query the user to pick a peripheral
    print("Please select a peripheral:")
    for i, peripheral in enumerate(peripherals):
        print(f"{i}: {peripheral.identifier()} [{peripheral.address()}]")
    for peripheral in peripherals:
        if peripheral.identifier() == "Kanye Sweep":
            print(f"Connecting to: {peripheral.identifier()} [{peripheral.address()}]")
            peripheral.connect()
            print(peripheral.identifier())


        else:
            print(f"Peripheral Kanye Sweep not found.")

    #choice = int(input("Enter choice: "))
    #peripheral = peripherals[choice]

    #print(f"Connecting to: {peripheral.identifier()} [{peripheral.address()}]")
    #peripheral.connect()

    print("Successfully connected, listing services...")
    services = peripheral.services()
    service_characteristic_pair = []
    for service in services:
        for characteristic in service.characteristics():
            service_characteristic_pair.append((service.uuid(), characteristic.uuid(), characteristic.descriptors()))

    # Query the user to pick a service/characteristic pair
    print("Please select a service/characteristic pair:")
    for i, (service_uuid, characteristic, descriptor) in enumerate(service_characteristic_pair):
        print(f"{i}: {service_uuid} {characteristic} {descriptor}")

    #choice = int(input("Enter choice: "))
    #service_uuid, characteristic_uuid, characteristic_descriptors = service_characteristic_pair[choice]

    # Write the content to the characteristic
    #contents = peripheral.read(service_uuid, characteristic_uuid)
    #print(f"Original contents: {contents}")
    asyncio.run(content())
    #asyncio.run(notify_me(service_characteristic_pair))
    peripheral.disconnect()