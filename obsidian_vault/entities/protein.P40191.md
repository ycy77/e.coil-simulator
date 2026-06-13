---
entity_id: "protein.P40191"
entity_type: "protein"
name: "pdxK"
source_database: "UniProt"
source_id: "P40191"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pdxK yfeI b2418 JW2411"
---

# pdxK

`protein.P40191`

## Static

- Type: `protein`
- Source: `UniProt:P40191`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: B6-vitamer kinase involved in the salvage pathway of pyridoxal 5'-phosphate (PLP). Catalyzes the phosphorylation of pyridoxine (PN), pyridoxal (PL), and pyridoxamine (PM), forming their respective 5'-phosphorylated esters, i.e. PNP, PLP and PMP. {ECO:0000269|PubMed:15249053, ECO:0000269|PubMed:9537380}. Pyridoxal kinase 1 is able to phosphorylate pyridoxal (PL), pyridoxine (PN), pyridoxamine (PM), and hydroxymethylpyrimidine (HMP), forming their respective 5'-phosphoesters . There are two pyridoxal kinases in E. coli: the enzyme described here (PdxK), and a second enzyme, PDXY-MONOMER PdxY . PdxK is the major PL kinase activity in the cell . Both enzymes function in the scavenger/salvage pathway of pyridoxal 5'-phosphate (PLP) . The HMP kinase activity of PdxK contributes to thiamine salvage . Under physiological conditions, MgATP is the favored cosubstrate over ZnATP . Potassium is required for catalytic activity; kinetic and inhibitor studies suggest a sequential random addition of the substrates . After approximately 25 catalytic turnovers, the pyridoxal kinase activity is inhibited by covalent binding of the PLP product, likely to the Lys229 residue within the active site . This complex may be formed by initial formation of a Schiff base bond between pyridoxal and Lys229, followed by a single catalytic cycle that converts pyridoxal to PLP...

## Biological Role

Catalyzes ATP:pyridoxal 5'-phosphotransferase (reaction.R00174), ATP:pyridoxine 5'-phosphotransferase (reaction.R01909). Component of pyridoxal kinase 1 / hydroxymethylpyrimidine kinase (complex.ecocyc.PDXK-CPLX).

## Enriched Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: B6-vitamer kinase involved in the salvage pathway of pyridoxal 5'-phosphate (PLP). Catalyzes the phosphorylation of pyridoxine (PN), pyridoxal (PL), and pyridoxamine (PM), forming their respective 5'-phosphorylated esters, i.e. PNP, PLP and PMP. {ECO:0000269|PubMed:15249053, ECO:0000269|PubMed:9537380}.

## Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00174|reaction.R00174]] `KEGG` `database` - via EC:2.7.1.35
- `catalyzes` --> [[reaction.R01909|reaction.R01909]] `KEGG` `database` - via EC:2.7.1.35
- `is_component_of` --> [[complex.ecocyc.PDXK-CPLX|complex.ecocyc.PDXK-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2418|gene.b2418]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P40191`
- `KEGG:ecj:JW2411;eco:b2418;ecoc:C3026_13440;`
- `GeneID:946881;`
- `GO:GO:0000287; GO:0005524; GO:0005829; GO:0008270; GO:0008478; GO:0008902; GO:0009443; GO:0030170; GO:0036172; GO:0042803`
- `EC:2.7.1.35`

## Notes

Pyridoxine/pyridoxal/pyridoxamine kinase (PN/PL/PM kinase) (EC 2.7.1.35) (B6-vitamer kinase) (Pyridoxal kinase 1) (PL kinase 1)
