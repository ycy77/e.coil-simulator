---
entity_id: "gene.b1917"
entity_type: "gene"
name: "tcyN"
source_database: "NCBI RefSeq"
source_id: "gene-b1917"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1917"
  - "tcyN"
---

# tcyN

`gene.b1917`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1917`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tcyN (gene.b1917) is a gene entity. It encodes tcyN (protein.P37774). Encoded protein function: FUNCTION: Part of the ABC transporter complex TcyJLN involved in L-cystine import (PubMed:20351115, PubMed:25139244, PubMed:25837721, PubMed:26350134). This high affinity cystine transporter is involved in resistance to oxidative stress by forming a L-cysteine/L-cystine shuttle system with the EamA transporter, which exports L-cysteine as reducing equivalents to the periplasm to prevent the cells from oxidative stress. Exported L-cysteine can reduce the periplasmic hydrogen peroxide to water, and then generated L-cystine is imported back into the cytoplasm via the TcyJLN complex (PubMed:20351115, PubMed:25837721). Functions at low cystine concentrations (PubMed:26350134). The system can also transport L-cysteine, diaminopimelic acid (DAP), djenkolate, lanthionine, D-cystine, homocystine, and it mediates accumulation of the toxic compounds L-selenaproline (SCA) and L-selenocystine (SeCys) (PubMed:25139244, PubMed:26350134). Could also facilitate threonine efflux (PubMed:28911185). Responsible for energy coupling to the transport system (Probable). {ECO:0000269|PubMed:20351115, ECO:0000269|PubMed:25139244, ECO:0000269|PubMed:25837721, ECO:0000269|PubMed:26350134, ECO:0000269|PubMed:28911185, ECO:0000305}. EcoCyc product frame: EG12347-MONOMER. EcoCyc synonyms: yecC...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37774|protein.P37774]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006384,ECOCYC:EG12347,GeneID:946422`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1997062-1997814:-; feature_type=gene
