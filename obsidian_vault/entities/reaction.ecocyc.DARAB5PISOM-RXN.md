---
entity_id: "reaction.ecocyc.DARAB5PISOM-RXN"
entity_type: "reaction"
name: "DARAB5PISOM-RXN"
source_database: "EcoCyc"
source_id: "DARAB5PISOM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DARAB5PISOM-RXN

`reaction.ecocyc.DARAB5PISOM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DARAB5PISOM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction interconverts D-arabinose-5-phosphate and D-ribulose-5-phosphate. D-arabinose-5-phosphate is a precursor to KDO. EcoCyc reaction equation: ARABINOSE-5P -> RIBULOSE-5P; direction=REVERSIBLE. This reaction interconverts D-arabinose-5-phosphate and D-ribulose-5-phosphate. D-arabinose-5-phosphate is a precursor to KDO.

## Biological Role

Catalyzed by D-arabinose 5-phosphate isomerase KdsD (complex.ecocyc.CPLX0-1262), D-arabinose 5-phosphate isomerase GutQ (complex.ecocyc.CPLX0-3929). Substrates: D-Arabinose 5-phosphate (molecule.C01112). Products: D-Ribulose 5-phosphate (molecule.C00199).

## Enriched Pathways

- `ecocyc.PWY-1269` CMP-3-deoxy-D-manno-octulosonate biosynthesis (EcoCyc)

## Annotation

This reaction interconverts D-arabinose-5-phosphate and D-ribulose-5-phosphate. D-arabinose-5-phosphate is a precursor to KDO.

## Pathways

- `ecocyc.PWY-1269` CMP-3-deoxy-D-manno-octulosonate biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1262|complex.ecocyc.CPLX0-1262]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-3929|complex.ecocyc.CPLX0-3929]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00199|molecule.C00199]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01112|molecule.C01112]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CD_2|molecule.ecocyc.CD_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HG_2|molecule.ecocyc.HG_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DARAB5PISOM-RXN`

## Notes

ARABINOSE-5P -> RIBULOSE-5P; direction=REVERSIBLE
