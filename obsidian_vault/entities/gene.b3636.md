---
entity_id: "gene.b3636"
entity_type: "gene"
name: "rpmG"
source_database: "NCBI RefSeq"
source_id: "gene-b3636"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3636"
  - "rpmG"
---

# rpmG

`gene.b3636`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3636`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpmG (gene.b3636) is a gene entity. It encodes rpmG (protein.P0A7N9). Encoded protein function: Large ribosomal subunit protein bL33 (50S ribosomal protein L33) EcoCyc product frame: EG10891-MONOMER. Genomic coordinates: 3811250-3811417. EcoCyc protein note: The L33 protein is a component of the 50S subunit of the ribosome. L33 is found in substoichiometric amounts and appears to require the presence of L3 and L28 for assembly . L33 is located within 21 Å of nucleotide C2475 of 23S rRNA, near the peptidyltransferase center . L33 had previously been shown to crosslink to 23S rRNA and to tRNA in the P site and E site . L33 also crosslinks to L1 and L27 and can be isolated in a complex with 5S rRNA, tRNA, and other proteins of the large ribosomal subunit . L33 can be exchanged between ribosomes; however, it is unclear whether this occurs in vivo . L33 is not exposed on the ribosomal surface . In ~ 25% of L33 proteins, the initiator methionine residue is monomethylated . In the remainder of L33 proteins, the initiating methionine is removed , and the first alanine residue is methylated . A strain containing an IS element insertion in rpmG shows no major defect in ribosome assembly ; L33 appears to have no significant role in ribosome synthesis or function . Overexpression of rpmG causes increased resistance to mitomycin C...

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7N9|protein.P0A7N9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011883,ECOCYC:EG10891,GeneID:946318`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3811250-3811417:-; feature_type=gene
