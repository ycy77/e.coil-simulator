---
entity_id: "gene.b2675"
entity_type: "gene"
name: "nrdE"
source_database: "NCBI RefSeq"
source_id: "gene-b2675"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2675"
  - "nrdE"
---

# nrdE

`gene.b2675`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2675`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nrdE (gene.b2675) is a gene entity. It encodes nrdE (protein.P39452). Encoded protein function: FUNCTION: Provides the precursors necessary for DNA synthesis. Catalyzes the biosynthesis of deoxyribonucleotides from the corresponding ribonucleotides. R1E contains the binding sites for both substrates and allosteric effectors and carries out the actual reduction of the ribonucleotide. EcoCyc product frame: NRDE-MONOMER. Genomic coordinates: 2801348-2803492.

## Biological Role

Repressed by nrdR (protein.P0A8D0), fur (protein.P0A9A9). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39452|protein.P39452]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nrdE; function=+
- `represses` <-- [[protein.P0A8D0|protein.P0A8D0]] `RegulonDB` `S` - regulator=NrdR; target=nrdE; function=-
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=nrdE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008806,ECOCYC:EG20257,GeneID:947155`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2801348-2803492:+; feature_type=gene
