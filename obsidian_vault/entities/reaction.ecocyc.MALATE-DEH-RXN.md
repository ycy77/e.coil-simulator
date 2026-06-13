---
entity_id: "reaction.ecocyc.MALATE-DEH-RXN"
entity_type: "reaction"
name: "MALATE-DEH-RXN"
source_database: "EcoCyc"
source_id: "MALATE-DEH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "MALIC DEHYDROGENASE"
---

# MALATE-DEH-RXN

`reaction.ecocyc.MALATE-DEH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:MALATE-DEH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

MAL + NAD -> PROTON + OXALACETIC_ACID + NADH; direction=REVERSIBLE EcoCyc reaction equation: MAL + NAD -> PROTON + OXALACETIC_ACID + NADH; direction=REVERSIBLE.

## Biological Role

Catalyzed by malate dehydrogenase (complex.ecocyc.MALATE-DEHASE). Substrates: NAD+ (molecule.C00003), (S)-Malate (molecule.C00149). Products: NADH (molecule.C00004), Oxaloacetate (molecule.C00036), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.GLUCONEO-PWY` gluconeogenesis I (EcoCyc)
- `ecocyc.GLYOXYLATE-BYPASS` glyoxylate cycle (EcoCyc)
- `ecocyc.TCA` TCA cycle I (prokaryotic) (EcoCyc)

## Annotation

MAL + NAD -> PROTON + OXALACETIC_ACID + NADH; direction=REVERSIBLE

## Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.GLUCONEO-PWY` gluconeogenesis I (EcoCyc)
- `ecocyc.GLYOXYLATE-BYPASS` glyoxylate cycle (EcoCyc)
- `ecocyc.TCA` TCA cycle I (prokaryotic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.MALATE-DEHASE|complex.ecocyc.MALATE-DEHASE]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00149|molecule.C00149]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:MALATE-DEH-RXN`

## Notes

MAL + NAD -> PROTON + OXALACETIC_ACID + NADH; direction=REVERSIBLE
