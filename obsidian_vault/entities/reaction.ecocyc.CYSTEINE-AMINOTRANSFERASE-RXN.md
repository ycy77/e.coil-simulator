---
entity_id: "reaction.ecocyc.CYSTEINE-AMINOTRANSFERASE-RXN"
entity_type: "reaction"
name: "CYSTEINE-AMINOTRANSFERASE-RXN"
source_database: "EcoCyc"
source_id: "CYSTEINE-AMINOTRANSFERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CYSTEINE-AMINOTRANSFERASE-RXN

`reaction.ecocyc.CYSTEINE-AMINOTRANSFERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CYSTEINE-AMINOTRANSFERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-KETOGLUTARATE + CYS -> GLT + 3-MERCAPTO-PYRUVATE; direction=REVERSIBLE EcoCyc reaction equation: 2-KETOGLUTARATE + CYS -> GLT + 3-MERCAPTO-PYRUVATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by aspartate aminotransferase (complex.ecocyc.ASPAMINOTRANS-DIMER). Substrates: 2-Oxoglutarate (molecule.C00026), L-Cysteine (molecule.C00097). Products: L-Glutamate (molecule.C00025), Mercaptopyruvate (molecule.C00957).

## Enriched Pathways

- `ecocyc.PWY-5329` L-cysteine degradation III (EcoCyc)

## Annotation

2-KETOGLUTARATE + CYS -> GLT + 3-MERCAPTO-PYRUVATE; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY-5329` L-cysteine degradation III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ASPAMINOTRANS-DIMER|complex.ecocyc.ASPAMINOTRANS-DIMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00957|molecule.C00957]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:CYSTEINE-AMINOTRANSFERASE-RXN`

## Notes

2-KETOGLUTARATE + CYS -> GLT + 3-MERCAPTO-PYRUVATE; direction=REVERSIBLE
