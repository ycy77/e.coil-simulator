---
entity_id: "gene.b1303"
entity_type: "gene"
name: "pspF"
source_database: "NCBI RefSeq"
source_id: "gene-b1303"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1303"
  - "pspF"
---

# pspF

`gene.b1303`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1303`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pspF (gene.b1303) is a gene entity. It encodes pspF (protein.P37344). Encoded protein function: FUNCTION: Transcriptional activator for the phage shock protein (psp) operon (pspABCDE) and pspG gene. {ECO:0000269|PubMed:15485810, ECO:0000269|PubMed:19804784, ECO:0000269|PubMed:8606168}. EcoCyc product frame: EG12344-MONOMER. EcoCyc synonyms: ycjB. Genomic coordinates: 1366935-1367912. EcoCyc protein note: The transcription factor PspF, for "Phage shock protein F," is a bacterial enhancer-binding protein required for RPON-MONOMER σ54-dependent transcription activation . This regulator activates the transcription of the psp regulon, and it is negatively autoregulated and coordinately activated by transcription of the divergent TU00326 operon . The PC00027 "integration host factor" facilitates control of the psp regulon . The psp regulon is defined as the phage shock protein system, which is involved in protecting the bacterium during infectious processes . The synthesis of this regulon is induced when Escherichia coli is grown under different extracytoplasmic stress conditions and upon infection by filamentous phage (phage shock) . The activity of PspF is inhibited by EG10776-MONOMER PspA, which is an accessory protein that binds directly to PspF to inhibit transcription of the psp regulon...

## Biological Role

Repressed by pspF (protein.P37344).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37344|protein.P37344]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37344|protein.P37344]] `RegulonDB` `S` - regulator=PspF; target=pspF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004383,ECOCYC:EG12344,GeneID:945683`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1366935-1367912:-; feature_type=gene
