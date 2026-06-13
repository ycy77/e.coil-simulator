---
entity_id: "gene.b2688"
entity_type: "gene"
name: "gshA"
source_database: "NCBI RefSeq"
source_id: "gene-b2688"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2688"
  - "gshA"
---

# gshA

`gene.b2688`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2688`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gshA (gene.b2688) is a gene entity. It encodes gshA (protein.P0A6W9). Encoded protein function: Glutamate--cysteine ligase (EC 6.3.2.2) (Gamma-ECS) (GCS) (Gamma-glutamylcysteine synthetase) EcoCyc product frame: GLUTCYSLIG-MONOMER. EcoCyc synonyms: gsh-I. Genomic coordinates: 2814883-2816439. EcoCyc protein note: gshA was first cloned and sequenced from E. coli B ; the sequence of the E. coli B and K-12 genes are identical. γ-Glutamate-cysteine ligase catalyzes the first of two steps in the pathway for the biosynthesis of GLUTATHIONE, also referred to as GSH for its γ-Glu-Cys-Gly tripeptide structure. The enzyme is feedback-inhibited by glutathione . The enzyme contains two divalent metal ions which play a role in amino acid binding. Substrate specificity depends on whether Mg2+ or Mn2+ is present; Mn2+ broadens the specificity . Transition state analog inhibitors have been used to study substrate recognition . The enzyme can utilize ethylamine as a substrate, thus producing theanine (γ-glutamylethylamide) . Crystal structures of the enzyme from E. coli B (whose wild-type sequence is identical to the K-12 enzyme) have been solved . The structure shows coordination of an inhibitor by three Mg2+ ions, and showing that the binding of cysteine follows an induced-fit model...

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00340` Histidine metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6W9|protein.P0A6W9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008845,ECOCYC:EG10418,GeneID:944881`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2814883-2816439:-; feature_type=gene
