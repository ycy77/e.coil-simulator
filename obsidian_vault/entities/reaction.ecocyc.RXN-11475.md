---
entity_id: "reaction.ecocyc.RXN-11475"
entity_type: "reaction"
name: "RXN-11475"
source_database: "EcoCyc"
source_id: "RXN-11475"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11475

`reaction.ecocyc.RXN-11475`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11475`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + MALONYL-ACP -> Malonyl-acp-methyl-ester + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + MALONYL-ACP -> Malonyl-acp-methyl-ester + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by bioC (protein.P12999). Substrates: S-Adenosyl-L-methionine (molecule.C00019). Products: S-Adenosyl-L-homocysteine (molecule.C00021).

## Enriched Pathways

- `ecocyc.PWY-6519` 8-amino-7-oxononanoate biosynthesis I (EcoCyc)

## Annotation

S-ADENOSYLMETHIONINE + MALONYL-ACP -> Malonyl-acp-methyl-ester + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6519` 8-amino-7-oxononanoate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P12999|protein.P12999]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11475`

## Notes

S-ADENOSYLMETHIONINE + MALONYL-ACP -> Malonyl-acp-methyl-ester + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT
