---
entity_id: "gene.b1594"
entity_type: "gene"
name: "mlc"
source_database: "NCBI RefSeq"
source_id: "gene-b1594"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1594"
  - "mlc"
---

# mlc

`gene.b1594`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1594`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mlc (gene.b1594) is a gene entity. It encodes mlc (protein.P50456). Encoded protein function: FUNCTION: Global regulator of carbohydrate metabolism (PubMed:10464268, PubMed:11361067, PubMed:11934616, PubMed:9484892, PubMed:9484893, PubMed:9781886). Represses the expression of several genes involved in sugar transport and utilization, in particular phosphoenolpyruvate-carbohydrate phosphotransferase system (PTS) genes (PubMed:10464268, PubMed:9484892, PubMed:9484893, PubMed:9781886). Represses expression of ptsG (EIICB(Glc)), which encodes the PTS system glucose-specific EIICB component (PubMed:9781886). Also represses the expression of the manXYZ operon, encoding the mannose-specific PTS system, expression of malT, encoding the transcriptional activator of the maltose regulon, and expression of the pts operon, composed of the genes ptsH, ptsI and crr (PubMed:10464268, PubMed:9484892, PubMed:9484893). Represses its own expression (PubMed:9484893). Acts by binding to the regulatory region of the target genes (PubMed:10464268, PubMed:9484893, PubMed:9781886). {ECO:0000269|PubMed:10464268, ECO:0000269|PubMed:11361067, ECO:0000269|PubMed:11934616, ECO:0000269|PubMed:9484892, ECO:0000269|PubMed:9484893, ECO:0000269|PubMed:9781886}. EcoCyc product frame: PD01896. EcoCyc synonyms: dgsA. Genomic coordinates: 1667344-1668564...

## Biological Role

Repressed by mlc (protein.P50456). Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P50456|protein.P50456]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mlc; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=mlc; function=+
- `represses` <-- [[protein.P50456|protein.P50456]] `RegulonDB` `S` - regulator=Mlc; target=mlc; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005323,ECOCYC:G6852,GeneID:945510`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1667344-1668564:-; feature_type=gene
