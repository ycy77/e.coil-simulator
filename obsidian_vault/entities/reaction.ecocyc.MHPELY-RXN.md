---
entity_id: "reaction.ecocyc.MHPELY-RXN"
entity_type: "reaction"
name: "MHPELY-RXN"
source_database: "EcoCyc"
source_id: "MHPELY-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# MHPELY-RXN

`reaction.ecocyc.MHPELY-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:MHPELY-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the seventh reaction in the branched meta-cleavage degradation pathway of 3-phenylpropionate and 3-(3-hydroxyphenyl)propionate. EcoCyc reaction equation: 4-HYDROXY-2-KETOVALERATE -> ACETALD + PYRUVATE; direction=REVERSIBLE. This is the seventh reaction in the branched meta-cleavage degradation pathway of 3-phenylpropionate and 3-(3-hydroxyphenyl)propionate.

## Biological Role

Catalyzed by mhpE (protein.P51020). Substrates: 4-Hydroxy-2-oxopentanoate (molecule.C03589). Products: Pyruvate (molecule.C00022), Acetaldehyde (molecule.C00084).

## Enriched Pathways

- `ecocyc.PWY-5162` 2-hydroxypenta-2,4-dienoate degradation (EcoCyc)

## Annotation

This is the seventh reaction in the branched meta-cleavage degradation pathway of 3-phenylpropionate and 3-(3-hydroxyphenyl)propionate.

## Pathways

- `ecocyc.PWY-5162` 2-hydroxypenta-2,4-dienoate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P51020|protein.P51020]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00084|molecule.C00084]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C03589|molecule.C03589]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:MHPELY-RXN`

## Notes

4-HYDROXY-2-KETOVALERATE -> ACETALD + PYRUVATE; direction=REVERSIBLE
