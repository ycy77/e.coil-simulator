---
entity_id: "gene.b3017"
entity_type: "gene"
name: "ftsP"
source_database: "NCBI RefSeq"
source_id: "gene-b3017"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3017"
  - "ftsP"
---

# ftsP

`gene.b3017`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3017`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ftsP (gene.b3017) is a gene entity. It encodes ftsP (protein.P26648). Encoded protein function: FUNCTION: Cell division protein that is required for growth during stress conditions. May be involved in protecting or stabilizing the divisomal assembly under conditions of stress. {ECO:0000255|HAMAP-Rule:MF_00915, ECO:0000269|PubMed:17766410}. EcoCyc product frame: EG11376-MONOMER. EcoCyc synonyms: sui, sufI. Genomic coordinates: 3161257-3162669. EcoCyc protein note: FtsP (SufI) is a component of the cell division machinery that is required during stress conditions and may play a role in stabilizing the assembly of the divisome . FtsP localizes to the septal ring; recruitment is dependent on FtsN . Translation of FtsP proceeds via many transient intermediates that match translational attenuation sites. Slowly translating regions are important for proper folding of the protein . Comparative molecular simulations of different folding schemes have been performed . FtsP is a soluble protein that is transported to the periplasm via the Tat pathway . Overexpression of FtsP saturates the Tat protein export system . The twin-arginine signal peptide of FtsP is unstructured in an aqueous environment, but adopts a helical structure in membrane-mimetic environments...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P26648|protein.P26648]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009905,ECOCYC:EG11376,GeneID:944982`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3161257-3162669:-; feature_type=gene
