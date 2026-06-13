---
entity_id: "protein.P77467"
entity_type: "protein"
name: "paaG"
source_database: "UniProt"
source_id: "P77467"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "paaG ydbT b1394 JW1389"
---

# paaG

`protein.P77467`

## Static

- Type: `protein`
- Source: `UniProt:P77467`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible conversion of the epoxide to 2-oxepin-2(3H)-ylideneacetyl-CoA (oxepin-CoA). {ECO:0000269|PubMed:12846838, ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:9748275}. PaaG is the predicted oxepin-CoA-forming ring 1,2-epoxyphenylacetyl-CoA isomerase involved in phenylacetate catabolism. The enzyme from Pseudomonas sp. strain Y2 has been biochemically characterized . A paaG mutant exhibits a defect in utilization of phenylacetate as a source of carbon . PaaG: "phenylacetic acid degradation"

## Biological Role

Catalyzes RXN0-6510 (reaction.ecocyc.RXN0-6510). Component of PaaF-PaaG hydratase-isomerase complex (complex.ecocyc.CPLX0-7988).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible conversion of the epoxide to 2-oxepin-2(3H)-ylideneacetyl-CoA (oxepin-CoA). {ECO:0000269|PubMed:12846838, ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:9748275}.

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-6510|reaction.ecocyc.RXN0-6510]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-7988|complex.ecocyc.CPLX0-7988]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b1394|gene.b1394]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77467`
- `KEGG:ecj:JW1389;eco:b1394;ecoc:C3026_08135;`
- `GeneID:946263;`
- `GO:GO:0006635; GO:0010124; GO:0016829; GO:0016853; GO:0042802; GO:1902494`
- `EC:5.3.3.18`

## Notes

1,2-epoxyphenylacetyl-CoA isomerase (EC 5.3.3.18)
