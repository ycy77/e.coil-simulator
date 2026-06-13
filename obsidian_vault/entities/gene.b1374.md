---
entity_id: "gene.b1374"
entity_type: "gene"
name: "pinR"
source_database: "NCBI RefSeq"
source_id: "gene-b1374"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1374"
  - "pinR"
---

# pinR

`gene.b1374`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1374`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pinR (gene.b1374) is a gene entity. It encodes pinR (protein.P0ADI0). Encoded protein function: Serine recombinase PinR (EC 3.1.22.-) (EC 6.5.1.-) (DNA-invertase PinR) (Putative DNA-invertase from lambdoid prophage Rac) (Site-specific recombinase PinR) EcoCyc product frame: G6697-MONOMER. EcoCyc synonyms: ynaD. Genomic coordinates: 1433084-1433674. EcoCyc protein note: No information about this protein was found by a literature search conducted on September 10, 2008.

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADI0|protein.P0ADI0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=pinR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004599,ECOCYC:G6697,GeneID:948973`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1433084-1433674:-; feature_type=gene
