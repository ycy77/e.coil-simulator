---
entity_id: "protein.P35340"
entity_type: "protein"
name: "ahpF"
source_database: "UniProt"
source_id: "P35340"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ahpF b0606 JW0599"
---

# ahpF

`protein.P35340`

## Static

- Type: `protein`
- Source: `UniProt:P35340`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Serves to protect the cell against DNA damage by alkyl hydroperoxides. It can use either NADH or NADPH as electron donor for direct reduction of redox dyes or of alkyl hydroperoxides when combined with the AhpC protein. AhpF is the peroxiredoxin reductase component of alkyl hydroperoxide reductase, and is one of the ten most abundant proteins in TAX-562 . The N-terminal domain of AhpF belongs to the family of protein-disulfide oxidoreductases, while the C terminus belongs to the thioredoxin reductase family . By similarity to the enzyme from Salmonella typhimurium, it is thought to channel electrons from NADH to the AhpC component for reduction of the hydroperoxide substrate. An internal redox-active disulfide bridge between two cysteine residues is reduced by electron transfer from NADH via the FAD cofactor. This reduction triggers a cascade of disulfide-exchange reactions, first intramolecularly, then intermolecularly to the disulfide cysteine residues of the AhpC component. AhpF consists of an N-terminal domain (NTD), an FAD-binding domain and an NADH-binding domain . A crystal structure of the catalytic core of AhpF containing the FAD cofactor has been solved at 1.9 Å resolution . Crystal structures of the full-length protein have been solved...

## Biological Role

Catalyzes RXN-8506 (reaction.ecocyc.RXN-8506). Component of alkyl hydroperoxide reductase (complex.ecocyc.CPLX0-245).

## Annotation

FUNCTION: Serves to protect the cell against DNA damage by alkyl hydroperoxides. It can use either NADH or NADPH as electron donor for direct reduction of redox dyes or of alkyl hydroperoxides when combined with the AhpC protein.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-8506|reaction.ecocyc.RXN-8506]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-245|complex.ecocyc.CPLX0-245]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0606|gene.b0606]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P35340`
- `KEGG:ecj:JW0599;eco:b0606;ecoc:C3026_03030;`
- `GeneID:93776878;947540;`
- `GO:GO:0000302; GO:0004791; GO:0005829; GO:0006979; GO:0008785; GO:0009321; GO:0042744; GO:0045454; GO:0051287; GO:0071949; GO:0102039`
- `EC:1.8.1.-`

## Notes

Alkyl hydroperoxide reductase subunit F (EC 1.8.1.-) (Alkyl hydroperoxide reductase F52A protein)
