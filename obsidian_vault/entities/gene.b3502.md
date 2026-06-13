---
entity_id: "gene.b3502"
entity_type: "gene"
name: "arsB"
source_database: "NCBI RefSeq"
source_id: "gene-b3502"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3502"
  - "arsB"
---

# arsB

`gene.b3502`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3502`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

arsB (gene.b3502) is a gene entity. It encodes arsB (protein.P0AB93). Encoded protein function: FUNCTION: Involved in arsenical resistance. Thought to form the channel of an arsenite pump (By similarity). {ECO:0000250}. EcoCyc product frame: ARSF-MONOMER. EcoCyc synonyms: arsF. Genomic coordinates: 3648935-3650224. EcoCyc protein note: Based on sequence similarity with the R773-plasmid encoded arsenite resistance operon, ArsB is a transporter and ArsC is an arsenate reductase . The chromosomally encoded operon, however, lacks arsA, which encodes a putative ATP-binding protein . Transport through ArsB occurs through a metalloid:proton antiport mechanism . Expression of arsA from the R773 plasmid increases resistance to As(III) and Sb(III) showing ArsB can act alone in metalloid:proton antiport or as part of an ATP-dependent ABC transporter . Antimonite stimulates uptake of arsenite, but arsenite inhibits uptake of antimonite suggesting co-transport of the two compounds possibly as six-membered, co-polymer rings . Deletion mutants of the chromosomal arsRBC operon exhibit 10-20 times more sensitivity to arsenite and 5-10 times more sensitivity to antimonite and arsenate than the parental strain . Expression of the cloned arsRBC conferred increased arsenite, arsenate, and antimonite resistance compared with wild-type as well as when expressed in an arsRBC deletion strain...

## Biological Role

Repressed by arsR (protein.P37309). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB93|protein.P0AB93]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=arsB; function=+
- `represses` <-- [[protein.P37309|protein.P37309]] `RegulonDB` `S` - regulator=ArsR; target=arsB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011437,ECOCYC:EG12236,GeneID:948011`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3648935-3650224:+; feature_type=gene
