---
entity_id: "gene.b1022"
entity_type: "gene"
name: "pgaC"
source_database: "NCBI RefSeq"
source_id: "gene-b1022"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1022"
  - "pgaC"
---

# pgaC

`gene.b1022`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1022`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pgaC (gene.b1022) is a gene entity. It encodes pgaC (protein.P75905). Encoded protein function: FUNCTION: Probable N-acetylglucosaminyltransferase that catalyzes the polymerization of single monomer units of UDP-N-acetylglucosamine to produce the linear homomer poly-beta-1,6-N-acetyl-D-glucosamine (PGA), a biofilm adhesin polysaccharide. {ECO:0000269|PubMed:15090514, ECO:0000269|PubMed:18359807}. EcoCyc product frame: G6529-MONOMER. EcoCyc synonyms: hmsR, ycdQ. Genomic coordinates: 1086521-1087846.

## Biological Role

Repressed by ompR (protein.P0AA16), csrA (protein.P69913). Activated by nhaR (protein.P0A9G2).

## Enriched Pathways

- `eco00543` Exopolysaccharide biosynthesis (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75905|protein.P75905]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9G2|protein.P0A9G2]] `RegulonDB` `S` - regulator=NhaR; target=pgaC; function=+
- `represses` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=pgaC; function=-
- `represses` <-- [[protein.P69913|protein.P69913]] `RegulonDB` `C` - regulator=carbon storage regulator CsrA; target=pgaC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003464,ECOCYC:G6529,GeneID:945606`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1086521-1087846:-; feature_type=gene
