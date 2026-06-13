---
entity_id: "gene.b1849"
entity_type: "gene"
name: "purT"
source_database: "NCBI RefSeq"
source_id: "gene-b1849"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1849"
  - "purT"
---

# purT

`gene.b1849`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1849`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

purT (gene.b1849) is a gene entity. It encodes purT (protein.P33221). Encoded protein function: FUNCTION: Involved in the de novo purine biosynthesis (PubMed:8117714, PubMed:8501063, PubMed:9184151). Catalyzes the transfer of formate to 5-phospho-ribosyl-glycinamide (GAR), producing 5-phospho-ribosyl-N-formylglycinamide (FGAR) (PubMed:8117714, PubMed:8501063, PubMed:9184151). Formate is provided by PurU via hydrolysis of 10-formyl-tetrahydrofolate (PubMed:8226647). PurT is also able to cleave acetyl phosphate and carbamoyl phosphate to produce ATP with acetate and carbamate, respectively (PubMed:8117714, PubMed:9184151). {ECO:0000269|PubMed:8117714, ECO:0000269|PubMed:8226647, ECO:0000269|PubMed:8501063, ECO:0000269|PubMed:9184151}. EcoCyc product frame: GARTRANSFORMYL2-MONOMER. Genomic coordinates: 1930881-1932059. EcoCyc protein note: E. coli contains two different phosphoribosylglycinamide (GAR) transformylases, both of which can catalyze the third step in de novo purine biosynthesis. The transformylase encoded by purN utilizes 10-formyl-tetrahydrofolate as the formyl donor. The second transformylase encoded by purT utilizes formate, which is provided by PurU-catalyzed hydrolysis of 10-formyl-tetrahydrofolate . The existence of these two transformylase enzymes was determined by mutant studies...

## Biological Role

Repressed by purR (protein.P0ACP7). Activated by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33221|protein.P33221]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACP7|protein.P0ACP7]] `RegulonDB` `C` - regulator=PurR; target=purT; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006162,ECOCYC:EG11809,GeneID:946368`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1930881-1932059:+; feature_type=gene
