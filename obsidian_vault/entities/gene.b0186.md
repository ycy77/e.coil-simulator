---
entity_id: "gene.b0186"
entity_type: "gene"
name: "ldcC"
source_database: "NCBI RefSeq"
source_id: "gene-b0186"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0186"
  - "ldcC"
---

# ldcC

`gene.b0186`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0186`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ldcC (gene.b0186) is a gene entity. It encodes ldcC (protein.P52095). Encoded protein function: FUNCTION: Plays a role in lysine utilization by acting as a lysine decarboxylase. {ECO:0000269|PubMed:9339543}. EcoCyc product frame: LDC2-MONOMER. EcoCyc synonyms: ldc, ldcH. Genomic coordinates: 209679-211820. EcoCyc protein note: There are two lysine decarboxylases in E. coli, encoded by the cadA and ldcC genes. The ldcC gene product, lysine decarboxylase 2 (LdcC), differs from the cadA-encoded enzyme in that it is weakly expressed, is more thermosensitive and has activity over a broad range of pH with a higher pH optimum than CadA . A 3D cryo-EM reconstruction of LdcC has been compared to that of CadA; the C-terminal β-sheet provides a sequence signature that allows classification of enzymes into LdcC-like vs. CadA-like and explains why only CadA, but not LdcC, can interact with RavA . ldcC is expressed at very low levels and shows RpoS-dependent induction during stationary phase . The alarmone (p)ppGpp inhibits LdcC activity . Expression of ldcC is downregulated under simulated microgravity conditions . A mutant that is missing all eight genes involved in polyamine biosynthesis, ΔspeABCDEF cadA ldcC, grows aerobically at a reduced rate. However, polyamines are required for growth under anaerobic conditions and at very high oxygen levels...

## Biological Role

Repressed by glaR (protein.P37338).

## Enriched Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52095|protein.P52095]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ldcC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000633,ECOCYC:G6094,GeneID:944887`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:209679-211820:+; feature_type=gene
