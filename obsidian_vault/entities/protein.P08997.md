---
entity_id: "protein.P08997"
entity_type: "protein"
name: "aceB"
source_database: "UniProt"
source_id: "P08997"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aceB mas b4014 JW3974"
---

# aceB

`protein.P08997`

## Static

- Type: `protein`
- Source: `UniProt:P08997`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

Malate synthase A (MSA) (EC 2.3.3.9) Malate synthase catalyzes the Claisen condensation of glyoxylate and acetyl-CoA, initially forming a malyl-CoA intermediate that is hydrolyzed to the products malate and CoA. There are two isozymes of malate synthase in E. coli . Malate synthase A is a key enzyme in the GLYOXYLATE-BYPASS. It metabolizes glyoxylate formed in the dissimilation of acetate. The isozyme MALSYNG-MONOMER is responsible for almost all of the malate synthase activity in cells metabolizing glyoxylate formed during growth on glycolate . Malate synthase A catalyzes the irreversible condensation of ACETYL-COA with GLYOX to produce MAL and CO-A. The formation of (S)-malate is a key reaction in the GLYOXYLATE-BYPASS. This cycle is similar to the TCA cycle (see TCA) but it bypasses the TCA cycle reactions that lead to a loss of CARBON-DIOXIDE, thus providing TCA cycle intermediates for cell carbon biosynthesis (see TCA-GLYOX-BYPASS). The glyoxylate cycle has been extensively studied in connection with growth on acetate which is used in the synthesis of these biosynthetic precursors. E. coli malate synthase A has been structurally characterized . Its encoding gene aceB is located in the aceBAK operon which is transcriptionally regulated by iclR and fadR. The operon is inducible by growth on acetate and is repressed on most other carbon sources...

## Biological Role

Catalyzes acetyl-CoA:glyoxylate C-acetyltransferase (thioester-hydrolysing, carboxymethyl-forming); (reaction.R00472), MALSYN-RXN (reaction.ecocyc.MALSYN-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

Malate synthase A (MSA) (EC 2.3.3.9)

## Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00472|reaction.R00472]] `KEGG` `database` - via EC:2.3.3.9
- `catalyzes` --> [[reaction.ecocyc.MALSYN-RXN|reaction.ecocyc.MALSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b4014|gene.b4014]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08997`
- `KEGG:ecj:JW3974;eco:b4014;ecoc:C3026_21685;`
- `GeneID:948512;`
- `GO:GO:0004474; GO:0005737; GO:0006097; GO:0006099`
- `EC:2.3.3.9`

## Notes

Malate synthase A (MSA) (EC 2.3.3.9)
