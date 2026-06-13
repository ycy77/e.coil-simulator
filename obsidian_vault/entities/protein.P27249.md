---
entity_id: "protein.P27249"
entity_type: "protein"
name: "glnD"
source_database: "UniProt"
source_id: "P27249"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glnD b0167 JW0162"
---

# glnD

`protein.P27249`

## Static

- Type: `protein`
- Source: `UniProt:P27249`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Modifies, by uridylylation and deuridylylation, the PII regulatory proteins GlnB and GlnK, in response to the nitrogen status of the cell that GlnD senses through the glutamine level. Under low glutamine levels, catalyzes the conversion of the PII proteins and UTP to PII-UMP and PPi, while under higher glutamine levels, GlnD hydrolyzes PII-UMP to PII and UMP (deuridylylation). Thus, controls uridylylation state and activity of the PII proteins, and plays an important role in the regulation of nitrogen assimilation and metabolism. {ECO:0000269|PubMed:10231487, ECO:0000269|PubMed:20363937, ECO:0000269|PubMed:6130097, ECO:0000269|PubMed:8843440, ECO:0000269|PubMed:9737855}. Uridylyltransferase (UTase) encoded by glnD is a bifunctional protein that catalyzes the uridylylation as well as the de-uridylylation of PROTEIN-PII. Uridylylation and deuridylylation are distinct reactions; uridylylation involves the transfer of a UMP group (derived from UTP) to PII-1 to form PII-1-UMP and pyrophosphate; deuridylylation of PII-1-UMP is a hydrolytic reaction that results in the release of UMP and PII-1...

## Biological Role

Catalyzes UTP:[protein-PII] uridylyltransferase (reaction.R04733), RXN-16381 (reaction.ecocyc.RXN-16381), RXN0-7378 (reaction.ecocyc.RXN0-7378), RXN0-801 (reaction.ecocyc.RXN0-801), URIDYLREM-RXN (reaction.ecocyc.URIDYLREM-RXN). Bound by Magnesium cation (molecule.C00305), Mn2+ (molecule.ecocyc.MN_2).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Modifies, by uridylylation and deuridylylation, the PII regulatory proteins GlnB and GlnK, in response to the nitrogen status of the cell that GlnD senses through the glutamine level. Under low glutamine levels, catalyzes the conversion of the PII proteins and UTP to PII-UMP and PPi, while under higher glutamine levels, GlnD hydrolyzes PII-UMP to PII and UMP (deuridylylation). Thus, controls uridylylation state and activity of the PII proteins, and plays an important role in the regulation of nitrogen assimilation and metabolism. {ECO:0000269|PubMed:10231487, ECO:0000269|PubMed:20363937, ECO:0000269|PubMed:6130097, ECO:0000269|PubMed:8843440, ECO:0000269|PubMed:9737855}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.R04733|reaction.R04733]] `KEGG` `database` - via EC:2.7.7.59
- `catalyzes` --> [[reaction.ecocyc.RXN-16381|reaction.ecocyc.RXN-16381]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7378|reaction.ecocyc.RXN0-7378]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-801|reaction.ecocyc.RXN0-801]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.URIDYLREM-RXN|reaction.ecocyc.URIDYLREM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0167|gene.b0167]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27249`
- `KEGG:ecj:JW0162;eco:b0167;ecoc:C3026_00760;`
- `GeneID:944863;`
- `GO:GO:0005829; GO:0006808; GO:0008081; GO:0008773`
- `EC:2.7.7.59; 3.1.4.-`

## Notes

Bifunctional uridylyltransferase/uridylyl-removing enzyme (UTase/UR) (Bifunctional [protein-PII] modification enzyme) (Bifunctional nitrogen sensor protein) [Includes: [Protein-PII] uridylyltransferase (PII uridylyltransferase) (UTase) (EC 2.7.7.59); [Protein-PII]-UMP uridylyl-removing enzyme (UR) (EC 3.1.4.-)]
