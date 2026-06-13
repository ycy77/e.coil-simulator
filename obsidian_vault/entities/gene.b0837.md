---
entity_id: "gene.b0837"
entity_type: "gene"
name: "yliI"
source_database: "NCBI RefSeq"
source_id: "gene-b0837"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0837"
  - "yliI"
---

# yliI

`gene.b0837`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0837`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yliI (gene.b0837) is a gene entity. It encodes yliI (protein.P75804). Encoded protein function: FUNCTION: Aldose sugar dehydrogenase with broad substrate specificity. The physiological substrate is unknown. Can oxidize glucose to gluconolactone. Can also utilize D-arabinose, L-arabinose and 2-deoxy-glucose. Has higher activity towards oligomeric sugars, such as maltose, maltotriose or cellobiose. It may function to input sugar-derived electrons into the respiratory network. {ECO:0000269|PubMed:16864586}. EcoCyc product frame: G6437-MONOMER. Genomic coordinates: 878742-879857. EcoCyc protein note: YliI is an aldose sugar dehydrogenase that requires the cofactor pyrroloquinoline quinone (PQQ) for activity . E. coli lacks the ability to synthesize PQQ however, it exhibits chemotaxis towards environmental PQQ , and may thus use an externally supplied cofactor . PQQ is transported across the outer membrane by the TonB-dependent transporter G6762-MONOMER PqqU . The physiological substrate of YliI is unknown . YliI localizes to the the periplasm and is associated with the outer membrane under certain physiological conditions . Sequence similarity suggests that YliI may contain β-barrel structures ; however, the β-propeller fold of YliI may have led to a false-positive prediction of a β-barrel structure (von Heijne, pers. comm., 8/8/2006)...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75804|protein.P75804]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002852,ECOCYC:G6437,GeneID:945467`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:878742-879857:+; feature_type=gene
