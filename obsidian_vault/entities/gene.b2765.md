---
entity_id: "gene.b2765"
entity_type: "gene"
name: "queD"
source_database: "NCBI RefSeq"
source_id: "gene-b2765"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2765"
  - "queD"
---

# queD

`gene.b2765`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2765`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

queD (gene.b2765) is a gene entity. It encodes queD (protein.P65870). Encoded protein function: FUNCTION: Catalyzes the conversion of 7,8-dihydroneopterin triphosphate (H2NTP) to 6-carboxy-5,6,7,8-tetrahydropterin (CPH4) and acetaldehyde. Can also convert 6-pyruvoyltetrahydropterin (PPH4) and sepiapterin to CPH4; these 2 compounds are probably intermediates in the reaction from H2NTP. {ECO:0000269|PubMed:19231875}. EcoCyc product frame: G7431-MONOMER. EcoCyc synonyms: ygcM, sscR. Genomic coordinates: 2892214-2892579.

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P65870|protein.P65870]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=queD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009068,ECOCYC:G7431,GeneID:945123`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2892214-2892579:+; feature_type=gene
