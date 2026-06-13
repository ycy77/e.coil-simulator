---
entity_id: "gene.b0402"
entity_type: "gene"
name: "proY"
source_database: "NCBI RefSeq"
source_id: "gene-b0402"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0402"
  - "proY"
---

# proY

`gene.b0402`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0402`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

proY (gene.b0402) is a gene entity. It encodes proY (protein.P0AAE2). Encoded protein function: FUNCTION: Permease that is involved in the transport across the cytoplasmic membrane of proline. EcoCyc product frame: PROY-MONOMER. EcoCyc synonyms: yajM. Genomic coordinates: 420986-422359. EcoCyc protein note: proY, expressed as part of the complete set of E. coli open reading frames (the pooled ASKA library) suppresses the conditional auxotrophy of hisB, hisH and hisI single gene knockouts however this rescue phenotype could not be confirmed using the purified proY ASKA plasmid . In Salmonella typhimurium, proY is the structural gene for a cryptic proline transporter; overexpression of proY supports the growth of a putP insertion mutant with proline as a sole nitrogen source . In the Transporter Classification Database, ProY is a member of the Amino Acid Transporter (AAT) family within the Amino Acid-Polyamine-Organocation (APC) superfamily . ProY is an inner membrane protein with 12 predicted transmembrane domains; experimental topology analysis suggests the C terminus is located in the cytoplasm

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAE2|protein.P0AAE2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001398,ECOCYC:G6233,GeneID:945050`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:420986-422359:+; feature_type=gene
