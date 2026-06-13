---
entity_id: "protein.P16256"
entity_type: "protein"
name: "panF"
source_database: "UniProt"
source_id: "P16256"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "panF b3258 JW3226"
---

# panF

`protein.P16256`

## Static

- Type: `protein`
- Source: `UniProt:P16256`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Catalyzes the sodium-dependent uptake of extracellular pantothenate. {ECO:0000269|PubMed:2193919, ECO:0000269|PubMed:3888959}. PanF is a pantothenate transporter which probably functions as a pantothenate/cation symporter. Whole cell transport assays have shown that the cloned panF gene can complement panF mutants with pantothenate transport defects . Overexpression of panF lead to increased pantothenate accumulation. Whole cell transport experiments have shown that PanF mediates high affinity pantothenate transport with a Km of approx 0.4 μM and pantothenate uptake was stimulated by the presence of sodium ions . PanF is a member of the SSS family of sodium/solute symporters, supporting the notion that it functions as a sodium/pantothenate symporter . Imported pantothenate is phosphorylated by pantothenate kinase, a key step in Coenzyme A synthesis.

## Biological Role

Catalyzes pantothenate:Na+ symport (reaction.ecocyc.TRANS-RXN-117). Transports Pantothenate (molecule.C00864), Sodium cation (molecule.C01330).

## Annotation

FUNCTION: Catalyzes the sodium-dependent uptake of extracellular pantothenate. {ECO:0000269|PubMed:2193919, ECO:0000269|PubMed:3888959}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-117|reaction.ecocyc.TRANS-RXN-117]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00864|molecule.C00864]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b3258|gene.b3258]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16256`
- `KEGG:ecj:JW3226;eco:b3258;ecoc:C3026_17725;`
- `GeneID:93778729;947752;`
- `GO:GO:0005886; GO:0015081; GO:0015233; GO:0015293; GO:0015887; GO:0036376`

## Notes

Sodium/pantothenate symporter (Pantothenate permease)
