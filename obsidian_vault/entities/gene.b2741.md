---
entity_id: "gene.b2741"
entity_type: "gene"
name: "rpoS"
source_database: "NCBI RefSeq"
source_id: "gene-b2741"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2741"
  - "rpoS"
---

# rpoS

`gene.b2741`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2741`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpoS (gene.b2741) is a gene entity. It encodes rpoS (protein.P13445). Encoded protein function: FUNCTION: Sigma factors are initiation factors that promote the attachment of RNA polymerase to specific initiation sites and are then released. This sigma factor is the master transcriptional regulator of the stationary phase and the general stress response. Controls, positively or negatively, the expression of several hundred genes, which are mainly involved in metabolism, transport, regulation and stress management. {ECO:0000255|HAMAP-Rule:MF_00959, ECO:0000269|PubMed:15558318, ECO:0000269|PubMed:15716429, ECO:0000269|PubMed:16511888, ECO:0000269|PubMed:21398637, ECO:0000269|PubMed:8475100}.; FUNCTION: Protects stationary phase cells from killing induced by endoribonuclease MazF. {ECO:0000269|PubMed:19251848}. EcoCyc product frame: RPOS-MONOMER. EcoCyc synonyms: sigS, otsX, abrD, appR, csi2, dpeB, katF, nur. Genomic coordinates: 2866559-2867551. EcoCyc protein note: rpoS encodes the alternative sigma factor σS, a subunit of RNA polymerase that acts as the master regulator of the general stress response in E. coli. Genome-wide analyses of RpoS-dependent gene expression showed that up to 10% of the genes in E. coli are under direct or indirect control of σS...

## Biological Role

Repressed by cyaR (gene.b4438), arcA (protein.P0A9Q1), crp (protein.P0ACJ8), mqsA (protein.Q46864). Activated by rprA (gene.b4431), arcZ (gene.b4450), rpoD (protein.P00579), torR (protein.P38684), DNA-binding transcriptional dual regulator TorR-phosphorylated (protein.ecocyc.PHOSPHO-TORR).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P13445|protein.P13445]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (9)

- `activates` <-- [[gene.b4431|gene.b4431]] `RegulonDB` `S` - regulator=RprA; target=rpoS; function=+
- `activates` <-- [[gene.b4450|gene.b4450]] `RegulonDB` `S` - regulator=ArcZ; target=rpoS; function=+
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rpoS; function=+
- `activates` <-- [[protein.P38684|protein.P38684]] `RegulonDB` `C` - regulator=TorR; target=rpoS; function=+
- `activates` <-- [[protein.ecocyc.PHOSPHO-TORR|protein.ecocyc.PHOSPHO-TORR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[gene.b4438|gene.b4438]] `RegulonDB` `S` - regulator=CyaR; target=rpoS; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=rpoS; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=rpoS; function=-
- `represses` <-- [[protein.Q46864|protein.Q46864]] `RegulonDB` `C` - regulator=MqsA; target=rpoS; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009001,ECOCYC:EG10510,GeneID:947210`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2866559-2867551:-; feature_type=gene
