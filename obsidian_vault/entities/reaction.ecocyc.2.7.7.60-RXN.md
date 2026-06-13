---
entity_id: "reaction.ecocyc.2.7.7.60-RXN"
entity_type: "reaction"
name: "2.7.7.60-RXN"
source_database: "EcoCyc"
source_id: "2.7.7.60-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "4-diphosphocytidyl-2C-methyl-D-erythritol synthase"
  - "MCT"
---

# 2.7.7.60-RXN

`reaction.ecocyc.2.7.7.60-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.7.7.60-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + 2-C-METHYL-D-ERYTHRITOL-4-PHOSPHATE + CTP -> 4-CYTIDINE-5-DIPHOSPHO-2-C + PPI; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + 2-C-METHYL-D-ERYTHRITOL-4-PHOSPHATE + CTP -> 4-CYTIDINE-5-DIPHOSPHO-2-C + PPI; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 2-C-methyl-D-erythritol 4-phosphate cytidylyltransferase (complex.ecocyc.CPLX0-234). Substrates: CTP (molecule.C00063), H+ (molecule.C00080), 2-C-Methyl-D-erythritol 4-phosphate (molecule.C11434). Products: Diphosphate (molecule.C00013), 4-(Cytidine 5'-diphospho)-2-C-methyl-D-erythritol (molecule.C11435).

## Enriched Pathways

- `ecocyc.NONMEVIPP-PWY` methylerythritol phosphate pathway I (EcoCyc)

## Annotation

PROTON + 2-C-METHYL-D-ERYTHRITOL-4-PHOSPHATE + CTP -> 4-CYTIDINE-5-DIPHOSPHO-2-C + PPI; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.NONMEVIPP-PWY` methylerythritol phosphate pathway I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-234|complex.ecocyc.CPLX0-234]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C11435|molecule.C11435]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00063|molecule.C00063]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C11434|molecule.C11434]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2.7.7.60-RXN`

## Notes

PROTON + 2-C-METHYL-D-ERYTHRITOL-4-PHOSPHATE + CTP -> 4-CYTIDINE-5-DIPHOSPHO-2-C + PPI; direction=LEFT-TO-RIGHT
