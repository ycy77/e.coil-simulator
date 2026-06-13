---
entity_id: "reaction.ecocyc.ADDALT-RXN"
entity_type: "reaction"
name: "ADDALT-RXN"
source_database: "EcoCyc"
source_id: "ADDALT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ADDALT-RXN

`reaction.ecocyc.ADDALT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ADDALT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of nucleotide metabolism. EcoCyc reaction equation: PROTON + WATER + DEOXYADENOSINE -> AMMONIUM + DEOXYINOSINE; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of nucleotide metabolism.

## Biological Role

Catalyzed by add (protein.P22333). Substrates: H2O (molecule.C00001), H+ (molecule.C00080), Deoxyadenosine (molecule.C00559). Products: Deoxyinosine (molecule.C05512), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.PWY-7179` purine deoxyribonucleosides degradation I (EcoCyc)

## Annotation

This reaction is part of nucleotide metabolism.

## Pathways

- `ecocyc.PWY-7179` purine deoxyribonucleosides degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P22333|protein.P22333]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C05512|molecule.C05512]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00559|molecule.C00559]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ADDALT-RXN`

## Notes

PROTON + WATER + DEOXYADENOSINE -> AMMONIUM + DEOXYINOSINE; direction=PHYSIOL-LEFT-TO-RIGHT
