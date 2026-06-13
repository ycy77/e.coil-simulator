---
entity_id: "gene.b1418"
entity_type: "gene"
name: "cybB"
source_database: "NCBI RefSeq"
source_id: "gene-b1418"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1418"
  - "cybB"
---

# cybB

`gene.b1418`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1418`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cybB (gene.b1418) is a gene entity. It encodes cybB (protein.P0ABE5). Encoded protein function: FUNCTION: B-type di-heme cytochrome (PubMed:29915379, PubMed:3510204, PubMed:35671795). Catalyzes the oxidation of superoxide to molecular oxygen and transfers the extracted electrons to ubiquinone through the two hemes (PubMed:29915379, PubMed:35671795). Can also use menaquinone (PubMed:35671795). The enzyme may be responsible for the detoxification of the superoxide anion produced in the membrane or at its surface (PubMed:29915379). However, it can also efficiently catalyze the formation of superoxide from ubiquinol under physiological conditions (PubMed:35671795). {ECO:0000269|PubMed:29915379, ECO:0000269|PubMed:3510204, ECO:0000269|PubMed:35671795}. EcoCyc product frame: CYTOCHROME-B561-MONOMER. Genomic coordinates: 1490902-1491432. EcoCyc protein note: CybB or cytochrome b561 is a membrane bound superoxide:ubiquinone oxidoreductase which catalyses the direct oxidation of superoxide to oxygen concomitant with the reduction of ubiquinone to ubiquinol; the primary function of CybB may be to quench superoxide produced by respiratory chain enzymes in or at the membrane surface . CybB is a small inner membrane protein forming a four-helix bundle; it contains two b-type hemes, one of which has the edge of the porphyrin ring exposed to the periplasm...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABE5|protein.P0ABE5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004733,ECOCYC:EG10172,GeneID:947241`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1490902-1491432:+; feature_type=gene
