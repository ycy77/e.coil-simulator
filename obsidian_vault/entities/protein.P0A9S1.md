---
entity_id: "protein.P0A9S1"
entity_type: "protein"
name: "fucO"
source_database: "UniProt"
source_id: "P0A9S1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fucO b2799 JW2770"
---

# fucO

`protein.P0A9S1`

## Static

- Type: `protein`
- Source: `UniProt:P0A9S1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Lactaldehyde reductase (EC 1.1.1.77) (Propanediol oxidoreductase) L-1,2-propanediol oxidoreductase is an iron-dependent group III dehydrogenase. It anaerobically reduces L-lactaldehyde, a product of both the L-fucose and L-rhamnose catabolic pathways, to L-1,2-propanediol, which is then excreted from the cell . A mutant's ability to grow on L-1,2-propanediol as the source of carbon and energy is due to constitutive production of FucO, and the enzyme then serves as a propanediol dehydrogenase . Another mutant strain was selected for the ability to utilize ethylene glycol as a carbon source. This ability is in part due to a regulatory mutation that increases the activity of FucO, which can utilize ethylene glycol as an alternate substrate . Crystal structures of the enzyme have been solved, showing a domain-swapped dimer in which the metal, cofactor and substrate binding sites could be located . An aspartate and three conserved histidine residues are required for Fe2+ binding and enzymatic activity . The stereoselectivity of the enzyme has been explained by a critical hydrogen bond interaction between the (2S)-hydroxyl and the side-chain of N151 . It was also proposed that a water molecule in the active site, which is hydrogen bonded to H267 and to the 2'-hydroxyl of the NADH ribose moiety, functions as a catalytic proton donor in the protonation of the product alcohol...

## Biological Role

Component of lactaldehyde reductase (complex.ecocyc.LACTALDREDUCT-CPLX).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

Lactaldehyde reductase (EC 1.1.1.77) (Propanediol oxidoreductase)

## Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.LACTALDREDUCT-CPLX|complex.ecocyc.LACTALDREDUCT-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2799|gene.b2799]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9S1`
- `KEGG:ecj:JW2770;eco:b2799;ecoc:C3026_15390;`
- `GeneID:93779199;947273;`
- `GO:GO:0000166; GO:0004022; GO:0005829; GO:0008198; GO:0008912; GO:0019301; GO:0042355; GO:0042803; GO:0042846; GO:0052660; GO:0052661`
- `EC:1.1.1.77`

## Notes

Lactaldehyde reductase (EC 1.1.1.77) (Propanediol oxidoreductase)
