---
entity_id: "reaction.ecocyc.4.1.2.28-RXN"
entity_type: "reaction"
name: "4.1.2.28-RXN"
source_database: "EcoCyc"
source_id: "4.1.2.28-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 4.1.2.28-RXN

`reaction.ecocyc.4.1.2.28-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:4.1.2.28-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-DH-3-DO-D-ARABINONATE -> GLYCOLALDEHYDE + PYRUVATE; direction=REVERSIBLE EcoCyc reaction equation: 2-DH-3-DO-D-ARABINONATE -> GLYCOLALDEHYDE + PYRUVATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by CP4-6 prophage; 2-dehydro-3-deoxygluconate aldolase (complex.ecocyc.CPLX0-7940), yjhH (protein.P39359). Substrates: 2-Dehydro-3-deoxy-D-xylonate (molecule.C03826). Products: Pyruvate (molecule.C00022), Glycolaldehyde (molecule.C00266).

## Enriched Pathways

- `ecocyc.PWY-7294` D-xylose degradation IV (EcoCyc)

## Annotation

2-DH-3-DO-D-ARABINONATE -> GLYCOLALDEHYDE + PYRUVATE; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY-7294` D-xylose degradation IV (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7940|complex.ecocyc.CPLX0-7940]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P39359|protein.P39359]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00266|molecule.C00266]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C03826|molecule.C03826]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:4.1.2.28-RXN`

## Notes

2-DH-3-DO-D-ARABINONATE -> GLYCOLALDEHYDE + PYRUVATE; direction=REVERSIBLE
