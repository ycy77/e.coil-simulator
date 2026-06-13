---
entity_id: "reaction.ecocyc.ALARACECAT-RXN"
entity_type: "reaction"
name: "ALARACECAT-RXN"
source_database: "EcoCyc"
source_id: "ALARACECAT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ALARACECAT-RXN

`reaction.ecocyc.ALARACECAT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ALARACECAT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-ALPHA-ALANINE -> D-ALANINE; direction=REVERSIBLE EcoCyc reaction equation: L-ALPHA-ALANINE -> D-ALANINE; direction=REVERSIBLE.

## Biological Role

Catalyzed by alanine racemase 2 (complex.ecocyc.CPLX0-7465), negative regulator of MalT activity/cystathionine β-lyase (complex.ecocyc.CPLX0-8092), alanine racemase 1 (complex.ecocyc.CPLX0-8202), cystathionine β-lyase / L-cysteine desulfhydrase / alanine racemase (complex.ecocyc.CYSTATHIONINE-BETA-LYASE-CPLX). Substrates: L-Alanine (molecule.C00041). Products: D-Alanine (molecule.C00133).

## Enriched Pathways

- `ecocyc.ALADEG-PWY` L-alanine degradation I (EcoCyc)
- `ecocyc.PWY-8072` alanine racemization (EcoCyc)

## Annotation

L-ALPHA-ALANINE -> D-ALANINE; direction=REVERSIBLE

## Pathways

- `ecocyc.ALADEG-PWY` L-alanine degradation I (EcoCyc)
- `ecocyc.PWY-8072` alanine racemization (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7465|complex.ecocyc.CPLX0-7465]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8092|complex.ecocyc.CPLX0-8092]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8202|complex.ecocyc.CPLX0-8202]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CYSTATHIONINE-BETA-LYASE-CPLX|complex.ecocyc.CYSTATHIONINE-BETA-LYASE-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00133|molecule.C00133]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-2482|molecule.ecocyc.CPD-2482]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-2483|molecule.ecocyc.CPD-2483]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1475|molecule.ecocyc.CPD0-1475]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.GLYCYLGLYCINE|molecule.ecocyc.GLYCYLGLYCINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ALARACECAT-RXN`

## Notes

L-ALPHA-ALANINE -> D-ALANINE; direction=REVERSIBLE
