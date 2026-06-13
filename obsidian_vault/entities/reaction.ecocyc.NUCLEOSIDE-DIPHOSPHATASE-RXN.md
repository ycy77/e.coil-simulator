---
entity_id: "reaction.ecocyc.NUCLEOSIDE-DIPHOSPHATASE-RXN"
entity_type: "reaction"
name: "NUCLEOSIDE-DIPHOSPHATASE-RXN"
source_database: "EcoCyc"
source_id: "NUCLEOSIDE-DIPHOSPHATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# NUCLEOSIDE-DIPHOSPHATASE-RXN

`reaction.ecocyc.NUCLEOSIDE-DIPHOSPHATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:NUCLEOSIDE-DIPHOSPHATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Nucleoside-Diphosphates + WATER -> Nucleoside-Monophosphates + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Nucleoside-Diphosphates + WATER -> Nucleoside-Monophosphates + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), a nucleoside diphosphate (molecule.ecocyc.Nucleoside-Diphosphates). Products: H+ (molecule.C00080), a nucleoside 5'-monophosphate (molecule.ecocyc.Nucleoside-Monophosphates), phosphate (molecule.ecocyc.Pi).

## Annotation

Nucleoside-Diphosphates + WATER -> Nucleoside-Monophosphates + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Nucleoside-Monophosphates|molecule.ecocyc.Nucleoside-Monophosphates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Nucleoside-Diphosphates|molecule.ecocyc.Nucleoside-Diphosphates]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:NUCLEOSIDE-DIPHOSPHATASE-RXN`

## Notes

Nucleoside-Diphosphates + WATER -> Nucleoside-Monophosphates + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
