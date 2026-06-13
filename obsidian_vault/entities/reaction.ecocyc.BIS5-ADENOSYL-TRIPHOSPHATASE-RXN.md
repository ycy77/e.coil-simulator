---
entity_id: "reaction.ecocyc.BIS5-ADENOSYL-TRIPHOSPHATASE-RXN"
entity_type: "reaction"
name: "BIS5-ADENOSYL-TRIPHOSPHATASE-RXN"
source_database: "EcoCyc"
source_id: "BIS5-ADENOSYL-TRIPHOSPHATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# BIS5-ADENOSYL-TRIPHOSPHATASE-RXN

`reaction.ecocyc.BIS5-ADENOSYL-TRIPHOSPHATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:BIS5-ADENOSYL-TRIPHOSPHATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN

## Enriched Summary

ADENOSINE5TRIPHOSPHO5ADENOSINE + WATER -> PROTON + AMP + ADP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: ADENOSINE5TRIPHOSPHO5ADENOSINE + WATER -> PROTON + AMP + ADP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ushA (protein.P07024). Substrates: H2O (molecule.C00001), P1,P3-Bis(5'-adenosyl) triphosphate (molecule.C06197). Products: ADP (molecule.C00008), AMP (molecule.C00020), H+ (molecule.C00080).

## Annotation

ADENOSINE5TRIPHOSPHO5ADENOSINE + WATER -> PROTON + AMP + ADP; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P07024|protein.P07024]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06197|molecule.C06197]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:BIS5-ADENOSYL-TRIPHOSPHATASE-RXN`

## Notes

ADENOSINE5TRIPHOSPHO5ADENOSINE + WATER -> PROTON + AMP + ADP; direction=LEFT-TO-RIGHT
