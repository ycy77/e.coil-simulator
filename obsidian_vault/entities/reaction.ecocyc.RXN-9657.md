---
entity_id: "reaction.ecocyc.RXN-9657"
entity_type: "reaction"
name: "crotonyl-[acp] reductase"
source_database: "EcoCyc"
source_id: "RXN-9657"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "NADH-specific enoyl-ACP reductase"
  - "NADH-enoyl acyl carrier protein reductase"
  - "Enoyl-ACP reductase"
---

# crotonyl-[acp] reductase

`reaction.ecocyc.RXN-9657`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9657`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Butanoyl-ACPs + NAD -> Crotonyl-ACPs + NADH + PROTON; direction=RIGHT-TO-LEFT EcoCyc reaction equation: Butanoyl-ACPs + NAD -> Crotonyl-ACPs + NADH + PROTON; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by enoyl-[acyl-carrier-protein] reductase (complex.ecocyc.CPLX0-8006). Substrates: NAD+ (molecule.C00003). Products: NADH (molecule.C00004), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.PWY-5971` palmitate biosynthesis II (type II fatty acid synthase) (EcoCyc)

## Annotation

Butanoyl-ACPs + NAD -> Crotonyl-ACPs + NADH + PROTON; direction=RIGHT-TO-LEFT

## Pathways

- `ecocyc.PWY-5971` palmitate biosynthesis II (type II fatty acid synthase) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8006|complex.ecocyc.CPLX0-8006]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00154|molecule.C00154]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-9657`

## Notes

Butanoyl-ACPs + NAD -> Crotonyl-ACPs + NADH + PROTON; direction=RIGHT-TO-LEFT
