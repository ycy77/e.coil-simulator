---
entity_id: "reaction.ecocyc.PGLYCDEHYDROG-RXN"
entity_type: "reaction"
name: "PGLYCDEHYDROG-RXN"
source_database: "EcoCyc"
source_id: "PGLYCDEHYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PGLYCDEHYDROG-RXN

`reaction.ecocyc.PGLYCDEHYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PGLYCDEHYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first committed step in the 'phosphorylated' pathway of serine synthesis. EcoCyc reaction equation: G3P + NAD -> PROTON + 3-P-HYDROXYPYRUVATE + NADH; direction=REVERSIBLE. This is the first committed step in the 'phosphorylated' pathway of serine synthesis.

## Biological Role

Catalyzed by phosphoglycerate dehydrogenase (complex.ecocyc.PGLYCDEHYDROG-CPLX). Substrates: NAD+ (molecule.C00003), 3-Phospho-D-glycerate (molecule.C00197). Products: NADH (molecule.C00004), H+ (molecule.C00080), 3-Phosphonooxypyruvate (molecule.C03232).

## Enriched Pathways

- `ecocyc.SERSYN-PWY-1` L-serine biosynthesis (EcoCyc)

## Annotation

This is the first committed step in the 'phosphorylated' pathway of serine synthesis.

## Pathways

- `ecocyc.SERSYN-PWY-1` L-serine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.PGLYCDEHYDROG-CPLX|complex.ecocyc.PGLYCDEHYDROG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03232|molecule.C03232]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00197|molecule.C00197]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PGLYCDEHYDROG-RXN`

## Notes

G3P + NAD -> PROTON + 3-P-HYDROXYPYRUVATE + NADH; direction=REVERSIBLE
