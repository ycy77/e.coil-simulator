---
entity_id: "reaction.ecocyc.RXN0-7298"
entity_type: "reaction"
name: "RXN0-7298"
source_database: "EcoCyc"
source_id: "RXN0-7298"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7298

`reaction.ecocyc.RXN0-7298`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7298`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PRENOL + ATP -> CPD-14332 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PRENOL + ATP -> CPD-14332 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by hydroxyethylthiazole kinase (complex.ecocyc.CPLX0-8211). Substrates: ATP (molecule.C00002), Prenol (molecule.C01390). Products: ADP (molecule.C00008), H+ (molecule.C00080), Dimethylallyl phosphate (molecule.C21214).

## Enriched Pathways

- `ecocyc.PWY0-1597` prenylated FMNH2 biosynthesis (EcoCyc)

## Annotation

PRENOL + ATP -> CPD-14332 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1597` prenylated FMNH2 biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8211|complex.ecocyc.CPLX0-8211]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C21214|molecule.C21214]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01390|molecule.C01390]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7298`

## Notes

PRENOL + ATP -> CPD-14332 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
