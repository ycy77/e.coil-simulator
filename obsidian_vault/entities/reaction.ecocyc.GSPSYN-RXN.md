---
entity_id: "reaction.ecocyc.GSPSYN-RXN"
entity_type: "reaction"
name: "GSPSYN-RXN"
source_database: "EcoCyc"
source_id: "GSPSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GSPSYN-RXN

`reaction.ecocyc.GSPSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GSPSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction synthesizes glutathionylspermidine. EcoCyc reaction equation: SPERMIDINE + GLUTATHIONE + ATP -> PROTON + GLUTATHIONYLSPERMIDINE + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction synthesizes glutathionylspermidine.

## Biological Role

Catalyzed by fused glutathionylspermidine amidase / glutathionylspermidine synthetase (complex.ecocyc.GSP-CPLX). Substrates: ATP (molecule.C00002), Glutathione (molecule.C00051), Spermidine (molecule.C00315). Products: ADP (molecule.C00008), H+ (molecule.C00080), Glutathionylspermidine (molecule.C05730), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-4121` glutathionylspermidine biosynthesis (EcoCyc)

## Annotation

This reaction synthesizes glutathionylspermidine.

## Pathways

- `ecocyc.PWY-4121` glutathionylspermidine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.GSP-CPLX|complex.ecocyc.GSP-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05730|molecule.C05730]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00315|molecule.C00315]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.PHOSPHONATE|molecule.ecocyc.PHOSPHONATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GSPSYN-RXN`

## Notes

SPERMIDINE + GLUTATHIONE + ATP -> PROTON + GLUTATHIONYLSPERMIDINE + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
