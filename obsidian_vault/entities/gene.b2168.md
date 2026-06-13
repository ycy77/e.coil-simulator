---
entity_id: "gene.b2168"
entity_type: "gene"
name: "fruK"
source_database: "NCBI RefSeq"
source_id: "gene-b2168"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2168"
  - "fruK"
---

# fruK

`gene.b2168`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2168`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fruK (gene.b2168) is a gene entity. It encodes fruK (protein.P0AEW9). Encoded protein function: FUNCTION: Catalyzes the ATP-dependent phosphorylation of fructose-l-phosphate to fructose-l,6-bisphosphate (PubMed:10833389, Ref.6). Is specific for fructose-l-phosphate (Ref.6). GTP, UTP and CTP can also function as phosphoryl donors showing 60%, 20% and 10% of the activity of ATP (Ref.6). {ECO:0000269|PubMed:10833389, ECO:0000269|Ref.6}. EcoCyc product frame: 1-PFK-MONOMER. EcoCyc synonyms: fpk. Genomic coordinates: 2261427-2262365. EcoCyc protein note: 1-phosphofructokinase is essential for the utilization of fructose as a carbon source. The enzyme is highly specific for fructose-1-phosphate . FruK has some sequence similarity to the minor form of 6-phosphofructokinase (PfkB), but not the major form (PfkA) . FruK belongs to the ribokinase family of sugar kinases . A fruK mutant is unable to grow on fructose or fructose-1-phosphate as the sole source of carbon . A ΔfruK mutant results in increased lag phase when grown on preferred carbon sources, and increased growth delays on non-preferred carbon sources, such as glycerol . FruK can carry out the reverse reaction to form fructose-1-phosphate (F1P) from physiological concentrations of fructose-1,6-bisphosphate (FBP), thus creating the effector molecule of PD00521...

## Biological Role

Repressed by cra (protein.P0ACP1).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEW9|protein.P0AEW9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=fruK; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007174,ECOCYC:EG10337,GeneID:946676`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2261427-2262365:-; feature_type=gene
