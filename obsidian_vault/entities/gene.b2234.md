---
entity_id: "gene.b2234"
entity_type: "gene"
name: "nrdA"
source_database: "NCBI RefSeq"
source_id: "gene-b2234"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2234"
  - "nrdA"
---

# nrdA

`gene.b2234`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2234`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nrdA (gene.b2234) is a gene entity. It encodes nrdA (protein.P00452). Encoded protein function: FUNCTION: Provides the precursors necessary for DNA synthesis. Catalyzes the biosynthesis of deoxyribonucleotides from the corresponding ribonucleotides. R1 contains the binding sites for both substrates and allosteric effectors and carries out the actual reduction of the ribonucleotide. It also provides redox-active cysteines. EcoCyc product frame: NRDA-MONOMER. EcoCyc synonyms: dnaF. Genomic coordinates: 2344865-2347150.

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

- `encodes` --> [[protein.P00452|protein.P00452]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P03004|protein.P03004]] `RegulonDB` `C` - regulator=DnaA; target=nrdA; function=-+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nrdA; function=+
- `activates` <-- [[protein.P0A8S1|protein.P0A8S1]] `RegulonDB` `S` - regulator=ArgP; target=nrdA; function=+
- `represses` <-- [[protein.P03004|protein.P03004]] `RegulonDB` `C` - regulator=DnaA; target=nrdA; function=-+
- `represses` <-- [[protein.P0A8D0|protein.P0A8D0]] `RegulonDB` `S` - regulator=NrdR; target=nrdA; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `C` - regulator=H-NS; target=nrdA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007383,ECOCYC:EG10660,GeneID:946612`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2344865-2347150:+; feature_type=gene
