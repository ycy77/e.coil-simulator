---
entity_id: "reaction.ecocyc.RXN0-5388"
entity_type: "reaction"
name: "RXN0-5388"
source_database: "EcoCyc"
source_id: "RXN0-5388"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5388

`reaction.ecocyc.RXN0-5388`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5388`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Menaquinones + PROTON + NADH -> PROTON + Menaquinols + NAD; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Menaquinones + PROTON + NADH -> PROTON + Menaquinols + NAD; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by NADH:quinone oxidoreductase I (complex.ecocyc.NADH-DHI-CPLX). Substrates: NADH (molecule.C00004), H+ (molecule.C00080), Menaquinone (molecule.C00828). Products: NAD+ (molecule.C00003), H+ (molecule.C00080), Menaquinol (molecule.C05819).

## Enriched Pathways

- `ecocyc.PWY0-1336` NADH to fumarate electron transfer (EcoCyc)
- `ecocyc.PWY0-1347` NADH to trimethylamine N-oxide electron transfer (EcoCyc)
- `ecocyc.PWY0-1348` NADH to dimethyl sulfoxide electron transfer (EcoCyc)
- `ecocyc.PWY0-1352` nitrate reduction VIII (dissimilatory) (EcoCyc)
- `ecocyc.PWY0-1590` NADH to hydrogen peroxide electron transfer (EcoCyc)

## Annotation

Menaquinones + PROTON + NADH -> PROTON + Menaquinols + NAD; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1336` NADH to fumarate electron transfer (EcoCyc)
- `ecocyc.PWY0-1347` NADH to trimethylamine N-oxide electron transfer (EcoCyc)
- `ecocyc.PWY0-1348` NADH to dimethyl sulfoxide electron transfer (EcoCyc)
- `ecocyc.PWY0-1352` nitrate reduction VIII (dissimilatory) (EcoCyc)
- `ecocyc.PWY0-1590` NADH to hydrogen peroxide electron transfer (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.NADH-DHI-CPLX|complex.ecocyc.NADH-DHI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05819|molecule.C05819]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00828|molecule.C00828]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5388`

## Notes

Menaquinones + PROTON + NADH -> PROTON + Menaquinols + NAD; direction=LEFT-TO-RIGHT
