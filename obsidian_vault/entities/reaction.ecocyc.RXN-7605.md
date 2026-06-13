---
entity_id: "reaction.ecocyc.RXN-7605"
entity_type: "reaction"
name: "RXN-7605"
source_database: "EcoCyc"
source_id: "RXN-7605"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-7605

`reaction.ecocyc.RXN-7605`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-7605`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + Demethylated-methyl-acceptors -> ADENOSYL-HOMO-CYS + Methylated-methyl-acceptors + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + Demethylated-methyl-acceptors -> ADENOSYL-HOMO-CYS + Methylated-methyl-acceptors + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: S-Adenosyl-L-methionine (molecule.C00019). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.PWY-6153` autoinducer AI-2 biosynthesis I (EcoCyc)

## Annotation

S-ADENOSYLMETHIONINE + Demethylated-methyl-acceptors -> ADENOSYL-HOMO-CYS + Methylated-methyl-acceptors + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6153` autoinducer AI-2 biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-7605`

## Notes

S-ADENOSYLMETHIONINE + Demethylated-methyl-acceptors -> ADENOSYL-HOMO-CYS + Methylated-methyl-acceptors + PROTON; direction=LEFT-TO-RIGHT
