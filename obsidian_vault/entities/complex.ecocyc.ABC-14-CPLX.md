---
entity_id: "complex.ecocyc.ABC-14-CPLX"
entity_type: "complex"
name: "histidine ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-14-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# histidine ABC transporter

`complex.ecocyc.ABC-14-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-14-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `structural`
- Components: [[protein.P07109|protein.P07109]], [[protein.P0AEU3|protein.P0AEU3]], [[protein.P52094|protein.P52094]], [[protein.P0AEU0|protein.P0AEU0]]

## Enriched Summary

HisPMQJ are predicted to be the components of an ATP-dependent histidine uptake system. hisP and hisMQ encode the ATP-binding component and two integral membrane components, respectively, of both the histidine ABC transporter and the lysine/arginine/ornithine ABC transporter of E. coli K-12. HisJ is the experimentally characterized periplasmic histidine-binding protein . Transport properties of the HisPMQJ complex in E. coli have not been characterized; extensive investigations on the orthologous proteins in Salmonella typhimurium, which was one of the first ABC transporters characterized have been reported (see and others for early characterization of HisPMQJ in S. typhimurium). The HisPMQJ transporter functions to scavenge histidine in response to nitrogen limitation; it appears to be the only transporter for histidine uptake in E. coli . The complex stoichiometry depicted (HisP2HisMHisQHisJ) has not been experimentally demonstrated but reflects an archetypal bacterial ABC transporter. HisPMQJ is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters. HisPMQJ are predicted to be the components of an ATP-dependent histidine uptake system. hisP and hisMQ encode the ATP-binding component and two integral membrane components, respectively, of both the histidine ABC transporter and the lysine/arginine/ornithine ABC transporter of E. coli K-12...

## Biological Role

Catalyzes ABC-14-RXN (reaction.ecocyc.ABC-14-RXN). Transports L-Histidine (molecule.C00135), hν (molecule.ecocyc.Light).

## Annotation

HisPMQJ are predicted to be the components of an ATP-dependent histidine uptake system. hisP and hisMQ encode the ATP-binding component and two integral membrane components, respectively, of both the histidine ABC transporter and the lysine/arginine/ornithine ABC transporter of E. coli K-12. HisJ is the experimentally characterized periplasmic histidine-binding protein . Transport properties of the HisPMQJ complex in E. coli have not been characterized; extensive investigations on the orthologous proteins in Salmonella typhimurium, which was one of the first ABC transporters characterized have been reported (see and others for early characterization of HisPMQJ in S. typhimurium). The HisPMQJ transporter functions to scavenge histidine in response to nitrogen limitation; it appears to be the only transporter for histidine uptake in E. coli . The complex stoichiometry depicted (HisP2HisMHisQHisJ) has not been experimentally demonstrated but reflects an archetypal bacterial ABC transporter. HisPMQJ is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.ABC-14-RXN|reaction.ecocyc.ABC-14-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00135|molecule.C00135]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (4)

- `is_component_of` <-- [[protein.P07109|protein.P07109]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P0AEU0|protein.P0AEU0]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AEU3|protein.P0AEU3]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P52094|protein.P52094]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ABC-14-CPLX`
- `QSPROTEOME:QS00049302`

## Notes

2*protein.P07109|1*protein.P0AEU3|1*protein.P52094|1*protein.P0AEU0
