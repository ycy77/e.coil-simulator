---
entity_id: "gene.b4225"
entity_type: "gene"
name: "chpB"
source_database: "NCBI RefSeq"
source_id: "gene-b4225"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4225"
  - "chpB"
---

# chpB

`gene.b4225`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4225`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

chpB (gene.b4225) is a gene entity. It encodes chpB (protein.P33647). Encoded protein function: FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system. ChpB is a sequence-specific mRNA and (weak) tmRNA endoribonuclease that inhibits protein synthesis and induces bacterial stasis. Cleavage is independent of the ribosome. Cleavage occurs at ACY sequences where Y is not C. The endoribonuclease activity is not as strong as that of MazF. The endoribonuclease activity (a toxin) is inhibited by its labile cognate antitoxin ChpS. Toxicity results when the levels of ChpS decrease in the cell, leading to mRNA degradation. Both ChpS and ChpB probably bind to the promoter region of the chpS-chpB operon to autoregulate their synthesis. {ECO:0000269|PubMed:12972253, ECO:0000269|PubMed:16413033, ECO:0000269|PubMed:21419338, ECO:0000269|PubMed:8226627}. EcoCyc product frame: EG12096-MONOMER. EcoCyc synonyms: yjfE, chpBK. Genomic coordinates: 4448692-4449042. EcoCyc protein note: ChpB is the toxin component of the ChpB-ChpS toxin-antitoxin system. ChpB inhibits cell growth when it is overexpressed, or when its partner protein ChpS is absent . This growth inhibition effect appears to result from ChpB's ability to cleave RNAs. Identified cleavage targets include RNAs from era, mazG, and translated tmRNA...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33647|protein.P33647]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=chpB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013822,ECOCYC:EG12096,GeneID:948747`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4448692-4449042:+; feature_type=gene
