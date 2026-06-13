---
entity_id: "gene.b0182"
entity_type: "gene"
name: "lpxB"
source_database: "NCBI RefSeq"
source_id: "gene-b0182"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0182"
  - "lpxB"
---

# lpxB

`gene.b0182`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0182`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lpxB (gene.b0182) is a gene entity. It encodes lpxB (protein.P10441). Encoded protein function: FUNCTION: Condensation of UDP-2,3-diacylglucosamine and 2,3-diacylglucosamine-1-phosphate to form lipid A disaccharide, a precursor of lipid A, a phosphorylated glycolipid that anchors the lipopolysaccharide to the outer membrane of the cell. EcoCyc product frame: LIPIDADISACCHARIDESYNTH-MONOMER. EcoCyc synonyms: pgsB. Genomic coordinates: 203348-204496.

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P10441|protein.P10441]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=lpxB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000620,ECOCYC:EG10546,GeneID:944838`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:203348-204496:+; feature_type=gene
