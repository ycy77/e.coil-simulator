---
entity_id: "protein.P76079"
entity_type: "protein"
name: "paaC"
source_database: "UniProt"
source_id: "P76079"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "paaC ydbP b1390 JW1385"
---

# paaC

`protein.P76079`

## Static

- Type: `protein`
- Source: `UniProt:P76079`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Component of 1,2-phenylacetyl-CoA epoxidase multicomponent enzyme system which catalyzes the reduction of phenylacetyl-CoA (PA-CoA) to form 1,2-epoxyphenylacetyl-CoA. The subunit C may be essential for structural integrity of the alpha subunit. {ECO:0000269|PubMed:16997993, ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:9748275}. PaaC is the structural β subunit of the catalytic core of the enzyme . PaaC: "phenylacetic acid degradation"

## Biological Role

Component of phenylacetyl-CoA 1,2-epoxidase (complex.ecocyc.CPLX0-1762).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Component of 1,2-phenylacetyl-CoA epoxidase multicomponent enzyme system which catalyzes the reduction of phenylacetyl-CoA (PA-CoA) to form 1,2-epoxyphenylacetyl-CoA. The subunit C may be essential for structural integrity of the alpha subunit. {ECO:0000269|PubMed:16997993, ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:9748275}.

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1762|complex.ecocyc.CPLX0-1762]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1390|gene.b1390]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76079`
- `KEGG:ecj:JW1385;eco:b1390;ecoc:C3026_08115;`
- `GeneID:945956;`
- `GO:GO:0005829; GO:0010124; GO:0062077`

## Notes

1,2-phenylacetyl-CoA epoxidase, subunit C (1,2-phenylacetyl-CoA epoxidase, structural subunit beta) (1,2-phenylacetyl-CoA monooxygenase, subunit C)
