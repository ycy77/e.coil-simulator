---
entity_id: "reaction.ecocyc.TRANS-RXN0-520"
entity_type: "reaction"
name: "β-methylgalactoside:Na+ symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-520"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# β-methylgalactoside:Na+ symport

`reaction.ecocyc.TRANS-RXN0-520`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-520`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

METHYL-BETA-D-GALACTOSIDE + NA+ -> METHYL-BETA-D-GALACTOSIDE + NA+; direction=REVERSIBLE EcoCyc reaction equation: METHYL-BETA-D-GALACTOSIDE + NA+ -> METHYL-BETA-D-GALACTOSIDE + NA+; direction=REVERSIBLE.

## Biological Role

Catalyzed by melB (protein.P02921). Substrates: Sodium cation (molecule.C01330), Methyl beta-D-galactoside (molecule.C03619). Products: Sodium cation (molecule.C01330), Methyl beta-D-galactoside (molecule.C03619).

## Annotation

METHYL-BETA-D-GALACTOSIDE + NA+ -> METHYL-BETA-D-GALACTOSIDE + NA+; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P02921|protein.P02921]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03619|molecule.C03619]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03619|molecule.C03619]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-520`

## Notes

METHYL-BETA-D-GALACTOSIDE + NA+ -> METHYL-BETA-D-GALACTOSIDE + NA+; direction=REVERSIBLE
