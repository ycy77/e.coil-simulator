---
entity_id: "gene.b0010"
entity_type: "gene"
name: "satP"
source_database: "NCBI RefSeq"
source_id: "gene-b0010"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0010"
  - "satP"
---

# satP

`gene.b0010`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0010`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

satP (gene.b0010) is a gene entity. It encodes satP (protein.P0AC98). Encoded protein function: FUNCTION: Uptake of acetate and succinate. Transport is energetically dependent on the protonmotive force. {ECO:0000269|PubMed:23844911}. EcoCyc product frame: EG11512-MONOMER. EcoCyc synonyms: yaaH. Genomic coordinates: 9928-10494. EcoCyc protein note: SatP is an acetate:proton symporter that is implicated in acetate homeostasis when E. coli K-12 is grown aerobically at high glucose concentrations; under these conditons, SatP is active in acetate transport at the exponential growth stage whereas the acetate permease YJCG-MONOMER "ActP" is more active at the entry to stationary phase; SatP is implicated in acetate uptake when E. coli is grown with acetic acid as the sole carbon and energy source . In transport assays, succinate is a competitive inhibitor for acetate uptake by YaaH; the absence of YaaH is associated with an increase in the amount of succinate found (at the 10 hour timepoint) in the culture supernatant of cells grown aerobically with glucose; this increase appears consistent with a decrease in succinate uptake . SatP contributes to the residual succinate uptake seen in mutant strains lacking the major aerobic succinate transporters DctA and DauA . SatP is predicted to have 6 membrane spanning alpha-helices with the C-terminus located in the cytoplasm...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC98|protein.P0AC98]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000032,ECOCYC:EG11512,GeneID:944792`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:9928-10494:-; feature_type=gene
