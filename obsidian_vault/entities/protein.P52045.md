---
entity_id: "protein.P52045"
entity_type: "protein"
name: "scpB"
source_database: "UniProt"
source_id: "P52045"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "scpB mmcD ygfG b2919 JW2886"
---

# scpB

`protein.P52045`

## Static

- Type: `protein`
- Source: `UniProt:P52045`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the decarboxylation of (R)-methylmalonyl-CoA to propionyl-CoA. Could be part of a pathway that converts succinate to propanoate. {ECO:0000269|PubMed:10769117}. Methylmalonyl-CoA decarboxylase is a biotin-independent enzyme that catalyzes the decarboxylation of methylmalonyl-CoA to propionyl-CoA. This reaction is suggested to be part of a pathway of succinate decarboxylation whose metabolic function is unknown . Crystal structures of the enzyme alone and in complex with an inert analog of methylmalonyl-CoA have been solved; the monomers are arranged in a dimer of trimers in the crystal. Unlike other members of this family of enzymes, active sites are not shared between monomers. A reaction mechanism was proposed . Overexpression of scpB reduces heterologous production of 6-deoxyerythronolide B (6dEB), the macrolactone precursor of erythromycin . Review:

## Biological Role

Component of methylmalonyl-CoA decarboxylase (complex.ecocyc.CPLX0-254).

## Enriched Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the decarboxylation of (R)-methylmalonyl-CoA to propionyl-CoA. Could be part of a pathway that converts succinate to propanoate. {ECO:0000269|PubMed:10769117}.

## Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-254|complex.ecocyc.CPLX0-254]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b2919|gene.b2919]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52045`
- `KEGG:ecj:JW2886;eco:b2919;ecoc:C3026_15995;`
- `GeneID:75205243;947408;`
- `GO:GO:0004492; GO:0005829; GO:0006635; GO:0016831`
- `EC:4.1.1.-`

## Notes

Methylmalonyl-CoA decarboxylase (MMCD) (EC 4.1.1.-) (Transcarboxylase)
