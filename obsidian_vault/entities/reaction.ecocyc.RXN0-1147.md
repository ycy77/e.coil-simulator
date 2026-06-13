---
entity_id: "reaction.ecocyc.RXN0-1147"
entity_type: "reaction"
name: "RXN0-1147"
source_database: "EcoCyc"
source_id: "RXN0-1147"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1147

`reaction.ecocyc.RXN0-1147`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1147`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

SUC-COA + Oxo-glutarate-dehydrogenase-DH-lipoyl -> CO-A + Oxo-glutarate-dehydro-suc-DH-lipoyl; direction=RIGHT-TO-LEFT EcoCyc reaction equation: SUC-COA + Oxo-glutarate-dehydrogenase-DH-lipoyl -> CO-A + Oxo-glutarate-dehydro-suc-DH-lipoyl; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by 2-oxoglutarate dehydrogenase E2 subunit (complex.ecocyc.E2O). Substrates: Succinyl-CoA (molecule.C00091), a [2-oxoglutarate dehydrogenase E2 protein] N6-dihydrolipoyl-L-lysine (molecule.ecocyc.Oxo-glutarate-dehydrogenase-DH-lipoyl). Products: CoA (molecule.C00010), a [2-oxoglutarate dehydrogenase E2 protein] N6-S-succinyldihydrolipoyl-L-lysine (molecule.ecocyc.Oxo-glutarate-dehydro-suc-DH-lipoyl).

## Enriched Pathways

- `ecocyc.PWY-5084` 2-oxoglutarate decarboxylation to succinyl-CoA (EcoCyc)

## Annotation

SUC-COA + Oxo-glutarate-dehydrogenase-DH-lipoyl -> CO-A + Oxo-glutarate-dehydro-suc-DH-lipoyl; direction=RIGHT-TO-LEFT

## Pathways

- `ecocyc.PWY-5084` 2-oxoglutarate decarboxylation to succinyl-CoA (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.E2O|complex.ecocyc.E2O]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Oxo-glutarate-dehydro-suc-DH-lipoyl|molecule.ecocyc.Oxo-glutarate-dehydro-suc-DH-lipoyl]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00091|molecule.C00091]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Oxo-glutarate-dehydrogenase-DH-lipoyl|molecule.ecocyc.Oxo-glutarate-dehydrogenase-DH-lipoyl]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1147`

## Notes

SUC-COA + Oxo-glutarate-dehydrogenase-DH-lipoyl -> CO-A + Oxo-glutarate-dehydro-suc-DH-lipoyl; direction=RIGHT-TO-LEFT
