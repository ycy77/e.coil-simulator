---
entity_id: "reaction.ecocyc.RXN-11633"
entity_type: "reaction"
name: "RXN-11633"
source_database: "EcoCyc"
source_id: "RXN-11633"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "S-adenosyl-L-methionine:16S rRNA (adenine<sup>1518</sup>-N6/adenine<sup>1519</sup>-N6)-dimethyltransferase"
  - "<i>ksgA</i> methyltransferase"
  - "S-adenosylmethionine-6-N,N-adenosyl (rRNA) dimethyltransferase"
---

# RXN-11633

`reaction.ecocyc.RXN-11633`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11633`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + 16S-rRNA-adenine1518-adenine1519 -> 16S-rRNA-N6-dimethyladenine1518-1519 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 16S-rRNA-adenine1518-adenine1519 -> 16S-rRNA-N6-dimethyladenine1518-1519 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rsmA (protein.P06992). Substrates: S-Adenosyl-L-methionine (molecule.C00019), adenine1518/adenine1519 in 16S rRNA (molecule.ecocyc.16S-rRNA-adenine1518-adenine1519). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), N6-dimethyladenine1518/N6-dimethyladenine1519in 16S rRNA (molecule.ecocyc.16S-rRNA-N6-dimethyladenine1518-1519).

## Annotation

S-ADENOSYLMETHIONINE + 16S-rRNA-adenine1518-adenine1519 -> 16S-rRNA-N6-dimethyladenine1518-1519 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P06992|protein.P06992]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.16S-rRNA-N6-dimethyladenine1518-1519|molecule.ecocyc.16S-rRNA-N6-dimethyladenine1518-1519]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.16S-rRNA-adenine1518-adenine1519|molecule.ecocyc.16S-rRNA-adenine1518-adenine1519]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11633`

## Notes

S-ADENOSYLMETHIONINE + 16S-rRNA-adenine1518-adenine1519 -> 16S-rRNA-N6-dimethyladenine1518-1519 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
