---
entity_id: "protein.P37677"
entity_type: "protein"
name: "lyx"
source_database: "UniProt"
source_id: "P37677"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lyx lyxK sgbK xylK yiaP b3580 JW3552"
---

# lyx

`protein.P37677`

## Static

- Type: `protein`
- Source: `UniProt:P37677`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the phosphorylation of L-xylulose and 3-keto-L-gulonate. Is involved in L-lyxose utilization via xylulose, and may also be involved in the utilization of 2,3-diketo-L-gulonate. {ECO:0000269|PubMed:11741871, ECO:0000269|PubMed:7961955}. L-xylulose kinase is the product of an apparently silent gene, lyxK. Once expression is activated through a mutation in the transcriptional repressor YiaJ , the kinase specifically phosphorylates L-xylulose. This allows E. coli to utilize the uncommon sugar, L-lyxose, using enzymes of the rhamnose degradation system. The product of the L-xylulose kinase reaction, L-xylulose 5-P, is further metabolized by the pentose phosphate pathway . LyxK is also able to catalyze the phosphorylation of 3-keto-L-gulonate .

## Biological Role

Catalyzes ATP:L-xylulose 5-phosphotransferase (reaction.R01901). Component of L-xylulose kinase (complex.ecocyc.LYXK-CPLX).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the phosphorylation of L-xylulose and 3-keto-L-gulonate. Is involved in L-lyxose utilization via xylulose, and may also be involved in the utilization of 2,3-diketo-L-gulonate. {ECO:0000269|PubMed:11741871, ECO:0000269|PubMed:7961955}.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01901|reaction.R01901]] `KEGG` `database` - via EC:2.7.1.53
- `is_component_of` --> [[complex.ecocyc.LYXK-CPLX|complex.ecocyc.LYXK-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3580|gene.b3580]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37677`
- `KEGG:ecj:JW3552;eco:b3580;ecoc:C3026_19410;`
- `GeneID:948101;`
- `GO:GO:0005524; GO:0008744; GO:0016301; GO:0016773; GO:0019324; GO:0042803`
- `EC:2.7.1.-; 2.7.1.53`

## Notes

L-xylulose/3-keto-L-gulonate kinase (L-xylulokinase) (EC 2.7.1.-) (EC 2.7.1.53) (3-dehydro-L-gulonate kinase)
