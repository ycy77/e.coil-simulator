---
entity_id: "gene.b2313"
entity_type: "gene"
name: "cvpA"
source_database: "NCBI RefSeq"
source_id: "gene-b2313"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2313"
  - "cvpA"
---

# cvpA

`gene.b2313`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2313`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cvpA (gene.b2313) is a gene entity. It encodes cvpA (protein.P08550). Encoded protein function: FUNCTION: Required for colicin V production from plasmid IncFI ColV3-K30. EcoCyc product frame: EG10169-MONOMER. EcoCyc synonyms: dedE. Genomic coordinates: 2430275-2430763. EcoCyc protein note: CvpA is required for wild-type production of colicin V from an episomal gene . A mutant exhibits a defect in production of colicin V from an episomal gene . A mutant exhibits adenine auxotrophy . CvpA has similarity to a Pseudomonas aeruginosa protein . Regulation has been described . CvpA: "colicin V production" .

## Biological Role

Repressed by ArgR-L-arginine DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-228), argR (protein.P0A6D0), purR (protein.P0ACP7). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08550|protein.P08550]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=cvpA; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-228|complex.ecocyc.CPLX0-228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=cvpA; function=-
- `represses` <-- [[protein.P0ACP7|protein.P0ACP7]] `RegulonDB` `C` - regulator=PurR; target=cvpA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007633,ECOCYC:EG10169,GeneID:945055`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2430275-2430763:-; feature_type=gene
