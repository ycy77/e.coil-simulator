---
entity_id: "reaction.ecocyc.ACETYLORNTRANSAM-RXN"
entity_type: "reaction"
name: "ACETYLORNTRANSAM-RXN"
source_database: "EcoCyc"
source_id: "ACETYLORNTRANSAM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ACETYLORNTRANSAM-RXN

`reaction.ecocyc.ACETYLORNTRANSAM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ACETYLORNTRANSAM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the fourth step in arginine biosynthesis. EcoCyc reaction equation: N-ALPHA-ACETYLORNITHINE + 2-KETOGLUTARATE -> CPD-469 + GLT; direction=REVERSIBLE. This is the fourth step in arginine biosynthesis.

## Biological Role

Catalyzed by N-acetylornithine aminotransferase / N-succinyldiaminopimelate aminotransferase (complex.ecocyc.ACETYLORNTRANSAM-CPLX), 4-aminobutyrate aminotransferase GabT (complex.ecocyc.GABATRANSAM-CPLX), succinylornithine transaminase (complex.ecocyc.SUCCORNTRANSAM-CPLX). Substrates: 2-Oxoglutarate (molecule.C00026), N-Acetylornithine (molecule.C00437). Products: L-Glutamate (molecule.C00025), N-Acetyl-L-glutamate 5-semialdehyde (molecule.C01250).

## Enriched Pathways

- `ecocyc.GLUTORN-PWY` L-ornithine biosynthesis I (EcoCyc)

## Annotation

This is the fourth step in arginine biosynthesis.

## Pathways

- `ecocyc.GLUTORN-PWY` L-ornithine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.ACETYLORNTRANSAM-CPLX|complex.ecocyc.ACETYLORNTRANSAM-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.GABATRANSAM-CPLX|complex.ecocyc.GABATRANSAM-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.SUCCORNTRANSAM-CPLX|complex.ecocyc.SUCCORNTRANSAM-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01250|molecule.C01250]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00437|molecule.C00437]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Sulfhydryl-Reagents|molecule.ecocyc.Sulfhydryl-Reagents]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ACETYLORNTRANSAM-RXN`

## Notes

N-ALPHA-ACETYLORNITHINE + 2-KETOGLUTARATE -> CPD-469 + GLT; direction=REVERSIBLE
