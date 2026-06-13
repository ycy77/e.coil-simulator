---
entity_id: "gene.b1198"
entity_type: "gene"
name: "dhaM"
source_database: "NCBI RefSeq"
source_id: "gene-b1198"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1198"
  - "dhaM"
---

# dhaM

`gene.b1198`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1198`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dhaM (gene.b1198) is a gene entity. It encodes dhaM (protein.P37349). Encoded protein function: FUNCTION: Component of the dihydroxyacetone kinase complex, which is responsible for the phosphoenolpyruvate (PEP)-dependent phosphorylation of dihydroxyacetone. DhaM serves as the phosphoryl donor. Is phosphorylated by phosphoenolpyruvate in an EI- and HPr-dependent reaction, and a phosphorelay system on histidine residues finally leads to phosphoryl transfer to DhaL and dihydroxyacetone. {ECO:0000269|PubMed:11350937}. EcoCyc product frame: EG12399-MONOMER. EcoCyc synonyms: ycgC, dhaH, ptsD. Genomic coordinates: 1247696-1249114.

## Biological Role

Activated by ygfI (protein.P52044).

## Enriched Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37349|protein.P37349]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `S` - regulator=SrsR; target=dhaM; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004024,ECOCYC:EG12399,GeneID:945749`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1247696-1249114:-; feature_type=gene
