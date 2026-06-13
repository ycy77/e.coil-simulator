---
entity_id: "gene.b0185"
entity_type: "gene"
name: "accA"
source_database: "NCBI RefSeq"
source_id: "gene-b0185"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0185"
  - "accA"
---

# accA

`gene.b0185`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0185`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

accA (gene.b0185) is a gene entity. It encodes accA (protein.P0ABD5). Encoded protein function: FUNCTION: Component of the acetyl coenzyme A carboxylase (ACC) complex. First, biotin carboxylase catalyzes the carboxylation of biotin on its carrier protein (BCCP) and then the CO(2) group is transferred by the carboxyltransferase to acetyl-CoA to form malonyl-CoA. {ECO:0000255|HAMAP-Rule:MF_00823, ECO:0000269|PubMed:15066985}. EcoCyc product frame: CARBOXYL-TRANSFERASE-ALPHA-MONOMER. Genomic coordinates: 208621-209580. EcoCyc protein note: accA is an essential gene . Transcription of accA is growth rate-regulated . AccA: "acetyl-CoA carboxylase A"

## Biological Role

Activated by rpoD (protein.P00579), fadR (protein.P0A8V6).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABD5|protein.P0ABD5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=accA; function=+
- `activates` <-- [[protein.P0A8V6|protein.P0A8V6]] `RegulonDB` `S` - regulator=FadR; target=accA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000630,ECOCYC:EG11647,GeneID:944895`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:208621-209580:+; feature_type=gene
