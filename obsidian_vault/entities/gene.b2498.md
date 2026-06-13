---
entity_id: "gene.b2498"
entity_type: "gene"
name: "upp"
source_database: "NCBI RefSeq"
source_id: "gene-b2498"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2498"
  - "upp"
---

# upp

`gene.b2498`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2498`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

upp (gene.b2498) is a gene entity. It encodes upp (protein.P0A8F0). Encoded protein function: FUNCTION: Catalyzes the conversion of uracil and 5-phospho-alpha-D-ribose 1-diphosphate (PRPP) to UMP and diphosphate. EcoCyc product frame: URACIL-PRIBOSYLTRANS-MONOMER. EcoCyc synonyms: uraP. Genomic coordinates: 2620246-2620872.

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8F0|protein.P0A8F0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=upp; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=upp; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008224,ECOCYC:EG11332,GeneID:946979`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2620246-2620872:-; feature_type=gene
