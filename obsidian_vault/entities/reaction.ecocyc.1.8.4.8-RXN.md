---
entity_id: "reaction.ecocyc.1.8.4.8-RXN"
entity_type: "reaction"
name: "1.8.4.8-RXN"
source_database: "EcoCyc"
source_id: "1.8.4.8-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 1.8.4.8-RXN

`reaction.ecocyc.1.8.4.8-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:1.8.4.8-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The third reaction in converting sulfate to sulfide. The first reaction in the reduction of sulfate to sulfite in the pathway leading to cysteine synthesis. Note: Reaction E.C. 1.8.99.4 was transferred to E.C 1.8.4.8 in 2000. EcoCyc reaction equation: 3-5-ADP + SO3 + Ox-Thioredoxin + PROTON -> PAPS + Red-Thioredoxin; direction=PHYSIOL-RIGHT-TO-LEFT. The third reaction in converting sulfate to sulfide. The first reaction in the reduction of sulfate to sulfite in the pathway leading to cysteine synthesis. Note: Reaction E.C. 1.8.99.4 was transferred to E.C 1.8.4.8 in 2000.

## Biological Role

Catalyzed by phosphoadenosine phosphosulfate reductase (complex.ecocyc.PAPSSULFOTRANS-CPLX). Substrates: Adenosine 3',5'-bisphosphate (molecule.C00054), H+ (molecule.C00080), Sulfite (molecule.C00094). Products: 3'-Phosphoadenylyl sulfate (molecule.C00053).

## Enriched Pathways

- `ecocyc.SO4ASSIM-PWY` assimilatory sulfate reduction I (EcoCyc)

## Annotation

The third reaction in converting sulfate to sulfide. The first reaction in the reduction of sulfate to sulfite in the pathway leading to cysteine synthesis. Note: Reaction E.C. 1.8.99.4 was transferred to E.C 1.8.4.8 in 2000.

## Pathways

- `ecocyc.SO4ASSIM-PWY` assimilatory sulfate reduction I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.PAPSSULFOTRANS-CPLX|complex.ecocyc.PAPSSULFOTRANS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00053|molecule.C00053]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00054|molecule.C00054]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00094|molecule.C00094]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00054|molecule.C00054]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:1.8.4.8-RXN`

## Notes

3-5-ADP + SO3 + Ox-Thioredoxin + PROTON -> PAPS + Red-Thioredoxin; direction=PHYSIOL-RIGHT-TO-LEFT
