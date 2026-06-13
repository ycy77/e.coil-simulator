---
entity_id: "gene.b1162"
entity_type: "gene"
name: "bluR"
source_database: "NCBI RefSeq"
source_id: "gene-b1162"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1162"
  - "bluR"
---

# bluR

`gene.b1162`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1162`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bluR (gene.b1162) is a gene entity. It encodes bluR (protein.P75989). Encoded protein function: FUNCTION: Controls the expression of several small proteins that may play a role in biofilm maturation. Binds to and represses the operator of the ycgZ-ymgA-ariR-ymgC operon and also regulates ynaK. Binding is antagonized by BluF upon blue light (470 nm) irradiation. Blue light may increase the affinity of BluF for BluR, allowing it to be released from its operator. {ECO:0000269|PubMed:19240136, ECO:0000269|PubMed:22783906}. EcoCyc product frame: G6602-MONOMER. EcoCyc synonyms: ycgE. Genomic coordinates: 1213328-1214059. EcoCyc protein note: BluR is a MerR-like regulator that contains an N-terminal helix-turn-helix DNA-binding region and a ligand-binding region in the C-terminal domain . BluR functions as a repressor for genes involved in the modulation of biofilm formation and for acid resistance genes . Its expression is strongly induced at low temperatures . BluR is a paralogue of MlrA, and it represses the transcription of the ycgZ-ymgA-ariR-ymgC operon . This operon is transcribed divergently on the opposite strand, under the control of σ38 (RpoS) RNA polymerase . Its gene products are involved in the production of colanic acid, a component of the biofilm matrix, via the Rcs phosphorelay system . The bluRF-ycgZ-ymgA-ariR region is conserved in various enteric bacteria...

## Biological Role

Activated by ygfI (protein.P52044).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75989|protein.P75989]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB|EcoCyc` `C` - regulator=SrsR; target=bluR; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003900,ECOCYC:G6602,GeneID:945735`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1213328-1214059:-; feature_type=gene
