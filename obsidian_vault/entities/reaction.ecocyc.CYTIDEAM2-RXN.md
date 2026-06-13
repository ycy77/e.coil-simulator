---
entity_id: "reaction.ecocyc.CYTIDEAM2-RXN"
entity_type: "reaction"
name: "CYTIDEAM2-RXN"
source_database: "EcoCyc"
source_id: "CYTIDEAM2-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CYTIDEAM2-RXN

`reaction.ecocyc.CYTIDEAM2-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CYTIDEAM2-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the pyrimidine salvage pathway. The enzyme converts exogenous and endogenous cytidine and 2'-deoxycytidine to the corresponding uracil nucleosides. Using this reaction, cytidine may also serve as a carbon source. EcoCyc reaction equation: PROTON + WATER + CYTIDINE -> URIDINE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of the pyrimidine salvage pathway. The enzyme converts exogenous and endogenous cytidine and 2'-deoxycytidine to the corresponding uracil nucleosides. Using this reaction, cytidine may also serve as a carbon source.

## Biological Role

Catalyzed by cytidine/deoxycytidine deaminase (complex.ecocyc.CYTIDEAM-CPLX). Substrates: H2O (molecule.C00001), H+ (molecule.C00080), Cytidine (molecule.C00475). Products: Uridine (molecule.C00299), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.PWY-6556` pyrimidine ribonucleosides salvage II (EcoCyc)
- `ecocyc.PWY-7193` pyrimidine ribonucleosides salvage I (EcoCyc)
- `ecocyc.PWY0-1295` pyrimidine ribonucleosides degradation (EcoCyc)
- `ecocyc.PWY0-163` salvage pathways of pyrimidine ribonucleotides (EcoCyc)

## Annotation

This reaction is part of the pyrimidine salvage pathway. The enzyme converts exogenous and endogenous cytidine and 2'-deoxycytidine to the corresponding uracil nucleosides. Using this reaction, cytidine may also serve as a carbon source.

## Pathways

- `ecocyc.PWY-6556` pyrimidine ribonucleosides salvage II (EcoCyc)
- `ecocyc.PWY-7193` pyrimidine ribonucleosides salvage I (EcoCyc)
- `ecocyc.PWY0-1295` pyrimidine ribonucleosides degradation (EcoCyc)
- `ecocyc.PWY0-163` salvage pathways of pyrimidine ribonucleotides (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CYTIDEAM-CPLX|complex.ecocyc.CYTIDEAM-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00299|molecule.C00299]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00475|molecule.C00475]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1311|molecule.ecocyc.CPD0-1311]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1312|molecule.ecocyc.CPD0-1312]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:CYTIDEAM2-RXN`

## Notes

PROTON + WATER + CYTIDINE -> URIDINE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT
