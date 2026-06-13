---
entity_id: "reaction.ecocyc.INOPHOSPHOR-RXN"
entity_type: "reaction"
name: "INOPHOSPHOR-RXN"
source_database: "EcoCyc"
source_id: "INOPHOSPHOR-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# INOPHOSPHOR-RXN

`reaction.ecocyc.INOPHOSPHOR-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:INOPHOSPHOR-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

INOSINE + Pi -> RIBOSE-1P + HYPOXANTHINE; direction=REVERSIBLE EcoCyc reaction equation: INOSINE + Pi -> RIBOSE-1P + HYPOXANTHINE; direction=REVERSIBLE.

## Biological Role

Catalyzed by nucleoside phosphorylase PpnP (complex.ecocyc.CPLX0-8619), purine nucleoside phosphorylase (complex.ecocyc.DEOD-CPLX), xanthosine phosphorylase (complex.ecocyc.XANTHOSINEPHOSPHORY-CPLX), yfiH (protein.P33644). Substrates: Inosine (molecule.C00294), phosphate (molecule.ecocyc.Pi). Products: Hypoxanthine (molecule.C00262), alpha-D-Ribose 1-phosphate (molecule.C00620).

## Enriched Pathways

- `ecocyc.PWY-6609` adenine and adenosine salvage III (EcoCyc)
- `ecocyc.PWY0-1296` purine ribonucleosides degradation (EcoCyc)
- `ecocyc.SALVADEHYPOX-PWY` adenosine nucleotides degradation II (EcoCyc)

## Annotation

INOSINE + Pi -> RIBOSE-1P + HYPOXANTHINE; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY-6609` adenine and adenosine salvage III (EcoCyc)
- `ecocyc.PWY0-1296` purine ribonucleosides degradation (EcoCyc)
- `ecocyc.SALVADEHYPOX-PWY` adenosine nucleotides degradation II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8619|complex.ecocyc.CPLX0-8619]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.DEOD-CPLX|complex.ecocyc.DEOD-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.XANTHOSINEPHOSPHORY-CPLX|complex.ecocyc.XANTHOSINEPHOSPHORY-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P33644|protein.P33644]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00262|molecule.C00262]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00620|molecule.C00620]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00294|molecule.C00294]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1045|molecule.ecocyc.CPD0-1045]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1653|molecule.ecocyc.CPD0-1653]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.FORMYCIN-A|molecule.ecocyc.FORMYCIN-A]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:INOPHOSPHOR-RXN`

## Notes

INOSINE + Pi -> RIBOSE-1P + HYPOXANTHINE; direction=REVERSIBLE
