---
entity_id: "gene.b0914"
entity_type: "gene"
name: "msbA"
source_database: "NCBI RefSeq"
source_id: "gene-b0914"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0914"
  - "msbA"
---

# msbA

`gene.b0914`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0914`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

msbA (gene.b0914) is a gene entity. It encodes msbA (protein.P60752). Encoded protein function: FUNCTION: Involved in lipopolysaccharide (LPS) biosynthesis. Translocates lipid A-core from the inner to the outer leaflet of the inner membrane (PubMed:12119303, PubMed:15304478, PubMed:28869968, PubMed:8809774, PubMed:9575204). Transmembrane domains (TMD) form a pore in the inner membrane and the ATP-binding domain (NBD) is responsible for energy generation (PubMed:12119303). Shows ATPase activity (PubMed:12119303, PubMed:18024585, PubMed:18344567, PubMed:19132955, PubMed:20412049, PubMed:21462989). May transport glycerophospholipids (PubMed:9575204). In proteoliposomes, mediates the ATP-dependent flipping of a variety of phospholipid and glycolipid derivatives (PubMed:20412049). May also function as a multidrug transporter (PubMed:19132955). {ECO:0000269|PubMed:12119303, ECO:0000269|PubMed:15304478, ECO:0000269|PubMed:18024585, ECO:0000269|PubMed:18344567, ECO:0000269|PubMed:19132955, ECO:0000269|PubMed:20412049, ECO:0000269|PubMed:21462989, ECO:0000269|PubMed:28869968, ECO:0000269|PubMed:8809774, ECO:0000269|PubMed:9575204}. EcoCyc product frame: EG10613-MONOMER. Genomic coordinates: 966621-968369...

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P60752|protein.P60752]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003113,ECOCYC:EG10613,GeneID:945530`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:966621-968369:+; feature_type=gene
