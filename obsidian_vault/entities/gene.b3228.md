---
entity_id: "gene.b3228"
entity_type: "gene"
name: "sspB"
source_database: "NCBI RefSeq"
source_id: "gene-b3228"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3228"
  - "sspB"
---

# sspB

`gene.b3228`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3228`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sspB (gene.b3228) is a gene entity. It encodes sspB (protein.P0AFZ3). Encoded protein function: FUNCTION: Enhances recognition of ssrA-tagged proteins by the ClpX-ClpP protease; the ssrA degradation tag (AANDENYALAA) is added trans-translationally to proteins that are stalled on the ribosome, freeing the ribosome and targeting stalled peptides for degradation. SspB activates the ATPase activity of ClpX. Seems to act in concert with SspA in the regulation of several proteins during exponential and stationary-phase growth.; FUNCTION: Also stimulates degradation of the N-terminus of RseA (residues 1-108, alone or in complex with sigma-E) by ClpX-ClpP in a non-ssrA-mediated fashion. EcoCyc product frame: EG10978-MONOMER. Genomic coordinates: 3376279-3376776. EcoCyc protein note: The SspB protein is a specificity-enhancing factor for the ClpXP protease . When protein synthesis is stalled, incomplete proteins that are produced are tagged with the small SsrA peptide. The ribosome-associated SspB protein binds to the SsrA tag and enhances degradation of the tagged peptide by the ClpXP protease . The SspB protein forms a homodimer with two independent binding sites for SsrA-tagged proteins . It also binds to ClpX and stimulates its ATPase activity...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFZ3|protein.P0AFZ3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010591,ECOCYC:EG10978,GeneID:944774`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3376279-3376776:-; feature_type=gene
