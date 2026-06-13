---
entity_id: "gene.b2165"
entity_type: "gene"
name: "psuG"
source_database: "NCBI RefSeq"
source_id: "gene-b2165"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2165"
  - "psuG"
---

# psuG

`gene.b2165`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2165`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

psuG (gene.b2165) is a gene entity. It encodes psuG (protein.P33025). Encoded protein function: FUNCTION: Catalyzes the reversible cleavage of pseudouridine 5'-phosphate (PsiMP) to ribose 5-phosphate and uracil. Functions biologically in the cleavage direction, as part of a pseudouridine degradation pathway. {ECO:0000255|HAMAP-Rule:MF_01876, ECO:0000269|PubMed:18591240, ECO:0000269|PubMed:23066817}. EcoCyc product frame: EG12033-MONOMER. EcoCyc synonyms: yeiN, pscG. Genomic coordinates: 2257429-2258367.

## Biological Role

Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33025|protein.P33025]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=psuG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007165,ECOCYC:EG12033,GeneID:946699`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2257429-2258367:-; feature_type=gene
