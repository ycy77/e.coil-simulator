---
entity_id: "gene.b2219"
entity_type: "gene"
name: "atoS"
source_database: "NCBI RefSeq"
source_id: "gene-b2219"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2219"
  - "atoS"
---

# atoS

`gene.b2219`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2219`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

atoS (gene.b2219) is a gene entity. It encodes atoS (protein.Q06067). Encoded protein function: FUNCTION: Member of the two-component regulatory system AtoS/AtoC. In the presence of acetoacetate, AtoS/AtoC stimulates the expression of the atoDAEB operon, leading to short chain fatty acid catabolism and activation of the poly-(R)-3-hydroxybutyrate (cPHB) biosynthetic pathway. Also induces the operon in response to spermidine (PubMed:16153782, PubMed:16564134, PubMed:17475408). Involved in the regulation of motility and chemotaxis, via transcriptional induction of the flagellar regulon (PubMed:22083893). AtoS is a membrane-associated kinase that phosphorylates and activates AtoC in response to environmental signals (PubMed:16153782, PubMed:18534200). {ECO:0000269|PubMed:16153782, ECO:0000269|PubMed:16564134, ECO:0000269|PubMed:17475408, ECO:0000269|PubMed:18534200, ECO:0000269|PubMed:22083893}. EcoCyc product frame: ATOS-MONOMER. Genomic coordinates: 2320043-2321869.

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q06067|protein.Q06067]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007341,ECOCYC:EG11667,GeneID:949011`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2320043-2321869:+; feature_type=gene
