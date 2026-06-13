---
entity_id: "protein.P37355"
entity_type: "protein"
name: "menH"
source_database: "UniProt"
source_id: "P37355"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "menH yfbB b2263 JW2258"
---

# menH

`protein.P37355`

## Static

- Type: `protein`
- Source: `UniProt:P37355`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes a proton abstraction reaction that results in 2,5-elimination of pyruvate from 2-succinyl-5-enolpyruvyl-6-hydroxy-3-cyclohexene-1-carboxylate (SEPHCHC) and the formation of 2-succinyl-6-hydroxy-2,4-cyclohexadiene-1-carboxylate (SHCHC). Is also able to catalyze the hydrolysis of the thioester bond in palmitoyl-CoA in vitro. {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:18284213}. MenH catalyzes the third step in the menaquinone biosynthesis pathway, a proton abstraction reaction that results in 2,5-elimination of pyruvate from CPD-9924 and the formation of CPD-9923 . SHCHC synthase activity was first detected in crude extracts . Structural modelling and site-directed mutagenesis allowed identification of active site residues . Crystal structures of the wild type protein and two active site mutants have been solved . MenH was initially suggested to catalyze a thioesterase step in the menaquinone biosynthetic pathway . However, the purified protein lacks thioesterase activity, but has efficient SHCHC synthase activity . Conflicting with this result, esterase activity of MenH with palmitoyl-CoA as the substrate was discovered in a high-throughput screen of purified proteins .

## Biological Role

Catalyzes RXN-9310 (reaction.ecocyc.RXN-9310).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes a proton abstraction reaction that results in 2,5-elimination of pyruvate from 2-succinyl-5-enolpyruvyl-6-hydroxy-3-cyclohexene-1-carboxylate (SEPHCHC) and the formation of 2-succinyl-6-hydroxy-2,4-cyclohexadiene-1-carboxylate (SHCHC). Is also able to catalyze the hydrolysis of the thioester bond in palmitoyl-CoA in vitro. {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:18284213}.

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-9310|reaction.ecocyc.RXN-9310]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2263|gene.b2263]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37355`
- `KEGG:ecj:JW2258;eco:b2263;ecoc:C3026_12640;`
- `GeneID:946736;`
- `GO:GO:0005829; GO:0009234; GO:0070205`
- `EC:4.2.99.20`

## Notes

2-succinyl-6-hydroxy-2,4-cyclohexadiene-1-carboxylate synthase (SHCHC synthase) (EC 4.2.99.20)
