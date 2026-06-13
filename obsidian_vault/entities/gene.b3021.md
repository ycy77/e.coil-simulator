---
entity_id: "gene.b3021"
entity_type: "gene"
name: "mqsA"
source_database: "NCBI RefSeq"
source_id: "gene-b3021"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3021"
  - "mqsA"
---

# mqsA

`gene.b3021`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3021`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mqsA (gene.b3021) is a gene entity. It encodes mqsA (protein.Q46864). Encoded protein function: FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. Labile antitoxin that binds to the MqsR mRNA interferase toxin and neutralizes its endoribonuclease activity. Overexpression prevents MqsR-mediated cessation of cell growth and inhibition of cell proliferation. Initially reported to act as a cotranscription factor with MqsA (PubMed:19690171, PubMed:20105222). Following further experiments, the MqsR-MqsA complex does not bind DNA and all reported data are actually due to a small fraction of free MqsA alone binding DNA. Addition of MqsR to a preformed MqsA-promoter DNA complex causes dissociation of the MqsA-DNA complex, probably causing derepression of MqsA-repressed transcripts (PubMed:23172222). MqsA binds to 2 palindromes in the promoter region of the mqsRA operon activating its transcription. Binds to other promoters, inducing mcbR and spy and repressing cspD among others (PubMed:20105222). Binds to and represses the rpoS promoter, the master stress regulator, resulting in decreased cyclic-di-GMP, reduced stress resistance, increased cell motility and decreased biofilm formation; in these experiments 5 TA systems are missing (lacks MazEF, RelEB, ChpB, YoeB-YefM, YafQ-DinJ) (PubMed:21516113)...

## Biological Role

Repressed by mqsA (protein.Q46864). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46864|protein.Q46864]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mqsA; function=+
- `represses` <-- [[protein.Q46864|protein.Q46864]] `RegulonDB` `S` - regulator=MqsA; target=mqsA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009923,ECOCYC:G7571,GeneID:945814`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3167851-3168246:-; feature_type=gene
