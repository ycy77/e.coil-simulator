---
entity_id: "protein.P77541"
entity_type: "protein"
name: "prpB"
source_database: "UniProt"
source_id: "P77541"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "prpB yahQ b0331 JW0323"
---

# prpB

`protein.P77541`

## Static

- Type: `protein`
- Source: `UniProt:P77541`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the catabolism of short chain fatty acids (SCFA) via the 2-methylcitrate cycle I (propionate degradation route). Catalyzes the thermodynamically favored C-C bond cleavage of (2R,3S)-2-methylisocitrate to yield pyruvate and succinate via an alpha-carboxy-carbanion intermediate. {ECO:0000255|HAMAP-Rule:MF_01939, ECO:0000269|PubMed:11422389, ECO:0000269|PubMed:15723538}. 2-Methylisocitrate lyase (PrpB) catalyzes the cleavage of 2-methylisocitrate to succinate and pyruvate, which is the final step in propionate metabolism via the methylcitrate cycle . The enzyme activity is sensitive to oxidation and is inactivated by 3-bromopyruvate alkylation . Crystal structures of the wild type and mutant enzyme in the apo- and product-bound forms have been solved . The structures enabled modeling of the active site and proposal of a catalytic mechanism involving an α-carboxy-carbanion transition state . Protein production is observed during growth on propionate, but not acetate or glucose . Expression of prpBCDE is regulated by PrpR and catabolite repression and is downregulated in the presence of a variety of sugars .

## Biological Role

Catalyzes (2S,3R)-3-hydroxybutane-1,2,3-tricarboxylate pyruvate-lyase (succinate-forming) (reaction.R00409). Component of 2-methylisocitrate lyase (complex.ecocyc.CPLX0-1021).

## Enriched Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Involved in the catabolism of short chain fatty acids (SCFA) via the 2-methylcitrate cycle I (propionate degradation route). Catalyzes the thermodynamically favored C-C bond cleavage of (2R,3S)-2-methylisocitrate to yield pyruvate and succinate via an alpha-carboxy-carbanion intermediate. {ECO:0000255|HAMAP-Rule:MF_01939, ECO:0000269|PubMed:11422389, ECO:0000269|PubMed:15723538}.

## Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00409|reaction.R00409]] `KEGG` `database` - via EC:4.1.3.30
- `is_component_of` --> [[complex.ecocyc.CPLX0-1021|complex.ecocyc.CPLX0-1021]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0331|gene.b0331]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77541`
- `KEGG:ecj:JW0323;eco:b0331;ecoc:C3026_01625;ecoc:C3026_24795;`
- `GeneID:944990;`
- `GO:GO:0000287; GO:0019629; GO:0046421`
- `EC:4.1.3.30`

## Notes

2-methylisocitrate lyase (2-MIC) (MICL) (EC 4.1.3.30) ((2R,3S)-2-methylisocitrate lyase)
