---
entity_id: "gene.b0776"
entity_type: "gene"
name: "bioF"
source_database: "NCBI RefSeq"
source_id: "gene-b0776"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0776"
  - "bioF"
---

# bioF

`gene.b0776`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0776`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bioF (gene.b0776) is a gene entity. It encodes bioF (protein.P12998). Encoded protein function: FUNCTION: Catalyzes the decarboxylative condensation of pimeloyl-[acyl-carrier protein] and L-alanine to produce 8-amino-7-oxononanoate (AON), [acyl-carrier protein], and carbon dioxide. Can also use pimeloyl-CoA instead of pimeloyl-ACP as substrate, but it is believed that pimeloyl-ACP rather than pimeloyl-CoA is the physiological substrate of BioF. {ECO:0000269|PubMed:10642176, ECO:0000269|PubMed:20693992}. EcoCyc product frame: 7KAPSYN-MONOMER. Genomic coordinates: 810381-811535.

## Biological Role

Repressed by birA (protein.P06709).

## Enriched Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P12998|protein.P12998]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P06709|protein.P06709]] `RegulonDB` `S` - regulator=BirA; target=bioF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002646,ECOCYC:EG10121,GeneID:945384`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:810381-811535:+; feature_type=gene
