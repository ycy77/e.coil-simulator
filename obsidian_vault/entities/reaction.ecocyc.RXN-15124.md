---
entity_id: "reaction.ecocyc.RXN-15124"
entity_type: "reaction"
name: "RXN-15124"
source_database: "EcoCyc"
source_id: "RXN-15124"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15124

`reaction.ecocyc.RXN-15124`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15124`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-AMINOACRYLATE -> CPD-16015; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 2-AMINOACRYLATE -> CPD-16015; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Dehydroalanine (molecule.C02218). Products: 2-iminopropanoate (molecule.ecocyc.CPD-16015).

## Enriched Pathways

- `ecocyc.LCYSDEG-PWY` L-cysteine degradation II (EcoCyc)
- `ecocyc.PWY0-1535` D-serine degradation (EcoCyc)
- `ecocyc.SERDEG-PWY` L-serine degradation (EcoCyc)
- `ecocyc.TRYPDEG-PWY` L-tryptophan degradation II (via pyruvate) (EcoCyc)

## Annotation

2-AMINOACRYLATE -> CPD-16015; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.LCYSDEG-PWY` L-cysteine degradation II (EcoCyc)
- `ecocyc.PWY0-1535` D-serine degradation (EcoCyc)
- `ecocyc.SERDEG-PWY` L-serine degradation (EcoCyc)
- `ecocyc.TRYPDEG-PWY` L-tryptophan degradation II (via pyruvate) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.CPD-16015|molecule.ecocyc.CPD-16015]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C02218|molecule.C02218]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15124`

## Notes

2-AMINOACRYLATE -> CPD-16015; direction=PHYSIOL-LEFT-TO-RIGHT
