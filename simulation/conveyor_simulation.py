# PLC Conveyor System Simulation

import time

def conveyor_system():

    print("Factory conveyor system started")

    while True:

        product_detected = input("Product detected? (y/n): ")

        if product_detected == "y":

            print("Sensor detected product")
            print("Conveyor motor running")

            time.sleep(2)

            inspection = input("Is product OK? (y/n): ")

            if inspection == "y":
                print("Product passed inspection → continues on conveyor")

            else:
                print("Defective product detected")
                print("Sorting actuator activated → product removed")

        else:
            print("No product on conveyor")

        print("----------------------------------")

conveyor_system()
