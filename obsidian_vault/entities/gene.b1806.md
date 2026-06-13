---
entity_id: "gene.b1806"
entity_type: "gene"
name: "yeaY"
source_database: "NCBI RefSeq"
source_id: "gene-b1806"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1806"
  - "yeaY"
---

# yeaY

`gene.b1806`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1806`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yeaY (gene.b1806) is a gene entity. It encodes yeaY (protein.P0AA91). Encoded protein function: Uncharacterized lipoprotein YeaY EcoCyc product frame: G6990-MONOMER. Genomic coordinates: 1889951-1890532. EcoCyc protein note: YeaY is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ). YeaY contains a signal sequence characteristic of bacterial lipoproteins followed by a characteristic Cys residue at position 23 which could serve as the lipid attachment site . YeaY shows significant sequence similarity to an outer membrane lipoprotein encoded by the carbon starvation-inducible and stationary phase-inducible slp gene in E. coli . yeaY is a member of the σE regulon .

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA91|protein.P0AA91]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=yeaY; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006011,ECOCYC:G6990,GeneID:946312`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1889951-1890532:-; feature_type=gene
