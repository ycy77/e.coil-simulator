---
entity_id: "gene.b0491"
entity_type: "gene"
name: "fetB"
source_database: "NCBI RefSeq"
source_id: "gene-b0491"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0491"
  - "fetB"
---

# fetB

`gene.b0491`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0491`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fetB (gene.b0491) is a gene entity. It encodes fetB (protein.P77307). Encoded protein function: FUNCTION: Part of the ABC transporter complex FetAB, which is probably involved in iron export and enhances resistance to H(2)O(2)-mediated oxidative stress. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:24038693}. EcoCyc product frame: G6267-MONOMER. EcoCyc synonyms: ybbM. Genomic coordinates: 516583-517362. EcoCyc protein note: FetB is the predicted inner membrane subunit of a putative ABC family transporter which has a role in iron homeostasis. Overexpression of fetAB increases resistance to H2O2 induced stress in the presence of Fe2+. Overexpression of fetAB decreases the intracellular iron levels of an E. coli K-12 Δfur strain. An E. coli K-12 ΔfetB strain has increased sensitivity to H2O2 compared to wild-type. Overexpression of fetAB from a plasmid abrogates the H2O2 sensitivity of the fetB knockout strain . FetB (formerly YbbM) is an inner membrane protein with seven predicted transmembrane domains. The C terminus is located in the cytoplasm . A FetB-gfp (green fluorescent protein) fusion localises to the inner membrane with the C-terminus located in the cytoplasm . fet: Fe transport

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77307|protein.P77307]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001705,ECOCYC:G6267,GeneID:945137`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:516583-517362:+; feature_type=gene
