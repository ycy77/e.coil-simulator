---
entity_id: "protein.P0ACG1"
entity_type: "protein"
name: "stpA"
source_database: "UniProt"
source_id: "P0ACG1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm, nucleoid {ECO:0000269|PubMed:21903814}. Note=Scattered throughout the nucleoid (PubMed:21903814). {ECO:0000269|PubMed:21903814}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "stpA hnsB b2669 JW2644"
---

# stpA

`protein.P0ACG1`

## Static

- Type: `protein`
- Source: `UniProt:P0ACG1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm, nucleoid {ECO:0000269|PubMed:21903814}. Note=Scattered throughout the nucleoid (PubMed:21903814). {ECO:0000269|PubMed:21903814}.

## Enriched Summary

FUNCTION: A DNA-binding protein that acts in a fashion similar to H-NS protein upon overexpression, represses a number of genes including the cryptic blg operon, hns, papB and the proU locus (PubMed:8890170). A subset of H-NS/StpA-regulated genes also require Hha for repression; Hha and Cnu (YdgT) increases the number of genes DNA bound by H-NS/StpA and may also modulate the oligomerization of the H-NS/StpA-complex (PubMed:23543115). Repression can be inhibited by dominant-negative mutants of StpA or H-NS (PubMed:8755860). {ECO:0000269|PubMed:23543115, ECO:0000269|PubMed:8755860, ECO:0000269|PubMed:8890170}.; FUNCTION: (Microbial infection) Originally isolated as a suppressor of a splicing defect of the thymidylate synthase (td) gene from bacteriophage T4 (PubMed:1480493). Acts as an RNA chaperone, accelerating splicing of viral pre-mRNA. Binds preferentially to unstructured over structured RNA; does not have a detectable high-affinity RNA-binding site in the pre-mRNA. There do not seem to be any specific RNA targets in transcribed E.coli DNA (PubMed:17267410). {ECO:0000269|PubMed:1480493, ECO:0000269|PubMed:17267410}. StpA protein, for "Suppressor of td phenotype A," is a nucleoid-associated multifunctional protein that acts as a transcriptional repressor , in chromosomal DNA packaging , and as a chaperone...

## Annotation

FUNCTION: A DNA-binding protein that acts in a fashion similar to H-NS protein upon overexpression, represses a number of genes including the cryptic blg operon, hns, papB and the proU locus (PubMed:8890170). A subset of H-NS/StpA-regulated genes also require Hha for repression; Hha and Cnu (YdgT) increases the number of genes DNA bound by H-NS/StpA and may also modulate the oligomerization of the H-NS/StpA-complex (PubMed:23543115). Repression can be inhibited by dominant-negative mutants of StpA or H-NS (PubMed:8755860). {ECO:0000269|PubMed:23543115, ECO:0000269|PubMed:8755860, ECO:0000269|PubMed:8890170}.; FUNCTION: (Microbial infection) Originally isolated as a suppressor of a splicing defect of the thymidylate synthase (td) gene from bacteriophage T4 (PubMed:1480493). Acts as an RNA chaperone, accelerating splicing of viral pre-mRNA. Binds preferentially to unstructured over structured RNA; does not have a detectable high-affinity RNA-binding site in the pre-mRNA. There do not seem to be any specific RNA targets in transcribed E.coli DNA (PubMed:17267410). {ECO:0000269|PubMed:1480493, ECO:0000269|PubMed:17267410}.

## Outgoing Edges (9)

- `activates` --> [[gene.b2754|gene.b2754]] `RegulonDB` `C` - regulator=StpA; target=cas2; function=+
- `activates` --> [[gene.b2755|gene.b2755]] `RegulonDB` `C` - regulator=StpA; target=cas1; function=+
- `activates` --> [[gene.b2756|gene.b2756]] `RegulonDB` `C` - regulator=StpA; target=casE; function=+
- `activates` --> [[gene.b2757|gene.b2757]] `RegulonDB` `C` - regulator=StpA; target=casD; function=+
- `activates` --> [[gene.b2758|gene.b2758]] `RegulonDB` `C` - regulator=StpA; target=casC; function=+
- `activates` --> [[gene.b2759|gene.b2759]] `RegulonDB` `C` - regulator=StpA; target=casB; function=+
- `activates` --> [[gene.b2760|gene.b2760]] `RegulonDB` `C` - regulator=StpA; target=casA; function=+
- `represses` --> [[gene.b2911|gene.b2911]] `RegulonDB` `S` - regulator=StpA; target=ssrS; function=-
- `represses` --> [[gene.b2912|gene.b2912]] `RegulonDB` `S` - regulator=StpA; target=fau; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b2669|gene.b2669]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACG1`
- `KEGG:ecj:JW2644;eco:b2669;ecoc:C3026_14710;`
- `GeneID:93779342;947130;`
- `GO:GO:0000976; GO:0001217; GO:0003677; GO:0003680; GO:0003681; GO:0003723; GO:0005829; GO:0009295; GO:0030527; GO:0032993; GO:0046983`

## Notes

DNA-binding protein StpA (H-NS homolog StpA)
