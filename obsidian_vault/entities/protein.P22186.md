---
entity_id: "protein.P22186"
entity_type: "protein"
name: "mraZ"
source_database: "UniProt"
source_id: "P22186"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm, nucleoid {ECO:0000255|HAMAP-Rule:MF_01008, ECO:0000269|PubMed:24659771}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mraZ yabB b0081 JW0079"
---

# mraZ

`protein.P22186`

## Static

- Type: `protein`
- Source: `UniProt:P22186`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm, nucleoid {ECO:0000255|HAMAP-Rule:MF_01008, ECO:0000269|PubMed:24659771}.

## Enriched Summary

FUNCTION: Negatively regulates its own expression and that of the subsequent genes in the proximal part of the division and cell wall (dcw) gene cluster. Acts by binding directly to DNA. May also regulate the expression of genes outside the dcw cluster. {ECO:0000255|HAMAP-Rule:MF_01008, ECO:0000269|PubMed:24659771}. MraZ is a transcriptional repressor involved in the control of cell division and cell wall genes . Based on differential gene expression analysis comparing the WT to a mraZ mutant, 100 genes under the control of MraZ were identified . The analysis showed that three successive TGGGN direct repeats are separated by two consecutive 5-nt spacers . By using synthetic gene circuits, it was demonstrated that MraZ acts as an activator under the tested conditions, with stronger activation when its binding site is located at positions +1 and -57 relative to the promoter compared to the distal upstream position -103 . The MraZ protein is highly conserved in bacteria , and MraW is more universal . MraZ is similar in both structure and sequence to the DNA-binding transition-state regulator AbrB from Bacillus subtilis . A preliminary analysis of the crystal structure of MraZ has been published . It was previously suggested that MraZ is an inhibitor of the RsmH methyltransferase , but this report has since been retracted . A mraZ null mutation has been generated...

## Annotation

FUNCTION: Negatively regulates its own expression and that of the subsequent genes in the proximal part of the division and cell wall (dcw) gene cluster. Acts by binding directly to DNA. May also regulate the expression of genes outside the dcw cluster. {ECO:0000255|HAMAP-Rule:MF_01008, ECO:0000269|PubMed:24659771}.

## Outgoing Edges (18)

- `represses` --> [[gene.b0081|gene.b0081]] `RegulonDB` `C` - regulator=MraZ; target=mraZ; function=-
- `represses` --> [[gene.b0082|gene.b0082]] `RegulonDB` `C` - regulator=MraZ; target=rsmH; function=-
- `represses` --> [[gene.b0083|gene.b0083]] `RegulonDB` `C` - regulator=MraZ; target=ftsL; function=-
- `represses` --> [[gene.b0084|gene.b0084]] `RegulonDB` `C` - regulator=MraZ; target=ftsI; function=-
- `represses` --> [[gene.b0085|gene.b0085]] `RegulonDB` `C` - regulator=MraZ; target=murE; function=-
- `represses` --> [[gene.b0086|gene.b0086]] `RegulonDB` `C` - regulator=MraZ; target=murF; function=-
- `represses` --> [[gene.b0087|gene.b0087]] `RegulonDB` `C` - regulator=MraZ; target=mraY; function=-
- `represses` --> [[gene.b0088|gene.b0088]] `RegulonDB` `C` - regulator=MraZ; target=murD; function=-
- `represses` --> [[gene.b0089|gene.b0089]] `RegulonDB` `C` - regulator=MraZ; target=ftsW; function=-
- `represses` --> [[gene.b0090|gene.b0090]] `RegulonDB` `C` - regulator=MraZ; target=murG; function=-
- `represses` --> [[gene.b0091|gene.b0091]] `RegulonDB` `C` - regulator=MraZ; target=murC; function=-
- `represses` --> [[gene.b0092|gene.b0092]] `RegulonDB` `C` - regulator=MraZ; target=ddlB; function=-
- `represses` --> [[gene.b0093|gene.b0093]] `RegulonDB` `C` - regulator=MraZ; target=ftsQ; function=-
- `represses` --> [[gene.b0094|gene.b0094]] `RegulonDB` `C` - regulator=MraZ; target=ftsA; function=-
- `represses` --> [[gene.b0095|gene.b0095]] `RegulonDB` `C` - regulator=MraZ; target=ftsZ; function=-
- `represses` --> [[gene.b0096|gene.b0096]] `RegulonDB` `C` - regulator=MraZ; target=lpxC; function=-
- `represses` --> [[gene.b3742|gene.b3742]] `RegulonDB` `S` - regulator=MraZ; target=mioC; function=-
- `represses` --> [[gene.b4810|gene.b4810]] `RegulonDB` `C` - regulator=MraZ; target=ftsO; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0081|gene.b0081]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P22186`
- `KEGG:ecj:JW0079;eco:b0081;`
- `GeneID:944810;`
- `GO:GO:0000976; GO:0003700; GO:0005737; GO:0009295; GO:0043565; GO:0045892; GO:2000143`

## Notes

Transcriptional regulator MraZ
