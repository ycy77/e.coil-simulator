---
entity_id: "protein.P52627"
entity_type: "protein"
name: "fliZ"
source_database: "UniProt"
source_id: "P52627"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fliZ yedH b1921 JW1906"
---

# fliZ

`protein.P52627`

## Static

- Type: `protein`
- Source: `UniProt:P52627`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: During the post-exponential growth phase transiently interferes with RpoS (sigma S) activity without affecting expression of RpoS itself. It is probably not an anti-sigma factor as its overexpression is detrimental in rapidly growing cells where there is almost no sigma S factor. There is a strong overlap between Crl-activated genes and FliZ-down-regulated genes. FliZ acts as a timing device for expression of the genes for the adhesive curli fimbriae by indirectly decreasing expression of the curli regulator CsgD. {ECO:0000269|PubMed:18765794}. The transcriptional repressor FliZ controls the transcription of genes involved in the regulation of curli expression and the motility system . During the post-exponential growth phase, this regulator is an abundant protein in the genome, with about 21,500 molecules per cell. Transcriptome expression analysis showed a global antagonistic effect between FliZ and σS that resulted in physiological traits, including flagellum-mediated motility and curli fimbria-mediated adhesion . Overexpression of FliZ slightly increased polyP accumulation . Moreover, FliZ interferes with binding within σS-dependent promoters, can also discriminate vegetative promoters, and can recognize alternative σS promoter-like sequences . The C-terminal domain of FliZ contains an α-helix that is similar to helix 3...

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Annotation

FUNCTION: During the post-exponential growth phase transiently interferes with RpoS (sigma S) activity without affecting expression of RpoS itself. It is probably not an anti-sigma factor as its overexpression is detrimental in rapidly growing cells where there is almost no sigma S factor. There is a strong overlap between Crl-activated genes and FliZ-down-regulated genes. FliZ acts as a timing device for expression of the genes for the adhesive curli fimbriae by indirectly decreasing expression of the curli regulator CsgD. {ECO:0000269|PubMed:18765794}.

## Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (19)

- `represses` --> [[gene.b1037|gene.b1037]] `RegulonDB` `S` - regulator=FliZ; target=csgG; function=-
- `represses` --> [[gene.b1038|gene.b1038]] `RegulonDB` `S` - regulator=FliZ; target=csgF; function=-
- `represses` --> [[gene.b1039|gene.b1039]] `RegulonDB` `S` - regulator=FliZ; target=csgE; function=-
- `represses` --> [[gene.b1040|gene.b1040]] `RegulonDB` `S` - regulator=FliZ; target=csgD; function=-
- `represses` --> [[gene.b1285|gene.b1285]] `RegulonDB` `C` - regulator=FliZ; target=pdeR; function=-
- `represses` --> [[gene.b1492|gene.b1492]] `RegulonDB` `S` - regulator=FliZ; target=gadC; function=-
- `represses` --> [[gene.b1493|gene.b1493]] `RegulonDB` `S` - regulator=FliZ; target=gadB; function=-
- `represses` --> [[gene.b1891|gene.b1891]] `RegulonDB` `S` - regulator=FliZ; target=flhC; function=-
- `represses` --> [[gene.b1892|gene.b1892]] `RegulonDB` `S` - regulator=FliZ; target=flhD; function=-
- `represses` --> [[gene.b2127|gene.b2127]] `RegulonDB` `C` - regulator=FliZ; target=mlrA; function=-
- `represses` --> [[gene.b3508|gene.b3508]] `RegulonDB` `S` - regulator=FliZ; target=yhiD; function=-
- `represses` --> [[gene.b3509|gene.b3509]] `RegulonDB` `S` - regulator=FliZ; target=hdeB; function=-
- `represses` --> [[gene.b3510|gene.b3510]] `RegulonDB` `S` - regulator=FliZ; target=hdeA; function=-
- `represses` --> [[gene.b3512|gene.b3512]] `RegulonDB` `C` - regulator=FliZ; target=gadE; function=-
- `represses` --> [[gene.b3513|gene.b3513]] `RegulonDB` `C` - regulator=FliZ; target=mdtE; function=-
- `represses` --> [[gene.b3514|gene.b3514]] `RegulonDB` `C` - regulator=FliZ; target=mdtF; function=-
- `represses` --> [[gene.b4045|gene.b4045]] `RegulonDB` `S` - regulator=FliZ; target=yjbJ; function=-
- `represses` --> [[gene.b4376|gene.b4376]] `RegulonDB` `S` - regulator=FliZ; target=osmY; function=-
- `represses` --> [[gene.b4718|gene.b4718]] `RegulonDB` `C` - regulator=FliZ; target=gadF; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1921|gene.b1921]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52627`
- `KEGG:ecj:JW1906;eco:b1921;ecoc:C3026_10900;`
- `GeneID:946833;`
- `GO:GO:0001046; GO:0015074; GO:0016989; GO:1902021`

## Notes

Regulator of sigma S factor FliZ
