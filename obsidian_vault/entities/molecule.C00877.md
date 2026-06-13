---
entity_id: "molecule.C00877"
entity_type: "small_molecule"
name: "Crotonoyl-CoA"
source_database: "KEGG"
source_id: "C00877"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Crotonoyl-CoA"
  - "Crotonyl-CoA"
  - "2-Butenoyl-CoA"
  - "trans-But-2-enoyl-CoA"
  - "But-2-enoyl-CoA"
  - "(E)-But-2-enoyl-CoA"
  - "(2E)-But-2-enoyl-CoA"
---

# Crotonoyl-CoA

`molecule.C00877`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00877`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Crotonoyl-CoA; Crotonyl-CoA; 2-Butenoyl-CoA; trans-But-2-enoyl-CoA; But-2-enoyl-CoA; (E)-But-2-enoyl-CoA; (2E)-But-2-enoyl-CoA EcoCyc common name: crotonyl-CoA.

## Biological Role

Produced in 3 reaction(s).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00380` Tryptophan metabolism (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)

## Annotation

KEGG compound: Crotonoyl-CoA; Crotonyl-CoA; 2-Butenoyl-CoA; trans-But-2-enoyl-CoA; But-2-enoyl-CoA; (E)-But-2-enoyl-CoA; (2E)-But-2-enoyl-CoA

## Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00380` Tryptophan metabolism (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.3-HYDROXBUTYRYL-COA-DEHYDRATASE-RXN|reaction.ecocyc.3-HYDROXBUTYRYL-COA-DEHYDRATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.BUTYRYL-COA-DEHYDROGENASE-RXN|reaction.ecocyc.BUTYRYL-COA-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-11667|reaction.ecocyc.RXN-11667]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00877`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
