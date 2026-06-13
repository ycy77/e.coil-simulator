---
entity_id: "gene.b2247"
entity_type: "gene"
name: "rhmD"
source_database: "NCBI RefSeq"
source_id: "gene-b2247"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2247"
  - "rhmD"
---

# rhmD

`gene.b2247`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2247`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rhmD (gene.b2247) is a gene entity. It encodes rhmD (protein.P77215). Encoded protein function: FUNCTION: Catalyzes the dehydration of L-rhamnonate to 2-keto-3-deoxy-L-rhamnonate (KDR). Can also dehydrate L-lyxonate, L-mannonate and D-gulonate, although less efficiently, but not 2-keto-4-hydroxyheptane-1,7-dioate. {ECO:0000269|PubMed:18754693}. EcoCyc product frame: G7160-MONOMER. EcoCyc synonyms: yfaW. Genomic coordinates: 2360209-2361414. EcoCyc protein note: YfaW is a L-rhamnonate dehydratase (RhamD) with promiscuous substrate specificity . RhamD is a member of the mandelate racemase (MR) subgroup of the enolase superfamily. A crystal structure has been solved at 2.1 Å resolution, where the enzyme is a tetramer of dimers. Although the enzyme is also an octamer in solution, based on the location of the active site, the minimum functional unit appears to be the monomer. A reaction mechanism and likely catalytic residues have been proposed, and site-directed mutants were assayed to confirm lack of activity .

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77215|protein.P77215]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007436,ECOCYC:G7160,GeneID:945881`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2360209-2361414:-; feature_type=gene
