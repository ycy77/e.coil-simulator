---
entity_id: "gene.b3397"
entity_type: "gene"
name: "nudE"
source_database: "NCBI RefSeq"
source_id: "gene-b3397"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3397"
  - "nudE"
---

# nudE

`gene.b3397`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3397`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nudE (gene.b3397) is a gene entity. It encodes nudE (protein.P45799). Encoded protein function: FUNCTION: Active on adenosine(5')triphospho(5')adenosine (Ap3A), ADP-ribose, NADH, adenosine(5')diphospho(5')adenosine (Ap2A). EcoCyc product frame: G7740-MONOMER. EcoCyc synonyms: yrfE. Genomic coordinates: 3525589-3526149. EcoCyc protein note: NudE belongs to the family of Nudix hydrolases . The enzyme is specific for nucleoside pyrophosphates with an ADP moiety; preferred substrates of NudE include adenosine(5')triphospho(5')adenosine (Ap3A), ADP-ribose, and NADH . Gel filtration experiments suggest that the enzyme is a dimer in solution . A crystal structure has been solved at 2.32 Å resolution . An mrcA nudE yrfF triple mutant exhibits phenotypes including mucoidy, heat sensitivity, growth defects, and resistance to phage or antibiotic drugs, whereas a single mrcA mutant does not . Expression of nudE may be regulated by ArcA . Review:

## Biological Role

Repressed by arcA (protein.P0A9Q1).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45799|protein.P45799]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=nudE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011086,ECOCYC:G7740,GeneID:947906`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3525589-3526149:-; feature_type=gene
