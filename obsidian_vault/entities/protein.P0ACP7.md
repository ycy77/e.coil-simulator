---
entity_id: "protein.P0ACP7"
entity_type: "protein"
name: "purR"
source_database: "UniProt"
source_id: "P0ACP7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "purR b1658 JW1650"
---

# purR

`protein.P0ACP7`

## Static

- Type: `protein`
- Source: `UniProt:P0ACP7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Is the main repressor of the genes involved in the de novo synthesis of purine nucleotides, regulating purB, purC, purEK, purF, purHD, purL, purMN and guaBA expression. In addition, it participates in the regulation or coregulation of genes involved in de novo pyrimidine nucleotide biosynthesis, salvage and uptake (pyrC, pyrD, carAB and codBA), and of several genes encoding enzymes necessary for nucleotide and polyamine biosynthesis (prsA, glyA, gcvTHP, speA, glnB). Binds to a 16-bp palindromic sequence located within the promoter region of pur regulon genes. The consensus binding sequence is 5'-ACGCAAACGTTTTCNT-3'. PurR is allosterically activated to bind its cognate DNA by binding the purine corepressors, hypoxanthine or guanine, thereby effecting transcription repression. {ECO:0000269|PubMed:1400170, ECO:0000269|PubMed:14741201, ECO:0000269|PubMed:2211500, ECO:0000269|PubMed:2404765}.

## Biological Role

Component of DNA-binding transcriptional repressor PurR (complex.ecocyc.PC00033).

## Annotation

FUNCTION: Is the main repressor of the genes involved in the de novo synthesis of purine nucleotides, regulating purB, purC, purEK, purF, purHD, purL, purMN and guaBA expression. In addition, it participates in the regulation or coregulation of genes involved in de novo pyrimidine nucleotide biosynthesis, salvage and uptake (pyrC, pyrD, carAB and codBA), and of several genes encoding enzymes necessary for nucleotide and polyamine biosynthesis (prsA, glyA, gcvTHP, speA, glnB). Binds to a 16-bp palindromic sequence located within the promoter region of pur regulon genes. The consensus binding sequence is 5'-ACGCAAACGTTTTCNT-3'. PurR is allosterically activated to bind its cognate DNA by binding the purine corepressors, hypoxanthine or guanine, thereby effecting transcription repression. {ECO:0000269|PubMed:1400170, ECO:0000269|PubMed:14741201, ECO:0000269|PubMed:2211500, ECO:0000269|PubMed:2404765}.

## Outgoing Edges (28)

- `is_component_of` --> [[complex.ecocyc.PC00033|complex.ecocyc.PC00033]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b0032|gene.b0032]] `RegulonDB` `S` - regulator=PurR; target=carA; function=-
- `represses` --> [[gene.b0033|gene.b0033]] `RegulonDB` `S` - regulator=PurR; target=carB; function=-
- `represses` --> [[gene.b0522|gene.b0522]] `RegulonDB` `S` - regulator=PurR; target=purK; function=-
- `represses` --> [[gene.b0523|gene.b0523]] `RegulonDB` `S` - regulator=PurR; target=purE; function=-
- `represses` --> [[gene.b0945|gene.b0945]] `RegulonDB` `S` - regulator=PurR; target=pyrD; function=-
- `represses` --> [[gene.b1062|gene.b1062]] `RegulonDB` `C` - regulator=PurR; target=pyrC; function=-
- `represses` --> [[gene.b1131|gene.b1131]] `RegulonDB` `S` - regulator=PurR; target=purB; function=-
- `represses` --> [[gene.b1132|gene.b1132]] `RegulonDB` `S` - regulator=PurR; target=hflD; function=-
- `represses` --> [[gene.b1207|gene.b1207]] `RegulonDB` `S` - regulator=PurR; target=prs; function=-
- `represses` --> [[gene.b1658|gene.b1658]] `RegulonDB` `C` - regulator=PurR; target=purR; function=-
- `represses` --> [[gene.b1849|gene.b1849]] `RegulonDB` `C` - regulator=PurR; target=purT; function=-
- `represses` --> [[gene.b2311|gene.b2311]] `RegulonDB` `C` - regulator=PurR; target=ubiX; function=-
- `represses` --> [[gene.b2312|gene.b2312]] `RegulonDB` `C` - regulator=PurR; target=purF; function=-
- `represses` --> [[gene.b2313|gene.b2313]] `RegulonDB` `C` - regulator=PurR; target=cvpA; function=-
- `represses` --> [[gene.b2476|gene.b2476]] `RegulonDB` `S` - regulator=PurR; target=purC; function=-
- `represses` --> [[gene.b2499|gene.b2499]] `RegulonDB` `S` - regulator=PurR; target=purM; function=-
- `represses` --> [[gene.b2500|gene.b2500]] `RegulonDB` `S` - regulator=PurR; target=purN; function=-
- `represses` --> [[gene.b2507|gene.b2507]] `RegulonDB` `S` - regulator=PurR; target=guaA; function=-
- `represses` --> [[gene.b2508|gene.b2508]] `RegulonDB` `S` - regulator=PurR; target=guaB; function=-
- `represses` --> [[gene.b2551|gene.b2551]] `RegulonDB` `C` - regulator=PurR; target=glyA; function=-
- `represses` --> [[gene.b2553|gene.b2553]] `RegulonDB` `S` - regulator=PurR; target=glnB; function=-
- `represses` --> [[gene.b2557|gene.b2557]] `RegulonDB` `S` - regulator=PurR; target=purL; function=-
- `represses` --> [[gene.b2937|gene.b2937]] `RegulonDB` `S` - regulator=PurR; target=speB; function=-
- `represses` --> [[gene.b2938|gene.b2938]] `RegulonDB` `S` - regulator=PurR; target=speA; function=-
- `represses` --> [[gene.b4005|gene.b4005]] `RegulonDB` `S` - regulator=PurR; target=purD; function=-
- `represses` --> [[gene.b4006|gene.b4006]] `RegulonDB` `S` - regulator=PurR; target=purH; function=-
- `represses` --> [[gene.b4177|gene.b4177]] `RegulonDB` `S` - regulator=PurR; target=purA; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1658|gene.b1658]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACP7`
- `KEGG:ecj:JW1650;eco:b1658;ecoc:C3026_09515;`
- `GeneID:75171720;75204504;945226;`
- `GO:GO:0000976; GO:0001217; GO:0002057; GO:0003700; GO:0005829; GO:0006164; GO:0006355; GO:0042803; GO:0045892; GO:1900372`

## Notes

HTH-type transcriptional repressor PurR (Pur regulon repressor) (Purine nucleotide synthesis repressor)
