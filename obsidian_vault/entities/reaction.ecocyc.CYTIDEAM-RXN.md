---
entity_id: "reaction.ecocyc.CYTIDEAM-RXN"
entity_type: "reaction"
name: "CYTIDEAM-RXN"
source_database: "EcoCyc"
source_id: "CYTIDEAM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CYTIDEAM-RXN

`reaction.ecocyc.CYTIDEAM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CYTIDEAM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the pyrimidine salvage pathway. The enzyme converts exogenous and endogenous cytidine and 2'-deoxycytidine to the corresponding uracil nucleosides. Using this reaction, cytidine may also serve as a carbon source. EcoCyc reaction equation: PROTON + WATER + DEOXYCYTIDINE -> DEOXYURIDINE + AMMONIUM; direction=LEFT-TO-RIGHT. This reaction is part of the pyrimidine salvage pathway. The enzyme converts exogenous and endogenous cytidine and 2'-deoxycytidine to the corresponding uracil nucleosides. Using this reaction, cytidine may also serve as a carbon source.

## Biological Role

Catalyzed by cytidine/deoxycytidine deaminase (complex.ecocyc.CYTIDEAM-CPLX). Substrates: H2O (molecule.C00001), H+ (molecule.C00080), Deoxycytidine (molecule.C00881). Products: Deoxyuridine (molecule.C00526), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.PWY-7181` pyrimidine deoxyribonucleosides degradation (EcoCyc)
- `ecocyc.PWY0-181` salvage pathways of pyrimidine deoxyribonucleotides (EcoCyc)

## Annotation

This reaction is part of the pyrimidine salvage pathway. The enzyme converts exogenous and endogenous cytidine and 2'-deoxycytidine to the corresponding uracil nucleosides. Using this reaction, cytidine may also serve as a carbon source.

## Pathways

- `ecocyc.PWY-7181` pyrimidine deoxyribonucleosides degradation (EcoCyc)
- `ecocyc.PWY0-181` salvage pathways of pyrimidine deoxyribonucleotides (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CYTIDEAM-CPLX|complex.ecocyc.CYTIDEAM-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00526|molecule.C00526]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00881|molecule.C00881]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1711|molecule.ecocyc.CPD0-1711]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:CYTIDEAM-RXN`

## Notes

PROTON + WATER + DEOXYCYTIDINE -> DEOXYURIDINE + AMMONIUM; direction=LEFT-TO-RIGHT
