---
entity_id: "protein.P75811"
entity_type: "protein"
name: "rcdA"
source_database: "UniProt"
source_id: "P75811"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rcdA ybjK b0846 JW5114"
---

# rcdA

`protein.P75811`

## Static

- Type: `protein`
- Source: `UniProt:P75811`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Regulates the expression of a number of genes involved in biofilm formation and stress response. Target genes include six stress-response transcriptional regulators: csgD, which is a master regulator of biofilm formation, appY, sxy, ycgF, fimB and rcdA itself. This indicates that a large number of genes must be regulated indirectly via these transcriptional regulators. Acts by binding to the upstream region of its target genes. {ECO:0000269|PubMed:23233451}.

## Biological Role

Component of DNA binding transcriptional dual regulator RcdA (complex.ecocyc.CPLX0-8597).

## Annotation

FUNCTION: Regulates the expression of a number of genes involved in biofilm formation and stress response. Target genes include six stress-response transcriptional regulators: csgD, which is a master regulator of biofilm formation, appY, sxy, ycgF, fimB and rcdA itself. This indicates that a large number of genes must be regulated indirectly via these transcriptional regulators. Acts by binding to the upstream region of its target genes. {ECO:0000269|PubMed:23233451}.

## Outgoing Edges (15)

- `activates` --> [[gene.b0846|gene.b0846]] `RegulonDB` `C` - regulator=RcdA; target=rcdA; function=+
- `activates` --> [[gene.b0953|gene.b0953]] `RegulonDB` `S` - regulator=RcdA; target=rmf; function=+
- `activates` --> [[gene.b1037|gene.b1037]] `RegulonDB` `S` - regulator=RcdA; target=csgG; function=+
- `activates` --> [[gene.b1038|gene.b1038]] `RegulonDB` `S` - regulator=RcdA; target=csgF; function=+
- `activates` --> [[gene.b1039|gene.b1039]] `RegulonDB` `S` - regulator=RcdA; target=csgE; function=+
- `activates` --> [[gene.b1040|gene.b1040]] `RegulonDB` `S` - regulator=RcdA; target=csgD; function=+
- `activates` --> [[gene.b1163|gene.b1163]] `RegulonDB` `C` - regulator=RcdA; target=bluF; function=+
- `activates` --> [[gene.b1536|gene.b1536]] `RegulonDB` `S` - regulator=RcdA; target=ydeI; function=+
- `activates` --> [[gene.b1597|gene.b1597]] `RegulonDB` `S` - regulator=RcdA; target=asr; function=+
- `activates` --> [[gene.b3995|gene.b3995]] `RegulonDB` `S` - regulator=RcdA; target=rsd; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-8597|complex.ecocyc.CPLX0-8597]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b0277|gene.b0277]] `RegulonDB` `S` - regulator=RcdA; target=yagK; function=-
- `represses` --> [[gene.b0844|gene.b0844]] `RegulonDB` `C` - regulator=RcdA; target=ybjI; function=-
- `represses` --> [[gene.b0845|gene.b0845]] `RegulonDB` `C` - regulator=RcdA; target=ybjJ; function=-
- `represses` --> [[gene.b0958|gene.b0958]] `RegulonDB` `C` - regulator=RcdA; target=sulA; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0846|gene.b0846]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75811`
- `KEGG:ecj:JW5114;eco:b0846;ecoc:C3026_05285;`
- `GeneID:945473;`
- `GO:GO:0003677; GO:0003700; GO:0006351; GO:0045893`

## Notes

HTH-type transcriptional regulator RcdA (Regulator of csgD)
