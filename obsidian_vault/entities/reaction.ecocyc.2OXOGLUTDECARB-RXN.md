---
entity_id: "reaction.ecocyc.2OXOGLUTDECARB-RXN"
entity_type: "reaction"
name: "2OXOGLUTDECARB-RXN"
source_database: "EcoCyc"
source_id: "2OXOGLUTDECARB-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "2-oxoglutarate decarboxylation"
  - "Oxoglutarate decarboxylase"
---

# 2OXOGLUTDECARB-RXN

`reaction.ecocyc.2OXOGLUTDECARB-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2OXOGLUTDECARB-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-KETOGLUTARATE + Oxo-glutarate-dehydrogenase-lipoyl + PROTON -> Oxo-glutarate-dehydro-suc-DH-lipoyl + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: 2-KETOGLUTARATE + Oxo-glutarate-dehydrogenase-lipoyl + PROTON -> Oxo-glutarate-dehydro-suc-DH-lipoyl + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 2-oxoglutarate decarboxylase, thiamine-requiring (complex.ecocyc.E1O). Substrates: 2-Oxoglutarate (molecule.C00026), H+ (molecule.C00080), a [2-oxoglutarate dehydrogenase E2 protein] N6-lipoyl-L-lysine (molecule.ecocyc.Oxo-glutarate-dehydrogenase-lipoyl). Products: CO2 (molecule.C00011), a [2-oxoglutarate dehydrogenase E2 protein] N6-S-succinyldihydrolipoyl-L-lysine (molecule.ecocyc.Oxo-glutarate-dehydro-suc-DH-lipoyl).

## Enriched Pathways

- `ecocyc.PWY-5084` 2-oxoglutarate decarboxylation to succinyl-CoA (EcoCyc)

## Annotation

2-KETOGLUTARATE + Oxo-glutarate-dehydrogenase-lipoyl + PROTON -> Oxo-glutarate-dehydro-suc-DH-lipoyl + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5084` 2-oxoglutarate decarboxylation to succinyl-CoA (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.E1O|complex.ecocyc.E1O]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Oxo-glutarate-dehydro-suc-DH-lipoyl|molecule.ecocyc.Oxo-glutarate-dehydro-suc-DH-lipoyl]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Oxo-glutarate-dehydrogenase-lipoyl|molecule.ecocyc.Oxo-glutarate-dehydrogenase-lipoyl]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:2OXOGLUTDECARB-RXN`

## Notes

2-KETOGLUTARATE + Oxo-glutarate-dehydrogenase-lipoyl + PROTON -> Oxo-glutarate-dehydro-suc-DH-lipoyl + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT
