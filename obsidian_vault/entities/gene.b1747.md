---
entity_id: "gene.b1747"
entity_type: "gene"
name: "astA"
source_database: "NCBI RefSeq"
source_id: "gene-b1747"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1747"
  - "astA"
---

# astA

`gene.b1747`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1747`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

astA (gene.b1747) is a gene entity. It encodes astA (protein.P0AE37). Encoded protein function: FUNCTION: Catalyzes the transfer of succinyl-CoA to arginine to produce N(2)-succinylarginine. {ECO:0000269|PubMed:9696779}. EcoCyc product frame: ARGSUCCTRAN-MONOMER. EcoCyc synonyms: ydjV. Genomic coordinates: 1829731-1830765. EcoCyc protein note: Arginine succinyltransferase (AstA) catalyzes the first reaction in the ammonia-producing arginine catabolic pathway, AST-PWY. The activity has only been assayed in crude cell extracts, and thus there is little direct evidence for the function of the astA gene product . AstA is a member of the acyl-CoA N-acyltransferase superfamily . Expression of the enzymes of the AST pathway is regulated by arginine and nitrogen availability via ArgR and NtrC .

## Biological Role

Activated by argR (protein.P0A6D0), glnG (protein.P0AFB8), rpoS (protein.P13445), rpoN (protein.P24255).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE37|protein.P0AE37]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `C` - regulator=ArgR; target=astA; function=+
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=astA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `C` - sigma=sigma38; target=astA; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `C` - sigma=sigma54; target=astA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005822,ECOCYC:G6943,GeneID:946261`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1829731-1830765:-; feature_type=gene
