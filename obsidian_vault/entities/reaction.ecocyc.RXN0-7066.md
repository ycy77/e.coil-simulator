---
entity_id: "reaction.ecocyc.RXN0-7066"
entity_type: "reaction"
name: "RXN0-7066"
source_database: "EcoCyc"
source_id: "RXN0-7066"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7066

`reaction.ecocyc.RXN0-7066`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7066`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + PREPHENATE -> PHENYL-PYRUVATE + CPD-15403 + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + PREPHENATE -> PHENYL-PYRUVATE + CPD-15403 + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by carboxy-S-adenosyl-L-methionine synthase (complex.ecocyc.CPLX0-8010). Substrates: S-Adenosyl-L-methionine (molecule.C00019), Prephenate (molecule.C00254). Products: H2O (molecule.C00001), Phenylpyruvate (molecule.C00166), S-adenosyl-S-carboxymethyl-L-homocysteine (molecule.ecocyc.CPD-15403).

## Enriched Pathways

- `ecocyc.PWY0-1554` 5-(methoxycarbonylmethoxy)uridine biosynthesis (EcoCyc)

## Annotation

S-ADENOSYLMETHIONINE + PREPHENATE -> PHENYL-PYRUVATE + CPD-15403 + WATER; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1554` 5-(methoxycarbonylmethoxy)uridine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8010|complex.ecocyc.CPLX0-8010]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00166|molecule.C00166]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15403|molecule.ecocyc.CPD-15403]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00254|molecule.C00254]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7066`

## Notes

S-ADENOSYLMETHIONINE + PREPHENATE -> PHENYL-PYRUVATE + CPD-15403 + WATER; direction=LEFT-TO-RIGHT
