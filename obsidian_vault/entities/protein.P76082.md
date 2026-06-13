---
entity_id: "protein.P76082"
entity_type: "protein"
name: "paaF"
source_database: "UniProt"
source_id: "P76082"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "paaF ydbR b1393 JW1388"
---

# paaF

`protein.P76082`

## Static

- Type: `protein`
- Source: `UniProt:P76082`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible conversion of enzymatically produced 2,3-dehydroadipyl-CoA into 3-hydroxyadipyl-CoA. {ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:9748275}. PaaF is a predicted 2,3-dehydroadipyl-CoA hydratase involved in phenylacetate catabolism. The enzyme from Pseudomonas sp. strain Y2 has been biochemically characterized . A paaF mutant exhibits a defect in utilization of phenylacetate as a source of carbon . PaaF: "phenylacetic acid degradation"

## Biological Role

Catalyzes 3-hydroxyisovaleryl-CoA hydro-lyase (reaction.R04137), (3S)-3-hydroxyacyl-CoA hydro-lyase (reaction.R06942), RXN-2425 (reaction.ecocyc.RXN-2425). Component of PaaF-PaaG hydratase-isomerase complex (complex.ecocyc.CPLX0-7988).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00380` Tryptophan metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00907` Pinene, camphor and geraniol degradation (KEGG)
- `eco00930` Caprolactam degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible conversion of enzymatically produced 2,3-dehydroadipyl-CoA into 3-hydroxyadipyl-CoA. {ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:9748275}.

## Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00380` Tryptophan metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00907` Pinene, camphor and geraniol degradation (KEGG)
- `eco00930` Caprolactam degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R04137|reaction.R04137]] `KEGG` `database` - via EC:4.2.1.17
- `catalyzes` --> [[reaction.R06942|reaction.R06942]] `KEGG` `database` - via EC:4.2.1.17
- `catalyzes` --> [[reaction.ecocyc.RXN-2425|reaction.ecocyc.RXN-2425]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-7988|complex.ecocyc.CPLX0-7988]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b1393|gene.b1393]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76082`
- `KEGG:ecj:JW1388;eco:b1393;ecoc:C3026_08130;`
- `GeneID:946011;`
- `GO:GO:0004300; GO:0006635; GO:0010124; GO:0018812; GO:0042802; GO:1902494`
- `EC:4.2.1.17`

## Notes

2,3-dehydroadipyl-CoA hydratase (EC 4.2.1.17) (Enoyl-CoA hydratase)
