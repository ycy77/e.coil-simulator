---
entity_id: "gene.b0166"
entity_type: "gene"
name: "dapD"
source_database: "NCBI RefSeq"
source_id: "gene-b0166"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0166"
  - "dapD"
---

# dapD

`gene.b0166`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0166`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dapD (gene.b0166) is a gene entity. It encodes dapD (protein.P0A9D8). Encoded protein function: FUNCTION: Catalyzes the formation of N-succinyl-2-amino-6-oxo-L-pimelate from succinyl-CoA and tetrahydrodipicolinate, a key step in lysine biosynthesis via diaminopimelate pathway. {ECO:0000269|PubMed:6365916}. EcoCyc product frame: MONOMER0-2001. EcoCyc synonyms: ssa. Genomic coordinates: 185123-185947. EcoCyc protein note: Tetrahydrodipicolinate succinylase (DapD) catalyzes the formation of N-succinyl-2-amino-6-ketopimelate from succinyl-CoA and tetrahydrodipicolinate, and is a key enzyme in the E. coli lysine biosynthetic pathway . A crystal structure of DapD from E. coli O157:H7 has been solved . Expression of dapD is repressed by lysine via ArgP . DapD: "diaminopimelate biosynthesis D"

## Biological Role

Activated by rpoD (protein.P00579), argP (protein.P0A8S1).

## Enriched Pathways

- `eco00300` Lysine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9D8|protein.P0A9D8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=dapD; function=+
- `activates` <-- [[protein.P0A8S1|protein.P0A8S1]] `RegulonDB` `S` - regulator=ArgP; target=dapD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000565,ECOCYC:EG10207,GeneID:944862`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:185123-185947:-; feature_type=gene
