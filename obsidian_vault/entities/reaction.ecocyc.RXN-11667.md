---
entity_id: "reaction.ecocyc.RXN-11667"
entity_type: "reaction"
name: "(S)-3-hydroxybutanoyl-CoA dehydrogenase"
source_database: "EcoCyc"
source_id: "RXN-11667"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# (S)-3-hydroxybutanoyl-CoA dehydrogenase

`reaction.ecocyc.RXN-11667`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11667`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-3-HYDROXYBUTANOYL-COA -> WATER + CROTONYL-COA; direction=REVERSIBLE EcoCyc reaction equation: S-3-HYDROXYBUTANOYL-COA -> WATER + CROTONYL-COA; direction=REVERSIBLE.

## Biological Role

Substrates: (S)-3-Hydroxybutanoyl-CoA (molecule.C01144). Products: H2O (molecule.C00001), Crotonoyl-CoA (molecule.C00877).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

S-3-HYDROXYBUTANOYL-COA -> WATER + CROTONYL-COA; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00877|molecule.C00877]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01144|molecule.C01144]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11667`

## Notes

S-3-HYDROXYBUTANOYL-COA -> WATER + CROTONYL-COA; direction=REVERSIBLE
