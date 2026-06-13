---
entity_id: "protein.P0AES2"
entity_type: "protein"
name: "gudD"
source_database: "UniProt"
source_id: "P0AES2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gudD ygcX b2787 JW2758"
---

# gudD

`protein.P0AES2`

## Static

- Type: `protein`
- Source: `UniProt:P0AES2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the dehydration of glucarate or L-idarate to 5-keto-4-deoxy-D-glucarate (5-kdGluc) (PubMed:9772162). Also catalyzes the epimerization of D-glucarate and L-idarate (PubMed:11513584). {ECO:0000269|PubMed:11513584, ECO:0000269|PubMed:9772162}. D-glucarate dehydratase catalyzes the dehydration of D-glucarate to 5-keto-4-deoxy-D-glucarate (KDG). Crystal structure of the enzyme alone and bound to the product or competitive inhibitors have been solved. The structures allowed the identification of active site residues and ligands for the Mg2+ cofactor. Further kinetic and structural analysis led to a proposed reaction mechanism involving an enediolate anion intermediate. Formation of this intermediate from both D-glucarate and L-idarate is the kinetically reversible first step in the overall reaction, accounting for the apparent D-glucarate/L-idarate epimerase activity of the enzyme . Enzymatic activity of D-glucarate dehydratase is induced by growth on D-glucarate, D-galactarate, and D-glycerate . Review:

## Biological Role

Catalyzes GLUCARDEHYDRA-RXN (reaction.ecocyc.GLUCARDEHYDRA-RXN), RXN0-5285 (reaction.ecocyc.RXN0-5285). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the dehydration of glucarate or L-idarate to 5-keto-4-deoxy-D-glucarate (5-kdGluc) (PubMed:9772162). Also catalyzes the epimerization of D-glucarate and L-idarate (PubMed:11513584). {ECO:0000269|PubMed:11513584, ECO:0000269|PubMed:9772162}.

## Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.GLUCARDEHYDRA-RXN|reaction.ecocyc.GLUCARDEHYDRA-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5285|reaction.ecocyc.RXN0-5285]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2787|gene.b2787]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AES2`
- `KEGG:ecj:JW2758;eco:b2787;ecoc:C3026_15325;`
- `GeneID:947258;`
- `GO:GO:0000287; GO:0008872; GO:0042838`
- `EC:4.2.1.40`

## Notes

Glucarate dehydratase (GDH) (GlucD) (EC 4.2.1.40) (D-glucarate dehydratase)
