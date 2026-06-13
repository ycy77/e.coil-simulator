---
entity_id: "protein.P39265"
entity_type: "protein"
name: "alsB"
source_database: "UniProt"
source_id: "P39265"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "alsB yjcX b4088 JW4049"
---

# alsB

`protein.P39265`

## Static

- Type: `protein`
- Source: `UniProt:P39265`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm.

## Enriched Summary

FUNCTION: Part of the binding-protein-dependent transport system AlsBAC for D-allose. {ECO:0000269|PubMed:9401019}. AlsB is the periplasmic binding protein of a D-allose ATP-binding cassette (ABC) transport system. AlsB binds D-allose with high affinity (KD = 0.33 µM) . A crystal structure of AlsB bound to D-allose has been reported ; the protein contains two α/β domains joined by a 3 stranded hinge and adopts a closed conformation in which a β D-allopyranose form of the sugar is buried at the interface between the two domains. Ligand free structures of AlsB adopt a conformation in which the interface between the two domains is opened up to the solvent; conformational change between ligand free (open) and liganded (closed) forms is associated with movement of the hinge . Overexpression of alsB increases the tolerance of E. coli to n-butanol .

## Biological Role

Component of D-allose ABC transporter (complex.ecocyc.ABC-42-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the binding-protein-dependent transport system AlsBAC for D-allose. {ECO:0000269|PubMed:9401019}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-42-CPLX|complex.ecocyc.ABC-42-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4088|gene.b4088]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39265`
- `KEGG:ecj:JW4049;eco:b4088;ecoc:C3026_22100;`
- `GeneID:948604;`
- `GO:GO:0015752; GO:0015754; GO:0016020; GO:0030288; GO:0048029; GO:0055052; GO:0055085`

## Notes

D-allose-binding periplasmic protein (ALBP)
