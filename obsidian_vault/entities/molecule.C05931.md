---
entity_id: "molecule.C05931"
entity_type: "small_molecule"
name: "N-Succinyl-L-glutamate"
source_database: "KEGG"
source_id: "C05931"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "N-Succinyl-L-glutamate"
  - "(2S)-2-(3-Carboxypropanoylamino)pentanedioic acid"
---

# N-Succinyl-L-glutamate

`molecule.C05931`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05931`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: N-Succinyl-L-glutamate; (2S)-2-(3-Carboxypropanoylamino)pentanedioic acid EcoCyc common name: N2-succinylglutamate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)

## Annotation

KEGG compound: N-Succinyl-L-glutamate; (2S)-2-(3-Carboxypropanoylamino)pentanedioic acid

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.SUCCGLUALDDEHYD-RXN|reaction.ecocyc.SUCCGLUALDDEHYD-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00411|reaction.R00411]] `KEGG` `database` - C05931 + C00001 <=> C00025 + C00042
- `is_substrate_of` --> [[reaction.ecocyc.SUCCGLUDESUCC-RXN|reaction.ecocyc.SUCCGLUDESUCC-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05931`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
