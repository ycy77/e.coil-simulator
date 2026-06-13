---
entity_id: "complex.ecocyc.ABC-3-CPLX"
entity_type: "complex"
name: "lysine / arginine / ornithine ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-3-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# lysine / arginine / ornithine ABC transporter

`complex.ecocyc.ABC-3-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-3-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P52094|protein.P52094]], [[protein.P07109|protein.P07109]], [[protein.P0AEU3|protein.P0AEU3]], [[protein.P09551|protein.P09551]]

## Enriched Summary

HisPMQ and ArgT are the components of an ATP-dependent uptake system for the basic amino acids lysine, arginine and ornithine. hisP, hisM and hisQ encode the ATP-binding component and two integral membrane components, respectively of an ABC transport system that interacts with two periplasmic binding proteins - ArgT and HISJ-MONOMER "HisJ". Early studies characterized a high affinity, binding protein dependent LAO uptake system in E. coli K-12 . E. coli argT is 89% similar to argT from Salmonella typhimurium which encodes a lysing/arginine/ornithine (LAO) periplasmic binding protein . The substrate specificities of ArgT and HisJ, the periplasmic histidine-binding protein, are believed to have diverged after a gene duplication event while the reliance upon HisPMQ for transport has been conserved . HisPMQArgT is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters. The complex stoichiometry depicted (HisP2HisMHisQArgT) has not been experimentally demonstrated but reflects an archetypal bacterial ABC transporter. HisPMQ and ArgT are the components of an ATP-dependent uptake system for the basic amino acids lysine, arginine and ornithine. hisP, hisM and hisQ encode the ATP-binding component and two integral membrane components, respectively of an ABC transport system that interacts with two periplasmic binding proteins - ArgT and HISJ-MONOMER "HisJ"...

## Biological Role

Catalyzes ABC-3-RXN (reaction.ecocyc.ABC-3-RXN), ABC-37-RXN (reaction.ecocyc.ABC-37-RXN), ABC-4-RXN (reaction.ecocyc.ABC-4-RXN). Transports L-Lysine (molecule.C00047), L-Ornithine (molecule.C00077), hν (molecule.ecocyc.Light).

## Annotation

HisPMQ and ArgT are the components of an ATP-dependent uptake system for the basic amino acids lysine, arginine and ornithine. hisP, hisM and hisQ encode the ATP-binding component and two integral membrane components, respectively of an ABC transport system that interacts with two periplasmic binding proteins - ArgT and HISJ-MONOMER "HisJ". Early studies characterized a high affinity, binding protein dependent LAO uptake system in E. coli K-12 . E. coli argT is 89% similar to argT from Salmonella typhimurium which encodes a lysing/arginine/ornithine (LAO) periplasmic binding protein . The substrate specificities of ArgT and HisJ, the periplasmic histidine-binding protein, are believed to have diverged after a gene duplication event while the reliance upon HisPMQ for transport has been conserved . HisPMQArgT is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters. The complex stoichiometry depicted (HisP2HisMHisQArgT) has not been experimentally demonstrated but reflects an archetypal bacterial ABC transporter.

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.ecocyc.ABC-3-RXN|reaction.ecocyc.ABC-3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ABC-37-RXN|reaction.ecocyc.ABC-37-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ABC-4-RXN|reaction.ecocyc.ABC-4-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00047|molecule.C00047]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00077|molecule.C00077]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (4)

- `is_component_of` <-- [[protein.P07109|protein.P07109]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P09551|protein.P09551]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AEU3|protein.P0AEU3]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P52094|protein.P52094]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ABC-3-CPLX`
- `QSPROTEOME:QS00049292`

## Notes

1*protein.P52094|2*protein.P07109|1*protein.P0AEU3|1*protein.P09551
