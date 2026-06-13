---
entity_id: "gene.b3073"
entity_type: "gene"
name: "patA"
source_database: "NCBI RefSeq"
source_id: "gene-b3073"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3073"
  - "patA"
---

# patA

`gene.b3073`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3073`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

patA (gene.b3073) is a gene entity. It encodes patA (protein.P42588). Encoded protein function: FUNCTION: Catalyzes the aminotransferase reaction from putrescine to 2-oxoglutarate, leading to glutamate and 4-aminobutanal, which spontaneously cyclizes to form 1-pyrroline (PubMed:12617754, PubMed:3510672). This is the first step in one of two pathways for putrescine degradation, where putrescine is converted into 4-aminobutanoate (gamma-aminobutyrate or GABA) via 4-aminobutanal, which allows E.coli to grow on putrescine as the sole nitrogen source (PubMed:22636776, PubMed:3510672). Also functions as a cadaverine transaminase in a a L-lysine degradation pathway to succinate that proceeds via cadaverine, glutarate and L-2-hydroxyglutarate (PubMed:12617754, PubMed:30498244). Is also able to transaminate spermidine, in lower extent, but not ornithine. Alpha-ketobutyrate and pyruvate can also act as amino acceptors, although much less efficiently (PubMed:12617754). {ECO:0000269|PubMed:12617754, ECO:0000269|PubMed:22636776, ECO:0000269|PubMed:30498244, ECO:0000269|PubMed:3510672}. EcoCyc product frame: G7596-MONOMER. EcoCyc synonyms: oat, pat, ygjG. Genomic coordinates: 3219494-3220873.

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by lrp (protein.P0ACJ0), glnG (protein.P0AFB8), rpoS (protein.P13445), rpoN (protein.P24255).

## Enriched Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P42588|protein.P42588]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=patA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=patA; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=patA; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010092,ECOCYC:G7596,GeneID:947120`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3219494-3220873:+; feature_type=gene
