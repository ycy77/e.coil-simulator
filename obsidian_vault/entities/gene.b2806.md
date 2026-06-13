---
entity_id: "gene.b2806"
entity_type: "gene"
name: "rlmM"
source_database: "NCBI RefSeq"
source_id: "gene-b2806"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2806"
  - "rlmM"
---

# rlmM

`gene.b2806`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2806`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rlmM (gene.b2806) is a gene entity. It encodes rlmM (protein.P0ADR6). Encoded protein function: FUNCTION: Catalyzes the 2'-O-methylation at nucleotide C2498 in 23S rRNA. Modifies C2498 in naked 23S rRNA, but not in assembled 50S subunits or ribosomes. {ECO:0000269|PubMed:19400805, ECO:0000269|PubMed:22923526}. EcoCyc product frame: EG11794-MONOMER. EcoCyc synonyms: ygdE. Genomic coordinates: 2940143-2941243. EcoCyc protein note: RlmM is the methyltransferase responsible for methylation of 23S rRNA at the 2'-O position of the ribose at the C2498 nucleotide within the peptidyl transferase loop. In vitro, the enzyme is active on naked 23S rRNA and unmodified domain V alone , but not assembled 50S ribosomal subunits or ribosomes . Crystal structures of RlmM have been solved , showing the presence of an N-terminal THUMP domain and aC-terminal Rossmann-like fold methyltransferase domain . RlmM was predicted to be an RNA 2'-O-ribose methyltranserase by sequence similarity. The extended N-terminus may act in target recognition . Phylogenetic analysis of this protein family has been performed . Phylogenetic profiling shows an unexplained link between RlmM and RdgC . An rlmM mutant has a slightly longer doubling time in rich medium than wild type and is slowly out-competed by wild type in a growth competition experiment...

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADR6|protein.P0ADR6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=rlmM; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009197,ECOCYC:EG11794,GeneID:947283`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2940143-2941243:-; feature_type=gene
