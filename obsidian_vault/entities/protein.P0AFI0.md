---
entity_id: "protein.P0AFI0"
entity_type: "protein"
name: "oxc"
source_database: "UniProt"
source_id: "P0AFI0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "oxc yfdU b2373 JW2370"
---

# oxc

`protein.P0AFI0`

## Static

- Type: `protein`
- Source: `UniProt:P0AFI0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the catabolism of oxalate and in the adapatation to low pH via the induction of the oxalate-dependent acid tolerance response (ATR). Catalyzes the decarboxylation of oxalyl-CoA to yield carbon dioxide and formyl-CoA. {ECO:0000269|PubMed:20553497}.

## Biological Role

Catalyzes oxalyl-CoA carboxy-lyase (formyl-CoA-forming) (reaction.R01908). Component of oxalyl-CoA decarboxylase (complex.ecocyc.CPLX0-7878).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Involved in the catabolism of oxalate and in the adapatation to low pH via the induction of the oxalate-dependent acid tolerance response (ATR). Catalyzes the decarboxylation of oxalyl-CoA to yield carbon dioxide and formyl-CoA. {ECO:0000269|PubMed:20553497}.

## Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01908|reaction.R01908]] `KEGG` `database` - via EC:4.1.1.8
- `is_component_of` --> [[complex.ecocyc.CPLX0-7878|complex.ecocyc.CPLX0-7878]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2373|gene.b2373]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFI0`
- `KEGG:ecj:JW2370;eco:b2373;ecoc:C3026_13195;`
- `GeneID:93774756;946845;`
- `GO:GO:0000287; GO:0001561; GO:0008949; GO:0030976; GO:0033611; GO:0042802; GO:0043531; GO:0071468`
- `EC:4.1.1.8`

## Notes

Oxalyl-CoA decarboxylase (EC 4.1.1.8)
