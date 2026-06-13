---
entity_id: "molecule.C07086"
entity_type: "small_molecule"
name: "Phenylacetic acid"
source_database: "KEGG"
source_id: "C07086"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Phenylacetic acid"
  - "Benzylformic acid"
  - "Phenylacetate"
  - "Benzeneacetic acid"
---

# Phenylacetic acid

`molecule.C07086`

## Static

- Type: `small_molecule`
- Source: `KEGG:C07086`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Phenylacetic acid; Benzylformic acid; Phenylacetate; Benzeneacetic acid EcoCyc common name: phenylacetate. Phenylacetic acid is an active auxin found predominantly in fruits, although its effect is much weaker than the effect of the major auxin molecule INDOLE_ACETATE_AUXIN .

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)

## Annotation

KEGG compound: Phenylacetic acid; Benzylformic acid; Phenylacetate; Benzeneacetic acid

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.PHENDEHYD-RXN|reaction.ecocyc.PHENDEHYD-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7104|reaction.ecocyc.RXN0-7104]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-10819|reaction.ecocyc.RXN-10819]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C07086`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
