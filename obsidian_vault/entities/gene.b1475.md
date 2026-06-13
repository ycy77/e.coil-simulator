---
entity_id: "gene.b1475"
entity_type: "gene"
name: "fdnH"
source_database: "NCBI RefSeq"
source_id: "gene-b1475"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1475"
  - "fdnH"
---

# fdnH

`gene.b1475`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1475`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fdnH (gene.b1475) is a gene entity. It encodes fdnH (protein.P0AAJ3). Encoded protein function: FUNCTION: Formate dehydrogenase allows E.coli to use formate as major electron donor during anaerobic respiration, when nitrate is used as electron acceptor. The beta subunit FdnH is an electron transfer unit containing 4 iron-sulfur clusters; it serves as a conduit for electrons that are transferred from the formate oxidation site in the alpha subunit (FdnG) to the menaquinone associated with the gamma subunit (FdnI) of formate dehydrogenase-N. Formate dehydrogenase-N is part of a system that generates proton motive force, together with the dissimilatory nitrate reductase (Nar). {ECO:0000269|PubMed:11884747}. EcoCyc product frame: FDNH-MONOMER. Genomic coordinates: 1550461-1551345. EcoCyc protein note: fdnH encodes the β subunit of formate dehydrogenase N (Fdh-N); it contains four [4Fe-4S] clusters (FS1, FS2, FS3 and FS4) and one C-terminal transmembrane helix . FdnH serves as a conduit for electrons that are transferred from the formate oxidation site in the α subunit (FdnG) to the menaquinone associated with the γ subunit (FdnI) . FdnH is a putative C-tail-anchored (TA) membrane protein .

## Biological Role

Repressed by fnr (protein.P0A9E5), narP (protein.P31802). Activated by fnr (protein.P0A9E5), narL (protein.P0AF28).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAJ3|protein.P0AAJ3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=fdnH; function=-+
- `activates` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `C` - regulator=NarL; target=fdnH; function=+
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=fdnH; function=-+
- `represses` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=fdnH; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004919,ECOCYC:EG11228,GeneID:948794`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1550461-1551345:+; feature_type=gene
