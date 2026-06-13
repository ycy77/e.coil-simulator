---
entity_id: "molecule.C03561"
entity_type: "small_molecule"
name: "(R)-3-Hydroxybutanoyl-CoA"
source_database: "KEGG"
source_id: "C03561"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(R)-3-Hydroxybutanoyl-CoA"
  - "(3R)-3-Hydroxybutanoyl-CoA"
---

# (R)-3-Hydroxybutanoyl-CoA

`molecule.C03561`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03561`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (R)-3-Hydroxybutanoyl-CoA; (3R)-3-Hydroxybutanoyl-CoA EcoCyc common name: (3R)-hydroxybutanoyl-CoA.

## Biological Role

Consumed as substrate in 3 reaction(s).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)

## Annotation

KEGG compound: (R)-3-Hydroxybutanoyl-CoA; (3R)-3-Hydroxybutanoyl-CoA

## Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)

## Outgoing Edges (3)

- `is_substrate_of` --> [[reaction.ecocyc.3-HYDROXBUTYRYL-COA-DEHYDRATASE-RXN|reaction.ecocyc.3-HYDROXBUTYRYL-COA-DEHYDRATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14255|reaction.ecocyc.RXN-14255]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN1-42|reaction.ecocyc.RXN1-42]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03561`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
