---
entity_id: "gene.b2620"
entity_type: "gene"
name: "smpB"
source_database: "NCBI RefSeq"
source_id: "gene-b2620"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2620"
  - "smpB"
---

# smpB

`gene.b2620`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2620`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

smpB (gene.b2620) is a gene entity. It encodes smpB (protein.P0A832). Encoded protein function: FUNCTION: Required for rescue of stalled ribosomes mediated by trans-translation. Binds to tmRNA RNA (also known as SsrA or 10Sa RNA, 363 nucleotides in this organism), required for stable binding of tmRNA to ribosomes (PubMed:10393194, PubMed:11904185, PubMed:11917023). tmRNA and SmpB together mimic tRNA shape, replacing the anticodon stem-loop with SmpB (Probable). tmRNA is encoded by the ssrA gene; the 2 termini fold to resemble tRNA(Ala) and it encodes a 'tag peptide', a short internal open reading frame. Able to recruit charged tmRNA to ribosomes (PubMed:15069072). Does not play a role in transcription, processing or Ala-aminoacylation of tmRNA (PubMed:10393194). Other studies have shown it stimulates aminoacylation of tmRNA (PubMed:11904185, PubMed:11917023). May protect tmRNA from degradation (PubMed:11917023). Binds to tmRNA that cannot be aminoacylated (tmRNA G3A), does not bind to tmRNA mutations near the tRNA-like termini (tmRNA G19C, A334U); other tmRNA mutations that block trans-translation still bind SmpB (PubMed:11917023). With tmRNA may play a role in bacterial persistence (PubMed:23812681). During trans-translation Ala-aminoacylated transfer-messenger RNA acts like a tRNA, entering the A-site of stalled ribosomes, displacing the stalled mRNA...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A832|protein.P0A832]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008622,ECOCYC:EG11782,GeneID:947296`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2754896-2755378:+; feature_type=gene
