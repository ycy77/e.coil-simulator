---
entity_id: "gene.b1816"
entity_type: "gene"
name: "yoaE"
source_database: "NCBI RefSeq"
source_id: "gene-b1816"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1816"
  - "yoaE"
---

# yoaE

`gene.b1816`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1816`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yoaE (gene.b1816) is a gene entity. It encodes yoaE (protein.P0AEC0). Encoded protein function: UPF0053 inner membrane protein YoaE EcoCyc product frame: G6997-MONOMER. Genomic coordinates: 1900029-1901585. EcoCyc protein note: YoaE is predicted to be an inner membrane protein with seven transmembrane domains; experimental topology analysis suggests that the C terminus is located in the cytoplasm . In Salmonella Enteritidis, YoaE was found to be required for survival in egg white . Overexpression of yoaE from an ASKA plasmid leads to a more than 3-fold increase in the MIC of hypochlorous acid .

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEC0|protein.P0AEC0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yoaE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006045,ECOCYC:G6997,GeneID:946335`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1900029-1901585:-; feature_type=gene
