---
entity_id: "gene.b0570"
entity_type: "gene"
name: "cusS"
source_database: "NCBI RefSeq"
source_id: "gene-b0570"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0570"
  - "cusS"
---

# cusS

`gene.b0570`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0570`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cusS (gene.b0570) is a gene entity. It encodes cusS (protein.P77485). Encoded protein function: FUNCTION: Member of the two-component regulatory system CusS/CusR involved in response to copper and silver. Acts as a copper/silver ion sensor. Activates CusR by phosphorylation. {ECO:0000269|PubMed:11004187, ECO:0000269|PubMed:11283292, ECO:0000269|PubMed:11399769, ECO:0000269|PubMed:15522865, ECO:0000269|PubMed:22348296}. EcoCyc product frame: MONOMER0-4178. EcoCyc synonyms: ybcZ. Genomic coordinates: 593328-594770. EcoCyc protein note: This is the phosphorylated form of G6318-MONOMER "CusS" - the sensor histidine kinase of the CusSR two-component signal transduction system.

## Biological Role

Activated by rpoD (protein.P00579), cusR (protein.P0ACZ8), phoB (protein.P0AFJ5), hprR (protein.P76340).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77485|protein.P77485]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cusS; function=+
- `activates` <-- [[protein.P0ACZ8|protein.P0ACZ8]] `RegulonDB` `C` - regulator=CusR; target=cusS; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `C` - regulator=PhoB; target=cusS; function=+
- `activates` <-- [[protein.P76340|protein.P76340]] `RegulonDB` `S` - regulator=HprR; target=cusS; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001946,ECOCYC:G6318,GeneID:945978`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:593328-594770:-; feature_type=gene
