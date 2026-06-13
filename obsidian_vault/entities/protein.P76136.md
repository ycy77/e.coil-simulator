---
entity_id: "protein.P76136"
entity_type: "protein"
name: "safA"
source_database: "UniProt"
source_id: "P76136"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:17998538}; Single-pass type II membrane protein {ECO:0000269|PubMed:17998538}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "safA yneN b1500 JW1494.1"
---

# safA

`protein.P76136`

## Static

- Type: `protein`
- Source: `UniProt:P76136`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:17998538}; Single-pass type II membrane protein {ECO:0000269|PubMed:17998538}.

## Enriched Summary

FUNCTION: Connects the signal transduction between the two-component systems EvgS/EvgA and PhoQ/PhoP, by directly interacting with PhoQ and thus activating the PhoQ/PhoP system, in response to acid stress conditions (PubMed:17998538). Activates the PhoQ/PhoP system by increasing autophosphorylation of PhoQ, thereby leading to the accumulation of phospho-PhoP (PubMed:23563556). {ECO:0000269|PubMed:17998538, ECO:0000269|PubMed:23563556}. SafA is a small membrane protein that functions to connect the the PWY0-1490 "EvgS/EvgA" and PWY0-1458 "PhoQ/PhoP" two component systems; activation of the EvgS/EvgA system induces SafA which in turn activates the PhoQ/PhoP system to induce PhoP regulated genes (see ). SafA contributes to a complex network of acid resistance gene regulation (see ). safA forms an operon with ydeO; safA-ydeO is a member of the EvgA regulon ; safA-ydeO is up-regulated when the EvgS/EvgA two-component system is activated . Deletion of safA results in a slight decrease in survival at pH 2.5 . Expression of safA from a heterologous promoter activates expression of PhoP regulon genes (eg mgtA, mgrB, rstAB, slyB and others) in a PhoQ/PhoP dependent manner . SafA interacts with, and activates PhoQ (see also ); SafA activates the autophosphorylation of PhoQ . SafA is a Type II membrane protein that spans the membrane once with its N-terminus in the cytoplasm...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Connects the signal transduction between the two-component systems EvgS/EvgA and PhoQ/PhoP, by directly interacting with PhoQ and thus activating the PhoQ/PhoP system, in response to acid stress conditions (PubMed:17998538). Activates the PhoQ/PhoP system by increasing autophosphorylation of PhoQ, thereby leading to the accumulation of phospho-PhoP (PubMed:23563556). {ECO:0000269|PubMed:17998538, ECO:0000269|PubMed:23563556}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b1500|gene.b1500]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76136`
- `KEGG:eco:b1500;ecoc:C3026_08685;`
- `GeneID:946061;`
- `GO:GO:0005886; GO:0010447`

## Notes

Two-component-system connector protein SafA (Regulatory protein b1500) (Sensor associating factor A)
