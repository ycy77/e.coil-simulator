---
entity_id: "gene.b2676"
entity_type: "gene"
name: "nrdF"
source_database: "NCBI RefSeq"
source_id: "gene-b2676"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2676"
  - "nrdF"
---

# nrdF

`gene.b2676`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2676`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nrdF (gene.b2676) is a gene entity. It encodes nrdF (protein.P37146). Encoded protein function: FUNCTION: Provides the precursors necessary for DNA synthesis. Catalyzes the biosynthesis of deoxyribonucleotides from the corresponding ribonucleotides. R2F contains the tyrosyl radical required for catalysis. EcoCyc product frame: NRDF-MONOMER. EcoCyc synonyms: ygaD. Genomic coordinates: 2803502-2804461.

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

- `encodes` --> [[protein.P37146|protein.P37146]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nrdF; function=+
- `represses` <-- [[protein.P0A8D0|protein.P0A8D0]] `RegulonDB` `S` - regulator=NrdR; target=nrdF; function=-
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=nrdF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008808,ECOCYC:EG12381,GeneID:947149`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2803502-2804461:+; feature_type=gene
