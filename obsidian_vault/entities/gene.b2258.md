---
entity_id: "gene.b2258"
entity_type: "gene"
name: "arnF"
source_database: "NCBI RefSeq"
source_id: "gene-b2258"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2258"
  - "arnF"
---

# arnF

`gene.b2258`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2258`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

arnF (gene.b2258) is a gene entity. It encodes arnF (protein.P76474). Encoded protein function: FUNCTION: Translocates 4-amino-4-deoxy-L-arabinose-phosphoundecaprenol (alpha-L-Ara4N-phosphoundecaprenol) from the cytoplasmic to the periplasmic side of the inner membrane. {ECO:0000269|PubMed:17928292}. EcoCyc product frame: G7171-MONOMER. EcoCyc synonyms: yfbJ. Genomic coordinates: 2372892-2373278. EcoCyc protein note: ArnF is an integral membrane component of the ArnE/ArnF undecaprenyl-phosphate-α-L-Ara4N flippase.

## Biological Role

Activated by basR (protein.P30843).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76474|protein.P76474]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P30843|protein.P30843]] `RegulonDB` `S` - regulator=BasR; target=arnF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007466,ECOCYC:G7171,GeneID:945344`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2372892-2373278:+; feature_type=gene
