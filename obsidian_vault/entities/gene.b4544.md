---
entity_id: "gene.b4544"
entity_type: "gene"
name: "arnE"
source_database: "NCBI RefSeq"
source_id: "gene-b4544"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4544"
  - "arnE"
---

# arnE

`gene.b4544`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4544`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

arnE (gene.b4544) is a gene entity. It encodes arnE (protein.Q47377). Encoded protein function: FUNCTION: Translocates 4-amino-4-deoxy-L-arabinose-phosphoundecaprenol (alpha-L-Ara4N-phosphoundecaprenol) from the cytoplasmic to the periplasmic side of the inner membrane. {ECO:0000269|PubMed:17928292}. EcoCyc product frame: MONOMER0-2682. EcoCyc synonyms: yfbW. Genomic coordinates: 2372557-2372892. EcoCyc protein note: ArnE is an integral membrane component of the ArnE/ArnF undecaprenyl-phosphate-α-L-Ara4N flippase.

## Biological Role

Activated by basR (protein.P30843).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47377|protein.Q47377]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P30843|protein.P30843]] `RegulonDB` `S` - regulator=BasR; target=arnE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0285065,ECOCYC:G0-10460,GeneID:1450282`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2372557-2372892:+; feature_type=gene
