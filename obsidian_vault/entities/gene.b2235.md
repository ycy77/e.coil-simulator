---
entity_id: "gene.b2235"
entity_type: "gene"
name: "nrdB"
source_database: "NCBI RefSeq"
source_id: "gene-b2235"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2235"
  - "nrdB"
---

# nrdB

`gene.b2235`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2235`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nrdB (gene.b2235) is a gene entity. It encodes nrdB (protein.P69924). Encoded protein function: FUNCTION: Provides the precursors necessary for DNA synthesis. Catalyzes the biosynthesis of deoxyribonucleotides from the corresponding ribonucleotides. R2 contains the tyrosyl radical required for catalysis. EcoCyc product frame: NRDB-MONOMER. EcoCyc synonyms: ftsB. Genomic coordinates: 2347384-2348514.

## Biological Role

Repressed by dnaA (protein.P03004), nrdR (protein.P0A8D0), hns (protein.P0ACF8). Activated by dnaA (protein.P03004), fis (protein.P0A6R3), argP (protein.P0A8S1).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69924|protein.P69924]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P03004|protein.P03004]] `RegulonDB` `C` - regulator=DnaA; target=nrdB; function=-+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=nrdB; function=+
- `activates` <-- [[protein.P0A8S1|protein.P0A8S1]] `RegulonDB` `S` - regulator=ArgP; target=nrdB; function=+
- `represses` <-- [[protein.P03004|protein.P03004]] `RegulonDB` `C` - regulator=DnaA; target=nrdB; function=-+
- `represses` <-- [[protein.P0A8D0|protein.P0A8D0]] `RegulonDB` `S` - regulator=NrdR; target=nrdB; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `C` - regulator=H-NS; target=nrdB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007386,ECOCYC:EG10661,GeneID:946732`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2347384-2348514:+; feature_type=gene
