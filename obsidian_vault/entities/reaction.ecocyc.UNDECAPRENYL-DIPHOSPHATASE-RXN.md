---
entity_id: "reaction.ecocyc.UNDECAPRENYL-DIPHOSPHATASE-RXN"
entity_type: "reaction"
name: "UNDECAPRENYL-DIPHOSPHATASE-RXN"
source_database: "EcoCyc"
source_id: "UNDECAPRENYL-DIPHOSPHATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# UNDECAPRENYL-DIPHOSPHATASE-RXN

`reaction.ecocyc.UNDECAPRENYL-DIPHOSPHATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:UNDECAPRENYL-DIPHOSPHATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN|CCO-CYTOSOL

## Enriched Summary

UNDECAPRENYL-DIPHOSPHATE + WATER -> PROTON + CPD-9646 + Pi; direction=LEFT-TO-RIGHT EcoCyc reaction equation: UNDECAPRENYL-DIPHOSPHATE + WATER -> PROTON + CPD-9646 + Pi; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pgpB (protein.P0A924), uppP (protein.P60932), ybjG (protein.P75806), lpxT (protein.P76445). Substrates: H2O (molecule.C00001), di-trans,poly-cis-Undecaprenyl diphosphate (molecule.C04574). Products: H+ (molecule.C00080), di-trans,poly-cis-Undecaprenyl phosphate (molecule.C17556), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-5785` di-trans,poly-cis-undecaprenyl phosphate biosynthesis (EcoCyc)

## Annotation

UNDECAPRENYL-DIPHOSPHATE + WATER -> PROTON + CPD-9646 + Pi; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5785` di-trans,poly-cis-undecaprenyl phosphate biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P0A924|protein.P0A924]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P60932|protein.P60932]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P75806|protein.P75806]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76445|protein.P76445]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C17556|molecule.C17556]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04574|molecule.C04574]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:UNDECAPRENYL-DIPHOSPHATASE-RXN`

## Notes

UNDECAPRENYL-DIPHOSPHATE + WATER -> PROTON + CPD-9646 + Pi; direction=LEFT-TO-RIGHT
