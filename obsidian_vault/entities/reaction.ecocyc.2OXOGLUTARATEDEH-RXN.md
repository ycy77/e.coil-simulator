---
entity_id: "reaction.ecocyc.2OXOGLUTARATEDEH-RXN"
entity_type: "reaction"
name: "2-oxoglutarate dehydrogenase complex"
source_database: "EcoCyc"
source_id: "2OXOGLUTARATEDEH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "2-oxoglutarate dehydrogenation"
  - "&alpha"
  - "-ketoglutarate oxidative   decarboxylation"
---

# 2-oxoglutarate dehydrogenase complex

`reaction.ecocyc.2OXOGLUTARATEDEH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2OXOGLUTARATEDEH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-KETOGLUTARATE + CO-A + NAD -> SUC-COA + CARBON-DIOXIDE + NADH; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 2-KETOGLUTARATE + CO-A + NAD -> SUC-COA + CARBON-DIOXIDE + NADH; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 2-oxoglutarate dehydrogenase complex (complex.ecocyc.2OXOGLUTARATEDEH-CPLX). Substrates: NAD+ (molecule.C00003), CoA (molecule.C00010), 2-Oxoglutarate (molecule.C00026). Products: NADH (molecule.C00004), CO2 (molecule.C00011), Succinyl-CoA (molecule.C00091).

## Enriched Pathways

- `ecocyc.TCA` TCA cycle I (prokaryotic) (EcoCyc)

## Annotation

2-KETOGLUTARATE + CO-A + NAD -> SUC-COA + CARBON-DIOXIDE + NADH; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.TCA` TCA cycle I (prokaryotic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.2OXOGLUTARATEDEH-CPLX|complex.ecocyc.2OXOGLUTARATEDEH-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00091|molecule.C00091]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2OXOGLUTARATEDEH-RXN`

## Notes

2-KETOGLUTARATE + CO-A + NAD -> SUC-COA + CARBON-DIOXIDE + NADH; direction=PHYSIOL-LEFT-TO-RIGHT
