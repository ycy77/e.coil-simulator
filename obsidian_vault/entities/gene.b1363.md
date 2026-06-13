---
entity_id: "gene.b1363"
entity_type: "gene"
name: "trkG"
source_database: "NCBI RefSeq"
source_id: "gene-b1363"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1363"
  - "trkG"
---

# trkG

`gene.b1363`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1363`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

trkG (gene.b1363) is a gene entity. It encodes trkG (protein.P23849). Encoded protein function: FUNCTION: Low-affinity potassium transport system. Interacts with Trk system potassium uptake protein TrkA. Requires TrkE (sapD) for maximal transport activity, low activity is seen in its absence; no further stimulation is seen with SapF (PubMed:11700350). Transport in the absence of SapD is dependent on a high membrane potential and a high cytoplasmic ATP concentration, suggesting this protein may be able to interact with other ATP-binding proteins (PubMed:11700350). Can transport potassium and rubidium (PubMed:7896723). {ECO:0000269|PubMed:11700350, ECO:0000269|PubMed:2022616, ECO:0000269|PubMed:2674131, ECO:0000269|PubMed:7896723}. EcoCyc product frame: TRKG-MONOMER. Genomic coordinates: 1423782-1425239. EcoCyc protein note: TrkG is a Na+-dependent potassium ion transporter that makes a minor contribution to K+ uptake; TrkG-mediated uptake contributes to potassium replenishment when Na+ is present in the growth environment . Early studies in E. coli K-12 identified four separate K+ uptake systems: two constitutive systems [TrkA (also called Trk) and TrkD (also called Kup)], a high affinity system (Kdp) and a non-saturable system TrkF (see also...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23849|protein.P23849]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004567,ECOCYC:EG11020,GeneID:945932`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1423782-1425239:+; feature_type=gene
