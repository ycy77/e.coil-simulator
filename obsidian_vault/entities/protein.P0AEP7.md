---
entity_id: "protein.P0AEP7"
entity_type: "protein"
name: "gcl"
source_database: "UniProt"
source_id: "P0AEP7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gcl b0507 JW0495"
---

# gcl

`protein.P0AEP7`

## Static

- Type: `protein`
- Source: `UniProt:P0AEP7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the condensation of two molecules of glyoxylate to give 2-hydroxy-3-oxopropanoate (also termed tartronate semialdehyde). Glyoxylate carboligase condenses two molecules of glyoxylate to form tartronate semialdehyde. The reaction takes place under completely anaerobic conditions . The enzyme requires FAD for activity, although the reaction catalyzed by glyoxylate carboligase has no oxidation or reduction step . It appears to be a dimer in solution . The protein sequence contains conserved quinone, thiamine diphosphate (ThDP) and FAD binding sites . A crystal structure of the enzyme has been solved at 2.7 Å resolution . Unlike other ThDP-dependent enzymes, glyoxylate carboligase does not contain the usually strictly conserved carboxylate group of glutamate within hydrogen bond distance of ThDP. Kinetic studies of the wild type and various mutant enzymes suggested an unusual activation mechanism for the thiazol cofactor . Glyoxylate carboligase activity is increased by growth on glycolate or glyoxylate as the sole source of carbon . gcl promoter activity and the kinetics of inductionby glyoxylate have been observed in single cells in real time . gcl mutants are unable to grow on glycolate or glyoxylate .

## Biological Role

Catalyzes glyoxylate carboxy-lyase (dimerizing; tartronate-semialdehyde-forming) (reaction.R00013). Component of glyoxylate carboligase (complex.ecocyc.GLYOCARBOLIG-CPLX).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the condensation of two molecules of glyoxylate to give 2-hydroxy-3-oxopropanoate (also termed tartronate semialdehyde).

## Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00013|reaction.R00013]] `KEGG` `database` - via EC:4.1.1.47
- `is_component_of` --> [[complex.ecocyc.GLYOCARBOLIG-CPLX|complex.ecocyc.GLYOCARBOLIG-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0507|gene.b0507]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEP7`
- `KEGG:ecj:JW0495;eco:b0507;ecoc:C3026_02490;`
- `GeneID:75170531;945394;`
- `GO:GO:0000287; GO:0005948; GO:0009028; GO:0009097; GO:0009099; GO:0009436; GO:0030976; GO:0042802; GO:0046296; GO:0050660; GO:0071949`
- `EC:4.1.1.47`

## Notes

Glyoxylate carboligase (EC 4.1.1.47) (Tartronate-semialdehyde synthase)
