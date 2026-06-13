---
entity_id: "molecule.C00338"
entity_type: "small_molecule"
name: "Lipopolysaccharide"
source_database: "KEGG"
source_id: "C00338"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Lipopolysaccharide"
  - "LPS"
---

# Lipopolysaccharide

`molecule.C00338`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00338`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Lipopolysaccharide; LPS EcoCyc common name: a lipopolysaccharide. This compound class stands for generic and unspecified lipopolysaccharides. The structure shown here is intended to provide a general overview and does not describe a lipopolysaccharide from a specific species. Lipopolysaccharides (LPS) are a major component of the outer membrane of almost all Gram-negative bacteria. While they are protecting the membrane from certain kinds of chemical attacks, they also induce a strong response from animal immune systems. Lipopolysaccharides can be conceptually divided into three parts: Lipid-A "lipid A", which anchors LPS into the membrane; the LPS-Core-Oligosaccharides "core oligosaccharide", which contributes to membrane stability; and the O-Antigens O-antigen, which is a polysaccharide that extends away from the cell surface. Lipopolysaccharides that comprise all three regions are called Smooth-Form-LPS "smooth (S)-form LPS", while LPS lacking the O-antigen are named LOS "rough (R)-form LPS" or lipooligosaccharide (LOS). Lipid A, which is common to most Gram negative bacteria, is the most toxic part. The core polysaccharide is genus specific, and contains unusual 7-carbon and 8-carbon sugars, and the O-antigen's side chains are variable in structure and toxicity. The O-antigen usually consists of about 20-40 repeated subunits.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Lipopolysaccharide; LPS

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.3.6.3.39-RXN|reaction.ecocyc.3.6.3.39-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.3.6.3.39-RXN|reaction.ecocyc.3.6.3.39-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19362|reaction.ecocyc.RXN-19362]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5129|reaction.ecocyc.RXN0-5129]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00338`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
