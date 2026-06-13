---
entity_id: "gene.b4382"
entity_type: "gene"
name: "deoA"
source_database: "NCBI RefSeq"
source_id: "gene-b4382"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4382"
  - "deoA"
---

# deoA

`gene.b4382`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4382`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

deoA (gene.b4382) is a gene entity. It encodes deoA (protein.P07650). Encoded protein function: FUNCTION: The enzymes which catalyze the reversible phosphorolysis of pyrimidine nucleosides are involved in the degradation of these compounds and in their utilization as carbon and energy sources, or in the rescue of pyrimidine bases for nucleotide synthesis. EcoCyc product frame: DEOA-MONOMER. EcoCyc synonyms: TP, tpp, ttg. Genomic coordinates: 4618229-4619551. EcoCyc protein note: DeoA is a thymidine phosphorylase which is part of the pathway that utilizes pyrimidine deoxyribonucleoside as a carbon and energy source. Thymidine phosphorylase catalyzes the phosphorolysis of thymidine and other pyrimidine 2-deoxyribosides. This enzyme is highly specific for deoxyribose 1-phosphate . The crystal structure of DeoA has been determined at 2.8 and 2.6 Å resolution . The enzyme is an S-shaped dimer with identical subunits that are related by a crystallographic 2-fold axis . Mutants lacking deoA readily incorporates exogenous thymidine into deoxyribonucleic acid, but not ribonucleic acid or other macromolecules . Thymidine phosphorylase mutants fail to grow on deoxycytodine, deoxyuridine and thymidine . More recently, a ΔdeoA mutant was found to be required for thymine-starvation induced chromosome fragmentation (TiCF) and may encode a critical anti-fragmentation factor...

## Biological Role

Repressed by modE (protein.P0A9G8), crp (protein.P0ACJ8), deoR (protein.P0ACK5), cytR (protein.P0ACN7). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07650|protein.P07650]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=deoA; function=-+
- `represses` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `S` - regulator=ModE; target=deoA; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=deoA; function=-+
- `represses` <-- [[protein.P0ACK5|protein.P0ACK5]] `RegulonDB` `S` - regulator=DeoR; target=deoA; function=-
- `represses` <-- [[protein.P0ACN7|protein.P0ACN7]] `RegulonDB` `C` - regulator=CytR; target=deoA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014374,ECOCYC:EG10219,GeneID:948901`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4618229-4619551:+; feature_type=gene
