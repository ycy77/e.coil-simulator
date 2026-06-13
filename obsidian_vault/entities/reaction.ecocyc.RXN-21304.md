---
entity_id: "reaction.ecocyc.RXN-21304"
entity_type: "reaction"
name: "RXN-21304"
source_database: "EcoCyc"
source_id: "RXN-21304"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21304

`reaction.ecocyc.RXN-21304`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21304`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

a-DNA-nucleotide-3-phosphoglycolaldehyde + WATER -> 3-Hydroxy-Terminated-DNAs + CPD-19745 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: a-DNA-nucleotide-3-phosphoglycolaldehyde + WATER -> 3-Hydroxy-Terminated-DNAs + CPD-19745 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nfo (protein.P0A6C1). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), glycolaldehyde phosphate (molecule.ecocyc.CPD-19745).

## Annotation

a-DNA-nucleotide-3-phosphoglycolaldehyde + WATER -> 3-Hydroxy-Terminated-DNAs + CPD-19745 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0A6C1|protein.P0A6C1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-19745|molecule.ecocyc.CPD-19745]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21304`

## Notes

a-DNA-nucleotide-3-phosphoglycolaldehyde + WATER -> 3-Hydroxy-Terminated-DNAs + CPD-19745 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
