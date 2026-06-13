---
entity_id: "gene.b2599"
entity_type: "gene"
name: "pheA"
source_database: "NCBI RefSeq"
source_id: "gene-b2599"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2599"
  - "pheA"
---

# pheA

`gene.b2599`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2599`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pheA (gene.b2599) is a gene entity. It encodes pheA (protein.P0A9J8). Encoded protein function: FUNCTION: Catalyzes the Claisen rearrangement of chorismate to prephenate and the decarboxylation/dehydration of prephenate to phenylpyruvate. {ECO:0000269|PubMed:4261395}. EcoCyc product frame: CHORISMUTPREPHENDEHYDRAT-MONOMER. Genomic coordinates: 2737745-2738905.

## Biological Role

Repressed by rydC (gene.b4597). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9J8|protein.P0A9J8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=pheA; function=+
- `represses` <-- [[gene.b4597|gene.b4597]] `RegulonDB` `S` - regulator=RydC; target=pheA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008545,ECOCYC:EG10707,GeneID:947081`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2737745-2738905:+; feature_type=gene
