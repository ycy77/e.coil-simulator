---
entity_id: "protein.P45565"
entity_type: "protein"
name: "ais"
source_database: "UniProt"
source_id: "P45565"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ais pmrG b2252 JW2246"
---

# ais

`protein.P45565`

## Static

- Type: `protein`
- Source: `UniProt:P45565`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000250}.

## Enriched Summary

FUNCTION: Catalyzes the dephosphorylation of heptose(II) of the outer membrane lipopolysaccharide core. {ECO:0000250}. Expression of ais is significantly induced by addition of 0.2 mM ZnSO4 to the medium . The orthologous gene product of Salmonella enterica, PmrG, has been characterized as a periplasmic phosphatase that hydrolyzes the phosphate group at Hep(II) in the lipopolysaccharide core region and plays a role in resistance to Fe3+ and Al3+ . Ais: "aluminum inducible protein"

## Annotation

FUNCTION: Catalyzes the dephosphorylation of heptose(II) of the outer membrane lipopolysaccharide core. {ECO:0000250}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b2252|gene.b2252]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45565`
- `KEGG:ecj:JW2246;eco:b2252;ecoc:C3026_12580;`
- `GeneID:944945;`
- `GO:GO:0008653; GO:0016791; GO:0042597`
- `EC:3.1.3.-`

## Notes

Lipopolysaccharide core heptose(II)-phosphate phosphatase (EC 3.1.3.-) (Polymyxin resistance protein PmrG)
