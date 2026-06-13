---
entity_id: "gene.b1163"
entity_type: "gene"
name: "bluF"
source_database: "NCBI RefSeq"
source_id: "gene-b1163"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1163"
  - "bluF"
---

# bluF

`gene.b1163`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1163`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bluF (gene.b1163) is a gene entity. It encodes bluF (protein.P75990). Encoded protein function: FUNCTION: Binds to and releases the BluR repressor from its bound DNA target in a blue light-dependent (470 nm) fashion. A shift to low temperature also triggers a BluF-mediated relief of repression by BluR, suggesting BluF may serve as a thermometer. Blue light may act to increase the affinity of BluF for BluR, allowing it to be released from its operator. The protein has a reversible photocycle, and undergoes structural changes, probably in the EAL domain, in response to light. {ECO:0000269|PubMed:15453820, ECO:0000269|PubMed:19240136, ECO:0000269|PubMed:20141167, ECO:0000269|PubMed:22783906}. EcoCyc product frame: G6603-MONOMER. EcoCyc synonyms: ycgF. Genomic coordinates: 1214264-1215475. EcoCyc protein note: The N-terminal domain of BluF is a member of the family of blue-light sensing proteins that use FAD. BluF interacts directly with the MerR-like transcription factor G6602-MONOMER BluR and interferes with binding of BluR to the ycgZ promoter in a blue light-dependent manner . The C-terminal EAL domain of BluF is degenerate; the protein does not bind cyclic di-guanosine monophosphate (c-di-GMP) and does not have c-di-GMP phosphodiesterase activity...

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by rpoD (protein.P00579), rcdA (protein.P75811).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75990|protein.P75990]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=bluF; function=+
- `activates` <-- [[protein.P75811|protein.P75811]] `RegulonDB` `C` - regulator=RcdA; target=bluF; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003903,ECOCYC:G6603,GeneID:947592`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1214264-1215475:-; feature_type=gene
