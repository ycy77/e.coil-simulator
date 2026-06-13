---
entity_id: "reaction.ecocyc.ISOCITDEH-RXN"
entity_type: "reaction"
name: "ISOCITDEH-RXN"
source_database: "EcoCyc"
source_id: "ISOCITDEH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "threo-D(s)-isocitrate oxidoreductase (decarboxylating)"
---

# ISOCITDEH-RXN

`reaction.ecocyc.ISOCITDEH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ISOCITDEH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

THREO-DS-ISO-CITRATE + NADP -> NADPH + 2-KETOGLUTARATE + CARBON-DIOXIDE; direction=REVERSIBLE EcoCyc reaction equation: THREO-DS-ISO-CITRATE + NADP -> NADPH + 2-KETOGLUTARATE + CARBON-DIOXIDE; direction=REVERSIBLE.

## Biological Role

Catalyzed by isocitrate dehydrogenase (complex.ecocyc.ISOCITHASE-CPLX). Substrates: NADP+ (molecule.C00006), D-threo-isocitrate (molecule.ecocyc.THREO-DS-ISO-CITRATE). Products: NADPH (molecule.C00005), CO2 (molecule.C00011), 2-Oxoglutarate (molecule.C00026).

## Enriched Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.TCA` TCA cycle I (prokaryotic) (EcoCyc)

## Annotation

THREO-DS-ISO-CITRATE + NADP -> NADPH + 2-KETOGLUTARATE + CARBON-DIOXIDE; direction=REVERSIBLE

## Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.TCA` TCA cycle I (prokaryotic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.ISOCITHASE-CPLX|complex.ecocyc.ISOCITHASE-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.THREO-DS-ISO-CITRATE|molecule.ecocyc.THREO-DS-ISO-CITRATE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00048|molecule.C00048]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01990|molecule.C01990]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PHENYLGLYOXAL|molecule.ecocyc.PHENYLGLYOXAL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ISOCITDEH-RXN`

## Notes

THREO-DS-ISO-CITRATE + NADP -> NADPH + 2-KETOGLUTARATE + CARBON-DIOXIDE; direction=REVERSIBLE
