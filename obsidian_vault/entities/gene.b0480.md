---
entity_id: "gene.b0480"
entity_type: "gene"
name: "ushA"
source_database: "NCBI RefSeq"
source_id: "gene-b0480"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0480"
  - "ushA"
---

# ushA

`gene.b0480`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0480`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ushA (gene.b0480) is a gene entity. It encodes ushA (protein.P07024). Encoded protein function: FUNCTION: Degradation of external UDP-glucose to uridine monophosphate and glucose-1-phosphate, which can then be used by the cell. EcoCyc product frame: USHA-MONOMER. Genomic coordinates: 504914-506566. EcoCyc protein note: The ushA gene of E. coli encodes a bifunctional enzyme with 5'-nucleotidase and UDP-sugar hydrolase activities. It has relatively broad substrate specificity, hydrolyzing 5'-ribonucleotides and 5'-deoxyribonucleotides , bis(5'-nucleosidyl)polyphosphates , UDP sugars , and CDP-alcohols . It also hydrolyzes the synthetic substrates bis(p-nitrophenyl)phosphate and p-nitrophenyl phosphate . UshA localizes to the periplasm where it is able to catalyze the degradation of external UDP-glucose to uridine, glucose-1-phosphate and inorganic phosphate which are then utilized by the cell. The nucleoside diphosphate sugar hydrolase activity is specific for UDP sugars . The periplasmic location suggests a general role for this enzyme in utilization of extracellular nucleotides . UshA is also involved in the degradation of internally formed nucleotides during degradation of cellular RNA . ushA knockout mutants lack major 5'-nucleotidase activity. An ushA aphA double knockout mutant is unable to utilize purine nucleotides as the sole carbon source...

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07024|protein.P07024]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001668,ECOCYC:EG11060,GeneID:947331`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:504914-506566:+; feature_type=gene
