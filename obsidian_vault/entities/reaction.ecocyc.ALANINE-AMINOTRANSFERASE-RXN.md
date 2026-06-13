---
entity_id: "reaction.ecocyc.ALANINE-AMINOTRANSFERASE-RXN"
entity_type: "reaction"
name: "ALANINE-AMINOTRANSFERASE-RXN"
source_database: "EcoCyc"
source_id: "ALANINE-AMINOTRANSFERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Glutamic--pyruvic transaminase"
  - "Glutamic--alanine transaminase"
---

# ALANINE-AMINOTRANSFERASE-RXN

`reaction.ecocyc.ALANINE-AMINOTRANSFERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ALANINE-AMINOTRANSFERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-KETOGLUTARATE + L-ALPHA-ALANINE -> GLT + PYRUVATE; direction=REVERSIBLE EcoCyc reaction equation: 2-KETOGLUTARATE + L-ALPHA-ALANINE -> GLT + PYRUVATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by glutamate—pyruvate aminotransferase AlaC (complex.ecocyc.CPLX0-7887), glutamate—pyruvate aminotransferase AlaA (complex.ecocyc.CPLX0-7888), glutamate—pyruvate aminotransferase AlaB (protein.ecocyc.MONOMER0-1241). Substrates: 2-Oxoglutarate (molecule.C00026), L-Alanine (molecule.C00041). Products: Pyruvate (molecule.C00022), L-Glutamate (molecule.C00025).

## Enriched Pathways

- `ecocyc.ALANINE-SYN2-PWY` L-alanine biosynthesis II (EcoCyc)

## Annotation

2-KETOGLUTARATE + L-ALPHA-ALANINE -> GLT + PYRUVATE; direction=REVERSIBLE

## Pathways

- `ecocyc.ALANINE-SYN2-PWY` L-alanine biosynthesis II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7887|complex.ecocyc.CPLX0-7887]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7888|complex.ecocyc.CPLX0-7888]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.ecocyc.MONOMER0-1241|protein.ecocyc.MONOMER0-1241]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ALANINE-AMINOTRANSFERASE-RXN`

## Notes

2-KETOGLUTARATE + L-ALPHA-ALANINE -> GLT + PYRUVATE; direction=REVERSIBLE
