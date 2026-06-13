---
entity_id: "protein.P0A6Y8"
entity_type: "protein"
name: "dnaK"
source_database: "UniProt"
source_id: "P0A6Y8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:16079137}. Cell inner membrane {ECO:0000269|PubMed:16079137}; Peripheral membrane protein {ECO:0000269|PubMed:16079137}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dnaK groP grpF seg b0014 JW0013"
---

# dnaK

`protein.P0A6Y8`

## Static

- Type: `protein`
- Source: `UniProt:P0A6Y8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:16079137}. Cell inner membrane {ECO:0000269|PubMed:16079137}; Peripheral membrane protein {ECO:0000269|PubMed:16079137}.

## Enriched Summary

FUNCTION: Plays an essential role in the initiation of phage lambda DNA replication, where it acts in an ATP-dependent fashion with the DnaJ protein to release lambda O and P proteins from the preprimosomal complex. DnaK is also involved in chromosomal DNA replication, possibly through an analogous interaction with the DnaA protein. Also participates actively in the response to hyperosmotic shock. DnaK is a Hsp70 (heat shock protein 70 kDa) chaperone. It assists in a number of cytoplasmic cellular processes involved in a "protein quality control" network, including folding of nascent polypeptide chains , rescue of misfolded proteins and protein secretion . The chaperone action of DnaK is powered by ATP hydrolysis and assisted by partner chaperones CPLX0-8191 "DnaJ", EG12193-MONOMER CbpA, EG11570-MONOMER DjlA and the nucleotide exchange factor CPLX0-8192 "GrpE". The DnaK system contributes to control of the heat shock response in E. coli through its interaction with RPOH-MONOMER "σ32", the primary sigma factor controlling heat shock response during log phase growth (reviewed in ). The DnaK chaperone system is also essential for bacteriophage λ DNA replication and is involved in the formation and disassembly of the initiation complex at the viral origin of replication ori-λ...

## Biological Role

Catalyzes RXN0-1061 (reaction.ecocyc.RXN0-1061).

## Enriched Pathways

- `eco03018` RNA degradation (KEGG)

## Annotation

FUNCTION: Plays an essential role in the initiation of phage lambda DNA replication, where it acts in an ATP-dependent fashion with the DnaJ protein to release lambda O and P proteins from the preprimosomal complex. DnaK is also involved in chromosomal DNA replication, possibly through an analogous interaction with the DnaA protein. Also participates actively in the response to hyperosmotic shock.

## Pathways

- `eco03018` RNA degradation (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1061|reaction.ecocyc.RXN0-1061]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0014|gene.b0014]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6Y8`
- `KEGG:ecj:JW0013;eco:b0014;`
- `GeneID:86862530;93777429;944750;`
- `GO:GO:0005524; GO:0005737; GO:0005829; GO:0005886; GO:0006260; GO:0006457; GO:0008270; GO:0009408; GO:0016020; GO:0016234; GO:0016887; GO:0016989; GO:0031072; GO:0032991; GO:0034620; GO:0042026; GO:0043335; GO:0043531; GO:0044183; GO:0051082; GO:0051087; GO:0065003; GO:0140662; GO:1990169`

## Notes

Chaperone protein DnaK (HSP70) (Heat shock 70 kDa protein) (Heat shock protein 70)
