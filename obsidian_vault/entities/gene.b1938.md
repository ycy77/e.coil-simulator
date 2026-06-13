---
entity_id: "gene.b1938"
entity_type: "gene"
name: "fliF"
source_database: "NCBI RefSeq"
source_id: "gene-b1938"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1938"
  - "fliF"
---

# fliF

`gene.b1938`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1938`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fliF (gene.b1938) is a gene entity. It encodes fliF (protein.P25798). Encoded protein function: FUNCTION: The M ring may be actively involved in energy transduction. EcoCyc product frame: FLIF-FLAGELLAR-MS-RING. EcoCyc synonyms: flaAII.1, flaBI. Genomic coordinates: 2013229-2014887. EcoCyc protein note: fliF encodes a flagellar protein that polymerizes to form the MS (membrane/supramembrane) ring of the flagellar basal body; together with the C (cytoplasmic ring) consisting of FliG, FliM and FliN proteins, the MS-C ring complex functions as the reversible rotor of the flagella motor. FliF is widely studied in Salmonella typhimurium however the characterization is considered to apply to the homologous protein in E. coli.The two proteins are 85% identitical over their entire length . In Salmonella typhimurium, the MS ring is an inner membrane structure consisting of approximately 26 subunits of FliF; the MS ring is the base of the flagella structure and serves as the 'housing' for the protein export apparatus that is required for construction of the flagella; at its cytoplasmic face the MS ring interacts with the upper C ring protein FliG and this interface is an essential component of flagella motor function . An E...

## Biological Role

Repressed by pdeL (protein.P21514), csgD (protein.P52106). Activated by FlhDC DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-3930).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25798|protein.P25798]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.CPLX0-3930|complex.ecocyc.CPLX0-3930]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P21514|protein.P21514]] `RegulonDB` `S` - regulator=PdeL; target=fliF; function=-
- `represses` <-- [[protein.P52106|protein.P52106]] `RegulonDB` `S` - regulator=CsgD; target=fliF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006454,ECOCYC:EG11347,GeneID:946448`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2013229-2014887:+; feature_type=gene
