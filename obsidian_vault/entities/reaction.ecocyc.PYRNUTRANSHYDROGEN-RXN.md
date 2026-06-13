---
entity_id: "reaction.ecocyc.PYRNUTRANSHYDROGEN-RXN"
entity_type: "reaction"
name: "PYRNUTRANSHYDROGEN-RXN"
source_database: "EcoCyc"
source_id: "PYRNUTRANSHYDROGEN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PYRNUTRANSHYDROGEN-RXN

`reaction.ecocyc.PYRNUTRANSHYDROGEN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PYRNUTRANSHYDROGEN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NAD + NADPH -> NADH + NADP; direction=REVERSIBLE EcoCyc reaction equation: NAD + NADPH -> NADH + NADP; direction=REVERSIBLE.

## Biological Role

Catalyzed by soluble pyridine nucleotide transhydrogenase (complex.ecocyc.UDHA-CPLX). Substrates: NAD+ (molecule.C00003), NADPH (molecule.C00005). Products: NADH (molecule.C00004), NADP+ (molecule.C00006).

## Annotation

NAD + NADPH -> NADH + NADP; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.UDHA-CPLX|complex.ecocyc.UDHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PYRNUTRANSHYDROGEN-RXN`

## Notes

NAD + NADPH -> NADH + NADP; direction=REVERSIBLE
