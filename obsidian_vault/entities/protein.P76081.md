---
entity_id: "protein.P76081"
entity_type: "protein"
name: "paaE"
source_database: "UniProt"
source_id: "P76081"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "paaE ydbR b1392 JW1387"
---

# paaE

`protein.P76081`

## Static

- Type: `protein`
- Source: `UniProt:P76081`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Component of 1,2-phenylacetyl-CoA epoxidase multicomponent enzyme system which catalyzes the reduction of phenylacetyl-CoA (PA-CoA) to form 1,2-epoxyphenylacetyl-CoA. The subunit E is a reductase with a preference for NADPH and FAD, capable of reducing cytochrome c. {ECO:0000269|PubMed:16997993, ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:21247899, ECO:0000269|PubMed:9748275}. PaaE has similarity to class IA-like reductases, members of the ferredoxin-NADP+ reductase (FNR) family of proteins . PaaE carries a [2Fe-2S] cluster similar to that of spinach ferredoxin . PaaE: "phenylacetic acid degradation"

## Biological Role

Component of phenylacetyl-CoA 1,2-epoxidase (complex.ecocyc.CPLX0-1762).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Component of 1,2-phenylacetyl-CoA epoxidase multicomponent enzyme system which catalyzes the reduction of phenylacetyl-CoA (PA-CoA) to form 1,2-epoxyphenylacetyl-CoA. The subunit E is a reductase with a preference for NADPH and FAD, capable of reducing cytochrome c. {ECO:0000269|PubMed:16997993, ECO:0000269|PubMed:20660314, ECO:0000269|PubMed:21247899, ECO:0000269|PubMed:9748275}.

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1762|complex.ecocyc.CPLX0-1762]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1392|gene.b1392]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76081`
- `KEGG:ecj:JW1387;eco:b1392;ecoc:C3026_08125;`
- `GeneID:945962;`
- `GO:GO:0005829; GO:0010124; GO:0016491; GO:0046872; GO:0050660; GO:0051537; GO:0062077`
- `EC:1.-.-.-`

## Notes

1,2-phenylacetyl-CoA epoxidase, subunit E (EC 1.-.-.-) (1,2-phenylacetyl-CoA epoxidase, reductase subunit) (1,2-phenylacetyl-CoA monooxygenase, subunit E)
