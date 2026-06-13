---
entity_id: "gene.b1288"
entity_type: "gene"
name: "fabI"
source_database: "NCBI RefSeq"
source_id: "gene-b1288"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1288"
  - "fabI"
---

# fabI

`gene.b1288`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1288`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fabI (gene.b1288) is a gene entity. It encodes fabI (protein.P0AEK4). Encoded protein function: FUNCTION: Catalyzes the reduction of a carbon-carbon double bond in an enoyl moiety that is covalently linked to an acyl carrier protein (ACP). Involved in the elongation cycle of fatty acid which are used in the lipid metabolism and in the biotin biosynthesis. {ECO:0000269|PubMed:10629181, ECO:0000269|PubMed:20693992, ECO:0000269|PubMed:7592873, ECO:0000269|PubMed:8119879, ECO:0000269|PubMed:8910376}. EcoCyc product frame: ENOYL-ACP-REDUCT-NADH-MONOMER. EcoCyc synonyms: envM, gts, qmeA. Genomic coordinates: 1350251-1351039.

## Biological Role

Activated by fadR (protein.P0A8V6).

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

- `encodes` --> [[protein.P0AEK4|protein.P0AEK4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0A8V6|protein.P0A8V6]] `RegulonDB` `S` - regulator=FadR; target=fabI; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004327,ECOCYC:EG11528,GeneID:945870`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1350251-1351039:-; feature_type=gene
