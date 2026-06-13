---
entity_id: "molecule.C00332"
entity_type: "small_molecule"
name: "Acetoacetyl-CoA"
source_database: "KEGG"
source_id: "C00332"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Acetoacetyl-CoA"
  - "Acetoacetyl coenzyme A"
  - "3-Acetoacetyl-CoA"
---

# Acetoacetyl-CoA

`molecule.C00332`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00332`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Acetoacetyl-CoA; Acetoacetyl coenzyme A; 3-Acetoacetyl-CoA

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 5 reaction(s).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00380` Tryptophan metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)

## Annotation

KEGG compound: Acetoacetyl-CoA; Acetoacetyl coenzyme A; 3-Acetoacetyl-CoA

## Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00380` Tryptophan metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)

## Outgoing Edges (7)

- `is_product_of` --> [[reaction.R00238|reaction.R00238]] `KEGG` `database` - 2 C00024 <=> C00010 + C00332
- `is_product_of` --> [[reaction.ecocyc.ACETOACETYL-COA-TRANSFER-RXN|reaction.ecocyc.ACETOACETYL-COA-TRANSFER-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ACETYL-COA-ACETYLTRANSFER-RXN|reaction.ecocyc.ACETYL-COA-ACETYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-11662|reaction.ecocyc.RXN-11662]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-20155|reaction.ecocyc.RXN-20155]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-25375|reaction.ecocyc.RXN-25375]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ACETYL-COA-ACETYLTRANSFER-RXN|reaction.ecocyc.ACETYL-COA-ACETYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00332`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
