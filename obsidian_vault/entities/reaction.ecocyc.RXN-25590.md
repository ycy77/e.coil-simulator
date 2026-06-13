---
entity_id: "reaction.ecocyc.RXN-25590"
entity_type: "reaction"
name: "RXN-25590"
source_database: "EcoCyc"
source_id: "RXN-25590"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-25590

`reaction.ecocyc.RXN-25590`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25590`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Menaquinols + an-oxidized-NapB-protein -> Menaquinones + PROTON + a-reduced-NapB-protein; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Menaquinols + an-oxidized-NapB-protein -> Menaquinones + PROTON + a-reduced-NapB-protein; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by napC (protein.P0ABL5). Substrates: Menaquinol (molecule.C05819). Products: H+ (molecule.C00080), Menaquinone (molecule.C00828).

## Annotation

Menaquinols + an-oxidized-NapB-protein -> Menaquinones + PROTON + a-reduced-NapB-protein; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0ABL5|protein.P0ABL5]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00828|molecule.C00828]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C05819|molecule.C05819]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-25590`

## Notes

Menaquinols + an-oxidized-NapB-protein -> Menaquinones + PROTON + a-reduced-NapB-protein; direction=LEFT-TO-RIGHT
