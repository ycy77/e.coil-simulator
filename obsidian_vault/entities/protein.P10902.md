---
entity_id: "protein.P10902"
entity_type: "protein"
name: "nadB"
source_database: "UniProt"
source_id: "P10902"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nadB nicB b2574 JW2558"
---

# nadB

`protein.P10902`

## Static

- Type: `protein`
- Source: `UniProt:P10902`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the oxidation of L-aspartate to iminoaspartate, the first step in the de novo biosynthesis of NAD(+) (PubMed:11294641, PubMed:2187483, PubMed:2841129, PubMed:7033218, PubMed:8706749, PubMed:8706750). Can use either oxygen or fumarate as electron acceptors, which allows the enzyme to be functional under aerobic and anaerobic conditions (PubMed:11294641, PubMed:12200425, PubMed:8706750). In vivo, fumarate is used under anaerobic conditions, and oxygen is the predominant electron acceptor under aerobic conditions due to the lower fumarate levels (PubMed:20149100). In vitro, fumarate is a more efficient electron acceptor and is kinetically superior to oxygen (PubMed:12200425, PubMed:20149100). {ECO:0000269|PubMed:11294641, ECO:0000269|PubMed:12200425, ECO:0000269|PubMed:20149100, ECO:0000269|PubMed:2187483, ECO:0000269|PubMed:2841129, ECO:0000269|PubMed:7033218, ECO:0000269|PubMed:8706749, ECO:0000269|PubMed:8706750}. L-aspartate oxidase (NadB) is the first enzyme in the de novo PYRIDNUCSYN-PWY pathway, catalyzing the FAD-dependent oxidation of L-aspartate to iminoaspartate...

## Biological Role

Catalyzes L-aspartic acid:oxygen oxidoreductase (deaminating) (reaction.R00357), L-aspartate:oxygen oxidoreductase (reaction.R00481), L-ASPARTATE-OXID-RXN (reaction.ecocyc.L-ASPARTATE-OXID-RXN), L-aspartate : fumarate oxidoreductase (deaminating) (reaction.ecocyc.RXN-9772). Bound by FAD (molecule.C00016).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the oxidation of L-aspartate to iminoaspartate, the first step in the de novo biosynthesis of NAD(+) (PubMed:11294641, PubMed:2187483, PubMed:2841129, PubMed:7033218, PubMed:8706749, PubMed:8706750). Can use either oxygen or fumarate as electron acceptors, which allows the enzyme to be functional under aerobic and anaerobic conditions (PubMed:11294641, PubMed:12200425, PubMed:8706750). In vivo, fumarate is used under anaerobic conditions, and oxygen is the predominant electron acceptor under aerobic conditions due to the lower fumarate levels (PubMed:20149100). In vitro, fumarate is a more efficient electron acceptor and is kinetically superior to oxygen (PubMed:12200425, PubMed:20149100). {ECO:0000269|PubMed:11294641, ECO:0000269|PubMed:12200425, ECO:0000269|PubMed:20149100, ECO:0000269|PubMed:2187483, ECO:0000269|PubMed:2841129, ECO:0000269|PubMed:7033218, ECO:0000269|PubMed:8706749, ECO:0000269|PubMed:8706750}.

## Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R00357|reaction.R00357]] `KEGG` `database` - via EC:1.4.3.16
- `catalyzes` --> [[reaction.R00481|reaction.R00481]] `KEGG` `database` - via EC:1.4.3.16
- `catalyzes` --> [[reaction.ecocyc.L-ASPARTATE-OXID-RXN|reaction.ecocyc.L-ASPARTATE-OXID-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9772|reaction.ecocyc.RXN-9772]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2574|gene.b2574]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P10902`
- `KEGG:ecj:JW2558;eco:b2574;ecoc:C3026_14260;`
- `GeneID:947049;`
- `GO:GO:0005829; GO:0008734; GO:0034628; GO:0050660`
- `EC:1.4.3.16; 1.5.99.-`

## Notes

L-aspartate oxidase (LASPO) (EC 1.4.3.16) (L-aspartate:fumarate oxidoreductase) (EC 1.5.99.-) (Quinolinate synthetase B)
