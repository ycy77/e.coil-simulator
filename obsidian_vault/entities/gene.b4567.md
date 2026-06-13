---
entity_id: "gene.b4567"
entity_type: "gene"
name: "yjjZ"
source_database: "NCBI RefSeq"
source_id: "gene-b4567"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4567"
  - "yjjZ"
---

# yjjZ

`gene.b4567`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4567`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjjZ (gene.b4567) is a gene entity. It encodes yjjZ (protein.P55914). Encoded protein function: Uncharacterized protein YjjZ EcoCyc product frame: MONOMER0-2696. Genomic coordinates: 4605804-4606040. EcoCyc protein note: Expression of yjjZ is significantly decreased in populations adapted to the presence of ampicillin, tetracycline, and n-butanol . Repression of yjjZ expression may lead to some growth improvement in the presence of n-butanol or n-hexane, although a ΔyjjZ mutant grows more slowly than wild-type . A ΔyjjZ mutant showed an increased growth rate compared to wild type in the absence of biofuel stress .

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9). Activated by rpoD (protein.P00579), oxyR (protein.P0ACQ4).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P55914|protein.P55914]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yjjZ; function=+
- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `C` - regulator=OxyR; target=yjjZ; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=yjjZ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0285088,ECOCYC:G0-10474,GeneID:1450313`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4605804-4606040:+; feature_type=gene
