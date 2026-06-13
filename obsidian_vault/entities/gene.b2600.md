---
entity_id: "gene.b2600"
entity_type: "gene"
name: "tyrA"
source_database: "NCBI RefSeq"
source_id: "gene-b2600"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2600"
  - "tyrA"
---

# tyrA

`gene.b2600`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2600`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tyrA (gene.b2600) is a gene entity. It encodes tyrA (protein.P07023). Encoded protein function: T-protein [Includes: Chorismate mutase (CM) (EC 5.4.99.5); Prephenate dehydrogenase (PDH) (EC 1.3.1.12)] EcoCyc product frame: CHORISMUTPREPHENDEHYDROG-MONOMER. Genomic coordinates: 2738948-2740069.

## Biological Role

Repressed by tyrR (protein.P07604). Activated by rpoD (protein.P00579), soxR (protein.P0ACS2).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00401` Novobiocin biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07023|protein.P07023]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=tyrA; function=+
- `activates` <-- [[protein.P0ACS2|protein.P0ACS2]] `RegulonDB` `S` - regulator=SoxR; target=tyrA; function=+
- `represses` <-- [[protein.P07604|protein.P07604]] `RegulonDB` `S` - regulator=TyrR; target=tyrA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008547,ECOCYC:EG11039,GeneID:947115`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2738948-2740069:-; feature_type=gene
