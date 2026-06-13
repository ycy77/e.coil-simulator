---
entity_id: "gene.b2237"
entity_type: "gene"
name: "inaA"
source_database: "NCBI RefSeq"
source_id: "gene-b2237"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2237"
  - "inaA"
---

# inaA

`gene.b2237`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2237`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

inaA (gene.b2237) is a gene entity. It encodes inaA (protein.P27294). Encoded protein function: FUNCTION: May be an environmental sensor responsive to several stimuli, including internal pH, proton motive force, temperature, and possibly other unknown factors. EcoCyc product frame: EG11422-MONOMER. EcoCyc synonyms: yfaG. Genomic coordinates: 2348822-2349472. EcoCyc protein note: inaA was originally identified as a gene whose expression is induced in the presence of benzoate and other weak acids that are able to traverse the cell membrane, and is inversely correlated with growth temperatures between 30 and 45°C . Salicylate (via MarA), paraquat, hydrogen peroxide (via SoxS) , and dipyridyl (via Rob) increase inaA expression. InaA: "internal acid-inducible"

## Biological Role

Repressed by glaR (protein.P37338). Activated by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), soxS (protein.P0A9E2), marA (protein.P0ACH5), rob (protein.P0ACI0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27294|protein.P27294]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `S` - regulator=SoxS; target=inaA; function=+
- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=inaA; function=+
- `activates` <-- [[protein.P0ACI0|protein.P0ACI0]] `RegulonDB` `S` - regulator=Rob; target=inaA; function=+
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=inaA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007393,ECOCYC:EG11422,GeneID:946731`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2348822-2349472:-; feature_type=gene
