---
entity_id: "protein.P0AB24"
entity_type: "protein"
name: "efeO"
source_database: "UniProt"
source_id: "P0AB24"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:16551627}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "efeO ycdO b1018 JW1003"
---

# efeO

`protein.P0AB24`

## Static

- Type: `protein`
- Source: `UniProt:P0AB24`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:16551627}.

## Enriched Summary

FUNCTION: Involved in Fe(2+) uptake. Could be an iron-binding and/or electron-transfer component. {ECO:0000269|PubMed:19701722}. EfeO is predicted to be the periplasmic, metal-binding component of a ferrous ion transport system (see ) that is cryptic in E. coli K-12. Analysis of transcriptional efe-lacZ fusions suggest that efeO does not possess a proximal promoter and is co-transcribed with efeU . efeU in E. coli K-12 is disrupted by a frameshift mutation leaving the efeU_1 and efeU_2 fragments nonfunctional; EfeO (and EfeB) are produced despite the frameshift mutation . The functional efeU (ycdN) gene in E. coli Nissle 1917 encodes an oxidase-dependent, OFeT family ferrous iron permease . The efeUOB operon of enterohaemorrhagic E. coli O157:H7, lacks any frameshift and is functional . efeUOB transcription in E. coli K-12 is subject to Fe(II)-Fur control in response to iron . EfeO levels increase under iron restriction and when Fur is inactivated; EfeO levels are independent of iron in a fur mutant . The efeUOB operon is induced at acid pH and subject to CpxAR dependent repression at alkaline pH . Low copy-number expression of a 'corrected' efeUOB operon in an E. coli K-12 strain lacking lacking all known iron-transport pathways confers a growth advantage under iron restricted conditions . EfeO levels increase when E. coli K-12 strain W3110 is grown at acid pH...

## Annotation

FUNCTION: Involved in Fe(2+) uptake. Could be an iron-binding and/or electron-transfer component. {ECO:0000269|PubMed:19701722}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b1018|gene.b1018]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AB24`
- `KEGG:ecj:JW1003;eco:b1018;ecoc:C3026_06190;`
- `GeneID:93776391;945603;`
- `GO:GO:0006979; GO:0009411; GO:0009636; GO:0030288; GO:0046677`

## Notes

Iron uptake system component EfeO
