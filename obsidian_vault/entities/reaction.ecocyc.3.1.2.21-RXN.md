---
entity_id: "reaction.ecocyc.3.1.2.21-RXN"
entity_type: "reaction"
name: "3.1.2.21-RXN"
source_database: "EcoCyc"
source_id: "3.1.2.21-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3.1.2.21-RXN

`reaction.ecocyc.3.1.2.21-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.1.2.21-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Dodecanoyl-ACPs + WATER -> ACP + DODECANOATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Dodecanoyl-ACPs + WATER -> ACP + DODECANOATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), Dodecanoic acid (molecule.C02679).

## Enriched Pathways

- `ecocyc.PWY-5971` palmitate biosynthesis II (type II fatty acid synthase) (EcoCyc)

## Annotation

Dodecanoyl-ACPs + WATER -> ACP + DODECANOATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5971` palmitate biosynthesis II (type II fatty acid synthase) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02679|molecule.C02679]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.1.2.21-RXN`

## Notes

Dodecanoyl-ACPs + WATER -> ACP + DODECANOATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
