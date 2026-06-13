---
entity_id: "reaction.ecocyc.DIMETHUROPORDEHYDROG-RXN"
entity_type: "reaction"
name: "DIMETHUROPORDEHYDROG-RXN"
source_database: "EcoCyc"
source_id: "DIMETHUROPORDEHYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DIMETHUROPORDEHYDROG-RXN

`reaction.ecocyc.DIMETHUROPORDEHYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DIMETHUROPORDEHYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is necessary for the synthesis of siroheme, which is an important and novel prosthetic group in the sulfite reductase reaction in the cysteine biosynthesis pathway and also in nitrate reductase. EcoCyc reaction equation: DIHYDROSIROHYDROCHLORIN + NAD -> PROTON + SIROHYDROCHLORIN + NADH; direction=LEFT-TO-RIGHT. This reaction is necessary for the synthesis of siroheme, which is an important and novel prosthetic group in the sulfite reductase reaction in the cysteine biosynthesis pathway and also in nitrate reductase.

## Biological Role

Catalyzed by siroheme synthase (complex.ecocyc.SIROHEMESYN-CPLX). Substrates: NAD+ (molecule.C00003), Precorrin 2 (molecule.C02463). Products: NADH (molecule.C00004), H+ (molecule.C00080), Sirohydrochlorin (molecule.C05778).

## Enriched Pathways

- `ecocyc.PWY-5194` siroheme biosynthesis (EcoCyc)

## Annotation

This reaction is necessary for the synthesis of siroheme, which is an important and novel prosthetic group in the sulfite reductase reaction in the cysteine biosynthesis pathway and also in nitrate reductase.

## Pathways

- `ecocyc.PWY-5194` siroheme biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.SIROHEMESYN-CPLX|complex.ecocyc.SIROHEMESYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05778|molecule.C05778]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02463|molecule.C02463]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DIMETHUROPORDEHYDROG-RXN`

## Notes

DIHYDROSIROHYDROCHLORIN + NAD -> PROTON + SIROHYDROCHLORIN + NADH; direction=LEFT-TO-RIGHT
