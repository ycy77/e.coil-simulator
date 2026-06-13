---
entity_id: "gene.b0087"
entity_type: "gene"
name: "mraY"
source_database: "NCBI RefSeq"
source_id: "gene-b0087"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0087"
  - "mraY"
---

# mraY

`gene.b0087`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0087`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mraY (gene.b0087) is a gene entity. It encodes mraY (protein.P0A6W3). Encoded protein function: FUNCTION: Catalyzes the initial step of the lipid cycle reactions in the biosynthesis of the cell wall peptidoglycan: transfers peptidoglycan precursor phospho-MurNAc-pentapeptide from UDP-MurNAc-pentapeptide onto the lipid carrier undecaprenyl phosphate, yielding undecaprenyl-pyrophosphoryl-MurNAc-pentapeptide, known as lipid I. {ECO:0000255|HAMAP-Rule:MF_00038, ECO:0000269|PubMed:1846850, ECO:0000269|PubMed:215212}. EcoCyc product frame: PHOSNACMURPENTATRANS-MONOMER. EcoCyc synonyms: murX. Genomic coordinates: 96002-97084. EcoCyc protein note: Phospho-N-acetylmuramoyl-pentapeptide transferase catalyzes the first step of the lipid cycle reactions in the biosynthetic pathway of cell wall peptidoglycans . MraY is of interest as an antibacterial drug target and has been used to assess high-throughput screening performance using the BioAssay Ontology .

## Biological Role

Repressed by pdhR (protein.P0ACL9), mraZ (protein.P22186).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01502` Vancomycin resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6W3|protein.P0A6W3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `S` - regulator=PdhR; target=mraY; function=-
- `represses` <-- [[protein.P22186|protein.P22186]] `RegulonDB` `C` - regulator=MraZ; target=mraY; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000316,ECOCYC:EG10604,GeneID:944814`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:96002-97084:+; feature_type=gene
