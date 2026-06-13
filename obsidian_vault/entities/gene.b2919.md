---
entity_id: "gene.b2919"
entity_type: "gene"
name: "scpB"
source_database: "NCBI RefSeq"
source_id: "gene-b2919"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2919"
  - "scpB"
---

# scpB

`gene.b2919`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2919`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

scpB (gene.b2919) is a gene entity. It encodes scpB (protein.P52045). Encoded protein function: FUNCTION: Catalyzes the decarboxylation of (R)-methylmalonyl-CoA to propionyl-CoA. Could be part of a pathway that converts succinate to propanoate. {ECO:0000269|PubMed:10769117}. EcoCyc product frame: G7516-MONOMER. EcoCyc synonyms: ygfG. Genomic coordinates: 3063993-3064778. EcoCyc protein note: Methylmalonyl-CoA decarboxylase is a biotin-independent enzyme that catalyzes the decarboxylation of methylmalonyl-CoA to propionyl-CoA. This reaction is suggested to be part of a pathway of succinate decarboxylation whose metabolic function is unknown . Crystal structures of the enzyme alone and in complex with an inert analog of methylmalonyl-CoA have been solved; the monomers are arranged in a dimer of trimers in the crystal. Unlike other members of this family of enzymes, active sites are not shared between monomers. A reaction mechanism was proposed . Overexpression of scpB reduces heterologous production of 6-deoxyerythronolide B (6dEB), the macrolactone precursor of erythromycin . Review:

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52045|protein.P52045]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=scpB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009581,ECOCYC:G7516,GeneID:947408`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3063993-3064778:+; feature_type=gene
