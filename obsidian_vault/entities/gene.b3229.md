---
entity_id: "gene.b3229"
entity_type: "gene"
name: "sspA"
source_database: "NCBI RefSeq"
source_id: "gene-b3229"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3229"
  - "sspA"
---

# sspA

`gene.b3229`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3229`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sspA (gene.b3229) is a gene entity. It encodes sspA (protein.P0ACA3). Encoded protein function: FUNCTION: Forms an equimolar complex with the RNA polymerase holoenzyme (RNAP) but not with the core enzyme. It is synthesized predominantly when cells are exposed to amino acid starvation, at which time it accounts for over 50% of the total protein synthesized. It is involved in the transition from P1 early to P1 late gene expression. Rnk and SspA can functionally replace P.aeruginosa alginate regulatory gene algR2. EcoCyc product frame: EG10977-MONOMER. EcoCyc synonyms: ssp, pog. Genomic coordinates: 3376782-3377420. EcoCyc protein note: The SspA protein is associated with RNA polymerase and is required for transcriptional activation of the bacteriophage P1 late promoter in vivo and in vitro and for the transcription of two peptidoglycan synthases . SspA is essential for cell survival during acid-induced stress, acting by inhibiting accumulation of the global regulator H-NS during stationary phase . SspA expression is induced by starvation for glucose, nitrogen, phosphate or amino acids, and it increases with decreasing growth rate . The SspA protein has been crystallized, but the crystals did not allow structure determination . Determination of a crystal structure was attempted with SspA proteins from Vibrio cholerae, Pseudomonas aeruginosa, and Yersinia pestis; only the Y...

## Biological Role

Activated by zraR (protein.P14375).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACA3|protein.P0ACA3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P14375|protein.P14375]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=sspA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010594,ECOCYC:EG10977,GeneID:944744`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3376782-3377420:-; feature_type=gene
