---
entity_id: "reaction.ecocyc.DARABALDOL-RXN"
entity_type: "reaction"
name: "DARABALDOL-RXN"
source_database: "EcoCyc"
source_id: "DARABALDOL-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DARABALDOL-RXN

`reaction.ecocyc.DARABALDOL-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DARABALDOL-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the third reaction in the metabolism of D-arabinose in E. coli K-12 through utilization of the L-fucose catabolism pathway enzymes. EcoCyc reaction equation: D-RIBULOSE-1-P -> GLYCOLALDEHYDE + DIHYDROXY-ACETONE-PHOSPHATE; direction=REVERSIBLE. This is the third reaction in the metabolism of D-arabinose in E. coli K-12 through utilization of the L-fucose catabolism pathway enzymes.

## Biological Role

Catalyzed by L-fuculose-phosphate aldolase (complex.ecocyc.CPLX0-7633). Substrates: D-Ribulose 1-phosphate (molecule.C22337). Products: Glycerone phosphate (molecule.C00111), Glycolaldehyde (molecule.C00266).

## Enriched Pathways

- `ecocyc.DARABCATK12-PWY` D-arabinose degradation II (EcoCyc)

## Annotation

This is the third reaction in the metabolism of D-arabinose in E. coli K-12 through utilization of the L-fucose catabolism pathway enzymes.

## Pathways

- `ecocyc.DARABCATK12-PWY` D-arabinose degradation II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7633|complex.ecocyc.CPLX0-7633]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00111|molecule.C00111]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00266|molecule.C00266]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C22337|molecule.C22337]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1102|molecule.ecocyc.CPD0-1102]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DARABALDOL-RXN`

## Notes

D-RIBULOSE-1-P -> GLYCOLALDEHYDE + DIHYDROXY-ACETONE-PHOSPHATE; direction=REVERSIBLE
