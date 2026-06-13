---
entity_id: "gene.b1823"
entity_type: "gene"
name: "cspC"
source_database: "NCBI RefSeq"
source_id: "gene-b1823"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1823"
  - "cspC"
---

# cspC

`gene.b1823`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1823`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cspC (gene.b1823) is a gene entity. It encodes cspC (protein.P0A9Y6). Encoded protein function: Cold shock-like protein CspC (CSP-C) EcoCyc product frame: EG12204-MONOMER. EcoCyc synonyms: msmB. Genomic coordinates: 1907226-1907435. EcoCyc protein note: CspC belongs to the cold shock family of proteins and functions as a transcription antiterminator at ρ-independent terminators both in vitro and in vivo . CspC appears to be involved in downregulating the heat shock response . CspC interacts with both RNA and single-stranded DNA; the consensus sequence AGGGAGGGA has been determined using an in vitro selection approach . CspE appears to interact specifically with U-rich mRNAs . Proteomic and microarray analysis identified genes whose expression is responsive to CspC levels, including rpoS . The stabilizing effect of CspC on the rpoS mRNA requires the 5' UTR of rpoS . Expression of cspC is not cold-shock inducible ; cspC is expressed constitutively during growth at 37°C . Expression of cspC and eight other csp genes during growth and under different media conditions has been measured . CspC protein levels decrease upon heat shock due to proteolysis possibly promoted by interacting with CPLX0-3934 GroES-GroEL . CspC protein levels increase during the transition to stationary phase...

## Biological Role

Repressed by btsR (protein.P0AFT5), rpoN (protein.P24255).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9Y6|protein.P0A9Y6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0AFT5|protein.P0AFT5]] `RegulonDB` `S` - regulator=BtsR; target=cspC; function=-
- `represses` <-- [[protein.P24255|protein.P24255]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006070,ECOCYC:EG12204,GeneID:946339`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1907226-1907435:-; feature_type=gene
