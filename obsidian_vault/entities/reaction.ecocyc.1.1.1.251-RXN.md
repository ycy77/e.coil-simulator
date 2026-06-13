---
entity_id: "reaction.ecocyc.1.1.1.251-RXN"
entity_type: "reaction"
name: "1.1.1.251-RXN"
source_database: "EcoCyc"
source_id: "1.1.1.251-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 1.1.1.251-RXN

`reaction.ecocyc.1.1.1.251-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:1.1.1.251-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the galactitol catabolism pathway. EcoCyc reaction equation: GALACTITOL-1-PHOSPHATE + NAD -> CPD-15826 + NADH + PROTON; direction=REVERSIBLE. This reaction is part of the galactitol catabolism pathway.

## Biological Role

Catalyzed by galactitol-1-phosphate 5-dehydrogenase (complex.ecocyc.CPLX0-8186). Substrates: NAD+ (molecule.C00003), Galactitol 1-phosphate (molecule.C06311). Products: NADH (molecule.C00004), H+ (molecule.C00080), keto-D-tagatose 6-phosphate (molecule.ecocyc.CPD-15826).

## Enriched Pathways

- `ecocyc.GALACTITOLCAT-PWY` galactitol degradation (EcoCyc)

## Annotation

This reaction is part of the galactitol catabolism pathway.

## Pathways

- `ecocyc.GALACTITOLCAT-PWY` galactitol degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8186|complex.ecocyc.CPLX0-8186]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15826|molecule.ecocyc.CPD-15826]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06311|molecule.C06311]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:1.1.1.251-RXN`

## Notes

GALACTITOL-1-PHOSPHATE + NAD -> CPD-15826 + NADH + PROTON; direction=REVERSIBLE
