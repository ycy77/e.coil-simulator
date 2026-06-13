---
entity_id: "gene.b1715"
entity_type: "gene"
name: "pheM"
source_database: "NCBI RefSeq"
source_id: "gene-b1715"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1715"
  - "pheM"
---

# pheM

`gene.b1715`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1715`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pheM (gene.b1715) is a gene entity. It encodes pheM (protein.P0AD74). Encoded protein function: Phenylalanine--tRNA ligase operon leader peptide (pheST attenuator peptide) EcoCyc product frame: EG11272-MONOMER. EcoCyc synonyms: phtL. Genomic coordinates: 1799226-1799270. EcoCyc protein note: The PheM leader peptide controls by attenuation the expression of the pheMST operon (which codes for phenylalanyl-tRNA synthetase) in response to phenylalanine availability . Specifically, decreased levels of charged tRNAPhe lead to derepression of pheMST . Although other ORFs have been detected upstream from pheS, PheM appears to be the only functional one . PheM is a 14-amino acid peptide, with five phenylalanine residues serving as regulatory points during attenuation . One of the first tests of pheM as an attenuator was done by .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD74|protein.P0AD74]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005727,ECOCYC:EG11272,GeneID:947212`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1799226-1799270:-; feature_type=gene
