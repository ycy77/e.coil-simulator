---
entity_id: "gene.b3020"
entity_type: "gene"
name: "ygiS"
source_database: "NCBI RefSeq"
source_id: "gene-b3020"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3020"
  - "ygiS"
---

# ygiS

`gene.b3020`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3020`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygiS (gene.b3020) is a gene entity. It encodes ygiS (protein.Q46863). Encoded protein function: FUNCTION: Probably part of a deoxycholate transport system. Its expression in the presence of deoxycholate in a ygiS deletion mutant increases intracellular deoxycholate levels and decreases cell growth; higher expression in the presence of deoxycholate inhibits cell growth completely. Bile acid detergents such as deoxycholate are important for host defense against bacterial growth in the gall bladder and duodenum. {ECO:0000269|PubMed:25534751}. EcoCyc product frame: YGIS-MONOMER. Genomic coordinates: 3166111-3167718. EcoCyc protein note: YgiS has 44% identity with OppA - the periplasmic binding protein of an oligopeptide ABC transporter . The mRNA interferase, G7572-MONOMER "MqsR", degrades ygiS mRNA in vitro; ygiS mRNA contains 43 potential MqsR cleavage sites (5'GCU) . YgiS reduces cell fitness against deoxycholate; YgiS is associated with increased intracellular deoxycholate concentrations . In the Transporter Classification Database YgiS is annotated as a probable deoxycholate binding periplasmic protein that may interact with the membrane and ATP-binding components of the oligopeptide ABC transporter (OppBCDF) to mediate deoxycholate uptake . ygiS is upregulated under glucose-limited fed-batch conditions...

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46863|protein.Q46863]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009920,ECOCYC:G7570,GeneID:947140`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3166111-3167718:-; feature_type=gene
