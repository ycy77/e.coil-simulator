---
entity_id: "protein.P11447"
entity_type: "protein"
name: "argH"
source_database: "UniProt"
source_id: "P11447"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "argH b3960 JW3932"
---

# argH

`protein.P11447`

## Static

- Type: `protein`
- Source: `UniProt:P11447`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

Argininosuccinate lyase (ASAL) (EC 4.3.2.1) (Arginosuccinase) Argininosuccinate lyase catalyzes the final step in the L-arginine biosynthesis pathway. A crystal structure of argininosuccinate lyase has been solved at 2.44 Å resolution; the enzyme appears to be tetrameric, with a dimer as the asymmetric unit of this crystal form . ArgH expression is repressed by the addition of arginine or ornithine to the medium .

## Biological Role

Catalyzes ARGSUCCINLYA-RXN (reaction.ecocyc.ARGSUCCINLYA-RXN).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

Argininosuccinate lyase (ASAL) (EC 4.3.2.1) (Arginosuccinase)

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ARGSUCCINLYA-RXN|reaction.ecocyc.ARGSUCCINLYA-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3960|gene.b3960]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P11447`
- `KEGG:ecj:JW3932;eco:b3960;ecoc:C3026_21400;`
- `GeneID:948463;`
- `GO:GO:0004056; GO:0005829; GO:0042450`
- `EC:4.3.2.1`

## Notes

Argininosuccinate lyase (ASAL) (EC 4.3.2.1) (Arginosuccinase)
