---
entity_id: "molecule.C00423"
entity_type: "small_molecule"
name: "trans-Cinnamate"
source_database: "KEGG"
source_id: "C00423"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "trans-Cinnamate"
  - "trans-Cinnamic acid"
  - "(E)-Cinnamate"
  - "(2E)-3-Phenylprop-2-enoate"
---

# trans-Cinnamate

`molecule.C00423`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00423`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: trans-Cinnamate; trans-Cinnamic acid; (E)-Cinnamate; (2E)-3-Phenylprop-2-enoate

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)

## Annotation

KEGG compound: trans-Cinnamate; trans-Cinnamic acid; (E)-Cinnamate; (2E)-3-Phenylprop-2-enoate

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.RXN-24042|reaction.ecocyc.RXN-24042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-466|reaction.ecocyc.TRANS-RXN0-466]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12072|reaction.ecocyc.RXN-12072]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-466|reaction.ecocyc.TRANS-RXN0-466]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00423`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
