---
entity_id: "gene.b2702"
entity_type: "gene"
name: "srlA"
source_database: "NCBI RefSeq"
source_id: "gene-b2702"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2702"
  - "srlA"
---

# srlA

`gene.b2702`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2702`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

srlA (gene.b2702) is a gene entity. It encodes srlA (protein.P56579). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitant with their translocation across the cell membrane. The enzyme II complex composed of SrlA, SrlB and SrlE is involved in glucitol/sorbitol transport. It can also use D-mannitol. {ECO:0000269|PubMed:1100608}. EcoCyc product frame: G8210-MONOMER. EcoCyc synonyms: gutA, sbl, srlA-1. Genomic coordinates: 2825832-2826395. EcoCyc protein note: Contains PTS enzyme IIC2 (IIC-N) domain . SrlA is predicted to contain 3 transmembrane helices; the C-terminus is located in the cytoplasm . srlA belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12 .

## Biological Role

Repressed by spf (gene.b3864). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P56579|protein.P56579]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=srlA; function=+
- `represses` <-- [[gene.b3864|gene.b3864]] `RegulonDB` `S` - regulator=Spf; target=srlA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008890,ECOCYC:G8210,GeneID:947575`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2825832-2826395:+; feature_type=gene
