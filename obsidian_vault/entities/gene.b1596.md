---
entity_id: "gene.b1596"
entity_type: "gene"
name: "ynfM"
source_database: "NCBI RefSeq"
source_id: "gene-b1596"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1596"
  - "ynfM"
---

# ynfM

`gene.b1596`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1596`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ynfM (gene.b1596) is a gene entity. It encodes ynfM (protein.P43531). Encoded protein function: Inner membrane transport protein YnfM EcoCyc product frame: B1596-MONOMER. EcoCyc synonyms: yzyC. Genomic coordinates: 1669699-1670952. EcoCyc protein note: Expression of cloned ynfLM in a K-12 strain which lacks the major efflux pump permease AcrB (E. coli KAM3; see ) confers hypersensitivity to acriflavine (minimum inhibitory concentration, 12.5 µg/mL for KAM3 versus 3.13 µg/mL for KAM3/pUCynfLM) but does not impact the resistance to a range of other antibiotics, dyes and toxic compounds; expression of cloned ynfM (pTrcHynfM) cannot be detected and KAM3 cells harbouring this expression vector do not exhibit the acriflavine hypersensitivity phenotype . In the Transporter Classification Database, YnfM is a member of the Acriflavin-sensitivity family within the Major Facilitator Superfamily (MFS) . YnfM has been implicated in arabinose efflux . ynfM is one of 35 efflux-encoding genes that have been deleted or inactivated in 'Efflux KnockOut-35' (EKO-35) - a K-12 BW25133-derived strain that lacks 35 efflux pumps and can be used as a platform to study their function .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P43531|protein.P43531]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005333,ECOCYC:G6854,GeneID:946138`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1669699-1670952:+; feature_type=gene
