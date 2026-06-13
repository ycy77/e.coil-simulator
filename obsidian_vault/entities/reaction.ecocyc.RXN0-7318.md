---
entity_id: "reaction.ecocyc.RXN0-7318"
entity_type: "reaction"
name: "RXN0-7318"
source_database: "EcoCyc"
source_id: "RXN0-7318"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7318

`reaction.ecocyc.RXN0-7318`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7318`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-12763 + NAD + WATER -> 5-AMINOPENTANOATE + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-12763 + NAD + WATER -> 5-AMINOPENTANOATE + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by γ-aminobutyraldehyde dehydrogenase (complex.ecocyc.CPLX0-3641). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), 5-Aminopentanal (molecule.C12455). Products: NADH (molecule.C00004), H+ (molecule.C00080), 5-Aminopentanoate (molecule.C00431).

## Enriched Pathways

- `ecocyc.PWY0-461` L-lysine degradation I (EcoCyc)

## Annotation

CPD-12763 + NAD + WATER -> 5-AMINOPENTANOATE + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-461` L-lysine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3641|complex.ecocyc.CPLX0-3641]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00431|molecule.C00431]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C12455|molecule.C12455]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7318`

## Notes

CPD-12763 + NAD + WATER -> 5-AMINOPENTANOATE + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
