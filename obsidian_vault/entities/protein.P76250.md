---
entity_id: "protein.P76250"
entity_type: "protein"
name: "dmlR"
source_database: "UniProt"
source_id: "P76250"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dmlR yeaT b1799 JW1788"
---

# dmlR

`protein.P76250`

## Static

- Type: `protein`
- Source: `UniProt:P76250`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Transcriptional regulator required for the aerobic growth on D-malate as the sole carbon source. Induces the expression of dmlA in response to D-malate or L- or meso-tartrate. Negatively regulates its own expression. {ECO:0000269|PubMed:17088549, ECO:0000269|PubMed:20233924}. DmlR (D-malate degradation regulator), formerly known as YeaT , is required for growth on D-malate as the sole carbon source under high-throughput growth conditions with limited aeration . DmlR is a LysR-type transcriptional regulator and has 49% sequence identity and 67% similarity with TtdR . Induction of dmlA by DmlR requires the presence of D-malate or L- or meso-tartate, but only D-malate supports aerobic growth . The expression of dmlR is subject to negative autoregulation independently of DcuS-DcuS and TtdR . DmlR was transcriptionally upregulated in iron excess over iron limitation at 63% dissolved oxygen as determined by RNA-seq . The DmlR binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding energy matrix and genomic binding profiles can be accessed at boltznet.bu.edu .

## Annotation

FUNCTION: Transcriptional regulator required for the aerobic growth on D-malate as the sole carbon source. Induces the expression of dmlA in response to D-malate or L- or meso-tartrate. Negatively regulates its own expression. {ECO:0000269|PubMed:17088549, ECO:0000269|PubMed:20233924}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b1799|gene.b1799]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76250`
- `KEGG:ecj:JW1788;eco:b1799;ecoc:C3026_10255;`
- `GeneID:946316;`
- `GO:GO:0003700; GO:0006108; GO:0006351; GO:0043565; GO:0045892; GO:0045893`

## Notes

HTH-type transcriptional regulator DmlR (D-malate degradation protein R)
