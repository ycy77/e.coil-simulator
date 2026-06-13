---
entity_id: "gene.b2158"
entity_type: "gene"
name: "yeiH"
source_database: "NCBI RefSeq"
source_id: "gene-b2158"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2158"
  - "yeiH"
---

# yeiH

`gene.b2158`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2158`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yeiH (gene.b2158) is a gene entity. It encodes yeiH (protein.P62723). Encoded protein function: UPF0324 inner membrane protein YeiH EcoCyc product frame: EG12027-MONOMER. Genomic coordinates: 2249717-2250766. EcoCyc protein note: YeiH is an inner membrane protein with nine predicted transmembrane domains; the C terminus is located in the periplasm . The tertiary structure of YeiH has been modeled .

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P62723|protein.P62723]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yeiH; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007142,ECOCYC:EG12027,GeneID:946668`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2249717-2250766:+; feature_type=gene
