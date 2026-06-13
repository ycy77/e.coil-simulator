---
entity_id: "protein.P52106"
entity_type: "protein"
name: "csgD"
source_database: "UniProt"
source_id: "P52106"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:16513732}; Peripheral membrane protein {ECO:0000305|PubMed:16513732}. Note=In experiments done with low-level constitutively expressed protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "csgD b1040 JW1023"
---

# csgD

`protein.P52106`

## Static

- Type: `protein`
- Source: `UniProt:P52106`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:16513732}; Peripheral membrane protein {ECO:0000305|PubMed:16513732}. Note=In experiments done with low-level constitutively expressed protein.

## Enriched Summary

FUNCTION: The master regulator for adhesive curli fimbriae expression; necessary for transcription of the csgBAC/ymdA operon. Plays a positive role in biofilm formation. May have the capability to respond to starvation and/or high cell density by activating csgBA transcription. Low-level constitutive expression confers an adherent curli fimbriae-expressing phenotype, up-regulates 10 genes and down-regulates 14 others. {ECO:0000269|PubMed:16513732}. The protein CsgD, for "Curlin subunit gene D," is a transcriptional regulator that regulates a number of genes involved in the Curli assembly, transport, and structural components , which are important for biofilm formation . CsgD was beneficial to biofilm formation in Salmonella Typhimurium, like in E. coli, after 48 h of growth . In addition, it also regulates genes related to cell surface-associated structures . It may also have the capability to respond to starvation and high cell density and positively controls σS expression . In general the environmental conditions, such as low osmolarity, low growth temperature (csgD and the production of the biofilm and cellulose . Since csgD is induced during the mid-exponential phase of growth and the CsgD-dependent activation of csg genes is detected in the stationary phase, it has been suggested that CsgD is posttranscriptionally activated in the stationary phase...

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: The master regulator for adhesive curli fimbriae expression; necessary for transcription of the csgBAC/ymdA operon. Plays a positive role in biofilm formation. May have the capability to respond to starvation and/or high cell density by activating csgBA transcription. Low-level constitutive expression confers an adherent curli fimbriae-expressing phenotype, up-regulates 10 genes and down-regulates 14 others. {ECO:0000269|PubMed:16513732}.

## Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (26)

- `activates` --> [[gene.b0385|gene.b0385]] `RegulonDB` `S` - regulator=CsgD; target=dgcC; function=+
- `activates` --> [[gene.b0964|gene.b0964]] `RegulonDB` `S` - regulator=CsgD; target=csgI; function=+
- `activates` --> [[gene.b1003|gene.b1003]] `RegulonDB` `S` - regulator=CsgD; target=yccJ; function=+
- `activates` --> [[gene.b1004|gene.b1004]] `RegulonDB` `S` - regulator=CsgD; target=wrbA; function=+
- `activates` --> [[gene.b1037|gene.b1037]] `RegulonDB` `S` - regulator=CsgD; target=csgG; function=+
- `activates` --> [[gene.b1038|gene.b1038]] `RegulonDB` `S` - regulator=CsgD; target=csgF; function=+
- `activates` --> [[gene.b1039|gene.b1039]] `RegulonDB` `S` - regulator=CsgD; target=csgE; function=+
- `activates` --> [[gene.b1040|gene.b1040]] `RegulonDB` `S` - regulator=CsgD; target=csgD; function=+
- `activates` --> [[gene.b1041|gene.b1041]] `RegulonDB` `S` - regulator=CsgD; target=csgB; function=+
- `activates` --> [[gene.b1042|gene.b1042]] `RegulonDB` `S` - regulator=CsgD; target=csgA; function=+
- `activates` --> [[gene.b1043|gene.b1043]] `RegulonDB` `S` - regulator=CsgD; target=csgC; function=+
- `activates` --> [[gene.b3661|gene.b3661]] `RegulonDB` `S` - regulator=CsgD; target=nlpA; function=+
- `represses` --> [[gene.b1070|gene.b1070]] `RegulonDB` `S` - regulator=CsgD; target=flgN; function=-
- `represses` --> [[gene.b1071|gene.b1071]] `RegulonDB` `S` - regulator=CsgD; target=flgM; function=-
- `represses` --> [[gene.b1920|gene.b1920]] `RegulonDB` `S` - regulator=CsgD; target=tcyJ; function=-
- `represses` --> [[gene.b1921|gene.b1921]] `RegulonDB` `S` - regulator=CsgD; target=fliZ; function=-
- `represses` --> [[gene.b1922|gene.b1922]] `RegulonDB` `S` - regulator=CsgD; target=fliA; function=-
- `represses` --> [[gene.b1937|gene.b1937]] `RegulonDB` `S` - regulator=CsgD; target=fliE; function=-
- `represses` --> [[gene.b1938|gene.b1938]] `RegulonDB` `S` - regulator=CsgD; target=fliF; function=-
- `represses` --> [[gene.b1939|gene.b1939]] `RegulonDB` `S` - regulator=CsgD; target=fliG; function=-
- `represses` --> [[gene.b1940|gene.b1940]] `RegulonDB` `S` - regulator=CsgD; target=fliH; function=-
- `represses` --> [[gene.b1941|gene.b1941]] `RegulonDB` `S` - regulator=CsgD; target=fliI; function=-
- `represses` --> [[gene.b1942|gene.b1942]] `RegulonDB` `S` - regulator=CsgD; target=fliJ; function=-
- `represses` --> [[gene.b1943|gene.b1943]] `RegulonDB` `S` - regulator=CsgD; target=fliK; function=-
- `represses` --> [[gene.b3156|gene.b3156]] `RegulonDB` `S` - regulator=CsgD; target=yhbS; function=-
- `represses` --> [[gene.b3157|gene.b3157]] `RegulonDB` `S` - regulator=CsgD; target=ubiT; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1040|gene.b1040]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52106`
- `KEGG:ecj:JW1023;eco:b1040;ecoc:C3026_06330;`
- `GeneID:949119;`
- `GO:GO:0000976; GO:0000987; GO:0001216; GO:0001217; GO:0005886; GO:0032993; GO:0042802; GO:1900190; GO:2000144`

## Notes

CsgBAC operon transcriptional regulatory protein
