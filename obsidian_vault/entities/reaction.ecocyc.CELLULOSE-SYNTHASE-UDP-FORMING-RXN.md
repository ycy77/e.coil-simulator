---
entity_id: "reaction.ecocyc.CELLULOSE-SYNTHASE-UDP-FORMING-RXN"
entity_type: "reaction"
name: "CELLULOSE-SYNTHASE-UDP-FORMING-RXN"
source_database: "EcoCyc"
source_id: "CELLULOSE-SYNTHASE-UDP-FORMING-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CELLULOSE-SYNTHASE-UDP-FORMING-RXN

`reaction.ecocyc.CELLULOSE-SYNTHASE-UDP-FORMING-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CELLULOSE-SYNTHASE-UDP-FORMING-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-12575 + CELLULOSE -> CELLULOSE + UDP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-12575 + CELLULOSE -> CELLULOSE + UDP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cellulose synthase (complex.ecocyc.CPLX0-8125). Substrates: UDP-glucose (molecule.C00029), Cellulose (molecule.C00760). Products: UDP (molecule.C00015), Cellulose (molecule.C00760).

## Annotation

CPD-12575 + CELLULOSE -> CELLULOSE + UDP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `activates` <-- [[molecule.C16463|molecule.C16463]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8125|complex.ecocyc.CPLX0-8125]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00760|molecule.C00760]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00029|molecule.C00029]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00760|molecule.C00760]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:CELLULOSE-SYNTHASE-UDP-FORMING-RXN`

## Notes

CPD-12575 + CELLULOSE -> CELLULOSE + UDP; direction=PHYSIOL-LEFT-TO-RIGHT
