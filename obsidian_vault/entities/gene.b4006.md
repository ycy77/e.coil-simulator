---
entity_id: "gene.b4006"
entity_type: "gene"
name: "purH"
source_database: "NCBI RefSeq"
source_id: "gene-b4006"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4006"
  - "purH"
---

# purH

`gene.b4006`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4006`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

purH (gene.b4006) is a gene entity. It encodes purH (protein.P15639). Encoded protein function: Bifunctional purine biosynthesis protein PurH [Includes: Phosphoribosylaminoimidazolecarboxamide formyltransferase (EC 2.1.2.3) (AICAR transformylase); IMP cyclohydrolase (EC 3.5.4.10) (ATIC) (IMP synthase) (Inosinicase)] EcoCyc product frame: AICARTRANSIMPCYCLO-CPLX. Genomic coordinates: 4205943-4207532. EcoCyc protein note: In bacteria and eukaryotes the last two reactions of the de novo purine biosynthetic pathway for IMP biosynthesis are sequentially catalyzed by a bifunctional enzyme containing aminoimidazole carboxamide ribonucleotide (AICAR) transformylase and IMP cyclohydrolase activities. To date, much of the biochemical and structural characterization has been done on the enzyme from organisms other than E. coli (see for example ). In E. coli early studies suggested an association between AICAR transformylase and IMP cyclohydrolase . Later studies concluded that AICAR transformylase and IMP cyclohydrolase form a bifunctional enzyme with both activities residing on a single polypeptide . Complementation studies suggested that the N-terminal domain contains the IMP cyclohydrolase activity and the C-terminal domain contains the AICAR transformylase activity . More recently recombinant, N-terminally His6-tagged enzyme from E...

## Biological Role

Repressed by CRP-cyclic-AMP DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-226), purR (protein.P0ACP7), rbsR (protein.P0ACQ0).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P15639|protein.P15639]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `represses` <-- [[complex.ecocyc.CPLX0-226|complex.ecocyc.CPLX0-226]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACP7|protein.P0ACP7]] `RegulonDB` `S` - regulator=PurR; target=purH; function=-
- `represses` <-- [[protein.P0ACQ0|protein.P0ACQ0]] `RegulonDB` `C` - regulator=RbsR; target=purH; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013097,ECOCYC:EG10795,GeneID:948503`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4205943-4207532:-; feature_type=gene
