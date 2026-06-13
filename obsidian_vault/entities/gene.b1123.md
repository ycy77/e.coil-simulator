---
entity_id: "gene.b1123"
entity_type: "gene"
name: "potD"
source_database: "NCBI RefSeq"
source_id: "gene-b1123"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1123"
  - "potD"
---

# potD

`gene.b1123`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1123`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

potD (gene.b1123) is a gene entity. It encodes potD (protein.P0AFK9). Encoded protein function: FUNCTION: Required for the activity of the bacterial periplasmic transport system of putrescine and spermidine. Polyamine binding protein. {ECO:0000269|PubMed:1939142}. EcoCyc product frame: POTD-MONOMER. Genomic coordinates: 1181783-1182829. EcoCyc protein note: potD encodes the periplasmic binding protein of an ATP dependent spermidine uptake system. PotD binds putrescine and spermidine ; PotD binds spermidine (Kd = 3.2 µM , Kd = 5.8 nM ) but will also bind putrescine with a lower affinity (Kd = 100 µM) . Purified, crystallized PotD is a dimer but the molecule is monomeric in the presence of spermidine; the switch from dimer to monomer may have physiological significance . The PotD monomer consists of two domains connected through a hinge region (two β strands and a short peptide segment); the two domains are divided by a deep cleft which contains the substrate binding site; spermidine interacts directly with aromatic and acidic side chains atoms in the PotD binding site; it also interacts indirectly via a water molecule located in the binding site . PotD or PotD precursor functions as a transcription regulator of the the potABCD operon . PotD regulates biofilm formation through an unknown mechanism .

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFK9|protein.P0AFK9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003789,ECOCYC:EG10752,GeneID:945682`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1181783-1182829:-; feature_type=gene
