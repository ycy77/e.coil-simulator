---
entity_id: "gene.b3231"
entity_type: "gene"
name: "rplM"
source_database: "NCBI RefSeq"
source_id: "gene-b3231"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3231"
  - "rplM"
---

# rplM

`gene.b3231`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3231`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rplM (gene.b3231) is a gene entity. It encodes rplM (protein.P0AA10). Encoded protein function: FUNCTION: This protein is one of the early assembly proteins of the 50S ribosomal subunit, although it is not seen to bind rRNA by itself. It is important during the early stages of 50S assembly. {ECO:0000269|PubMed:3298242}. EcoCyc product frame: EG10874-MONOMER. Genomic coordinates: 3378223-3378651. EcoCyc protein note: The L13 protein is an early assembly component of the 50S subunit of the ribosome . The RNA helicase EG10975-MONOMER SrmB was initially proposed to be necessary for the assembly of L13 into the ribosome . However, it was recently shown that SrmB positively regulates expression of L13 and S9 by preventing premature transcription termination; thus, the role of SrmB in ribosome assembly may be to ensure the synthesis of adequate levels of L13 and S9 . L13 interacts with 23S rRNA and crosslinks to it in both free ribosomes and the initiation complex . L13 is located within 21 Å of nucleotide C2475 of 23S rRNA, near the peptidyltransferase center . L13 binds to 5S rRNA and can be crosslinked to L2 , L3 , L20 and L21 . L13 interacts with tRNA in the P site . EG50004-MONOMER Ribosome modulation factor binds near L2, L13, and S13 . A puromycin analog , a tobramycin analog , and a pactamycin analog can be crosslinked to L13...

## Biological Role

Repressed by rplM (protein.P0AA10), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA10|protein.P0AA10]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0AA10|protein.P0AA10]] `RegulonDB` `S` - regulator=RplM; target=rplM; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=rplM; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010599,ECOCYC:EG10874,GeneID:947828`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3378223-3378651:-; feature_type=gene
