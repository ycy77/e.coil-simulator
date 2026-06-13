---
entity_id: "gene.b3747"
entity_type: "gene"
name: "kup"
source_database: "NCBI RefSeq"
source_id: "gene-b3747"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3747"
  - "kup"
---

# kup

`gene.b3747`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3747`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

kup (gene.b3747) is a gene entity. It encodes kup (protein.P63183). Encoded protein function: FUNCTION: Responsible for the low-affinity transport of potassium into the cell (PubMed:10214935, PubMed:11682179, PubMed:2649491, PubMed:28522840, PubMed:8226635). Likely operates as a K(+):H(+) symporter (PubMed:10214935, PubMed:11682179). Kup is probably the major potassium uptake system upon hyper-osmotic stress at a low pH (PubMed:10214935). Can also transport Cs(+) and Rb(+) (PubMed:2649491, PubMed:28522840). In the absence of potassium, Kup-mediated Cs(+) uptake partially supports cell growth, however, at a much lower rate than with sufficient K(+) (PubMed:28522840). This effect depends on the maintenance of basal levels of intracellular K(+) by other K(+) uptake transporters (PubMed:28522840). {ECO:0000269|PubMed:10214935, ECO:0000269|PubMed:11682179, ECO:0000269|PubMed:2649491, ECO:0000269|PubMed:28522840, ECO:0000269|PubMed:8226635}. EcoCyc product frame: KUP-MONOMER. EcoCyc synonyms: trkD. Genomic coordinates: 3931316-3933184. EcoCyc protein note: Early studies in E. coli K-12 identified four separate K+ uptake systems: two constitutive systems [TrkD (also called Kup) and TrkA* (also called Trk)], a high affinity system (ATPASE-1-CPLX "KdpFABC") and a non-saturable system TrkF (see also...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P63183|protein.P63183]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012251,ECOCYC:EG11541,GeneID:948255`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3931316-3933184:+; feature_type=gene
