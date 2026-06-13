---
entity_id: "protein.P0ADX9"
entity_type: "protein"
name: "rsmD"
source_database: "UniProt"
source_id: "P0ADX9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rsmD yhhF b3465 JW3430"
---

# rsmD

`protein.P0ADX9`

## Static

- Type: `protein`
- Source: `UniProt:P0ADX9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Specifically methylates the guanine in position 966 of 16S rRNA in the assembled 30S particle. {ECO:0000269|PubMed:17189261}. RsmD is the methyltransferase responsible for methylation of 16S rRNA at the N2 postion of the G966 nucleotide . Its substrate is the 16S ribosomal subunit, but not free unmethylated 16S rRNA . RsmD binds 30S ribosomal subunits with rRNA unmodified at G996 tightly . Binding of S7 and S19 together to 16S rRNA allows methylation by RsmD . Methylation of G966 and C967 in 16S rRNA appears to stabilize the binding of initiator tRNA to the 30S pre-initiation complex prior to recognition of the start codon, thus modulating the early stages of translation initiation . A crystal structure of RsmD has been solved at 2.05 Å resolution; the structure shows strong similarity to that of the RsmC methyltransferase . rsmD mutants appear to have no growth defect when grown alone, but have a modest effect on cell fitness in a growth competition assay . Deletion of rsmD alters the initiation frequency from certain translation initiation codons . Review:

## Biological Role

Catalyzes RXN0-6515 (reaction.ecocyc.RXN0-6515).

## Annotation

FUNCTION: Specifically methylates the guanine in position 966 of 16S rRNA in the assembled 30S particle. {ECO:0000269|PubMed:17189261}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-6515|reaction.ecocyc.RXN0-6515]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3465|gene.b3465]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADX9`
- `KEGG:ecj:JW3430;eco:b3465;ecoc:C3026_18770;`
- `GeneID:93778526;947977;`
- `GO:GO:0003676; GO:0052913; GO:0070475`
- `EC:2.1.1.171`

## Notes

Ribosomal RNA small subunit methyltransferase D (EC 2.1.1.171) (16S rRNA m2G966 methyltransferase) (rRNA (guanine-N(2)-)-methyltransferase)
