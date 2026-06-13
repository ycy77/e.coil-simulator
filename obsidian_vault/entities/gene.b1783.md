---
entity_id: "gene.b1783"
entity_type: "gene"
name: "yeaG"
source_database: "NCBI RefSeq"
source_id: "gene-b1783"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1783"
  - "yeaG"
---

# yeaG

`gene.b1783`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1783`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yeaG (gene.b1783) is a gene entity. It encodes yeaG (protein.P0ACY3). Encoded protein function: FUNCTION: Kinase that plays a role in the adaptation to sustained nitrogen starvation (PubMed:26621053). May act by indirectly repressing the transcription of the two toxin/antitoxin modules mqsR/mqsA and dinJ/yafQ, which positively impacts the expression of rpoS, the master regulator of the general bacterial stress response (PubMed:26621053). In vitro, can phosphorylate the isocitrate lyase AceA only in the presence of malate, suggesting that it may play a role during glucose to malate shift (PubMed:33889145). Displays autokinase and casein kinase activities in vitro (PubMed:18276156). It can also phosphorylate specifically a 65 kDa unidentified cytoplasmic protein (Ref.5). {ECO:0000269|PubMed:18276156, ECO:0000269|PubMed:26621053, ECO:0000269|PubMed:33889145, ECO:0000269|Ref.5}. EcoCyc product frame: G6969-MONOMER. Genomic coordinates: 1866908-1868842. EcoCyc protein note: YeaG plays a role in the adaptation to sustained nitrogen (N) starvation . YeaG is a member of the PrkA family of serine protein kinases. Purified YeaG has autokinase and casein kinase activity . YeaG may phosphorylate an unknown 65 kDa cytoplasmic protein...

## Biological Role

Repressed by sdsR (gene.b4433). Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACY3|protein.P0ACY3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[gene.b4433|gene.b4433]] `RegulonDB` `S` - regulator=SdsR; target=yeaG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005935,ECOCYC:G6969,GeneID:946297`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1866908-1868842:+; feature_type=gene
