---
entity_id: "gene.b4179"
entity_type: "gene"
name: "rnr"
source_database: "NCBI RefSeq"
source_id: "gene-b4179"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4179"
  - "rnr"
---

# rnr

`gene.b4179`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4179`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rnr (gene.b4179) is a gene entity. It encodes rnr (protein.P21499). Encoded protein function: FUNCTION: 3'-5' exoribonuclease that releases 5'-nucleoside monophosphates and is involved in maturation of structured RNAs (rRNAs, tRNAs and SsrA/tmRNA). In stationary phase, involved in the post-transcriptional regulation of ompA mRNA stability. Shortens RNA processively to di- and trinucleotides. In vitro, exhibits helicase activity, which is independent of its RNase activity. RNases 2 and R (rnb and this entry) contribute to rRNA degradation during starvation, while RNase R and PNPase (this entry and pnp) are the major contributors to quality control of rRNA during steady state growth (PubMed:21135037). Required for the expression of virulence genes in enteroinvasive strains of E.coli. {ECO:0000269|PubMed:11948193, ECO:0000269|PubMed:14622421, ECO:0000269|PubMed:16556233, ECO:0000269|PubMed:20023028, ECO:0000269|PubMed:21135037}. EcoCyc product frame: EG11259-MONOMER. EcoCyc synonyms: vacB, yjeC. Genomic coordinates: 4406654-4409095. EcoCyc protein note: RNase R is a ribonuclease that has been implicated in rRNA maturation, mRNA degradation during stationary phase, degradation of polyadenylated mRNAs, and tmRNA-mediated degradation of non-stop mRNAs...

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco03018` RNA degradation (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21499|protein.P21499]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013678,ECOCYC:EG11259,GeneID:948692`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4406654-4409095:+; feature_type=gene
