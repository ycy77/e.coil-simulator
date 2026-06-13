---
entity_id: "protein.P76077"
entity_type: "protein"
name: "paaA"
source_database: "UniProt"
source_id: "P76077"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "paaA ydbO b1388 JW1383"
---

# paaA

`protein.P76077`

## Static

- Type: `protein`
- Source: `UniProt:P76077`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Component of 1,2-phenylacetyl-CoA epoxidase multicomponent enzyme system which catalyzes the reduction of phenylacetyl-CoA (PA-CoA) to form 1,2-epoxyphenylacetyl-CoA. The subunit A is the catalytic subunit involved in the incorporation of one atom of molecular oxygen into phenylacetyl-CoA. {ECO:0000269|PubMed:16997993, ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:21247899, ECO:0000269|PubMed:9748275}. PaaA is the catalytic α subunit of the catalytic core of the enzyme . PaaA has similarity to the large (α) subunit of diiron monooxygenase complexes . PaaA: "phenylacetic acid degradation"

## Biological Role

Component of phenylacetyl-CoA 1,2-epoxidase (complex.ecocyc.CPLX0-1762).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Component of 1,2-phenylacetyl-CoA epoxidase multicomponent enzyme system which catalyzes the reduction of phenylacetyl-CoA (PA-CoA) to form 1,2-epoxyphenylacetyl-CoA. The subunit A is the catalytic subunit involved in the incorporation of one atom of molecular oxygen into phenylacetyl-CoA. {ECO:0000269|PubMed:16997993, ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:21247899, ECO:0000269|PubMed:9748275}.

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1762|complex.ecocyc.CPLX0-1762]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1388|gene.b1388]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76077`
- `KEGG:ecj:JW1383;eco:b1388;ecoc:C3026_08105;`
- `GeneID:945833;`
- `GO:GO:0005829; GO:0010124; GO:0062077; GO:0097266`
- `EC:1.14.13.149`

## Notes

1,2-phenylacetyl-CoA epoxidase, subunit A (EC 1.14.13.149) (1,2-phenylacetyl-CoA epoxidase, catalytic subunit alpha) (1,2-phenylacetyl-CoA monooxygenase, subunit A)
