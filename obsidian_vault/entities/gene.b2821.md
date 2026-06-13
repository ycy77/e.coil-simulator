---
entity_id: "gene.b2821"
entity_type: "gene"
name: "ptrA"
source_database: "NCBI RefSeq"
source_id: "gene-b2821"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2821"
  - "ptrA"
---

# ptrA

`gene.b2821`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2821`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ptrA (gene.b2821) is a gene entity. It encodes ptrA (protein.P05458). Encoded protein function: FUNCTION: Endopeptidase that degrades small peptides of less than 7 kDa, such as glucagon and insulin. EcoCyc product frame: EG10786-MONOMER. EcoCyc synonyms: ptr. Genomic coordinates: 2955996-2958884. EcoCyc protein note: Protease III is a periplasmic protein that rapidly degrades small proteins and peptides in vitro . Protease III is partially responsible for degrading A-β-lactamase as well as misfolded MalE31 . Protease III is a zinc metalloendopeptidase with a nontraditional zinc-binding motif, featuring the consensus sequence HXXEH rather than the more traditional HEXXH . In addition to the two histidines in the zinc-binding motif, glutamate162 is also required for zinc coordination . A 50 kDa polypeptide with no apparent protease function derived from the N-terminal end of protease III can be found in the periplasm under some circumstances .

## Biological Role

Repressed by lexA (protein.P0A7C2), nac (protein.Q47005). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P05458|protein.P05458]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ptrA; function=+
- `represses` <-- [[protein.P0A7C2|protein.P0A7C2]] `RegulonDB` `C` - regulator=LexA; target=ptrA; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ptrA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009252,ECOCYC:EG10786,GeneID:947284`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2955996-2958884:-; feature_type=gene
