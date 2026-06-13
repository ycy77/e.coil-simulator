---
entity_id: "gene.b4213"
entity_type: "gene"
name: "cpdB"
source_database: "NCBI RefSeq"
source_id: "gene-b4213"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4213"
  - "cpdB"
---

# cpdB

`gene.b4213`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4213`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cpdB (gene.b4213) is a gene entity. It encodes cpdB (protein.P08331). Encoded protein function: FUNCTION: This bifunctional enzyme catalyzes two consecutive reactions during ribonucleic acid degradation. Converts a 2',3'-cyclic nucleotide to a 3'-nucleotide and then the 3'-nucleotide to the corresponding nucleoside and phosphate. {ECO:0000269|PubMed:3005231}. EcoCyc product frame: CPDB-MONOMER. Genomic coordinates: 4434622-4436565. EcoCyc protein note: cpdB encodes periplasmic 2',3'-cyclic nucleotide 2'-phosphodiesterase . First characterized in E. coli B, the enzyme contains both cyclic phosphodiesterase and 3'-nucleotidase activity and catalyses the hydrolysis of 2',3'-cyclic nucleotides to yield nucleotides and phosphate via a two-step reaction . Kinetic analyses suggest that the enzyme has two distinct active sites . The physiological role of CpdB may be to break down ribonucleotide 2',3'-cyclic phosphates which can be formed when RNA is digested by ribosome-bound RNase . Purified, recombinant CpdB, cloned from E...

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08331|protein.P08331]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cpdB; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=cpdB; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=cpdB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013782,ECOCYC:EG10160,GeneID:948729`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4434622-4436565:-; feature_type=gene
