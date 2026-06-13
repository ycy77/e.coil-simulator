---
entity_id: "reaction.ecocyc.TRANS-RXN0-517"
entity_type: "reaction"
name: "C4-dicarboxylate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-517"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# C4-dicarboxylate:proton symport

`reaction.ecocyc.TRANS-RXN0-517`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-517`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

C4-dicarboxylates + PROTON -> PROTON + C4-dicarboxylates; direction=REVERSIBLE EcoCyc reaction equation: C4-dicarboxylates + PROTON -> PROTON + C4-dicarboxylates; direction=REVERSIBLE.

## Biological Role

Catalyzed by dctA (protein.P0A830). Substrates: H+ (molecule.C00080), a C4-dicarboxylate (molecule.ecocyc.C4-dicarboxylates). Products: H+ (molecule.C00080), a C4-dicarboxylate (molecule.ecocyc.C4-dicarboxylates).

## Annotation

C4-dicarboxylates + PROTON -> PROTON + C4-dicarboxylates; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A830|protein.P0A830]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.C4-dicarboxylates|molecule.ecocyc.C4-dicarboxylates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.C4-dicarboxylates|molecule.ecocyc.C4-dicarboxylates]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-517`

## Notes

C4-dicarboxylates + PROTON -> PROTON + C4-dicarboxylates; direction=REVERSIBLE
