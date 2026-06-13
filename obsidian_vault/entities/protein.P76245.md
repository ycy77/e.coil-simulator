---
entity_id: "protein.P76245"
entity_type: "protein"
name: "dgcP"
source_database: "UniProt"
source_id: "P76245"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dgcP yeaP b1794 JW5292"
---

# dgcP

`protein.P76245`

## Static

- Type: `protein`
- Source: `UniProt:P76245`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the synthesis of cyclic-di-GMP (c-di-GMP) via the condensation of 2 GTP molecules. Cyclic-di-GMP is a second messenger which controls cell surface-associated traits in bacteria. {ECO:0000269|PubMed:15716451}. DgcP has an N-terminal GAF domain and a C-terminal GGDEF domain with diguanylate cyclase activity . dgcP is expressed during exponential growth. A dgcP mutant shows reduced expression of the csgBAC curli structural operon, but has no effect on CsgD accumulation or dgcC expression . DgcP: diguanylate cyclase P Reviews:

## Biological Role

Catalyzes RXN0-5359 (reaction.ecocyc.RXN0-5359).

## Annotation

FUNCTION: Catalyzes the synthesis of cyclic-di-GMP (c-di-GMP) via the condensation of 2 GTP molecules. Cyclic-di-GMP is a second messenger which controls cell surface-associated traits in bacteria. {ECO:0000269|PubMed:15716451}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5359|reaction.ecocyc.RXN0-5359]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1794|gene.b1794]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76245`
- `KEGG:ecj:JW5292;eco:b1794;ecoc:C3026_10225;`
- `GeneID:948969;`
- `GO:GO:0005525; GO:0005886; GO:0043709; GO:0046872; GO:0052621; GO:1902201`
- `EC:2.7.7.65`

## Notes

Diguanylate cyclase DgcP (DGC) (EC 2.7.7.65)
