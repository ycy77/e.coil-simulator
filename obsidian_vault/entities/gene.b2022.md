---
entity_id: "gene.b2022"
entity_type: "gene"
name: "hisB"
source_database: "NCBI RefSeq"
source_id: "gene-b2022"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2022"
  - "hisB"
---

# hisB

`gene.b2022`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2022`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hisB (gene.b2022) is a gene entity. It encodes hisB (protein.P06987). Encoded protein function: Histidine biosynthesis bifunctional protein HisB [Includes: Histidinol-phosphatase (EC 3.1.3.15); Imidazoleglycerol-phosphate dehydratase (IGPD) (EC 4.2.1.19)] EcoCyc product frame: IMIDPHOSPHADEHYDHISTIDPHOSPHA-MONOMER. Genomic coordinates: 2093468-2094535.

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00340` Histidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06987|protein.P06987]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=hisB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006720,ECOCYC:EG10445,GeneID:946552`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2093468-2094535:+; feature_type=gene
