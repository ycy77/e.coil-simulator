---
entity_id: "gene.b2380"
entity_type: "gene"
name: "pyrS"
source_database: "NCBI RefSeq"
source_id: "gene-b2380"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2380"
  - "pyrS"
---

# pyrS

`gene.b2380`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2380`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pyrS (gene.b2380) is a gene entity. It encodes ypdA (protein.P0AA93). Encoded protein function: FUNCTION: Member of the two-component regulatory system YpdA/YpdB, which is part of a nutrient-sensing regulatory network composed of YpdA/YpdB, the high-affinity pyruvate signaling system BtsS/BtsR and their respective target proteins, YhjX and BtsT. YpdA activates YpdB by phosphorylation in response to high concentrations of extracellular pyruvate. Activation of the YpdA/YpdB signaling cascade also promotes BtsS/BtsR-mediated btsT expression. {ECO:0000269|PubMed:23222720, ECO:0000269|PubMed:24659770}. EcoCyc product frame: MONOMER0-4287. EcoCyc synonyms: ypdA. Genomic coordinates: 2498671-2500368. EcoCyc protein note: PyrS is the sensory kinase of a two-component signal transduction system which senses extracellular pyruvate and induces expression of the putative pyruvate transporter YHJX-MONOMER "YhjX" . PyrS is predicted to be an inner membrane protein with 6 trans-membrane domains . Phosphorylation of PyrS has not been detected in vitro, however substitution of the conserved histidine residue H371 with glutamine prevents yhjX induction in vivo . yhjX is not induced in a pyrSRypdC deletion mutant; complementation with pyrSRypdC expressed in trans restores induction...

## Biological Role

Activated by arcA (protein.P0A9Q1).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA93|protein.P0AA93]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=pyrS; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007855,ECOCYC:G7243,GeneID:946723`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2498671-2500368:+; feature_type=gene
