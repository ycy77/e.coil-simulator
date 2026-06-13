---
entity_id: "protein.P36929"
entity_type: "protein"
name: "rsmB"
source_database: "UniProt"
source_id: "P36929"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rsmB fmu/fmv rrmB sun yhdB b3289 JW3250"
---

# rsmB

`protein.P36929`

## Static

- Type: `protein`
- Source: `UniProt:P36929`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Specifically methylates the cytosine at position 967 (m5C967) of 16S rRNA (PubMed:10026269, PubMed:10194318). It recognizes protein-free synthetic 16S RNA as a substrate (PubMed:10026269). {ECO:0000269|PubMed:10026269, ECO:0000269|PubMed:10194318}. RsmB is the methyltransferase responsible for methylation of 16S rRNA at the C967 nucleotide . In vitro, the enzyme is active on free 16S rRNA, but not 30S ribosomal subunits . Methylation of G966 and C967 in 16S rRNA appears to stabilize the binding of initiator tRNA to the 30S pre-initiation complex prior to recognition of the start codon, thus modulating the early stages of translation initiation . The crystal structure of the apoenzyme has been solved at 1.65 Å resolution, and that of the enzyme complexed with AdoMet at 2.1 Å resolution . A null mutation in rsmB has no significant effect on the growth rate in rich or minimal media , although competitive growth experiments reveal a fitness defect . Deletion of rsmB alters the initiation frequency from certain translation initiation codons . A C375A mutant is catalytically inactive, while a C325A mutant retains activity . RsmB: "rRNA small subunit methyltransferase B" Review:

## Biological Role

Catalyzes RXN-11591 (reaction.ecocyc.RXN-11591).

## Annotation

FUNCTION: Specifically methylates the cytosine at position 967 (m5C967) of 16S rRNA (PubMed:10026269, PubMed:10194318). It recognizes protein-free synthetic 16S RNA as a substrate (PubMed:10026269). {ECO:0000269|PubMed:10026269, ECO:0000269|PubMed:10194318}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11591|reaction.ecocyc.RXN-11591]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3289|gene.b3289]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P36929`
- `KEGG:ecj:JW3250;eco:b3289;ecoc:C3026_17880;`
- `GeneID:947789;`
- `GO:GO:0003723; GO:0005829; GO:0006355; GO:0009383; GO:0070475`
- `EC:2.1.1.176`

## Notes

Ribosomal RNA small subunit methyltransferase B (EC 2.1.1.176) (16S rRNA m5C967 methyltransferase) (rRNA (cytosine-C(5)-)-methyltransferase RsmB)
