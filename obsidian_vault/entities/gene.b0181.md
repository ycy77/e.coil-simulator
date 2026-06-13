---
entity_id: "gene.b0181"
entity_type: "gene"
name: "lpxA"
source_database: "NCBI RefSeq"
source_id: "gene-b0181"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0181"
  - "lpxA"
---

# lpxA

`gene.b0181`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0181`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lpxA (gene.b0181) is a gene entity. It encodes lpxA (protein.P0A722). Encoded protein function: FUNCTION: Involved in the biosynthesis of lipid A, a phosphorylated glycolipid that anchors the lipopolysaccharide to the outer membrane of the cell. EcoCyc product frame: UDPNACETYLGLUCOSAMACYLTRANS-MONOMER. Genomic coordinates: 202560-203348.

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A722|protein.P0A722]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=lpxA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000618,ECOCYC:EG10545,GeneID:944849`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:202560-203348:+; feature_type=gene
