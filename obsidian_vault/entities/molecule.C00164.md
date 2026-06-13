---
entity_id: "molecule.C00164"
entity_type: "small_molecule"
name: "Acetoacetate"
source_database: "KEGG"
source_id: "C00164"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Acetoacetate"
  - "3-Oxobutanoic acid"
  - "beta-Ketobutyric acid"
  - "Acetoacetic acid"
---

# Acetoacetate

`molecule.C00164`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00164`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Acetoacetate; 3-Oxobutanoic acid; beta-Ketobutyric acid; Acetoacetic acid Ketone bodies are carbonyl compounds produced as water-soluble byproducts when fatty acids are broken down for energy in the liver (ketogenesis). There are only three endogenous ketone bodies: 3-KETOBUTYRATE, CPD-335, and ACETONE. Ketone bodies are mostly synthesized in liver mitochondria, but are exported from hepatocytes for circulation to metabolizing tissues. Heart, skeletal muscle under exertion, and brain under starvation conditions use ketone bodies as a major energy source .

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

KEGG compound: Acetoacetate; 3-Oxobutanoic acid; beta-Ketobutyric acid; Acetoacetic acid

## Pathways

- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (5)

- `activates` --> [[reaction.ecocyc.RXN0-6502|reaction.ecocyc.RXN0-6502]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Reactions
- `is_product_of` --> [[reaction.ecocyc.RXN-25375|reaction.ecocyc.RXN-25375]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-281|reaction.ecocyc.TRANS-RXN0-281]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.ACETOACETYL-COA-TRANSFER-RXN|reaction.ecocyc.ACETOACETYL-COA-TRANSFER-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-281|reaction.ecocyc.TRANS-RXN0-281]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00164`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
