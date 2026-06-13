---
entity_id: "gene.b1135"
entity_type: "gene"
name: "rluE"
source_database: "NCBI RefSeq"
source_id: "gene-b1135"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1135"
  - "rluE"
---

# rluE

`gene.b1135`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1135`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rluE (gene.b1135) is a gene entity. It encodes rluE (protein.P75966). Encoded protein function: FUNCTION: Responsible for synthesis of pseudouridine from uracil-2457 in 23S ribosomal RNA. {ECO:0000269|PubMed:11720289}. EcoCyc product frame: G6581-MONOMER. EcoCyc synonyms: ymfC. Genomic coordinates: 1194298-1194951. EcoCyc protein note: RluE is the pseudouridine synthase that catalyzes formation of the universally conserved pseudouridine at position 2457 in the peptidyltransferase center of 23S rRNA. RluE belongs to the RsuA family of RNA pseudouridine synthases . Crystal structures of the full-length protein and the C-terminal catalytic domain have been solved at 1.6 and 1.2 Å resolution, respectively. The conserved active site residue Asp79 is essential for activity . RluE interacts with the H89 helix and its single-stranded flanking regions within 23S rRNA; specific regions within RluE that are involved in rRNA interactions as well as additional active site residues were identified by mutagenesis . An rluE null mutant exhibits no obvious growth defect . A 20°C conditional lethal with 37°C permissive phenotype occurred for a ΔrluE ΔEG11118 "rluC" double mutant along with a lower tripeptide synthesis rate compared to the single mutations...

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75966|protein.P75966]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=rluE; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003820,ECOCYC:G6581,GeneID:945701`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1194298-1194951:-; feature_type=gene
