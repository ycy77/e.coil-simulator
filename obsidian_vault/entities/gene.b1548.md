---
entity_id: "gene.b1548"
entity_type: "gene"
name: "nohA"
source_database: "NCBI RefSeq"
source_id: "gene-b1548"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1548"
  - "nohA"
---

# nohA

`gene.b1548`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1548`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nohA (gene.b1548) is a gene entity. It encodes nohA (protein.P31061). Encoded protein function: Prophage DNA-packing protein NohA (Prophage Qin DNA-packaging protein Nu1 homolog) EcoCyc product frame: EG11634-MONOMER. EcoCyc synonyms: nohQ. Genomic coordinates: 1635798-1636367. EcoCyc protein note: Transcription of nohA is regulated by Fur .

## Biological Role

Repressed by fur (protein.P0A9A9).

## Enriched Pathways

- `eco03258` Virion - Bacteriophage lambda (KEGG)

## Annotation

NCBI RefSeq gene feature

## Pathways

- `eco03258` Virion - Bacteriophage lambda (KEGG)

## Outgoing Edges (1)

- `encodes` --> [[protein.P31061|protein.P31061]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=nohA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005172,ECOCYC:EG11634,GeneID:946021`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1635798-1636367:-; feature_type=gene
