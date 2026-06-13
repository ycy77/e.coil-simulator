---
entity_id: "complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX"
entity_type: "complex"
name: "flagellar basal body"
source_database: "EcoCyc"
source_id: "FLAGELLAR-MOTOR-COMPLEX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "flagellar motor complex"
---

# flagellar basal body

`complex.ecocyc.FLAGELLAR-MOTOR-COMPLEX`

## Static

- Type: `complex`
- Source: `EcoCyc:FLAGELLAR-MOTOR-COMPLEX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6S0|protein.P0A6S0]], [[protein.P09348|protein.P09348]], [[protein.P0AF06|protein.P0AF06]], [[protein.P0ABW9|protein.P0ABW9]], [[protein.P0ABX2|protein.P0ABX2]], [[protein.P75938|protein.P75938]], [[protein.P0ABX5|protein.P0ABX5]], [[protein.P0A6S3|protein.P0A6S3]], [[protein.P25798|protein.P25798]], [[protein.P0ABZ1|protein.P0ABZ1]], [[protein.P06974|protein.P06974]], [[protein.P15070|protein.P15070]], [[protein.P0ABX8|protein.P0ABX8]], [[protein.P0A8T5|protein.P0A8T5]]

## Enriched Summary

The flagellar basal body is a multisubunit trans-envelope complex that functions as a reversible rotary motor driving the flagellar filaments that enable swimming and swarming motility. Composed of a rotor plus multiple stator units, this proton motive force (PMF) powered molecular motor can operate in both CCW and CW directions; dynamic properties of the system such as rotation rate and torque generated have been widely investigated (see and reviews ) When the direction of motor rotation is CCW (viewed from the cell's exterior), individual filaments join together in a bundle and the cell moves steadily forward in a "run"; when rotor direction switches to CW, the coordination of the flagellar bundle is disrupted and the cell 'tumbles' to alter course; a tumble can result from a change in direction of as few as one filament in a bundle . Flagella motors respond to chemical stimuli by changing their speed and CW bias in a process known as chemotaxis (see and reviews ). Flagella motors also respond to changes in mechanical load and external osmolarity . The core flagellar basal body consists of C (cytoplasmic), MS (membrane/supramembrane), P (peptidoglycan) and L (lipopolysaccharide) ring structures, and a central rod which connects the flagellar hook to the MS ring...

## Biological Role

Component of flagellum (complex.ecocyc.CPLX0-7452).

## Annotation

The flagellar basal body is a multisubunit trans-envelope complex that functions as a reversible rotary motor driving the flagellar filaments that enable swimming and swarming motility. Composed of a rotor plus multiple stator units, this proton motive force (PMF) powered molecular motor can operate in both CCW and CW directions; dynamic properties of the system such as rotation rate and torque generated have been widely investigated (see and reviews ) When the direction of motor rotation is CCW (viewed from the cell's exterior), individual filaments join together in a bundle and the cell moves steadily forward in a "run"; when rotor direction switches to CW, the coordination of the flagellar bundle is disrupted and the cell 'tumbles' to alter course; a tumble can result from a change in direction of as few as one filament in a bundle . Flagella motors respond to chemical stimuli by changing their speed and CW bias in a process known as chemotaxis (see and reviews ). Flagella motors also respond to changes in mechanical load and external osmolarity . The core flagellar basal body consists of C (cytoplasmic), MS (membrane/supramembrane), P (peptidoglycan) and L (lipopolysaccharide) ring structures, and a central rod which connects the flagellar hook to the MS ring. The MS-C ring complex is a reversible rotor; the C ring (also called the switch complex) is composed of FliG, FliM and FliN proteins and is the key component for directional switching and torque generation; the MS ring which lies in and above the plane of the inner membrane is a polymer of FliF subunits. FlgI and FlgH proteins form the L-P ring complex which may act as a molecular bushing while FlgB, FlgC, FlgF, and FlgG comprise the rod. MotA and MotB form the stator complex which provides the energy for torq

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7452|complex.ecocyc.CPLX0-7452]] `EcoCyc` `database` - EcoCyc component coefficient=120

## Incoming Edges (14)

- `is_component_of` <-- [[protein.P06974|protein.P06974]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P09348|protein.P09348]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0A6S0|protein.P0A6S0]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0A6S3|protein.P0A6S3]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0A8T5|protein.P0A8T5]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0ABW9|protein.P0ABW9]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0ABX2|protein.P0ABX2]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0ABX5|protein.P0ABX5]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0ABX8|protein.P0ABX8]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0ABZ1|protein.P0ABZ1]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0AF06|protein.P0AF06]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P15070|protein.P15070]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P25798|protein.P25798]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P75938|protein.P75938]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:FLAGELLAR-MOTOR-COMPLEX`
- `QSPROTEOME:QS00196935`

## Notes

protein.P0A6S0|protein.P09348|protein.P0AF06|protein.P0ABW9|protein.P0ABX2|protein.P75938|protein.P0ABX5|protein.P0A6S3|protein.P25798|protein.P0ABZ1|protein.P06974|protein.P15070|protein.P0ABX8|protein.P0A8T5
