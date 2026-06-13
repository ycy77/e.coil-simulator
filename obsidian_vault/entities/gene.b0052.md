---
entity_id: "gene.b0052"
entity_type: "gene"
name: "pdxA"
source_database: "NCBI RefSeq"
source_id: "gene-b0052"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0052"
  - "pdxA"
---

# pdxA

`gene.b0052`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0052`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pdxA (gene.b0052) is a gene entity. It encodes pdxA (protein.P19624). Encoded protein function: FUNCTION: Catalyzes the NAD(P)-dependent oxidation of 4-(phosphooxy)-L-threonine (HTP) into 2-amino-3-oxo-4-(phosphooxy)butyric acid which spontaneously decarboxylates to form 3-amino-2-oxopropyl phosphate (AHAP). {ECO:0000255|HAMAP-Rule:MF_00536, ECO:0000269|PubMed:15026039, ECO:0000269|Ref.5}. EcoCyc product frame: PDXA-MONOMER. Genomic coordinates: 52427-53416.

## Biological Role

Repressed by glaR (protein.P37338).

## Enriched Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P19624|protein.P19624]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=pdxA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000178,ECOCYC:EG10691,GeneID:944919`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:52427-53416:-; feature_type=gene
