---
entity_id: "reaction.ecocyc.RXN-7716"
entity_type: "reaction"
name: "RXN-7716"
source_database: "EcoCyc"
source_id: "RXN-7716"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-7716

`reaction.ecocyc.RXN-7716`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-7716`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Oxo-glutarate-dehydrogenase-DH-lipoyl + NAD -> Oxo-glutarate-dehydrogenase-lipoyl + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Oxo-glutarate-dehydrogenase-DH-lipoyl + NAD -> Oxo-glutarate-dehydrogenase-lipoyl + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lipoamide dehydrogenase (complex.ecocyc.E3-CPLX). Substrates: NAD+ (molecule.C00003), a [2-oxoglutarate dehydrogenase E2 protein] N6-dihydrolipoyl-L-lysine (molecule.ecocyc.Oxo-glutarate-dehydrogenase-DH-lipoyl). Products: NADH (molecule.C00004), H+ (molecule.C00080), a [2-oxoglutarate dehydrogenase E2 protein] N6-lipoyl-L-lysine (molecule.ecocyc.Oxo-glutarate-dehydrogenase-lipoyl).

## Enriched Pathways

- `ecocyc.PWY-5084` 2-oxoglutarate decarboxylation to succinyl-CoA (EcoCyc)

## Annotation

Oxo-glutarate-dehydrogenase-DH-lipoyl + NAD -> Oxo-glutarate-dehydrogenase-lipoyl + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5084` 2-oxoglutarate decarboxylation to succinyl-CoA (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.E3-CPLX|complex.ecocyc.E3-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Oxo-glutarate-dehydrogenase-lipoyl|molecule.ecocyc.Oxo-glutarate-dehydrogenase-lipoyl]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Oxo-glutarate-dehydrogenase-DH-lipoyl|molecule.ecocyc.Oxo-glutarate-dehydrogenase-DH-lipoyl]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-7716`

## Notes

Oxo-glutarate-dehydrogenase-DH-lipoyl + NAD -> Oxo-glutarate-dehydrogenase-lipoyl + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
