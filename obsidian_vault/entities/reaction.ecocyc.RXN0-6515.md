---
entity_id: "reaction.ecocyc.RXN0-6515"
entity_type: "reaction"
name: "RXN0-6515"
source_database: "EcoCyc"
source_id: "RXN0-6515"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6515

`reaction.ecocyc.RXN0-6515`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6515`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The enzyme efficiently methylates guanine966 of the assembled 30S subunits in vitro. Protein-free 16S rRNA is not a substrate for RsmD.The enzyme specifically methylates guanine966 at N2 in 16S rRNA. EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 16S-rRNA-guanine-966 -> ADENOSYL-HOMO-CYS + 16S-rRNA-N2-methylguanine966 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. The enzyme efficiently methylates guanine966 of the assembled 30S subunits in vitro. Protein-free 16S rRNA is not a substrate for RsmD.The enzyme specifically methylates guanine966 at N2 in 16S rRNA.

## Biological Role

Catalyzed by rsmD (protein.P0ADX9). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a guanine966 in 16S rRNA (molecule.ecocyc.16S-rRNA-guanine-966). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), an N2-methylguanine966 in 16S rRNA (molecule.ecocyc.16S-rRNA-N2-methylguanine966).

## Annotation

The enzyme efficiently methylates guanine966 of the assembled 30S subunits in vitro. Protein-free 16S rRNA is not a substrate for RsmD.The enzyme specifically methylates guanine966 at N2 in 16S rRNA.

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0ADX9|protein.P0ADX9]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.16S-rRNA-N2-methylguanine966|molecule.ecocyc.16S-rRNA-N2-methylguanine966]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.16S-rRNA-guanine-966|molecule.ecocyc.16S-rRNA-guanine-966]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6515`

## Notes

S-ADENOSYLMETHIONINE + 16S-rRNA-guanine-966 -> ADENOSYL-HOMO-CYS + 16S-rRNA-N2-methylguanine966 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
