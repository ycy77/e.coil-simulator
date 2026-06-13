---
entity_id: "protein.P10384"
entity_type: "protein"
name: "fadL"
source_database: "UniProt"
source_id: "P10384"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:16079137}; Multi-pass membrane protein {ECO:0000269|PubMed:16079137}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fadL ttr b2344 JW2341"
---

# fadL

`protein.P10384`

## Static

- Type: `protein`
- Source: `UniProt:P10384`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:16079137}; Multi-pass membrane protein {ECO:0000269|PubMed:16079137}.

## Enriched Summary

FUNCTION: Involved in translocation of long-chain fatty acids across the outer membrane. It is a receptor for the bacteriophage T2. FadL may form a specific channel. FadL is an outer membrane, ligand gated channel that functions in the uptake of long chain (C12-C18) fatty acids (LCFAs) . Exogenous long-chain fatty acids are first recognized at the surface of FadL by a low-affinity binding site, followed by diffusion to a high-affinity binding site within a barrel. This translocation displaces an N-terminus plug, opening the barrel and resulting in release of the substrate in the outer membrane. Mutations in FadL can be generated that distinguish regions required for binding from those required for transport . FadL binding affinity is highest for OLEATE-CPD and PALMITATE; no binding of the medium-chain acid CPD-3617 is detected . FadL crystal structures at 2.6 and 2.8 Å indicate that the protein forms a 14-stranded antiparallel β barrel. The amino terminus forms a small "hatch" domain which plugs the barrel on the extracellular side. A prominent hydrophobic pocket is located inside the barrel towards the extracellular side of the membrane and forms a high affinity substrate binding site; a hydrophobic groove formed between two extracellular loops may constitute a low-affinity site for initial interaction with LCFAs...

## Biological Role

Catalyzes RXN0-1802 (reaction.ecocyc.RXN0-1802).

## Annotation

FUNCTION: Involved in translocation of long-chain fatty acids across the outer membrane. It is a receptor for the bacteriophage T2. FadL may form a specific channel.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1802|reaction.ecocyc.RXN0-1802]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2344|gene.b2344]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P10384`
- `KEGG:ecj:JW2341;eco:b2344;ecoc:C3026_13045;`
- `GeneID:946820;`
- `GO:GO:0009279; GO:0015483; GO:0015909; GO:0022834`

## Notes

Long-chain fatty acid transport protein (Outer membrane FadL protein) (Outer membrane flp protein)
