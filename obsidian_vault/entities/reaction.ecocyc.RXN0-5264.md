---
entity_id: "reaction.ecocyc.RXN0-5264"
entity_type: "reaction"
name: "Trimethylamine-N-oxide reductase (menaquinone)"
source_database: "EcoCyc"
source_id: "RXN0-5264"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "TMAO reductase"
  - "TOR"
---

# Trimethylamine-N-oxide reductase (menaquinone)

`reaction.ecocyc.RXN0-5264`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5264`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

TRIMETHYLAMINE-N-O + PROTON + Menaquinols -> Menaquinones + WATER + TRIMETHYLAMINE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: TRIMETHYLAMINE-N-O + PROTON + Menaquinols -> Menaquinones + WATER + TRIMETHYLAMINE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by menaquinol:trimethylamine N-oxide oxidoreductase I (complex.ecocyc.TMAOREDUCTI-CPLX). Substrates: H+ (molecule.C00080), Trimethylamine N-oxide (molecule.C01104), Menaquinol (molecule.C05819). Products: H2O (molecule.C00001), Trimethylamine (molecule.C00565), Menaquinone (molecule.C00828).

## Enriched Pathways

- `ecocyc.PWY0-1347` NADH to trimethylamine N-oxide electron transfer (EcoCyc)
- `ecocyc.PWY0-1355` formate to trimethylamine N-oxide electron transfer (EcoCyc)
- `ecocyc.PWY0-1578` hydrogen to trimethylamine N-oxide electron transfer (EcoCyc)

## Annotation

TRIMETHYLAMINE-N-O + PROTON + Menaquinols -> Menaquinones + WATER + TRIMETHYLAMINE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1347` NADH to trimethylamine N-oxide electron transfer (EcoCyc)
- `ecocyc.PWY0-1355` formate to trimethylamine N-oxide electron transfer (EcoCyc)
- `ecocyc.PWY0-1578` hydrogen to trimethylamine N-oxide electron transfer (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.TMAOREDUCTI-CPLX|complex.ecocyc.TMAOREDUCTI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00565|molecule.C00565]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00828|molecule.C00828]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01104|molecule.C01104]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05819|molecule.C05819]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5264`

## Notes

TRIMETHYLAMINE-N-O + PROTON + Menaquinols -> Menaquinones + WATER + TRIMETHYLAMINE; direction=LEFT-TO-RIGHT
