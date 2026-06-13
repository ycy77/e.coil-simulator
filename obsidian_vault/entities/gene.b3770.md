---
entity_id: "gene.b3770"
entity_type: "gene"
name: "ilvE"
source_database: "NCBI RefSeq"
source_id: "gene-b3770"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3770"
  - "ilvE"
---

# ilvE

`gene.b3770`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3770`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ilvE (gene.b3770) is a gene entity. It encodes ilvE (protein.P0AB80). Encoded protein function: FUNCTION: Acts on leucine, isoleucine and valine. EcoCyc product frame: BRANCHED-CHAINAMINOTRANSFER-MONOMER. Genomic coordinates: 3952484-3953413.

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB80|protein.P0AB80]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ilvE; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `C` - regulator=Lrp; target=ilvE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012316,ECOCYC:EG10497,GeneID:948278`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3952484-3953413:+; feature_type=gene
