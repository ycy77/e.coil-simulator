---
entity_id: "gene.b4254"
entity_type: "gene"
name: "argI"
source_database: "NCBI RefSeq"
source_id: "gene-b4254"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4254"
  - "argI"
---

# argI

`gene.b4254`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4254`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

argI (gene.b4254) is a gene entity. It encodes argI (protein.P04391). Encoded protein function: FUNCTION: Reversibly catalyzes the transfer of the carbamoyl group from carbamoyl phosphate (CP) to the N(epsilon) atom of ornithine (ORN) to produce L-citrulline, which is a substrate for argininosuccinate synthetase, the enzyme involved in the final step in arginine biosynthesis. {ECO:0000269|PubMed:3072022, ECO:0000269|PubMed:789338}. EcoCyc product frame: CHAINI-MONOMER. Genomic coordinates: 4477307-4478311.

## Biological Role

Repressed by argR (protein.P0A6D0). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P04391|protein.P04391]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=argI; function=+
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `C` - regulator=ArgR; target=argI; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013927,ECOCYC:EG10069,GeneID:948774`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4477307-4478311:-; feature_type=gene
