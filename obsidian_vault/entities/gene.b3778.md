---
entity_id: "gene.b3778"
entity_type: "gene"
name: "rep"
source_database: "NCBI RefSeq"
source_id: "gene-b3778"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3778"
  - "rep"
---

# rep

`gene.b3778`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3778`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rep (gene.b3778) is a gene entity. It encodes rep (protein.P09980). Encoded protein function: FUNCTION: Rep helicase is a single-stranded (ss)DNA-dependent ATPase involved in DNA replication; it can initiate unwinding at a nick in the DNA. It binds to ssDNA and acts in a progressive fashion along the DNA in the 3' to 5' direction (PubMed:221901, PubMed:11428893, PubMed:17382604). Binds double-stranded (ds)DNA with a 5' ss- but not 3' ss-extension and forked structures with either lagging or leading ssDNA (PubMed:17382604). Part of the PriC-Rep pathway for restart of stalled replication forks, which reloads the DnaB replicative helicase on sites other than the origin of replication (PubMed:10835375). {ECO:0000255|HAMAP-Rule:MF_01920, ECO:0000269|PubMed:10835375, ECO:0000269|PubMed:11428893, ECO:0000269|PubMed:17382604, ECO:0000269|PubMed:221901}. EcoCyc product frame: EG10837-MONOMER. EcoCyc synonyms: dasC, mbrA, mmrA. Genomic coordinates: 3960677-3962698.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09980|protein.P09980]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=rep; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012344,ECOCYC:EG10837,GeneID:948292`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3960677-3962698:+; feature_type=gene
