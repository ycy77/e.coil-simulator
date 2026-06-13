---
entity_id: "gene.b3599"
entity_type: "gene"
name: "mtlA"
source_database: "NCBI RefSeq"
source_id: "gene-b3599"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3599"
  - "mtlA"
---

# mtlA

`gene.b3599`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3599`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mtlA (gene.b3599) is a gene entity. It encodes mtlA (protein.P00550). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. This system is involved in D-mannitol transport (PubMed:2123863, PubMed:368051, PubMed:6427236). Also able to use D-mannonic acid (PubMed:6427236). {ECO:0000269|PubMed:2123863, ECO:0000269|PubMed:368051, ECO:0000269|PubMed:6427236}. EcoCyc product frame: MTLA-MONOMER. EcoCyc synonyms: mtlC. Genomic coordinates: 3772281-3774194.

## Biological Role

Repressed by fis (protein.P0A6R3). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00550|protein.P00550]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=mtlA; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=mtlA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011761,ECOCYC:EG10615,GeneID:948118`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3772281-3774194:+; feature_type=gene
