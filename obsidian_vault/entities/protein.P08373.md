---
entity_id: "protein.P08373"
entity_type: "protein"
name: "murB"
source_database: "UniProt"
source_id: "P08373"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "murB yijB b3972 JW3940"
---

# murB

`protein.P08373`

## Static

- Type: `protein`
- Source: `UniProt:P08373`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Cell wall formation. UDP-N-acetylenolpyruvoylglucosamine reductase (MurB) catalyzes the second committed step in the biosynthesis of peptidoglycan. The enzyme is essential for growth and is a target for development of new antibiotics . Crystal structures of the enzyme have been solved , and the NADP+ binding site has been localized by NMR and appears to co-localize with the binding pocket for UDP-N-acetylenolpyruvoylglucosamine . The kinetic mechanism of the enzyme has been investigated. The reaction appears to proceed as a sequence of two half-reactions . MurA, MurB and MurC are capable of chemo-enzymatic labeling and modifying of UDP-GlcNAc-RNA in vitro . Reviews:

## Biological Role

Catalyzes UDP-N-acetylmuramate:NADP+ oxidoreductase (reaction.R03191), UDP-N-acetylmuramate:NADP+ oxidoreductase (reaction.R03192), UDPNACETYLMURAMATEDEHYDROG-RXN (reaction.ecocyc.UDPNACETYLMURAMATEDEHYDROG-RXN). Bound by FAD (molecule.C00016).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Cell wall formation.

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R03191|reaction.R03191]] `KEGG` `database` - via EC:1.3.1.98
- `catalyzes` --> [[reaction.R03192|reaction.R03192]] `KEGG` `database` - via EC:1.3.1.98
- `catalyzes` --> [[reaction.ecocyc.UDPNACETYLMURAMATEDEHYDROG-RXN|reaction.ecocyc.UDPNACETYLMURAMATEDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3972|gene.b3972]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08373`
- `KEGG:ecj:JW3940;eco:b3972;ecoc:C3026_21460;`
- `GeneID:948470;`
- `GO:GO:0005737; GO:0005829; GO:0008360; GO:0008762; GO:0009252; GO:0050660; GO:0051301; GO:0071555; GO:0071949`
- `EC:1.3.1.98`

## Notes

UDP-N-acetylenolpyruvoylglucosamine reductase (EC 1.3.1.98) (UDP-N-acetylmuramate dehydrogenase)
