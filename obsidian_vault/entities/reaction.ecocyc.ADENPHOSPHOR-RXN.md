---
entity_id: "reaction.ecocyc.ADENPHOSPHOR-RXN"
entity_type: "reaction"
name: "ADENPHOSPHOR-RXN"
source_database: "EcoCyc"
source_id: "ADENPHOSPHOR-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ADENPHOSPHOR-RXN

`reaction.ecocyc.ADENPHOSPHOR-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ADENPHOSPHOR-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ADENOSINE + Pi -> RIBOSE-1P + ADENINE; direction=REVERSIBLE EcoCyc reaction equation: ADENOSINE + Pi -> RIBOSE-1P + ADENINE; direction=REVERSIBLE.

## Biological Role

Catalyzed by nucleoside phosphorylase PpnP (complex.ecocyc.CPLX0-8619), purine nucleoside phosphorylase (complex.ecocyc.DEOD-CPLX), yfiH (protein.P33644). Substrates: Adenosine (molecule.C00212), phosphate (molecule.ecocyc.Pi). Products: Adenine (molecule.C00147), alpha-D-Ribose 1-phosphate (molecule.C00620).

## Enriched Pathways

- `ecocyc.PWY-6609` adenine and adenosine salvage III (EcoCyc)
- `ecocyc.PWY-6611` adenine and adenosine salvage V (EcoCyc)
- `ecocyc.PWY0-1296` purine ribonucleosides degradation (EcoCyc)

## Annotation

ADENOSINE + Pi -> RIBOSE-1P + ADENINE; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY-6609` adenine and adenosine salvage III (EcoCyc)
- `ecocyc.PWY-6611` adenine and adenosine salvage V (EcoCyc)
- `ecocyc.PWY0-1296` purine ribonucleosides degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8619|complex.ecocyc.CPLX0-8619]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.DEOD-CPLX|complex.ecocyc.DEOD-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P33644|protein.P33644]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00147|molecule.C00147]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00620|molecule.C00620]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00212|molecule.C00212]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ADENPHOSPHOR-RXN`

## Notes

ADENOSINE + Pi -> RIBOSE-1P + ADENINE; direction=REVERSIBLE
