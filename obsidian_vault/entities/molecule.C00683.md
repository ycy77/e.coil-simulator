---
entity_id: "molecule.C00683"
entity_type: "small_molecule"
name: "(S)-Methylmalonyl-CoA"
source_database: "KEGG"
source_id: "C00683"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(S)-Methylmalonyl-CoA"
  - "(S)-Methylmalonyl-coenzyme A"
  - "(2S)-Methylmalonyl-CoA"
  - "D-Methylmalonyl-CoA"
---

# (S)-Methylmalonyl-CoA

`molecule.C00683`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00683`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (S)-Methylmalonyl-CoA; (S)-Methylmalonyl-coenzyme A; (2S)-Methylmalonyl-CoA; D-Methylmalonyl-CoA

## Biological Role

Produced in 2 reaction(s).

## Enriched Pathways

- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)

## Annotation

KEGG compound: (S)-Methylmalonyl-CoA; (S)-Methylmalonyl-coenzyme A; (2S)-Methylmalonyl-CoA; D-Methylmalonyl-CoA

## Pathways

- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.METHYLMALONYL-COA-EPIM-RXN|reaction.ecocyc.METHYLMALONYL-COA-EPIM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PROPIONYL-COA-CARBOXY-RXN|reaction.ecocyc.PROPIONYL-COA-CARBOXY-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00683`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
