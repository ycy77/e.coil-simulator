---
entity_id: "gene.b4364"
entity_type: "gene"
name: "yjjP"
source_database: "NCBI RefSeq"
source_id: "gene-b4364"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4364"
  - "yjjP"
---

# yjjP

`gene.b4364`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4364`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjjP (gene.b4364) is a gene entity. It encodes yjjP (protein.P0ADD5). Encoded protein function: FUNCTION: Involved in succinate export with YjjB. Both proteins are required for export (PubMed:28673128). Contributes to succinate production under both aerobic and anaerobic conditions (PubMed:28673128). {ECO:0000269|PubMed:28673128}. EcoCyc product frame: G7946-MONOMER. Genomic coordinates: 4602088-4602858. EcoCyc protein note: yjjP and yjjB are implicated in succinate export. Deletion of these genes in an E. coli K-12 strain that has been engineered for anaerobic succinate production decreases succinate production significantly; heterologous expression of these genes in an engineered strain of Pantoea ananatis enhances succinate production under aerobic conditions; heterologous expression of these genes in an engineered strain of Corynebacterium glutamicum restores succinate production under anaerobic conditions . YjjP contains 5 predicted transmembrane regions, YjjB contains 4 predicted transmembrane regions and together these proteins may constitute a 'split-type' ThrE family transporter . Based on a high-throughput reporter assay, the carboxy-terminus of YjjP is in the periplasm . Homologs of YjjP and YjjB are present in other gram-negative succinate producing species such as Enterobacter aerogenes, Actinobacillus succinogenes and Mannheimia succiniciproducens .

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADD5|protein.P0ADD5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=yjjP; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=yjjP; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014313,ECOCYC:G7946,GeneID:948812`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4602088-4602858:-; feature_type=gene
