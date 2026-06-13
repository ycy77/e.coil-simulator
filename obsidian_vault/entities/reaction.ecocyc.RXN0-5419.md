---
entity_id: "reaction.ecocyc.RXN0-5419"
entity_type: "reaction"
name: "RXN0-5419"
source_database: "EcoCyc"
source_id: "RXN0-5419"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5419

`reaction.ecocyc.RXN0-5419`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5419`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + Nonmethylated-Ribosomal-Protein-L11s -> Methylated-Ribosomal-Protein-L11s + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + Nonmethylated-Ribosomal-Protein-L11s -> Methylated-Ribosomal-Protein-L11s + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by prmA (protein.P0A8T1). Substrates: S-Adenosyl-L-methionine (molecule.C00019). Products: S-Adenosyl-L-homocysteine (molecule.C00021).

## Annotation

S-ADENOSYLMETHIONINE + Nonmethylated-Ribosomal-Protein-L11s -> Methylated-Ribosomal-Protein-L11s + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0A8T1|protein.P0A8T1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5419`

## Notes

S-ADENOSYLMETHIONINE + Nonmethylated-Ribosomal-Protein-L11s -> Methylated-Ribosomal-Protein-L11s + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT
