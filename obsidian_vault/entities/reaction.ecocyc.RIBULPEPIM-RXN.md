---
entity_id: "reaction.ecocyc.RIBULPEPIM-RXN"
entity_type: "reaction"
name: "RIBULPEPIM-RXN"
source_database: "EcoCyc"
source_id: "RIBULPEPIM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RIBULPEPIM-RXN

`reaction.ecocyc.RIBULPEPIM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:RIBULPEPIM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The third step of L-arabinose catabolism. EcoCyc reaction equation: L-RIBULOSE-5-P -> XYLULOSE-5-PHOSPHATE; direction=REVERSIBLE. The third step of L-arabinose catabolism.

## Biological Role

Catalyzed by L-ribulose-5-phosphate 4-epimerase AraD (complex.ecocyc.RIBULPEPIM-CPLX), sgbE (protein.P37680), ulaF (protein.P39306). Substrates: L-Ribulose 5-phosphate (molecule.C01101). Products: D-Xylulose 5-phosphate (molecule.C00231).

## Enriched Pathways

- `ecocyc.ARABCAT-PWY` L-arabinose degradation I (EcoCyc)
- `ecocyc.LYXMET-PWY` L-lyxose degradation (EcoCyc)
- `ecocyc.PWY-6961` L-ascorbate degradation II (bacterial, aerobic) (EcoCyc)
- `ecocyc.PWY0-301` L-ascorbate degradation I (bacterial, anaerobic) (EcoCyc)

## Annotation

The third step of L-arabinose catabolism.

## Pathways

- `ecocyc.ARABCAT-PWY` L-arabinose degradation I (EcoCyc)
- `ecocyc.LYXMET-PWY` L-lyxose degradation (EcoCyc)
- `ecocyc.PWY-6961` L-ascorbate degradation II (bacterial, aerobic) (EcoCyc)
- `ecocyc.PWY0-301` L-ascorbate degradation I (bacterial, anaerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.RIBULPEPIM-CPLX|complex.ecocyc.RIBULPEPIM-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P37680|protein.P37680]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P39306|protein.P39306]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00231|molecule.C00231]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01101|molecule.C01101]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RIBULPEPIM-RXN`

## Notes

L-RIBULOSE-5-P -> XYLULOSE-5-PHOSPHATE; direction=REVERSIBLE
