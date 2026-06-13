---
entity_id: "gene.b2436"
entity_type: "gene"
name: "hemF"
source_database: "NCBI RefSeq"
source_id: "gene-b2436"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2436"
  - "hemF"
---

# hemF

`gene.b2436`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2436`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hemF (gene.b2436) is a gene entity. It encodes hemF (protein.P36553). Encoded protein function: FUNCTION: Involved in the heme biosynthesis. Catalyzes the aerobic oxidative decarboxylation of propionate groups of rings A and B of coproporphyrinogen-III to yield the vinyl groups in protoporphyrinogen-IX. {ECO:0000255|HAMAP-Rule:MF_00333, ECO:0000269|PubMed:12975365, ECO:0000269|PubMed:13129604}. EcoCyc product frame: COPROGENOXI-MONOMER. EcoCyc synonyms: popB, sec. Genomic coordinates: 2553225-2554124.

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36553|protein.P36553]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=hemF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008034,ECOCYC:EG12189,GeneID:946908`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2553225-2554124:+; feature_type=gene
