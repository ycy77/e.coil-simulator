---
entity_id: "protein.P0A9C3"
entity_type: "protein"
name: "galM"
source_database: "UniProt"
source_id: "P0A9C3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "galM b0756 JW0739"
---

# galM

`protein.P0A9C3`

## Static

- Type: `protein`
- Source: `UniProt:P0A9C3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Mutarotase converts alpha-aldose to the beta-anomer. It is active on D-glucose, L-arabinose, D-xylose, D-galactose, maltose and lactose. Epimerization of the β anomer of galactose to the α anomer links the metabolism of lactose and galactose. Although the interconversion of α- and β-galactose is spontaneous in vitro, the reaction is largely dependent on the presence of galactose-1-epimerase in vivo . The enzymatic reaction appears to follow a bifunctional mechanism, a simultaneous attack of a nucleophilic and electrophilic group of the enzyme on the substrate. The reaction proceeds from the pyranose form via the open chain intermediate, producing either pyranose or furanose products . The histidine residues H104 and H175 are essential for catalytic activity . A catalytic mechanism has been proposed . When overexpressed, a small amount of galactose-1-epimerase also appears in the periplasm and cell supernatant . galM is required for utilization of galactose generated from lactose, but is not required for utilization of extracellular galactose .

## Biological Role

Catalyzes ALDOSE1EPIM-RXN (reaction.ecocyc.ALDOSE1EPIM-RXN).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Mutarotase converts alpha-aldose to the beta-anomer. It is active on D-glucose, L-arabinose, D-xylose, D-galactose, maltose and lactose.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ALDOSE1EPIM-RXN|reaction.ecocyc.ALDOSE1EPIM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0756|gene.b0756]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9C3`
- `KEGG:ecj:JW0739;eco:b0756;ecoc:C3026_03825;`
- `GeneID:944943;`
- `GO:GO:0004034; GO:0005737; GO:0006006; GO:0030246; GO:0033499`
- `EC:5.1.3.3`

## Notes

Aldose 1-epimerase (EC 5.1.3.3) (Galactose mutarotase) (Type-1 mutarotase)
