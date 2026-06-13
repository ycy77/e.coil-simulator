---
entity_id: "gene.b3222"
entity_type: "gene"
name: "nanK"
source_database: "NCBI RefSeq"
source_id: "gene-b3222"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3222"
  - "nanK"
---

# nanK

`gene.b3222`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3222`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nanK (gene.b3222) is a gene entity. It encodes nanK (protein.P45425). Encoded protein function: FUNCTION: Catalyzes the phosphorylation of N-acetylmannosamine (ManNAc) to ManNAc-6-P. Also has low level glucokinase activity in vitro. {ECO:0000269|PubMed:15157072, ECO:0000269|PubMed:17979299}. EcoCyc product frame: NANK-MONOMER. EcoCyc synonyms: yhcI. Genomic coordinates: 3369475-3370350.

## Biological Role

Repressed by fis (protein.P0A6R3), nanR (protein.P0A8W0). Activated by crp (protein.P0ACJ8), nac (protein.Q47005).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45425|protein.P45425]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=nanK; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=nanK; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nanK; function=-
- `represses` <-- [[protein.P0A8W0|protein.P0A8W0]] `RegulonDB` `C` - regulator=NanR; target=nanK; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010571,ECOCYC:G7676,GeneID:947757`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3369475-3370350:-; feature_type=gene
