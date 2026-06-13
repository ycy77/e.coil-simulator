---
entity_id: "protein.P56580"
entity_type: "protein"
name: "srlE"
source_database: "UniProt"
source_id: "P56580"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:3553176}; Multi-pass membrane protein {ECO:0000255, ECO:0000305|PubMed:3553176}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "srlE gutA gutE b2703 JW5430"
---

# srlE

`protein.P56580`

## Static

- Type: `protein`
- Source: `UniProt:P56580`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:3553176}; Multi-pass membrane protein {ECO:0000255, ECO:0000305|PubMed:3553176}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II complex composed of SrlA, SrlB and SrlE is involved in glucitol/sorbitol transport. It can also use D-mannitol. {ECO:0000269|PubMed:1100608}. Contains PTS Enzyme IIB and IIC1 (IIC-C) domain. The IIB domain is largely hydrophilic and contains a cysteine residue at position 71 which may be the second phosphorylation site .

## Biological Role

Catalyzes protein-N(pi)-phosphohistidine:D-sorbitol 6-phosphotransferase (reaction.R05820). Component of sorbitol-specific PTS enzyme II (complex.ecocyc.CPLX-169).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II complex composed of SrlA, SrlB and SrlE is involved in glucitol/sorbitol transport. It can also use D-mannitol. {ECO:0000269|PubMed:1100608}.

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R05820|reaction.R05820]] `KEGG` `database` - via EC:2.7.1.198
- `is_component_of` --> [[complex.ecocyc.CPLX-169|complex.ecocyc.CPLX-169]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2703|gene.b2703]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P56580`
- `KEGG:ecj:JW5430;eco:b2703;ecoc:C3026_14880;`
- `GeneID:948933;`
- `GO:GO:0005886; GO:0008982; GO:0009401; GO:0015795; GO:0016301; GO:0090563; GO:1902495`
- `EC:2.7.1.198`

## Notes

PTS system glucitol/sorbitol-specific EIIB component (EC 2.7.1.198) (EII-Gut) (Enzyme II-Gut) (Glucitol/sorbitol-specific phosphotransferase enzyme IIB component)
