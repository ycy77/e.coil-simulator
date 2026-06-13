---
entity_id: "reaction.ecocyc.AMPSYN-RXN"
entity_type: "reaction"
name: "AMPSYN-RXN"
source_database: "EcoCyc"
source_id: "AMPSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# AMPSYN-RXN

`reaction.ecocyc.AMPSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:AMPSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The final step in the de novo biosynthesis of purines, the second of the two step sequence from IMP to AMP. EcoCyc reaction equation: ADENYLOSUCC -> FUM + AMP; direction=PHYSIOL-LEFT-TO-RIGHT. The final step in the de novo biosynthesis of purines, the second of the two step sequence from IMP to AMP.

## Biological Role

Catalyzed by adenylosuccinate lyase (complex.ecocyc.CPLX0-7959). Substrates: N6-(1,2-Dicarboxyethyl)-AMP (molecule.C03794). Products: AMP (molecule.C00020), Fumarate (molecule.C00122).

## Enriched Pathways

- `ecocyc.PWY-7219` adenosine ribonucleotides de novo biosynthesis (EcoCyc)

## Annotation

The final step in the de novo biosynthesis of purines, the second of the two step sequence from IMP to AMP.

## Pathways

- `ecocyc.PWY-7219` adenosine ribonucleotides de novo biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7959|complex.ecocyc.CPLX0-7959]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00122|molecule.C00122]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C03794|molecule.C03794]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:AMPSYN-RXN`

## Notes

ADENYLOSUCC -> FUM + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
