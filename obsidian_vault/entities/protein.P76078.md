---
entity_id: "protein.P76078"
entity_type: "protein"
name: "paaB"
source_database: "UniProt"
source_id: "P76078"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "paaB ynbF b1389 JW1384"
---

# paaB

`protein.P76078`

## Static

- Type: `protein`
- Source: `UniProt:P76078`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Component of 1,2-phenylacetyl-CoA epoxidase multicomponent enzyme system which catalyzes the reduction of phenylacetyl-CoA (PA-CoA) to form 1,2-epoxyphenylacetyl-CoA. The subunit B may play a regulatory role or be directly involved in electron transport. {ECO:0000269|PubMed:16997993, ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:9748275}. PaaB has similarity to the activator protein of diiron monooxygenase complexes . PaaB: "phenylacetic acid degradation"

## Biological Role

Component of phenylacetyl-CoA 1,2-epoxidase (complex.ecocyc.CPLX0-1762).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Component of 1,2-phenylacetyl-CoA epoxidase multicomponent enzyme system which catalyzes the reduction of phenylacetyl-CoA (PA-CoA) to form 1,2-epoxyphenylacetyl-CoA. The subunit B may play a regulatory role or be directly involved in electron transport. {ECO:0000269|PubMed:16997993, ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:9748275}.

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1762|complex.ecocyc.CPLX0-1762]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1389|gene.b1389]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76078`
- `KEGG:ecj:JW1384;eco:b1389;ecoc:C3026_08110;`
- `GeneID:75203475;947595;`
- `GO:GO:0005829; GO:0010124; GO:0062077`

## Notes

1,2-phenylacetyl-CoA epoxidase, subunit B (1,2-phenylacetyl-CoA monooxygenase, subunit B)
