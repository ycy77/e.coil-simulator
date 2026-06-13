---
entity_id: "gene.b1744"
entity_type: "gene"
name: "astE"
source_database: "NCBI RefSeq"
source_id: "gene-b1744"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1744"
  - "astE"
---

# astE

`gene.b1744`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1744`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

astE (gene.b1744) is a gene entity. It encodes astE (protein.P76215). Encoded protein function: FUNCTION: Transforms N(2)-succinylglutamate into succinate and glutamate. {ECO:0000269|PubMed:9696779}. EcoCyc product frame: SUCCGLUDESUCC-MONOMER. EcoCyc synonyms: ydjS. Genomic coordinates: 1825955-1826923. EcoCyc protein note: Succinylglutamate desuccinylase catalyzes the fifth and final reaction in the ammonia-producing arginine catabolic pathway, AST-PWY. The activity has only been assayed in crude cell extracts, and thus there is little direct evidence for the function of the astE gene product . Deletion of astE enhances tolerance to n-butanol . Expression of the enzymes of the AST pathway is regulated by arginine and nitrogen availability via ArgR and NtrC .

## Biological Role

Activated by argR (protein.P0A6D0), glnG (protein.P0AFB8), rpoS (protein.P13445), rpoN (protein.P24255).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76215|protein.P76215]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `C` - regulator=ArgR; target=astE; function=+
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=astE; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `C` - sigma=sigma38; target=astE; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `C` - sigma=sigma54; target=astE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005815,ECOCYC:G6940,GeneID:946256`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1825955-1826923:-; feature_type=gene
