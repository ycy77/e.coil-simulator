---
entity_id: "gene.b4387"
entity_type: "gene"
name: "ytjB"
source_database: "NCBI RefSeq"
source_id: "gene-b4387"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4387"
  - "ytjB"
---

# ytjB

`gene.b4387`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4387`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ytjB (gene.b4387) is a gene entity. It encodes ytjB (protein.P0AGC7). Encoded protein function: Probable inner membrane protein Smp EcoCyc product frame: EG10951-MONOMER. EcoCyc synonyms: smp. Genomic coordinates: 4624145-4624789. EcoCyc protein note: Smp is a membrane protein ; Smp is a predicted bitopic inner membrane protein . The signal sequence may also have a regulatory function; the mRNA encoding this region is predicted to have distinct secondary structure . Disruption of the smp gene affects lipoate metabolism, apparently due to effects on lplA transcription . Mutations in the signal sequence result in increased smp transcription . IS30 insertions in the 5' end of the adjacent and divergently transcribed gene, serB, also result in increased smp transcription . ytjB belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12 . Regulation has been described .

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGC7|protein.P0AGC7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0014387,ECOCYC:EG10951,GeneID:946089`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4624145-4624789:-; feature_type=gene
