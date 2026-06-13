---
entity_id: "gene.b1918"
entity_type: "gene"
name: "tcyL"
source_database: "NCBI RefSeq"
source_id: "gene-b1918"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1918"
  - "tcyL"
---

# tcyL

`gene.b1918`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1918`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tcyL (gene.b1918) is a gene entity. It encodes tcyL (protein.P0AFT2). Encoded protein function: FUNCTION: Part of the ABC transporter complex TcyJLN involved in L-cystine import (PubMed:20351115, PubMed:25139244, PubMed:25837721, PubMed:26350134). This high affinity cystine transporter is involved in resistance to oxidative stress by forming a L-cysteine/L-cystine shuttle system with the EamA transporter, which exports L-cysteine as reducing equivalents to the periplasm to prevent the cells from oxidative stress. Exported L-cysteine can reduce the periplasmic hydrogen peroxide to water, and then generated L-cystine is imported back into the cytoplasm via the TcyJLN complex (PubMed:20351115, PubMed:25837721). Functions at low cystine concentrations (PubMed:26350134). The system can also transport L-cysteine, diaminopimelic acid (DAP), djenkolate, lanthionine, D-cystine, homocystine, and it mediates accumulation of the toxic compounds L-selenaproline (SCA) and L-selenocystine (SeCys) (PubMed:25139244, PubMed:26350134). Responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000269|PubMed:20351115, ECO:0000269|PubMed:25139244, ECO:0000269|PubMed:25837721, ECO:0000269|PubMed:26350134, ECO:0000305}. EcoCyc product frame: G7037-MONOMER. EcoCyc synonyms: yecS. Genomic coordinates: 1997811-1998479...

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFT2|protein.P0AFT2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006386,ECOCYC:G7037,GeneID:949105`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1997811-1998479:-; feature_type=gene
