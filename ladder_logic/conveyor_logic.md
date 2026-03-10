# PLC Conveyor Sorting Logic

## System Inputs

I0.0 → Start Button  
I0.1 → Product Detection Sensor  
I0.2 → Inspection Sensor  

## System Outputs

Q0.0 → Conveyor Motor  
Q0.1 → Sorting Actuator  

## Control Logic

1. When Start Button is pressed, conveyor motor starts.

2. When Product Detection Sensor detects a product, conveyor moves the product forward.

3. When product reaches Inspection Sensor:

- If product is OK → conveyor continues.
- If product is defective → sorting actuator pushes product off conveyor.

## Purpose

This PLC logic simulates an industrial conveyor sorting system used in automated factories.
