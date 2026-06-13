---
entity_id: "gene.b0422"
entity_type: "gene"
name: "xseB"
source_database: "NCBI RefSeq"
source_id: "gene-b0422"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0422"
  - "xseB"
---

# xseB

`gene.b0422`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0422`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

xseB (gene.b0422) is a gene entity. It encodes xseB (protein.P0A8G9). Encoded protein function: FUNCTION: Bidirectionally degrades single-stranded DNA into large acid-insoluble oligonucleotides, which are then degraded further into small acid-soluble oligonucleotides. It can degrade 3' or 5' ss regions extending from the termini of duplex DNA molecules and displaced ss regions. It can also excise thymine dimers in vitro (Probable) (PubMed:22718974, PubMed:4602029, PubMed:4602030). Required for production of the mature 5'-end of retron Ec78 or Ec83 msDNA. When in excess of the large subunit, counteracts the large subunit's toxicity (PubMed:26626352). {ECO:0000269|PubMed:22718974, ECO:0000269|PubMed:26626352, ECO:0000269|PubMed:4602029, ECO:0000269|PubMed:4602030, ECO:0000305|PubMed:6284744}. EcoCyc product frame: EG11098-MONOMER. EcoCyc synonyms: yajE. Genomic coordinates: 441101-441343. EcoCyc protein note: XseB is the small subunit of exonuclease VII (ExoVII) - a single-strand DNA exonuclease implicated in various aspects of DNA repair.

## Enriched Pathways

- `eco03430` Mismatch repair (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8G9|protein.P0A8G9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001466,ECOCYC:EG11098,GeneID:945069`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:441101-441343:-; feature_type=gene
