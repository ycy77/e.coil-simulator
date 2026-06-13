---
entity_id: "reaction.ecocyc.FHLMULTI-RXN"
entity_type: "reaction"
name: "FHLMULTI-RXN"
source_database: "EcoCyc"
source_id: "FHLMULTI-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# FHLMULTI-RXN

`reaction.ecocyc.FHLMULTI-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:FHLMULTI-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Decomposition of formate to CO2 and H2. EcoCyc reaction equation: PROTON + FORMATE -> CARBON-DIOXIDE + HYDROGEN-MOLECULE; direction=LEFT-TO-RIGHT. Decomposition of formate to CO2 and H2.

## Biological Role

Catalyzed by formate hydrogenlyase complex (complex.ecocyc.FHLMULTI-CPLX). Substrates: Formate (molecule.C00058), H+ (molecule.C00080). Products: CO2 (molecule.C00011), Hydrogen (molecule.C00282).

## Enriched Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.PWY-6772` hydrogen production V (EcoCyc)

## Annotation

Decomposition of formate to CO2 and H2.

## Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.PWY-6772` hydrogen production V (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.FHLMULTI-CPLX|complex.ecocyc.FHLMULTI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00282|molecule.C00282]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00058|molecule.C00058]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:FHLMULTI-RXN`

## Notes

PROTON + FORMATE -> CARBON-DIOXIDE + HYDROGEN-MOLECULE; direction=LEFT-TO-RIGHT
