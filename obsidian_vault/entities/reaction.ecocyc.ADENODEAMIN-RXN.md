---
entity_id: "reaction.ecocyc.ADENODEAMIN-RXN"
entity_type: "reaction"
name: "ADENODEAMIN-RXN"
source_database: "EcoCyc"
source_id: "ADENODEAMIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ADENODEAMIN-RXN

`reaction.ecocyc.ADENODEAMIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ADENODEAMIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of nucleotide metabolism. EcoCyc reaction equation: PROTON + WATER + ADENOSINE -> AMMONIUM + INOSINE; direction=LEFT-TO-RIGHT. This reaction is part of nucleotide metabolism.

## Biological Role

Catalyzed by add (protein.P22333), yfiH (protein.P33644). Substrates: H2O (molecule.C00001), H+ (molecule.C00080), Adenosine (molecule.C00212). Products: Inosine (molecule.C00294), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.PWY-6609` adenine and adenosine salvage III (EcoCyc)
- `ecocyc.PWY-6611` adenine and adenosine salvage V (EcoCyc)
- `ecocyc.PWY0-1296` purine ribonucleosides degradation (EcoCyc)
- `ecocyc.SALVADEHYPOX-PWY` adenosine nucleotides degradation II (EcoCyc)

## Annotation

This reaction is part of nucleotide metabolism.

## Pathways

- `ecocyc.PWY-6609` adenine and adenosine salvage III (EcoCyc)
- `ecocyc.PWY-6611` adenine and adenosine salvage V (EcoCyc)
- `ecocyc.PWY0-1296` purine ribonucleosides degradation (EcoCyc)
- `ecocyc.SALVADEHYPOX-PWY` adenosine nucleotides degradation II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P22333|protein.P22333]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P33644|protein.P33644]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00294|molecule.C00294]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00212|molecule.C00212]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.COFORMYCIN|molecule.ecocyc.COFORMYCIN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ADENODEAMIN-RXN`

## Notes

PROTON + WATER + ADENOSINE -> AMMONIUM + INOSINE; direction=LEFT-TO-RIGHT
