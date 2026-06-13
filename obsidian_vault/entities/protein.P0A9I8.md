---
entity_id: "protein.P0A9I8"
entity_type: "protein"
name: "nirD"
source_database: "UniProt"
source_id: "P0A9I8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nirD b3366 JW3329"
---

# nirD

`protein.P0A9I8`

## Static

- Type: `protein`
- Source: `UniProt:P0A9I8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Required for activity of the reductase. {ECO:0000269|PubMed:1435259}. NirD may be a subunit of the NADH-dependent nitrite reductase. Presence of nirD is required for nitrite reductase activity in cell extracts, and the NirD protein appears to be present in partially purified nitrite reductase . NirD interacts directly with NirB in a BACTH experiment . However, the function of NirD in enabling nitrite reductase activity has not been determined. NirD interacts directly with the catalytic domain of RELA-MONOMER RelA, thereby inhibiting the synthesis of (p)ppGpp and the stringent response. The E50K mutation eliminates the interaction with RelA, but does not affect the interaction with NirB . Overexpression of nirD leads to a decrease of the intracellular levels of (p)ppGpp . Expression of nirD is upregulated upon exposure to silver nanoparticles . NirD: "nitrite reductase"

## Biological Role

Catalyzes ammonia:NAD+ oxidoreductase (reaction.R00787). Component of nitrite reductase - NADH dependent (complex.ecocyc.NITRITREDUCT-CPLX).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)

## Annotation

FUNCTION: Required for activity of the reductase. {ECO:0000269|PubMed:1435259}.

## Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00787|reaction.R00787]] `KEGG` `database` - via EC:1.7.1.15
- `is_component_of` --> [[complex.ecocyc.NITRITREDUCT-CPLX|complex.ecocyc.NITRITREDUCT-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3366|gene.b3366]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9I8`
- `KEGG:ecj:JW3329;eco:b3366;ecoc:C3026_18280;`
- `GeneID:86862235;93778631;947881;`
- `GO:GO:0005737; GO:0009344; GO:0042128; GO:0051537; GO:0106316`
- `EC:1.7.1.15`

## Notes

Nitrite reductase (NADH) small subunit (EC 1.7.1.15)
