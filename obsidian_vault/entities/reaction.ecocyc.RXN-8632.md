---
entity_id: "reaction.ecocyc.RXN-8632"
entity_type: "reaction"
name: "RXN-8632"
source_database: "EcoCyc"
source_id: "RXN-8632"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-8632

`reaction.ecocyc.RXN-8632`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8632`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROPANE-1-2-DIOL + NAD -> ACETOL + NADH + PROTON; direction=REVERSIBLE EcoCyc reaction equation: PROPANE-1-2-DIOL + NAD -> ACETOL + NADH + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by L-1,2-propanediol dehydrogenase / glycerol dehydrogenase (complex.ecocyc.GLYCDEH-CPLX). Substrates: NAD+ (molecule.C00003), (S)-propane-1,2-diol (molecule.ecocyc.PROPANE-1-2-DIOL). Products: NADH (molecule.C00004), H+ (molecule.C00080), Hydroxyacetone (molecule.C05235).

## Enriched Pathways

- `ecocyc.PWY-5453` methylglyoxal degradation III (EcoCyc)

## Annotation

PROPANE-1-2-DIOL + NAD -> ACETOL + NADH + PROTON; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY-5453` methylglyoxal degradation III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.GLYCDEH-CPLX|complex.ecocyc.GLYCDEH-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05235|molecule.C05235]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.PROPANE-1-2-DIOL|molecule.ecocyc.PROPANE-1-2-DIOL]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8632`

## Notes

PROPANE-1-2-DIOL + NAD -> ACETOL + NADH + PROTON; direction=REVERSIBLE
