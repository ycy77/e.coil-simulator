---
entity_id: "reaction.ecocyc.RXN-15943"
entity_type: "reaction"
name: "RXN-15943"
source_database: "EcoCyc"
source_id: "RXN-15943"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15943

`reaction.ecocyc.RXN-15943`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15943`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DIHYDROXY-ACETONE-PHOSPHATE + ACETYL-COA -> CPD0-2467 + CO-A; direction=RIGHT-TO-LEFT EcoCyc reaction equation: DIHYDROXY-ACETONE-PHOSPHATE + ACETYL-COA -> CPD0-2467 + CO-A; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by 3-hydroxy-2,4-pentadione 5-phosphate thiolase (complex.ecocyc.CPLX0-7820). Substrates: Acetyl-CoA (molecule.C00024), Glycerone phosphate (molecule.C00111). Products: CoA (molecule.C00010), 3-hydroxy-2,4-dioxopentyl phosphate (molecule.ecocyc.CPD0-2467).

## Enriched Pathways

- `ecocyc.PWY0-1569` autoinducer AI-2 degradation (EcoCyc)

## Annotation

DIHYDROXY-ACETONE-PHOSPHATE + ACETYL-COA -> CPD0-2467 + CO-A; direction=RIGHT-TO-LEFT

## Pathways

- `ecocyc.PWY0-1569` autoinducer AI-2 degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7820|complex.ecocyc.CPLX0-7820]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2467|molecule.ecocyc.CPD0-2467]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00111|molecule.C00111]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15943`

## Notes

DIHYDROXY-ACETONE-PHOSPHATE + ACETYL-COA -> CPD0-2467 + CO-A; direction=RIGHT-TO-LEFT
