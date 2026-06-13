---
entity_id: "protein.P31545"
entity_type: "protein"
name: "efeB"
source_database: "UniProt"
source_id: "P31545"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:16551627}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "efeB ycdB b1019 JW1004"
---

# efeB

`protein.P31545`

## Static

- Type: `protein`
- Source: `UniProt:P31545`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:16551627}.

## Enriched Summary

FUNCTION: Involved in the recovery of exogenous heme iron. Extracts iron from heme while preserving the protoporphyrin ring intact. Also displays peroxidase activity on guaiacol in vitro. {ECO:0000269|PubMed:16551627, ECO:0000269|PubMed:19564607}. efeB is predicted to encode a periplasmic component of a ferrous iron transport system (see ) that is cryptic in E. coli K-12; EfeB is implicated in exogenous heme iron acquisition. Analysis of transcriptional efe-lacZ fusions suggest that efeB does not possess a proximal promoter and is co-transcribed with efeUO . efeU in E. coli K-12 is disrupted by a frameshift mutation leaving the efeU_1 and efeU_2 fragments nonfunctional; EfeB (and EfeO) are produced despite the frameshift mutation . The functional efeU (ycdN) gene in E. coli Nissle 1917 encodes an oxidase-dependent, OFeT family ferrous iron permease . The efeUOB operon of enterohaemorrhagic E. coli O157:H7 lacks any frameshift and is functional . EfeB has been implicated in exogenous heme iron acquisition. Due to the lack of an outer membrane receptor for heme, E. coli K-12 is unable to utilize heme as a source of iron . However, expression of the foreign heme receptor protein HasR from Serratia marcescens enables utilization of heme as a source of iron. Subsequent heme uptake through the E...

## Biological Role

Component of heme-containing peroxidase/deferrochelatase (complex.ecocyc.CPLX0-7810).

## Annotation

FUNCTION: Involved in the recovery of exogenous heme iron. Extracts iron from heme while preserving the protoporphyrin ring intact. Also displays peroxidase activity on guaiacol in vitro. {ECO:0000269|PubMed:16551627, ECO:0000269|PubMed:19564607}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7810|complex.ecocyc.CPLX0-7810]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1019|gene.b1019]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31545`
- `KEGG:ecj:JW1004;eco:b1019;ecoc:C3026_06195;`
- `GeneID:946500;`
- `GO:GO:0004325; GO:0004601; GO:0005829; GO:0006974; GO:0020037; GO:0030288; GO:0033212; GO:0042597; GO:0046872`
- `EC:1.11.1.-; 4.98.1.1`

## Notes

Deferrochelatase (EC 4.98.1.1) (Peroxidase EfeB) (EC 1.11.1.-)
