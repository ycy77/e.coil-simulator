---
entity_id: "reaction.ecocyc.O-SUCCINYLBENZOATE-COA-LIG-RXN"
entity_type: "reaction"
name: "O-SUCCINYLBENZOATE-COA-LIG-RXN"
source_database: "EcoCyc"
source_id: "O-SUCCINYLBENZOATE-COA-LIG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# O-SUCCINYLBENZOATE-COA-LIG-RXN

`reaction.ecocyc.O-SUCCINYLBENZOATE-COA-LIG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:O-SUCCINYLBENZOATE-COA-LIG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the fourth reaction in menaquinone biosynthesis. EcoCyc reaction equation: ATP + O-SUCCINYLBENZOATE + CO-A -> AMP + PPI + CPD-6972; direction=PHYSIOL-LEFT-TO-RIGHT. This is the fourth reaction in menaquinone biosynthesis.

## Biological Role

Catalyzed by o-succinylbenzoate—CoA ligase (complex.ecocyc.MENE-CPLX). Substrates: ATP (molecule.C00002), CoA (molecule.C00010), 2-Succinylbenzoate (molecule.C02730). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), 2-Succinylbenzoyl-CoA (molecule.C03160).

## Enriched Pathways

- `ecocyc.PWY-5837` 1,4-dihydroxy-2-naphthoate biosynthesis (EcoCyc)

## Annotation

This is the fourth reaction in menaquinone biosynthesis.

## Pathways

- `ecocyc.PWY-5837` 1,4-dihydroxy-2-naphthoate biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.MENE-CPLX|complex.ecocyc.MENE-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03160|molecule.C03160]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02730|molecule.C02730]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DIETHYLPYROCARBONATE|molecule.ecocyc.DIETHYLPYROCARBONATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HG_2|molecule.ecocyc.HG_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:O-SUCCINYLBENZOATE-COA-LIG-RXN`

## Notes

ATP + O-SUCCINYLBENZOATE + CO-A -> AMP + PPI + CPD-6972; direction=PHYSIOL-LEFT-TO-RIGHT
