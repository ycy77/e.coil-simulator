---
entity_id: "complex.ecocyc.CPLX0-3382"
entity_type: "complex"
name: "type II secretion system"
source_database: "EcoCyc"
source_id: "CPLX0-3382"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "GspC-O secreton  complex"
---

# type II secretion system

`complex.ecocyc.CPLX0-3382`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3382`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P45757|protein.P45757]], [[protein.P45758|protein.P45758]], [[protein.P45759|protein.P45759]], [[protein.P41441|protein.P41441]], [[protein.P41442|protein.P41442]], [[protein.P41443|protein.P41443]], [[protein.P45760|protein.P45760]], [[protein.P45761|protein.P45761]], [[protein.P45762|protein.P45762]], [[protein.P45763|protein.P45763]], [[protein.P36678|protein.P36678]]

## Enriched Summary

E. coli K-12 contains a cluster of genes (gsp) predicted to encode the components of a type II secretion system; the cluster consists of two divergent operons TU0-14374 gspC-O and TU-8433 gspAB which are transcriptionally repressed by PD00288 nucleoid-structuring protein H-NS under standard laboratory conditions . Overexpression of the full cluster supports secretion of (plasmid expressed) EG11237-MONOMER and (plasmid expressed) G7706-MONOMER pseudopilin GspG in a hns mutant strain . gsp: general secretory pathway (and see ) The complex depicted here contains the core components of the E. coli Type II secreton, it does not include the accessory components, G7701-MONOMER GspA and EG11263-MONOMER GspB, nor the EG11359-MONOMER prepilin peptidase GspO. E. coli K-12 contains a cluster of genes (gsp) predicted to encode the components of a type II secretion system; the cluster consists of two divergent operons TU0-14374 gspC-O and TU-8433 gspAB which are transcriptionally repressed by PD00288 nucleoid-structuring protein H-NS under standard laboratory conditions . Overexpression of the full cluster supports secretion of (plasmid expressed) EG11237-MONOMER and (plasmid expressed) G7706-MONOMER pseudopilin GspG in a hns mutant strain . gsp: general secretory pathway (and see ) The complex depicted here contains the core components of the E...

## Biological Role

Catalyzes TRANS-RXN-510 (reaction.ecocyc.TRANS-RXN-510). Transports hν (molecule.ecocyc.Light).

## Annotation

E. coli K-12 contains a cluster of genes (gsp) predicted to encode the components of a type II secretion system; the cluster consists of two divergent operons TU0-14374 gspC-O and TU-8433 gspAB which are transcriptionally repressed by PD00288 nucleoid-structuring protein H-NS under standard laboratory conditions . Overexpression of the full cluster supports secretion of (plasmid expressed) EG11237-MONOMER and (plasmid expressed) G7706-MONOMER pseudopilin GspG in a hns mutant strain . gsp: general secretory pathway (and see ) The complex depicted here contains the core components of the E. coli Type II secreton, it does not include the accessory components, G7701-MONOMER GspA and EG11263-MONOMER GspB, nor the EG11359-MONOMER prepilin peptidase GspO.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-510|reaction.ecocyc.TRANS-RXN-510]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (11)

- `is_component_of` <-- [[protein.P36678|protein.P36678]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P41441|protein.P41441]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P41442|protein.P41442]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P41443|protein.P41443]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P45757|protein.P45757]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P45758|protein.P45758]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P45759|protein.P45759]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P45760|protein.P45760]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P45761|protein.P45761]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P45762|protein.P45762]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P45763|protein.P45763]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:CPLX0-3382`
- `QSPROTEOME:QS00196503`

## Notes

protein.P45757|protein.P45758|protein.P45759|protein.P41441|protein.P41442|protein.P41443|protein.P45760|protein.P45761|protein.P45762|protein.P45763|protein.P36678
