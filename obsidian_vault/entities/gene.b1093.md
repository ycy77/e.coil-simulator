---
entity_id: "gene.b1093"
entity_type: "gene"
name: "fabG"
source_database: "NCBI RefSeq"
source_id: "gene-b1093"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1093"
  - "fabG"
---

# fabG

`gene.b1093`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1093`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fabG (gene.b1093) is a gene entity. It encodes fabG (protein.P0AEK2). Encoded protein function: FUNCTION: Catalyzes the NADPH-dependent reduction of beta-ketoacyl-ACP substrates to beta-hydroxyacyl-ACP products, the first reductive step in the elongation cycle of fatty acid biosynthesis. {ECO:0000269|PubMed:10629181, ECO:0000269|PubMed:14996818, ECO:0000269|PubMed:7592873, ECO:0000269|PubMed:8631920, ECO:0000269|PubMed:8910376}. EcoCyc product frame: 3-OXOACYL-ACP-REDUCT-MONOMER. Genomic coordinates: 1150670-1151404.

## Biological Role

Activated by rpoD (protein.P00579), fadR (protein.P0A8V6).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEK2|protein.P0AEK2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fabG; function=+
- `activates` <-- [[protein.P0A8V6|protein.P0A8V6]] `RegulonDB` `C` - regulator=FadR; target=fabG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003700,ECOCYC:EG11318,GeneID:945645`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1150670-1151404:+; feature_type=gene
