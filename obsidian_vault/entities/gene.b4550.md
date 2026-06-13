---
entity_id: "gene.b4550"
entity_type: "gene"
name: "arfA"
source_database: "NCBI RefSeq"
source_id: "gene-b4550"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4550"
  - "arfA"
---

# arfA

`gene.b4550`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4550`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

arfA (gene.b4550) is a gene entity. It encodes arfA (protein.P36675). Encoded protein function: FUNCTION: Rescues ribosomes stalled at the 3' end of non-stop mRNAs (PubMed:21062370, PubMed:21435036). This activity is crucial when the stalled ribosome cannot be rescued by the SsrA(tmRNA)-SmpB quality control system (PubMed:21062370, PubMed:21435036). Binds the 30S subunit, contacting 16S rRNA with the N-terminus near the decoding center and its C-terminus in the mRNA entry channel; contacts change in the presence of release factor 2 (RF2, also named PrfB) (PubMed:25355516, PubMed:27906160, PubMed:27906161, PubMed:27934701, PubMed:28077875). Requires RF2/PrfB to hydrolyze stalled peptidyl-tRNA on the ribosome; recruits and probably helps position RF2/PrfB correctly in the ribosomal A site so RF2's GGQ motif can hydrolyze the peptidyl-tRNA bond (PubMed:22857598, PubMed:22922063, PubMed:25355516, PubMed:27906160, PubMed:27906161, PubMed:27934701, PubMed:28077875). Does not release ribosomes with a programmed pause caused by regulatory chains such as SecM-mediated pausing (PubMed:22857598). Binds tRNA which may stimulate its ribosome rescue activity (PubMed:22857598)...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36675|protein.P36675]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=arfA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0285071,ECOCYC:G0-10465,GeneID:1450289`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3438431-3438649:-; feature_type=gene
