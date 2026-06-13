---
entity_id: "gene.b3521"
entity_type: "gene"
name: "rcdB"
source_database: "NCBI RefSeq"
source_id: "gene-b3521"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3521"
  - "rcdB"
---

# rcdB

`gene.b3521`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3521`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rcdB (gene.b3521) is a gene entity. It encodes yhjC (protein.P37641). Encoded protein function: Uncharacterized HTH-type transcriptional regulator YhjC EcoCyc product frame: EG12247-MONOMER. EcoCyc synonyms: yhjC. Genomic coordinates: 3672414-3673313. EcoCyc protein note: YhjC was predicted to be a LysR-type transcription factor . This protein contains a helix-turn-helix motif to bind DNA in its N-terminal domain, and it was predicted that this protein regulates genes related to metabolism and antibiotic sensitivity . Genome-wide YhjC binding sites were determined in vivo by the chromatin immunoprecipitation method combined with lambda exonuclease digestion (ChIP-exo) in glucose M9 minimal medium . The YhjC binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding energy matrix and genomic binding profiles can be accessed at boltznet.bu.edu . Transcription of the yhjC gene is affected by temperature .

## Biological Role

Activated by phoB (protein.P0AFJ5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37641|protein.P37641]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=rcdB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011503,ECOCYC:EG12247,GeneID:948035`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3672414-3673313:+; feature_type=gene
