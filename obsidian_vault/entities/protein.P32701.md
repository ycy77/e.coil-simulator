---
entity_id: "protein.P32701"
entity_type: "protein"
name: "pdeC"
source_database: "UniProt"
source_id: "P32701"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pdeC yjcC b4061 JW4022"
---

# pdeC

`protein.P32701`

## Static

- Type: `protein`
- Source: `UniProt:P32701`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Phosphodiesterase (PDE) that catalyzes the hydrolysis of cyclic-di-GMP (c-di-GMP) to 5'-pGpG (By similarity). Cyclic-di-GMP is a second messenger which controls cell surface-associated traits in bacteria. Overexpression reduces biofilm formation (PubMed:19460094). {ECO:0000250|UniProtKB:P21514, ECO:0000269|PubMed:19460094}. PdeC is a c-di-GMP-specific phosphodiesterase whose activity is implicated in modulating matrix formation in the deeper layers of E. coli biofilm. Overexpression of pdeC reduces biofilm formation . PdeC is an inner membrane protein with two predicted transmembrane domains which flank a predicted periplasmic CSS domain containing two highly conserved cysteines, followed by a cytoplasmic C-terminal EAL domain with phosphodiesterase activity . Purified PdeC reconstituted into nanodiscs exhibits c-di-GMP phosphodiesterase activity only in the presence of reducing agent (DTT) . The periplasmic CSS domain contains two cysteine residues which form a disulphide bond; the redox state of the periplasmic CSS domain controls phosphodiesterase activity; PdeC is highly active when the CSS domain is in the free thiol state...

## Biological Role

Catalyzes cyclic bis(3->5')diguanylate 3-guanylylhydrolase (reaction.R08991), RXN0-4181 (reaction.ecocyc.RXN0-4181).

## Annotation

FUNCTION: Phosphodiesterase (PDE) that catalyzes the hydrolysis of cyclic-di-GMP (c-di-GMP) to 5'-pGpG (By similarity). Cyclic-di-GMP is a second messenger which controls cell surface-associated traits in bacteria. Overexpression reduces biofilm formation (PubMed:19460094). {ECO:0000250|UniProtKB:P21514, ECO:0000269|PubMed:19460094}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R08991|reaction.R08991]] `KEGG` `database` - via EC:3.1.4.52
- `catalyzes` --> [[reaction.ecocyc.RXN0-4181|reaction.ecocyc.RXN0-4181]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4061|gene.b4061]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32701`
- `KEGG:ecj:JW4022;eco:b4061;ecoc:C3026_21945;`
- `GeneID:948568;`
- `GO:GO:0005886; GO:0071111; GO:1900190`
- `EC:3.1.4.52`

## Notes

Probable cyclic di-GMP phosphodiesterase PdeC (EC 3.1.4.52)
