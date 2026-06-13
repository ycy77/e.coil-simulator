---
entity_id: "gene.b3185"
entity_type: "gene"
name: "rpmA"
source_database: "NCBI RefSeq"
source_id: "gene-b3185"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3185"
  - "rpmA"
---

# rpmA

`gene.b3185`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3185`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpmA (gene.b3185) is a gene entity. It encodes rpmA (protein.P0A7L8). Encoded protein function: Large ribosomal subunit protein bL27 (50S ribosomal protein L27) EcoCyc product frame: EG50002-MONOMER. EcoCyc synonyms: rpz. Genomic coordinates: 3332862-3333119. EcoCyc protein note: The L27 protein is a component of the 50S subunit of the ribosome. It was initially thought to be a functional component of the peptidyl transferase center ; single-molecule fluorescence resonance energy transfer studies have indicated that L27 stabilizes the peptidyl-tRNA . L27 is involved in the assembly of the small and large ribosomal subunits into the 70S ribosome . L27 was thought to participate both in the assembly of the 50S subunit and in the peptidyl transferase reaction . L27 crosslinks to aminoacylated tRNA in the A and P site . Involvement of L27 with the peptidyl transferase center was also suggested by its interactions with various antibiotics: N-bromoacetyl chloramphenicol, an antibiotic that interacts with the peptidyl transferase center, affinity labels L27 . L27 is labeled by the macrolides carbomycin A, niddamycin and tylosin, which inhibit ribosomal activity . L27 can also be crosslinked to the spiramycin derivative dihydrospiramycin . It was later shown that L27 does not participate in peptide bond formation or peptidyl-tRNA hydrolysis...

## Biological Role

Activated by rpoD (protein.P00579), mlrA (protein.P33358).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7L8|protein.P0A7L8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rpmA; function=+
- `activates` <-- [[protein.P33358|protein.P33358]] `RegulonDB` `S` - regulator=MlrA; target=rpmA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010468,ECOCYC:EG50002,GeneID:945190`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3332862-3333119:-; feature_type=gene
