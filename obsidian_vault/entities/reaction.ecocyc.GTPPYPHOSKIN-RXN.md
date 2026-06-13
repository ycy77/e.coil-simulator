---
entity_id: "reaction.ecocyc.GTPPYPHOSKIN-RXN"
entity_type: "reaction"
name: "GTPPYPHOSKIN-RXN"
source_database: "EcoCyc"
source_id: "GTPPYPHOSKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GTPPYPHOSKIN-RXN

`reaction.ecocyc.GTPPYPHOSKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GTPPYPHOSKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a pppGpp (guanosine 3'-diphosphate 5'-triphosphate) synthesis reaction. EcoCyc reaction equation: GTP + ATP -> GDP-TP + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. This is a pppGpp (guanosine 3'-diphosphate 5'-triphosphate) synthesis reaction.

## Biological Role

Catalyzed by relA (protein.P0AG20). Substrates: ATP (molecule.C00002), GTP (molecule.C00044). Products: AMP (molecule.C00020), H+ (molecule.C00080), Guanosine 3'-diphosphate 5'-triphosphate (molecule.C04494).

## Enriched Pathways

- `ecocyc.PPGPPMET-PWY` ppGpp metabolism (EcoCyc)

## Annotation

This is a pppGpp (guanosine 3'-diphosphate 5'-triphosphate) synthesis reaction.

## Pathways

- `ecocyc.PPGPPMET-PWY` ppGpp metabolism (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AG20|protein.P0AG20]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04494|molecule.C04494]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GTPPYPHOSKIN-RXN`

## Notes

GTP + ATP -> GDP-TP + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
