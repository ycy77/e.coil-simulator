---
entity_id: "gene.b3849"
entity_type: "gene"
name: "trkH"
source_database: "NCBI RefSeq"
source_id: "gene-b3849"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3849"
  - "trkH"
---

# trkH

`gene.b3849`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3849`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

trkH (gene.b3849) is a gene entity. It encodes trkH (protein.P0AFZ7). Encoded protein function: FUNCTION: Low-affinity potassium transport system. Interacts with Trk system potassium uptake protein TrkA. Requires TrkE (sapD) for transport activity, 20% more uptake is seen with both SapD and SapF (PubMed:11700350). Transport in the absence of SapD and SapF is dependent on a high membrane potential and a high cytoplasmic ATP concentration, suggesting this protein may be able to interact with other ATP-binding proteins (PubMed:11700350). Can transport potassium and rubidium (PubMed:7896723). {ECO:0000250, ECO:0000269|PubMed:11700350, ECO:0000269|PubMed:7896723}. EcoCyc product frame: TRKH-MONOMER. Genomic coordinates: 4033145-4034596. EcoCyc protein note: TrkH is a Na+-independent potassium ion transporter that functions as a major K+-uptake system; TrkH-mediated potassium uptake is able to support growth in low K+ medium (0.1mM K+) in the absence of other potassium uptake systems . Early studies in E. coli K-12 identified four separate K+ uptake systems: two constitutive systems [TrkA (also called Trk) and TrkD (also called Kup)], a high affinity system (Kdp) and a non-saturable system TrkF (see also...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFZ7|protein.P0AFZ7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012574,ECOCYC:EG11021,GeneID:948333`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4033145-4034596:+; feature_type=gene
