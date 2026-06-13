---
entity_id: "gene.b4260"
entity_type: "gene"
name: "pepA"
source_database: "NCBI RefSeq"
source_id: "gene-b4260"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4260"
  - "pepA"
---

# pepA

`gene.b4260`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4260`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pepA (gene.b4260) is a gene entity. It encodes pepA (protein.P68767). Encoded protein function: FUNCTION: Probably involved in the processing and regular turnover of intracellular proteins (PubMed:20067529). Catalyzes the removal of unsubstituted N-terminal amino acids from various peptides. Required for plasmid ColE1 site-specific recombination but not in its aminopeptidase activity. Could act as a structural component of the putative nucleoprotein complex in which the Xer recombination reaction takes place (PubMed:8057849). {ECO:0000269|PubMed:8057849, ECO:0000305|PubMed:20067529}. EcoCyc product frame: EG10694-MONOMER. EcoCyc synonyms: carP, xerB. Genomic coordinates: 4484440-4485951.

## Biological Role

Repressed by pepA (protein.P68767). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P68767|protein.P68767]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=pepA; function=+
- `represses` <-- [[protein.P68767|protein.P68767]] `RegulonDB` `S` - regulator=PepA; target=pepA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013953,ECOCYC:EG10694,GeneID:948791`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4484440-4485951:-; feature_type=gene
