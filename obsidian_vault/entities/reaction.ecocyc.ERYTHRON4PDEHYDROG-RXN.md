---
entity_id: "reaction.ecocyc.ERYTHRON4PDEHYDROG-RXN"
entity_type: "reaction"
name: "ERYTHRON4PDEHYDROG-RXN"
source_database: "EcoCyc"
source_id: "ERYTHRON4PDEHYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ERYTHRON4PDEHYDROG-RXN

`reaction.ecocyc.ERYTHRON4PDEHYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ERYTHRON4PDEHYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the de novo synthesis of pyridoxine and pyridoxal phosphate. EcoCyc reaction equation: ERYTHRONATE-4P + NAD -> PROTON + 3OH-4P-OH-ALPHA-KETOBUTYRATE + NADH; direction=LEFT-TO-RIGHT. This reaction is part of the de novo synthesis of pyridoxine and pyridoxal phosphate.

## Biological Role

Catalyzed by erythronate-4-phosphate dehydrogenase (complex.ecocyc.CPLX0-8212). Substrates: NAD+ (molecule.C00003), 4-Phospho-D-erythronate (molecule.C03393). Products: NADH (molecule.C00004), H+ (molecule.C00080), 2-Oxo-3-hydroxy-4-phosphobutanoate (molecule.C06054).

## Enriched Pathways

- `ecocyc.PYRIDOXSYN-PWY` pyridoxal 5'-phosphate biosynthesis I (EcoCyc)

## Annotation

This reaction is part of the de novo synthesis of pyridoxine and pyridoxal phosphate.

## Pathways

- `ecocyc.PYRIDOXSYN-PWY` pyridoxal 5'-phosphate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8212|complex.ecocyc.CPLX0-8212]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06054|molecule.C06054]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03393|molecule.C03393]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ERYTHRON4PDEHYDROG-RXN`

## Notes

ERYTHRONATE-4P + NAD -> PROTON + 3OH-4P-OH-ALPHA-KETOBUTYRATE + NADH; direction=LEFT-TO-RIGHT
