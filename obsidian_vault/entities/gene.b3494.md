---
entity_id: "gene.b3494"
entity_type: "gene"
name: "uspB"
source_database: "NCBI RefSeq"
source_id: "gene-b3494"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3494"
  - "uspB"
---

# uspB

`gene.b3494`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3494`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uspB (gene.b3494) is a gene entity. It encodes uspB (protein.P0A8S5). Encoded protein function: Universal stress protein B EcoCyc product frame: EG12231-MONOMER. EcoCyc synonyms: yhiO. Genomic coordinates: 3639385-3639720. EcoCyc protein note: UspB plays a role in the RuvABC recombination repair pathway and is required for wild-type ethanol tolerance in stationary phase . UspB is an inner membrane protein with two predicted transmembrane domains. The C terminus is located in the periplasm . A uspB mutant exhibits ethanol sensitivity, but not heat sensitivity, in stationary phase . A uspB mutant shows increased sensitivity to DNA damaging agents and phenocopies a ruvC mutant; overexpression of ruvC suppresses the UV-sensitive growth phenotype of the uspB mutant . Overproduction of UspB results in stationary phase inviability . uspB is transcribed under stress conditions including starvation; it depends on σS and is influenced by H-NS . Expression also requires the presence of ppGpp , but is not induced by UV stress . uspB mRNA stability during glucose starvation is diminished in the absence of CPLX0-3281 function . In a long-term evolution experiment under freeze-thaw-growth (FTG) conditions, an IS150 insertion in the 5' UTR of uspB was recovered multiple times and shown to be beneficial under the FTG regime. The IS150 insertion reduces uspB transcription...

## Biological Role

Activated by rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8S5|protein.P0A8S5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=uspB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011410,ECOCYC:EG12231,GeneID:948008`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3639385-3639720:-; feature_type=gene
