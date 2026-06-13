---
entity_id: "gene.b4399"
entity_type: "gene"
name: "creC"
source_database: "NCBI RefSeq"
source_id: "gene-b4399"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4399"
  - "creC"
---

# creC

`gene.b4399`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4399`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

creC (gene.b4399) is a gene entity. It encodes creC (protein.P08401). Encoded protein function: FUNCTION: Member of the two-component regulatory system CreC/CreB involved in catabolic regulation. CreC may function as a membrane-associated protein kinase that phosphorylates CreB in response to environmental signals. CreC can also phosphorylate PhoB. {ECO:0000269|PubMed:15522865, ECO:0000269|PubMed:2228961}. EcoCyc product frame: CREC-MONOMER. EcoCyc synonyms: phoM. Genomic coordinates: 4636696-4638120.

## Biological Role

Activated by rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08401|protein.P08401]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=creC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0014430,ECOCYC:EG10730,GeneID:948609`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4636696-4638120:+; feature_type=gene
