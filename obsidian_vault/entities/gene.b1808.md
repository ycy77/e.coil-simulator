---
entity_id: "gene.b1808"
entity_type: "gene"
name: "yoaA"
source_database: "NCBI RefSeq"
source_id: "gene-b1808"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1808"
  - "yoaA"
---

# yoaA

`gene.b1808`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1808`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yoaA (gene.b1808) is a gene entity. It encodes yoaA (protein.P76257). Encoded protein function: FUNCTION: DNA-dependent ATPase and 5'-3' DNA helicase (PubMed:36509145). Has single-stranded (ss)DNA-dependent ATPase activity and 5'-3' helicase activity on forked DNA; both activities were measure in a YoaA:HolC (chi) complex (PubMed:36509145). Requires a 20-35 nucleotide (nt) 5'-ssDNA tail; dsDNA with a 20 nt gap is also unwound (PubMed:36509145). Unwinds damaged 3' nascent ends (such as those terminated by 3' azidothymidine (AZT), 3' dideoxy-C or an abasic site on the translocating strand), to promote repair and AZT excision (PubMed:36509145). Without HolC the protein has much lower activity which could be due to YoaA instability or helicase stimulation by HolC (PubMed:36509145). Genetically identified as involved in the repair of replication forks and tolerance of the chain-terminating nucleoside analog AZT (PubMed:26544712, PubMed:33582602, PubMed:34181484). May act in proofreading during nucleotide misincorporation, it appears to aid in the removal of potential A-to-T transversion mutations in ndk mutants (Probable) (PubMed:34181484). {ECO:0000250|UniProtKB:P27296, ECO:0000269|PubMed:26544712, ECO:0000269|PubMed:33582602, ECO:0000269|PubMed:34181484, ECO:0000269|PubMed:36509145}. EcoCyc product frame: G6992-MONOMER. Genomic coordinates: 1891325-1893235...

## Biological Role

Repressed by DNA-binding transcriptional repressor LexA (complex.ecocyc.PC00010), lexA (protein.P0A7C2).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76257|protein.P76257]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[complex.ecocyc.PC00010|complex.ecocyc.PC00010]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A7C2|protein.P0A7C2]] `RegulonDB` `S` - regulator=LexA; target=yoaA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006016,ECOCYC:G6992,GeneID:946305`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1891325-1893235:-; feature_type=gene
