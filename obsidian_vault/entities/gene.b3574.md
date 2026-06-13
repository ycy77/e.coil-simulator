---
entity_id: "gene.b3574"
entity_type: "gene"
name: "plaR"
source_database: "NCBI RefSeq"
source_id: "gene-b3574"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3574"
  - "plaR"
---

# plaR

`gene.b3574`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3574`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

plaR (gene.b3574) is a gene entity. It encodes plaR (protein.P37671). Encoded protein function: FUNCTION: Transcription factor involved in the utilization of L-ascorbate (PubMed:30137486, PubMed:31892694). Negatively controls the transcription of the yiaKLMNOPQRS (yiaK-S or yiaK-yiaL-yiaM-yiaN-yiaO-lyxK-sgbH-sgbU-sgbE) operon, which is involved in the L-ascorbate degradation pathway (PubMed:10913096, PubMed:30137486). It may repress the ascorbate utilization pathway, therefore regulating the level of D-xylulose-5-phosphate that feeds into the pentose phosphate pathway (PubMed:30137486). It is involved in the utilization of plant-derived materials as nutrients for survival, including ascorbate from fruits and galacturonate from plant pectin (PubMed:31892694). In addition, the targets include genes involved in the utilization of other plant-derived materials as nutrients such as fructose, sorbitol, glycerol and fructoselysine (PubMed:31892694). Acts by binding to specific DNA sequences (PlaR-box) in the promoter regions of target operons, repressing their transcription (PubMed:10913096, PubMed:31892694). {ECO:0000269|PubMed:10913096, ECO:0000269|PubMed:30137486, ECO:0000269|PubMed:31892694}. EcoCyc product frame: EG12278-MONOMER. EcoCyc synonyms: yiaJ. Genomic coordinates: 3741684-3742532...

## Biological Role

Repressed by crp (protein.P0ACJ8), plaR (protein.P37671). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37671|protein.P37671]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=plaR; function=+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=plaR; function=-
- `represses` <-- [[protein.P37671|protein.P37671]] `RegulonDB` `C` - regulator=PlaR; target=plaR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011677,ECOCYC:EG12278,GeneID:948084`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3741684-3742532:-; feature_type=gene
