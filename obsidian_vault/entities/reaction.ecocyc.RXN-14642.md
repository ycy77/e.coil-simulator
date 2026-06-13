---
entity_id: "reaction.ecocyc.RXN-14642"
entity_type: "reaction"
name: "RXN-14642"
source_database: "EcoCyc"
source_id: "RXN-14642"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14642

`reaction.ecocyc.RXN-14642`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14642`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLYCOLALDEHYDE + Acceptor -> GLYCOLLATE + Donor-H2 + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: GLYCOLALDEHYDE + Acceptor -> GLYCOLLATE + Donor-H2 + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: Glycolaldehyde (molecule.C00266). Products: H+ (molecule.C00080), Glycolate (molecule.C00160).

## Enriched Pathways

- `ecocyc.PWY-7294` D-xylose degradation IV (EcoCyc)

## Annotation

GLYCOLALDEHYDE + Acceptor -> GLYCOLLATE + Donor-H2 + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7294` D-xylose degradation IV (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00160|molecule.C00160]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00266|molecule.C00266]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14642`

## Notes

GLYCOLALDEHYDE + Acceptor -> GLYCOLLATE + Donor-H2 + PROTON; direction=LEFT-TO-RIGHT
