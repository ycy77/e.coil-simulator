---
entity_id: "reaction.ecocyc.ADENYLOSUCCINATE-SYNTHASE-RXN"
entity_type: "reaction"
name: "ADENYLOSUCCINATE-SYNTHASE-RXN"
source_database: "EcoCyc"
source_id: "ADENYLOSUCCINATE-SYNTHASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "IMP-ASPARTATE LIGASE"
---

# ADENYLOSUCCINATE-SYNTHASE-RXN

`reaction.ecocyc.ADENYLOSUCCINATE-SYNTHASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ADENYLOSUCCINATE-SYNTHASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first committed step in AMP biosynthesis, converting IMP to AMP. EcoCyc reaction equation: L-ASPARTATE + IMP + GTP -> PROTON + ADENYLOSUCC + Pi + GDP; direction=PHYSIOL-LEFT-TO-RIGHT. This is the first committed step in AMP biosynthesis, converting IMP to AMP.

## Biological Role

Catalyzed by adenylosuccinate synthetase (complex.ecocyc.ADENYLOSUCCINATE-SYN-DIMER). Substrates: GTP (molecule.C00044), L-Aspartate (molecule.C00049), IMP (molecule.C00130). Products: GDP (molecule.C00035), H+ (molecule.C00080), N6-(1,2-Dicarboxyethyl)-AMP (molecule.C03794), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-7219` adenosine ribonucleotides de novo biosynthesis (EcoCyc)

## Annotation

This is the first committed step in AMP biosynthesis, converting IMP to AMP.

## Pathways

- `ecocyc.PWY-7219` adenosine ribonucleotides de novo biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.ADENYLOSUCCINATE-SYN-DIMER|complex.ecocyc.ADENYLOSUCCINATE-SYN-DIMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03794|molecule.C03794]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00130|molecule.C00130]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01228|molecule.C01228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1055|molecule.ecocyc.CPD0-1055]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ADENYLOSUCCINATE-SYNTHASE-RXN`

## Notes

L-ASPARTATE + IMP + GTP -> PROTON + ADENYLOSUCC + Pi + GDP; direction=PHYSIOL-LEFT-TO-RIGHT
