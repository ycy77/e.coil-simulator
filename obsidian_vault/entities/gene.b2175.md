---
entity_id: "gene.b2175"
entity_type: "gene"
name: "mepS"
source_database: "NCBI RefSeq"
source_id: "gene-b2175"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2175"
  - "mepS"
---

# mepS

`gene.b2175`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2175`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mepS (gene.b2175) is a gene entity. It encodes mepS (protein.P0AFV4). Encoded protein function: FUNCTION: A murein DD-endopeptidase with specificity for D-Ala-meso-diaminopimelic acid (mDAP) cross-links. Its role is probably to cleave D-Ala-mDAP cross-links to allow insertion of new glycans and thus cell wall expansion. Functionally redundant with MepM and MepH. Also has weak LD-carboxypeptidase activity on L-mDAP-D-Ala peptide bonds. Partially suppresses a prc disruption mutant. {ECO:0000269|PubMed:23062283, ECO:0000269|PubMed:9158724}. EcoCyc product frame: G7147-MONOMER. EcoCyc synonyms: yeiV, spr. Genomic coordinates: 2269979-2270545. EcoCyc protein note: Purified MepS (formerly Spr) is a murein DD-endopeptidase with specificity for D-ala-m-DAP (4→3) cross links; the endopeptidase activity of MepS is associated with murein incorporation during cell growth; purified MepS also has weak LD-carboxypeptidase activity; purifed MepS has murein hydrolase activity on intact peptidoglycan (PG) sacculi . Purified MepS hydrolyses both 4→3 and 3→3 (m-DAP-mDAP) cross-links with similar efficacy . In addition to promoting cell elongation, MepS influences the cell division process; elevated MepS activity interferes with the activation of septal PG biogenesis by the divisome...

## Biological Role

Repressed by oxyS (gene.b4458).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFV4|protein.P0AFV4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[gene.b4458|gene.b4458]] `RegulonDB` `S` - regulator=OxyS; target=mepS; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007200,ECOCYC:G7147,GeneID:946686`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2269979-2270545:+; feature_type=gene
