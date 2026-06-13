---
entity_id: "reaction.ecocyc.RXN-24864"
entity_type: "reaction"
name: "RXN-24864"
source_database: "EcoCyc"
source_id: "RXN-24864"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24864

`reaction.ecocyc.RXN-24864`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24864`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A-KDPB-SUBUNIT-L-SERINE + ATP -> A-KDPB-PHOSPHO-SERINE + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: A-KDPB-SUBUNIT-L-SERINE + ATP -> A-KDPB-PHOSPHO-SERINE + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by serine histidine kinase KdpD (complex.ecocyc.KDPD-CPLX). Substrates: ATP (molecule.C00002), a [K+ transporting P-type ATPase KdpB subunit]-L-serine (molecule.ecocyc.A-KDPB-SUBUNIT-L-SERINE). Products: ADP (molecule.C00008), H+ (molecule.C00080), a [K+ transporting P-type ATPase KdpB subunit]-O-phospho-L-serine (molecule.ecocyc.A-KDPB-PHOSPHO-SERINE).

## Annotation

A-KDPB-SUBUNIT-L-SERINE + ATP -> A-KDPB-PHOSPHO-SERINE + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.KDPD-CPLX|complex.ecocyc.KDPD-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.A-KDPB-PHOSPHO-SERINE|molecule.ecocyc.A-KDPB-PHOSPHO-SERINE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.A-KDPB-SUBUNIT-L-SERINE|molecule.ecocyc.A-KDPB-SUBUNIT-L-SERINE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24864`

## Notes

A-KDPB-SUBUNIT-L-SERINE + ATP -> A-KDPB-PHOSPHO-SERINE + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
