---
entity_id: "reaction.ecocyc.RXN0-5437"
entity_type: "reaction"
name: "RXN0-5437"
source_database: "EcoCyc"
source_id: "RXN0-5437"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5437

`reaction.ecocyc.RXN0-5437`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5437`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + rRNA-Adenines -> N6N6-Dimethyladenine-Containing-rRNAs + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + rRNA-Adenines -> N6N6-Dimethyladenine-Containing-rRNAs + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: S-Adenosyl-L-methionine (molecule.C00019), an adenine in rRNA (molecule.ecocyc.rRNA-Adenines). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), an N6,N6-dimethyladenine in rRNA (molecule.ecocyc.N6N6-Dimethyladenine-Containing-rRNAs).

## Annotation

S-ADENOSYLMETHIONINE + rRNA-Adenines -> N6N6-Dimethyladenine-Containing-rRNAs + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.N6N6-Dimethyladenine-Containing-rRNAs|molecule.ecocyc.N6N6-Dimethyladenine-Containing-rRNAs]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.rRNA-Adenines|molecule.ecocyc.rRNA-Adenines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5437`

## Notes

S-ADENOSYLMETHIONINE + rRNA-Adenines -> N6N6-Dimethyladenine-Containing-rRNAs + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
