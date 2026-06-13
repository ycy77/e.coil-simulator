---
entity_id: "reaction.ecocyc.RXN-20755"
entity_type: "reaction"
name: "RXN-20755"
source_database: "EcoCyc"
source_id: "RXN-20755"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20755

`reaction.ecocyc.RXN-20755`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20755`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GERANYL-PP + tRNA-Containing-5MeAminoMe-2-ThioU -> mnm5GeS2U + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GERANYL-PP + tRNA-Containing-5MeAminoMe-2-ThioU -> mnm5GeS2U + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Geranyl diphosphate (molecule.C00341), a 5-[(methylamino)methyl]-2-thiouridine34 in tRNA (molecule.ecocyc.tRNA-Containing-5MeAminoMe-2-ThioU). Products: Diphosphate (molecule.C00013), a 5-methylaminomethyl-2-(S-geranyl)thiouridine34 in tRNA (molecule.ecocyc.mnm5GeS2U).

## Enriched Pathways

- `ecocyc.PWY-7892` tRNA-uridine34 modifications (E. coli) (EcoCyc)

## Annotation

GERANYL-PP + tRNA-Containing-5MeAminoMe-2-ThioU -> mnm5GeS2U + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7892` tRNA-uridine34 modifications (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.mnm5GeS2U|molecule.ecocyc.mnm5GeS2U]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00341|molecule.C00341]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.tRNA-Containing-5MeAminoMe-2-ThioU|molecule.ecocyc.tRNA-Containing-5MeAminoMe-2-ThioU]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20755`

## Notes

GERANYL-PP + tRNA-Containing-5MeAminoMe-2-ThioU -> mnm5GeS2U + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
