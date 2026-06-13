---
entity_id: "gene.b0437"
entity_type: "gene"
name: "clpP"
source_database: "NCBI RefSeq"
source_id: "gene-b0437"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0437"
  - "clpP"
---

# clpP

`gene.b0437`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0437`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

clpP (gene.b0437) is a gene entity. It encodes clpP (protein.P0A6G7). Encoded protein function: FUNCTION: Cleaves peptides in various proteins in a process that requires ATP hydrolysis. Has a chymotrypsin-like activity. Plays a major role in the degradation of misfolded proteins. May play the role of a master protease which is attracted to different substrates by different specificity factors such as ClpA or ClpX. Participates in the final steps of RseA-sigma-E degradation, liberating sigma-E to induce the extracytoplasmic-stress response. Degrades antitoxin MazE (PubMed:24375411). {ECO:0000255|HAMAP-Rule:MF_00444, ECO:0000269|PubMed:12941278, ECO:0000269|PubMed:15371343, ECO:0000269|PubMed:24375411}. EcoCyc product frame: EG10158-MONOMER. EcoCyc synonyms: lopP. Genomic coordinates: 456677-457300.

## Biological Role

Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0), rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6G7|protein.P0A6G7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=clpP; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=clpP; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001515,ECOCYC:EG10158,GeneID:945082`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:456677-457300:+; feature_type=gene
