---
entity_id: "protein.P0A9U6"
entity_type: "protein"
name: "puuR"
source_database: "UniProt"
source_id: "P0A9U6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "puuR ycjC b1299 JW1292"
---

# puuR

`protein.P0A9U6`

## Static

- Type: `protein`
- Source: `UniProt:P0A9U6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Represses puuA, puuD and puuP. {ECO:0000269|PubMed:15590624, ECO:0000269|PubMed:20639325}. PuuR is a transcription repressor that regulates transcription of several genes and operons involved in putrescine utilization and transport . Transcription of puuA was induced in a puuR deletion mutant . This regulator is comprised of two domains: the carboxy-terminal domain, which is similar to cupin superfamily proteins, and the amino-terminal domain, which has high similarity to regulators of the HTH-XRE family . Nemoto et al. showed that this regulator binds to four target sites in the divergent region located between the operons puuA and puuDR. Its regulator represses transcription by overlapping the promoters puuAp and puuDp, and the binding targets for PuuR consist of 15 nucleotides, with the following recognition sequence: AAAATATAATGAACA . The transcription of the puu genes occurs when putrescine interacts with PuuR; this effect changes the conformation of PuuR, and its regulator dissociates from the binding sites. When the level of putrescine decreases in the cell, PuuR can repress the transcription of puu genes . PuuR was transcriptionally upregulated in iron excess over iron limitation at 6.3% and 21% of dissolved oxygen as determined by RNA-seq . Deletion of puuR impairs pili-dependent surface motility (PDSM) in E. coli strain W3110 .

## Biological Role

Component of PuuR-putrescine (complex.ecocyc.CPLX0-8085).

## Annotation

FUNCTION: Represses puuA, puuD and puuP. {ECO:0000269|PubMed:15590624, ECO:0000269|PubMed:20639325}.

## Outgoing Edges (9)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8085|complex.ecocyc.CPLX0-8085]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b1296|gene.b1296]] `RegulonDB` `C` - regulator=PuuR; target=puuP; function=-
- `represses` --> [[gene.b1297|gene.b1297]] `RegulonDB` `C` - regulator=PuuR; target=puuA; function=-
- `represses` --> [[gene.b1298|gene.b1298]] `RegulonDB` `C` - regulator=PuuR; target=puuD; function=-
- `represses` --> [[gene.b1299|gene.b1299]] `RegulonDB` `S` - regulator=PuuR; target=puuR; function=-
- `represses` --> [[gene.b1300|gene.b1300]] `RegulonDB` `S` - regulator=PuuR; target=puuC; function=-
- `represses` --> [[gene.b1301|gene.b1301]] `RegulonDB` `S` - regulator=PuuR; target=puuB; function=-
- `represses` --> [[gene.b1302|gene.b1302]] `RegulonDB` `C` - regulator=PuuR; target=puuE; function=-
- `represses` --> [[gene.b4742|gene.b4742]] `RegulonDB` `S` - regulator=PuuR; target=ymjE; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1299|gene.b1299]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9U6`
- `KEGG:ecj:JW1292;eco:b1299;`
- `GeneID:86859881;93775425;945886;`
- `GO:GO:0003677; GO:0003700; GO:0006351; GO:0006355; GO:0009447`

## Notes

HTH-type transcriptional regulator PuuR
