---
entity_id: "reaction.ecocyc.ALCOHOL-DEHYDROGENASE-NADPORNOP_-RXN"
entity_type: "reaction"
name: "ALCOHOL-DEHYDROGENASE-NADPORNOP+-RXN"
source_database: "EcoCyc"
source_id: "ALCOHOL-DEHYDROGENASE-NADPORNOP+-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Aldehyde reductase (NADPH)"
---

# ALCOHOL-DEHYDROGENASE-NADPORNOP+-RXN

`reaction.ecocyc.ALCOHOL-DEHYDROGENASE-NADPORNOP_-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ALCOHOL-DEHYDROGENASE-NADPORNOP+-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NADP + Alcohols -> Aldehydes + NADPH + PROTON; direction=REVERSIBLE EcoCyc reaction equation: NADP + Alcohols -> Aldehydes + NADPH + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by NADPH-dependent aldehyde reductase YqhD (complex.ecocyc.CPLX0-7667), NADPH-dependent aldehyde reductase Ahr (complex.ecocyc.CPLX0-8549), ybbO (protein.P0AFP4), yahK (protein.P75691). Substrates: NADP+ (molecule.C00006), an alcohol (molecule.ecocyc.Alcohols). Products: NADPH (molecule.C00005), Aldehyde (molecule.C00071), H+ (molecule.C00080).

## Annotation

NADP + Alcohols -> Aldehydes + NADPH + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7667|complex.ecocyc.CPLX0-7667]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8549|complex.ecocyc.CPLX0-8549]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AFP4|protein.P0AFP4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P75691|protein.P75691]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00071|molecule.C00071]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Alcohols|molecule.ecocyc.Alcohols]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ALCOHOL-DEHYDROGENASE-NADPORNOP+-RXN`

## Notes

NADP + Alcohols -> Aldehydes + NADPH + PROTON; direction=REVERSIBLE
