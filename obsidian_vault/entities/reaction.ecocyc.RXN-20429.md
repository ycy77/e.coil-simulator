---
entity_id: "reaction.ecocyc.RXN-20429"
entity_type: "reaction"
name: "RXN-20429"
source_database: "EcoCyc"
source_id: "RXN-20429"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20429

`reaction.ecocyc.RXN-20429`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20429`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

a-DNA-nucleotide-3-phosphoglycolate + WATER -> 3-Hydroxy-Terminated-DNAs + CPD-67 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: a-DNA-nucleotide-3-phosphoglycolate + WATER -> 3-Hydroxy-Terminated-DNAs + CPD-67 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by xthA (protein.P09030). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), 2-Phosphoglycolate (molecule.C00988).

## Annotation

a-DNA-nucleotide-3-phosphoglycolate + WATER -> 3-Hydroxy-Terminated-DNAs + CPD-67 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P09030|protein.P09030]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00988|molecule.C00988]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20429`

## Notes

a-DNA-nucleotide-3-phosphoglycolate + WATER -> 3-Hydroxy-Terminated-DNAs + CPD-67 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
