---
entity_id: "reaction.ecocyc.RXN0-6950"
entity_type: "reaction"
name: "RXN0-6950"
source_database: "EcoCyc"
source_id: "RXN0-6950"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6950

`reaction.ecocyc.RXN0-6950`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6950`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + 23S-rRNA-guanine-2069 -> 23S-rRNA-N7-methylguanine-2069 + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 23S-rRNA-guanine-2069 -> 23S-rRNA-N7-methylguanine-2069 + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rlmL (protein.P75864). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a guanine2069 in 23S rRNA (molecule.ecocyc.23S-rRNA-guanine-2069). Products: S-Adenosyl-L-homocysteine (molecule.C00021), an N7-methylguanine2069 in 23S rRNA (molecule.ecocyc.23S-rRNA-N7-methylguanine-2069).

## Annotation

S-ADENOSYLMETHIONINE + 23S-rRNA-guanine-2069 -> 23S-rRNA-N7-methylguanine-2069 + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P75864|protein.P75864]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.23S-rRNA-N7-methylguanine-2069|molecule.ecocyc.23S-rRNA-N7-methylguanine-2069]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.23S-rRNA-guanine-2069|molecule.ecocyc.23S-rRNA-guanine-2069]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6950`

## Notes

S-ADENOSYLMETHIONINE + 23S-rRNA-guanine-2069 -> 23S-rRNA-N7-methylguanine-2069 + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT
