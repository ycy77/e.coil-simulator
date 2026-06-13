---
entity_id: "molecule.C06453"
entity_type: "small_molecule"
name: "Methylcobalamin"
source_database: "KEGG"
source_id: "C06453"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Methylcobalamin"
  - "Methylcob(III)alamin"
---

# Methylcobalamin

`molecule.C06453`

## Static

- Type: `small_molecule`
- Source: `KEGG:C06453`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Methylcobalamin; Methylcob(III)alamin EcoCyc common name: methylcob(III)alamin.

## Biological Role

Binds metH (protein.P13009).

## Enriched Pathways

- `eco04980` Cobalamin transport and metabolism (KEGG)

## Annotation

KEGG compound: Methylcobalamin; Methylcob(III)alamin

## Pathways

- `eco04980` Cobalamin transport and metabolism (KEGG)

## Outgoing Edges (2)

- `binds` --> [[protein.P13009|protein.P13009]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `represses` --> [[reaction.ecocyc.ETHAMLY-RXN|reaction.ecocyc.ETHAMLY-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C06453`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
