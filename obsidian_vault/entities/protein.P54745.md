---
entity_id: "protein.P54745"
entity_type: "protein"
name: "mngA"
source_database: "UniProt"
source_id: "P54745"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000305|PubMed:14645248}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000305|PubMed:14645248}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mngA hrsA b0731 JW0720"
---

# mngA

`protein.P54745`

## Static

- Type: `protein`
- Source: `UniProt:P54745`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000305|PubMed:14645248}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000305|PubMed:14645248}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane (PubMed:14645248, PubMed:9063979). This system is involved in mannosyl-D-glycerate transport (PubMed:14645248). Also involved in thermoinduction of ompC (PubMed:9063979). {ECO:0000269|PubMed:14645248, ECO:0000269|PubMed:9063979}. MngA, a PTS permease, belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its substrates in a process called group translocation (reviewed in . MngA takes up exogenous 2-O-α-mannosyl-D-glycerate (MG), releasing the phosphate ester into the cell cytoplasm for hydrolysis by the mngB encoded EG13236-MONOMER . E. coli K-12 can use MG as the sole source of carbon. An E. coli ΔmngA strain cannot grow with MG as sole carbon source. MG induces expression of mngA. Membranes containing MngA are able to phosphorylate MG in vitro in the presence of PEP, PtsI and PtsH . mngA formerly known as hsrA was initially identified during a study of thermoresponsive genes in E. coli K-12...

## Biological Role

Catalyzes RXN0-2522 (reaction.ecocyc.RXN0-2522).

## Enriched Pathways

- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane (PubMed:14645248, PubMed:9063979). This system is involved in mannosyl-D-glycerate transport (PubMed:14645248). Also involved in thermoinduction of ompC (PubMed:9063979). {ECO:0000269|PubMed:14645248, ECO:0000269|PubMed:9063979}.

## Pathways

- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-2522|reaction.ecocyc.RXN0-2522]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0731|gene.b0731]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P54745`
- `KEGG:ecj:JW0720;eco:b0731;`
- `GeneID:945355;`
- `GO:GO:0005351; GO:0005886; GO:0009401; GO:0016301; GO:0022877; GO:0051476; GO:0090563; GO:0090581`
- `EC:2.7.1.195`

## Notes

PTS system 2-O-alpha-mannosyl-D-glycerate-specific EIIABC component (2-O-alpha-mannosyl-D-glycerate-specific phosphotransferase enzyme MngA) (Protein-Npi-phosphohistidine--2-O-alpha-mannosyl-D-glycerate phosphotransferase) [Includes: 2-O-alpha-mannosyl-D-glycerate-specific phosphotransferase enzyme IIA component (PTS system EIIA component); 2-O-alpha-mannosyl-D-glycerate-specific phosphotransferase enzyme IIB component (EC 2.7.1.195) (PTS system EIIB component); 2-O-alpha-mannosyl-D-glycerate-specific permease IIC component (PTS system EIIC component)]
