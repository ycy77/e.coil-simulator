---
entity_id: "reaction.ecocyc.RXN-13403"
entity_type: "reaction"
name: "RXN-13403"
source_database: "EcoCyc"
source_id: "RXN-13403"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-13403

`reaction.ecocyc.RXN-13403`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-13403`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + UROPORPHYRINOGEN-III -> ADENOSYL-HOMO-CYS + DIHYDROSIROHYDROCHLORIN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + UROPORPHYRINOGEN-III -> ADENOSYL-HOMO-CYS + DIHYDROSIROHYDROCHLORIN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by siroheme synthase (complex.ecocyc.SIROHEMESYN-CPLX). Substrates: S-Adenosyl-L-methionine (molecule.C00019), Uroporphyrinogen III (molecule.C01051). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), Precorrin 2 (molecule.C02463).

## Annotation

S-ADENOSYLMETHIONINE + UROPORPHYRINOGEN-III -> ADENOSYL-HOMO-CYS + DIHYDROSIROHYDROCHLORIN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.SIROHEMESYN-CPLX|complex.ecocyc.SIROHEMESYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02463|molecule.C02463]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01051|molecule.C01051]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-13403`

## Notes

S-ADENOSYLMETHIONINE + UROPORPHYRINOGEN-III -> ADENOSYL-HOMO-CYS + DIHYDROSIROHYDROCHLORIN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
